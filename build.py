#!/usr/bin/python

# this file builds content from asciidoc to ccutil ready format BUT is only
# used for validating content, rather than the actual conversion. For the
# actual conversion, the file build_for_portal.py is used (on the portal).

# the only difference between this and build_for_portal file is in the
# section on _fix_links. This file replaces link anchors within the same file
# to the top of the file so that Travis build passes. Travis builds don't
# know books external to them and this helps pass the builds.

import argparse
import configparser
import filecmp
import fnmatch
import logging
import os
import re
import shutil
import subprocess
import sys
import time
import yaml
import requests
import tempfile

from aura import cli

cli.init_logging(False, True)

has_errors = False
CLONE_DIR = "."
BASE_PORTAL_URL = "https://access.redhat.com/documentation/en-us/"
# ID_RE = re.compile("^\[(?:\[|id=\'|#)(.*?)(\'?,.*?)?(?:\]|\')?\]", re.M | re.DOTALL)
ID_RE = re.compile("^\[(?:\[|id=\'|#|id=\")(.*?)(\'?,.*?)?(?:\]|\'|\")?\]", re.M | re.DOTALL)
LINKS_RE = re.compile("(?:xref|link):([\./\w_-]*/?[\w_.-]*\.(?:html|adoc))?(#[\w_-]*)?(\[.*?\])", re.M | re.DOTALL)
EXTERNAL_LINK_RE = re.compile("[\./]*([\w_-]+)/[\w_/-]*?([\w_.-]*\.(?:html|adoc))", re.DOTALL)
INCLUDE_RE = re.compile("include::(.*?)\[(.*?)\]", re.M)
IFDEF_RE = re.compile(r"^if(n?)def::(.*?)\[\]", re.M)
ENDIF_RE = re.compile(r"^endif::(.*?)\[\]\r?\n", re.M)
COMMENT_CONTENT_RE = re.compile(r"^^////$.*?^////$", re.M | re.DOTALL)
TAG_CONTENT_RE = re.compile(r"//\s+tag::(.*?)\[\].*?// end::(.*?)\[\]", re.M | re.DOTALL)
CMP_IGNORE_FILES = [".git", ".gitignore", "README.md", "build.cfg"]
DEVNULL = open(os.devnull, 'wb')


MASTER_FILE_BASE = "= {title}\n\
:product-author: {product-author}\n\
:product-title: {product}\n\
:product-version: {product-version}\n\
:{distro}:\n\
:imagesdir: images\n\
:idseparator: -\n\
{preface-title}\n"

DOCINFO_BASE = "<title>{title}</title>\n\
<productname>{{product-title}}</productname>\n\
<productnumber>{{product-version}}</productnumber>\n\
<subtitle>Enter a short description here.</subtitle>\n\
<abstract>\n\
    <para>A short overview and summary of the book's subject and purpose, traditionally no more than one paragraph long.</para>\n\
</abstract>\n\
<authorgroup>\n\
    <orgname>{product-author}</orgname>\n\
</authorgroup>\n\
<xi:include href=\"Common_Content/Legal_Notice.xml\" xmlns:xi=\"http://www.w3.org/2001/XInclude\" />\n"

# A list of book titles, that still use the old drupal url format (ie includes the product/version in the book title part)
# eg. openshift-enterprise/version-3.0/openshift-enterprise-30-getting-started vs openshift-enterprise/version-3.0/getting-started
DRUPAL_OLD_URL_TITLES = [
    "Administrator Guide",
    "Architecture",
    "CLI Reference",
    "Creating Images",
    "Developer Guide",
    "Getting Started",
    "REST API Reference",
    "Using Images",
    "What's New?"
]

# A mapping of upstream book/category names to CP book names
BOOK_NAME_OVERRIDES = {
    "Administration": "Administrator Guide"
}

# Lines that should be stripped out/ignored when cleaning the content
IGNORE_LINES = [
    "{product-author}\n",
    "{product-version}\n",
    "{product-version]\n",
    "{Lucas Costi}\n",
    "toc::[]\n"
]

# Each MACRO in this list is omitted from the output
# if the input appears as ':MACRO:' (colon, MACRO, colon).
IGNORE_MACROS = [
    "description",
    "keywords",
    "icons",
    "data-uri",
    "toc",
    "toc-title"
]

# Files where the title should be removed when building the all-in-one
ALL_IN_ONE_SCRAP_TITLE = [
    "welcome/index.adoc"
]

# Files that should be commented out in the toc structure
COMMENT_FILES = [
    "admin_guide/overview.adoc",
    "creating_images/overview.adoc",
    "dev_guide/overview.adoc",
    "using_images/overview.adoc",
    "rest_api/overview.adoc"
]

# Map FILENAME to a map of TITLE to ID.  In most of the cases the
# ID is the TITLE downcased, with "strange" chars replaced by hyphen.
# A notable exception is 'any' TITLE.
TITLE_IDS = {}
# A dictionary of existing dup ids to new unique ids
DUPLICATE_IDS = {}
# Map FILENAME to a map of BAD to GOOD.  Most of the time, BAD and GOOD
# are in link syntax, i.e., beginning with "link:", but not always.
INCORRECT_LINKS = {}

log = logging.getLogger("build")


def setup_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--distro", help="The distribution to build for", default="openshift-enterprise")
    parser.add_argument("--all-in-one", help=argparse.SUPPRESS, action="store_true")
    parser.add_argument("--title", help=argparse.SUPPRESS, default="Documentation")
    parser.add_argument("--product", default="OpenShift Enterprise")
    parser.add_argument("--version", default="3.0")
    parser.add_argument("--author", default="Red Hat OpenShift Documentation Team")
    parser.add_argument("--upstream-url", help="The upstream source url", default="https://github.com/openshift/openshift-docs.git")
    parser.add_argument("--upstream-branch", help="The upstream source branch", default="enterprise-3.0")
    parser.add_argument("--branch", help="The GitLab branch to commit changes into", default="GA")
    parser.add_argument("-p", "--push", help="Commit and push the changes into GitLab", action="store_true")
    parser.add_argument("--no-clean", help="Don't clean the drupal-build directory before building", action="store_true")
    parser.add_argument("--no-upstream-fetch", help="Don't fetch the upstream sources", action="store_true")
    return parser


def find_build_config_file():
    """
    Finds the build config file to use, as it might be _topic_map.yml or _build_cfg.yml
    """

    # updated 23rd Nov to support files in _topic_maps folder

    # load everything from the _topic_maps folder
    file_list = os.listdir(os.path.join(CLONE_DIR, "_topic_maps"))

    # create a temp file combining all values from that folder
    # don't delete it immediately, and give it a suffix of swp which makes it ignored by git
    with tempfile.NamedTemporaryFile(dir=CLONE_DIR, delete=False, suffix=".swp") as tmp:
        for f in file_list:
            with open(os.path.join(CLONE_DIR, "_topic_maps", f), "rb") as infile:
                tmp.write(infile.read())

    config = os.path.abspath(tmp.name)
    log.info(config)

    # backup look for a single _topic_map in the cloned directory
    if not os.path.isfile(config):
        config = os.path.abspath(os.path.join(CLONE_DIR, "_topic_map.yml"))

    return config


def parse_build_config(config):
    """
    Parses the build config and returns a tree based structure for the config.
    """
    config = os.path.expanduser(config)
    with open(config, "r") as f:
        data = list(yaml.load_all(f,Loader=yaml.FullLoader))

    for book in data:
        book_name = book['Name']
        if book_name in BOOK_NAME_OVERRIDES:
            book['Name'] = BOOK_NAME_OVERRIDES[book_name]

    return data


def iter_tree(node, distro, dir_callback=None, topic_callback=None, include_path=True, parent_dir="", depth=0):
    """
    Iterates over a build config tree starting from a specifc node, skipping content where the distro doesn't match. Additionally calls are
    made to the dir_callback or topic_callback functions when a directory or topic is found.
    """
    if "Topics" in node:
        if check_node_distro_matches(node, distro):
            if include_path:
                topics_dir = os.path.join(parent_dir, node["Dir"])
            else:
                topics_dir = ""

            if dir_callback is not None:
                dir_callback(node, parent_dir, depth)

            for topic in node["Topics"]:
                iter_tree(topic, distro, dir_callback, topic_callback, True, topics_dir, depth + 1)
    elif check_node_distro_matches(node, distro):
        if topic_callback is not None:
            topic_callback(node, parent_dir, depth)


def check_node_distro_matches(node, distro):
    """
    Checks to see if the specified distro matches a distro in the nodes distros list. If there is no distros list specified on the
    node then all distros are allowed, so return true.
    """
    if "Distros" not in node:
        return True
    else:
        node_distros = [x.strip() for x in node['Distros'].split(",")]
        for node_distro in node_distros:
            # Check for an exact match, or a glob match
            if node_distro == distro or fnmatch.fnmatchcase(distro, node_distro):
                return True

    return False


def ensure_directory(directory):
    """
    Creates DIRECTORY if it does not exist.
    """
    if not os.path.exists(directory):
        os.mkdir(directory)


def build_master_files(info):
    """
    Builds the master.adoc and docinfo.xml files for each guide specified in the config.
    """
    dest_dir = info['dest_dir']

    all_in_one = info['all_in_one']
    all_in_one_text = ""
    for book in info['book_nodes']:
        book_dest_dir = os.path.join(dest_dir, book['Dir'])
        ensure_directory(book_dest_dir)

        book_info = dict(info)
        book_info['title'] = book['Name']

        master = generate_master_entry(book, book['Dir'], info['distro'], all_in_one, all_in_one=all_in_one)

        # Save the content
        if not all_in_one:
            master_file = os.path.join(book_dest_dir, 'master.adoc')
            docinfo_file = os.path.join(book_dest_dir, 'docinfo.xml')
            master_base = MASTER_FILE_BASE.format(**book_info)

            log.debug("Writing " + master_file)
            with open(master_file, "w") as f:
                f.write(master_base + master)
            log.debug("Writing " + docinfo_file)
            with open(docinfo_file, "w") as f:
                f.write(DOCINFO_BASE.format(**book_info))
        else:
            if all_in_one_text == "":
                # Remove the title for the first file in the book
                master = master.replace("= " + book['Name'] + "\n", "")

                # Set the preface title from the first file in the book
                first_file = os.path.join(info['src_dir'], book['Dir'], book['Topics'][0]['File'] + ".adoc")
                preface_title = None
                with open(first_file, "r") as f:
                    line = f.readline()
                    while line:
                        if include_line(line):
                            preface_title = re.sub("^=+ ", "", line)
                            break
                        line = f.readline()
                if preface_title is not None:
                    info['preface-title'] = ":preface-title: " + preface_title
            all_in_one_text += master

    if all_in_one:
        master_file = os.path.join(dest_dir, 'master.adoc')
        docinfo_file = os.path.join(dest_dir, 'docinfo.xml')

        master_base = MASTER_FILE_BASE.format(**info)

        log.debug("Writing " + master_file)
        with open(master_file, "w") as f:
            f.write(master_base + all_in_one_text)
        log.debug("Writing " + docinfo_file)
        with open(docinfo_file, "w") as f:
            f.write(DOCINFO_BASE.format(**info))


def generate_master_entry(node, book_dir, distro, include_name=True, all_in_one=False):
    """
    Generates the master.adoc core content for a specific book/node.
    """
    master_entries = []

    def dir_callback(dir_node, parent_dir, depth):
            if include_name or depth > 0:
                master_entries.append("=" * (depth + 1) + " " + dir_node["Name"].replace("\\", ""))

    def topic_callback(topic_node, parent_dir, depth):
        book_file_path = os.path.join(parent_dir, topic_node["File"] + ".adoc")
        file_path = os.path.join(book_dir, book_file_path)
        include = "include::" + book_file_path + "[leveloffset=+" + str(depth) + "]"
        if not all_in_one and file_path in COMMENT_FILES:
            master_entries.append("////")
            master_entries.append(include)
            master_entries.append("////")
        else:
            master_entries.append(include)
        # Add a blank line
        master_entries.append("")

    # Iterate over the tree and build the master.adoc content
    iter_tree(node, distro, dir_callback, topic_callback, include_name)
    return "\n".join(master_entries)


def reformat_for_drupal(info):
    """
    Reformats the source content for use in the Customer Portal. This function does the following:

    - Copies images over and flattens them into a single dir
    - Copies source asciidoc over
    - Filters the AsciiDoc source to remove duplicate macro definitions, that should only be in the main file.
    - Adds id's for each file, so the files can be properly cross referenced.
    - Adds id's to sections that are cross referenced, but have no id.
    - Fixes duplicate id's in the source content.
    - Fixes links that have been done incorrectly and should be cross references instead.
    """
    books = info['book_nodes']
    src_dir = info['src_dir']
    dest_dir = info['dest_dir']
    distro = info['distro']

    # Build a mapping of files to ids
    # Note: For all-in-one we have to collect ids from all books first
    file_to_id_map = {}
    if info['all_in_one']:
        book_ids = []
        for book in books:
            book_ids.extend(collect_existing_ids(book, distro, src_dir))
        for book in books:
            file_to_id_map.update(build_file_to_id_map(book, distro, book_ids, src_dir))
    else:
        for book in books:
            book_ids = collect_existing_ids(book, distro, src_dir)
            file_to_id_map.update(build_file_to_id_map(book, distro, book_ids, src_dir))
    info['file_to_id_map'] = file_to_id_map

    # Reformat the data
    for book in books:
        log.info("Processing %s", book['Dir'])
        book_src_dir = os.path.join(src_dir, book['Dir'])

        if info['all_in_one']:
            images_dir = os.path.join(dest_dir, "images")
        else:
            book_dest_dir = os.path.join(dest_dir, book['Dir'])
            images_dir = os.path.join(book_dest_dir, "images")

        ensure_directory(images_dir)

        log.debug("Copying source files for " + book['Name'])
        copy_files(book, book_src_dir, src_dir, dest_dir, info)

        log.debug("Copying images for " + book['Name'])
        copy_images(book, src_dir, images_dir, distro)


def copy_images(node, src_path, dest_dir, distro):
    """
    Copy images over to the destination directory and flatten all image directories into the one top level dir.
    """
    def dir_callback(dir_node, parent_dir, depth):
        node_dir = os.path.join(parent_dir, dir_node['Dir'])
        src = os.path.join(node_dir, "images")

        if os.path.exists(src):
            src_files = os.listdir(src)
            for src_file in src_files:
                shutil.copy(os.path.join(src, src_file), dest_dir)

    iter_tree(node, distro, dir_callback, parent_dir=src_path)


def copy_files(node, book_src_dir, src_dir, dest_dir, info):
    """
    Recursively copy files from the source directory to the destination directory, making sure to scrub the content, add id's where the
    content is referenced elsewhere and fix any links that should be cross references.
    """
    def dir_callback(dir_node, parent_dir, depth):
        node_dest_dir = os.path.join(dest_dir, parent_dir, dir_node['Dir'])
        ensure_directory(node_dest_dir)

    def topic_callback(topic_node, parent_dir, depth):
        node_src_dir = os.path.join(src_dir, parent_dir)
        node_dest_dir = os.path.join(dest_dir, parent_dir)

        src_file = os.path.join(node_src_dir, topic_node["File"] + ".adoc")
        dest_file = os.path.join(node_dest_dir, topic_node["File"] + ".adoc")

        # Copy the file
        copy_file(info, book_src_dir, src_file, dest_dir, dest_file)

    iter_tree(node, info['distro'], dir_callback, topic_callback)


def copy_file(info, book_src_dir, src_file, dest_dir, dest_file, include_check=True, tag=None, cwd=None):
    """
    Copies a source file to destination, making sure to scrub the content, add id's where the content is referenced elsewhere and fix any
    links that should be cross references. Also copies any includes that are referenced, since they aren't included in _build_cfg.yml.
    """
    # It's possible that the file might have been created by another include, if so then just return
    if os.path.isfile(dest_file):
        return

    # Touch the dest file, so we can handle circular includes
    parent_dir = os.path.dirname(dest_file)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    #os.mknod(dest_file)
    open(dest_file, 'w').close()
    # Scrub/fix the content
    content = scrub_file(info, book_src_dir, src_file, tag=tag, cwd=cwd)

    # Check for any includes
    if include_check:
        cleaned_content = remove_conditional_content(content, info)
        include_iter = INCLUDE_RE.finditer(cleaned_content)
        for include in include_iter:
            include_text = include.group(0)
            include_path = include.group(1)
            include_unparsed_vars = include.group(2)

            # Determine the include vars
            include_vars = {}
            if include_unparsed_vars is not None and len(include_unparsed_vars) > 0:
                for meta in re.split(r"\s*,\s*", include_unparsed_vars):
                    key, value = re.split("\s*=\s*", meta, 2)
                    include_vars[key] = value

            # Determine the include src/dest paths
            include_file = os.path.join(os.path.dirname(book_src_dir), include_path)
            relative_path = os.path.relpath(include_file, os.path.dirname(src_file))

            # If the path is in another book, copy it into this one
            relative_book_path = os.path.relpath(include_file, book_src_dir)
            if relative_book_path.startswith("../"):
                path, src_book_name = os.path.split(book_src_dir)
                dest_include_dir = os.path.join(dest_dir, src_book_name, "includes")
                relative_path = os.path.join(os.path.relpath(dest_include_dir, parent_dir), os.path.basename(include_file))
            else:
                dest_include_dir = os.path.abspath(os.path.join(os.path.dirname(dest_file), os.path.dirname(relative_path)))
            dest_include_file = os.path.join(dest_include_dir, os.path.basename(include_file))

            # Make sure we have a reference to the current working dir
            current_dir = cwd or os.path.dirname(src_file)
            include_tag = include_vars.get("tag", None)

            # Copy the file and fix the content
            if not os.path.isfile(dest_include_file):
                copy_file(info, book_src_dir, include_file, dest_dir, dest_include_file, tag=include_tag, cwd=current_dir)
            else:
                # The file has already been copied, so just fix the links for this tag
                with open(dest_include_file, 'r') as f:
                    include_content = f.read()

                # Fix any links
                include_content = fix_links(include_content, info, book_src_dir, include_file, tag=include_tag, cwd=cwd)

                with open(dest_include_file, "w") as f:
                    f.write(include_content)

            content = content.replace(include_text, include.expand("include::" + relative_path + "[\\2]"))

    with open(dest_file, "w") as f:
        f.write(content)


def scrub_file(info, book_src_dir, src_file, tag=None, cwd=None):
    """
    Scrubs a file and returns the cleaned file contents.
    """
    base_src_file = src_file.replace(info['src_dir'] + "/", "")

    # added 1/Sep/2020
    # to allow loading files like json and yaml from external sources, this
    # procedure loads the file recognizing that it starts with http
    # it then checks if it exists or not, and if it exists, returns the raw data
    # data that it finds.
    if(base_src_file.startswith("https://raw.githubusercontent.com/openshift/")):
        try:
            response = requests.get(base_src_file)
            if(response):
                return response.text
            else:
                raise ConnectionError("Malformed URL")
        except Exception as exception:
            log.error("An include file wasn't found: %s", base_src_file)
            has_errors = True
            sys.exit(-1)

    # Get a list of predefined custom title ids for the file
    title_ids = TITLE_IDS.get(base_src_file, {})

    # Read in the source content
    with open(src_file, 'r') as f:
        src_file_content = f.readlines()

    # Scrub the content
    content = ""
    header_found = content_found = False
    current_id = None
    for line in src_file_content:
        # Ignore any leading blank lines, before any meaningful content is found
        if line.strip() == "" and not content_found:
            continue

        # Check if the line should be included in the output
        if include_line(line):
            content_found = True

            # Setup the document header content/id
            if not header_found and line.strip() != "" and line.startswith("="):
                header_found = True

                if info['all_in_one'] and base_src_file in ALL_IN_ONE_SCRAP_TITLE and line.startswith("= "):
                    continue
                # Add a section id if one doesn't exist, so we have something to link to
                elif current_id is None and src_file in info['file_to_id_map']:
                    file_id = info['file_to_id_map'][src_file]
                    content += "[[" + file_id + "]]\n"
            # Add a custom title id, if one is needed
            elif line.startswith("=") and current_id is None:
                for title in title_ids:
                    title_re = r"^=+ " + title.replace(".", "\\.").replace("?", "\\?") + "( (anchor|\[).*?)?(\n)?$"
                    if re.match(title_re, line):
                        content += "[[" + title_ids[title] + "]]\n"

            # Set the current id based on the line content
            if current_id is None and ID_RE.match(line.strip()):
                current_id = line.strip()
            elif current_id is not None and line.strip != "":
                current_id = None

            # Add the line to the processed content
            content += line

    # Fix up any duplicate ids
    if base_src_file in DUPLICATE_IDS:
        for duplicate_id, new_id in list(DUPLICATE_IDS[base_src_file].items()):
            content = content.replace("[[" + duplicate_id + "]]", "[[" + new_id + "]]")

    # Replace incorrect links with correct ones
    if base_src_file in INCORRECT_LINKS:
        for incorrect_link, fixed_link in list(INCORRECT_LINKS[base_src_file].items()):
            content = content.replace(incorrect_link, fixed_link)

    # Fix up the links
    content = fix_links(content, info, book_src_dir, src_file, tag=tag, cwd=cwd)

    return content


def include_line(line):
    """
    Determines if a line should be included in the filtered output.
    """
    if line in IGNORE_LINES:
        return False

    for macro in IGNORE_MACROS:
        if line.startswith(":" + macro + ":"):
            return False

    return True


def fix_links(content, info, book_src_dir, src_file, tag=None, cwd=None):
    """
    Fix any links that were done incorrectly and reference the output instead of the source content.
    """
    if info['all_in_one']:
        content = fix_links(content, info['src_dir'], src_file, info)
    else:
        # Determine if the tag should be passed when fixing the links. If it's in the same book, then process the entire file. If it's
        # outside the book then don't process it.
        if book_src_dir in src_file:
            content = _fix_links(content, book_src_dir, src_file, info, cwd=cwd)
        else:
            content = _fix_links(content, book_src_dir, src_file, info, tag=tag, cwd=cwd)

    return content


def _fix_links(content, book_dir, src_file, info, tag=None, cwd=None):
    """
    Fix any links that were done incorrectly and reference the output instead of the source content.
    """
    # TODO Deal with xref so that they keep the proper path. Atm it'll just strip the path and leave only the id
    file_to_id_map = info['file_to_id_map']
    current_dir = cwd or os.path.dirname(src_file)
    cleaned_content = remove_conditional_content(content, info, tag=tag)
    links = LINKS_RE.finditer(cleaned_content)

    for link in links:
        link_text = link.group(0)
        link_file = link.group(1)
        link_anchor = link.group(2)
        link_title = link.group(3)

        if link_file is not None:
            fixed_link_file = link_file.replace(".html", ".adoc")
            fixed_link_file_abs = os.path.abspath(os.path.join(current_dir, fixed_link_file))
            if fixed_link_file_abs in file_to_id_map:
                if fixed_link_file_abs.startswith(book_dir + os.sep) or fixed_link_file_abs == src_file:
                    # We are dealing with a cross reference within the same book here
                    if link_anchor is None:
                        # Cross reference to the top of a topic, without an id being specified
                        link_anchor = "#" + file_to_id_map[fixed_link_file_abs]

                    fixed_link = "xref:" + link_anchor.replace("#", "") + link_title
                else:
                    # We are dealing with a cross reference to another book here
                    external_link = EXTERNAL_LINK_RE.search(link_file)
                    book_dir_name = external_link.group(1)

                    # Find the book name
                    book_name = book_dir_name
                    for book in info['data']:
                        if check_node_distro_matches(book, info['distro']) and book['Dir'] == book_dir_name:
                            book_name = book['Name']
                            break

                    fixed_link_file = BASE_PORTAL_URL + build_portal_url(info, book_name)

                    if link_anchor is None:
                        fixed_link = "link:" + fixed_link_file + "#" + file_to_id_map[fixed_link_file_abs] + link_title
                    else:
                        fixed_link = "link:" + fixed_link_file + link_anchor + link_title
            else:
                # Cross reference or link that isn't in the docs suite
                fixed_link = link_text
                if EXTERNAL_LINK_RE.search(link_file) is not None:
                    rel_src_file = src_file.replace(os.path.dirname(book_dir) + "/", "")
                    has_errors = True
                    log.error("ERROR (%s): \"%s\" appears to try to reference a file not included in the \"%s\" distro", rel_src_file, link_text.replace("\n", ""), info['distro'])
                    sys.exit(-1)
        else:
            fixed_link = "xref:" + link_anchor.replace("#", "") + link_title

        content = content.replace(link_text, fixed_link)

    return content


def remove_conditional_content(content, info, tag=None):
    """
    Removes any conditional content that doesn't match for the specified distro
    """
    # Remove any ifdef content
    ifdef = IFDEF_RE.search(content)
    while ifdef is not None:
        is_not_def = ifdef.group(1) == "n"
        ifdef_distros = ifdef.group(2).split(",")
        pos = ifdef.start()
        end = ifdef.end()

        # Determine if we should strip the conditional content, based on the distro
        strip_content = False
        if is_not_def and info['distro'] in ifdef_distros:
            strip_content = True
        elif not is_not_def and info['distro'] not in ifdef_distros:
            strip_content = True

        # Remove the conditional content
        if strip_content:
            # Find the correct endif for the current ifdef
            search_pos = end
            endpos = len(content)
            while True:
                next_ifdef = IFDEF_RE.search(content, search_pos)
                endif = ENDIF_RE.search(content, search_pos)

                if not endif:
                    break
                elif not next_ifdef or next_ifdef.start() > endif.start():
                    endpos = endif.end()
                    break
                else:
                    search_pos = endif.end()

            # Replace the content and move the end pos to be the same as the start since the content was removed
            ifdef_text = content[pos:endpos]
            content = content.replace(ifdef_text, "")
            end = pos

        # Move onto the next ifdef
        ifdef = IFDEF_RE.search(content, end)

    # Remove commented out content
    for comment in COMMENT_CONTENT_RE.finditer(content):
        content = content.replace(comment.group(0), "")

    # Remove content outside of tags
    if tag is not None:
        for tag_match in TAG_CONTENT_RE.finditer(content):
            tag_text = tag_match.group(0)
            tag_label = tag_match.group(1)
            if tag_label == tag:
                # Tag matches, so only use the content in the tag
                content = tag_text

    return content


def collect_existing_ids(node, distro, path):
    """
    Examines all nodes asciidoc file contents and returns any existing ids.
    """
    book_ids = []

    def topic_callback(topic_node, parent_dir, depth):
        src_file = os.path.join(parent_dir, topic_node["File"] + ".adoc")
        file_ids = extract_file_ids(src_file)
        book_ids.extend(file_ids)

    iter_tree(node, distro, topic_callback=topic_callback, parent_dir=path)

    return book_ids


def build_file_to_id_map(node, distro, existing_ids, path=""):
    """
    Builds a mapping of file names/paths to the root id for the file. This is used to fix the links that are done incorrectly.
    """
    file_to_id_map = {}

    def topic_callback(topic_node, parent_dir, depth):
        src_file = os.path.join(parent_dir, topic_node["File"] + ".adoc")
        file_to_id_map[src_file] = build_file_id(topic_node["Name"], file_to_id_map, existing_ids)

    iter_tree(node, distro, topic_callback=topic_callback, parent_dir=path)
    return file_to_id_map


def extract_file_ids(file_path):
    """
    Extracts all the ids used in the specified file.
    """
    with open(file_path, "r") as f:
        content = f.read()

    ids = ID_RE.finditer(content)
    return [id.group(1) for id in ids]


def build_file_id(file_title, file_to_id_map, existing_ids):
    """
    Generates a unique id for a file, based on it's title.
    """
    file_id = base_id = re.sub(r"[\[\]\(\)#]", "", file_title.lower().replace("_", "-").replace(" ", "-"))
    count = 1
    while file_id in existing_ids or file_id in list(file_to_id_map.values()):
        file_id = base_id + "-" + str(count)
        count += 1

    return file_id


def build_portal_url(info, book_name):
    """
    Builds a portal url path by escaping the content in the same way drupal does.
    """
    product = info['product']
    version = info['product-version']

    return generate_url_from_name(product) + "/" + generate_url_from_name(version) + "/html-single/" + generate_url_from_name(book_name) + "/"


def replace_nbsp(val):
    """Replaces non breaking spaces with a regular space"""
    if val is not None:
        # Check if the string is unicode
        if isinstance(val, str):
            return val.replace('\xa0', ' ')
        else:
            return val.replace('\xc2\xa0', ' ')
    else:
        return None


def generate_url_from_name(name, delimiter='_'):
    """
    Generates a url fragment from a product, version or titles name.
    """
    # Remove characters that aren't allowed in urls
    url = re.sub("^\.+|[^0-9a-zA-Z _\-.]+", "", replace_nbsp(name))
    # Replace spaces with the delimiter
    url = re.sub("\s+", delimiter, url)
    # Replace multiple underscores with a single underscore
    url = re.sub(delimiter + "+", delimiter, url)
    return url.lower()


def call_git_command(*args, **kwargs):
    """
    Calls a git command and retries the command if it is unable to connect to the remote repo
    """
    retries = kwargs.pop("retries", 3)
    try:
        output = subprocess.check_output(*args, **kwargs)
        if output is not None:
            sys.stdout.write(output)
        return output
    except subprocess.CalledProcessError as e:
        retries -= 1
        if retries > 0 and "fatal: Could not read from remote repository" in e.output:
            # Connection failed, so wait a couple of secs and try again
            time.sleep(2)
            call_git_command(*args, retries=retries, **kwargs)
        else:
            raise


def fetch_sources(url, branch, dir=None, clone_dirname=None):
    """
    Fetches sources from a git repository. If the repository doesn't exist it'll be cloned into `dir_name`, otherwise if it already has been
    cloned, the repo will just be updated.
    """
    # Setup the defaults
    if dir is None:
        dir = os.getcwd()
    if clone_dirname is None:
        clone_dirname = url.split('/')[-1].replace(".git", "")

    # If the dir already exists update the content, otherwise clone it
    clone_dir = os.path.abspath(os.path.join(dir, clone_dirname))
    if os.path.exists(os.path.join(clone_dir, ".git")):
        cmd = ["git", "pull", "-f"]
        cmd_dir = clone_dir

        # Do a checkout to make sure we are on the right branch
        checkout_cmd = ["git", "checkout", branch]
        subprocess.check_output(checkout_cmd, cwd=cmd_dir, stderr=subprocess.STDOUT)
    else:
        cmd = ["git", "clone", "-b", branch, url, clone_dirname]
        cmd_dir = os.path.abspath(dir)

    # Execute the command
    call_git_command(cmd, cwd=cmd_dir, stderr=subprocess.STDOUT)


def sync_directories(src_dir, dest_dir, ignore=None):
    """
    Syncs two directories so that the both contain the same content, with the exception of ignored files.
    """
    if ignore is None:
        ignore = []
    ignore.extend(CMP_IGNORE_FILES)

    dcmp = filecmp.dircmp(src_dir, dest_dir, ignore)
    _sync_directories_dircmp(dcmp)


def _sync_directories_dircmp(dcmp):
    # Remove files that only exist in the dest directory
    for filename in dcmp.right_only:
        right = os.path.join(dcmp.right, filename)
        if os.path.isfile(right):
            os.remove(right)
        else:
            shutil.rmtree(right)

    # Copy files that only exist in the source directory or files that have changed
    for filename in dcmp.left_only+dcmp.common_files:
        left = os.path.join(dcmp.left, filename)
        right = os.path.join(dcmp.right, filename)
        if os.path.isfile(left):
            shutil.copy2(left, right)
        else:
            shutil.copytree(left, right)

    # Sync sub directories
    for subdcmp in list(dcmp.subdirs.values()):
        _sync_directories_dircmp(subdcmp)


def commit_and_push_changes(git_dir, git_branch, git_upstream_branch):
    """
    Adds, commits and pushes any changes to a local git repository.
    """
    # Add all the changes
    add_cmd = ["git", "add", "--all"]
    subprocess.check_call(add_cmd, cwd=git_dir)
    try:
        # Commit the changes
        commit_cmd = ["git", "commit", "-m", "Merge branch 'upstream/" + git_upstream_branch + "' into " + git_branch,
                      "--author", "CCS OSE Build Script <no-reply@redhat.com>"]
        call_git_command(commit_cmd, cwd=git_dir, stderr=subprocess.STDOUT)
        # Push the changes
        push_cmd = ["git", "push"]
        call_git_command(push_cmd, cwd=git_dir, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        if e.output is None or "nothing to commit" not in e.output:
            raise


def parse_repo_config(config_file, distro, version):
    # Make sure the repo config file exists
    if not os.path.isfile(config_file):
        log.error("Failed loading the repo configuration from %s", config_file)
        sys.exit(-1)

    parser = configparser.SafeConfigParser()
    parser.read(config_file)

    repo_urls = dict()
    section_name = distro + "-" + version
    if parser.has_section(section_name):
        for (key, value) in parser.items(section_name):
            repo_urls[key] = value

    return repo_urls


def main():
    parser = setup_parser()
    args = parser.parse_args()
    logging.basicConfig(format='%(message)s', level=logging.INFO, stream=sys.stdout)

    # Copy down the latest files
    if not args.no_upstream_fetch:
        log.info("Fetching the upstream sources")
        fetch_sources(args.upstream_url, args.upstream_branch, clone_dirname=CLONE_DIR)

    config = find_build_config_file()
    src_dir = os.path.dirname(config)

    # Parse the build config
    data = parse_build_config(config)

    # Filter the list of books that should be built
    book_nodes = [node for node in data if check_node_distro_matches(node, args.distro)]

    # Make the new source tree
    dest_dir = os.path.join(os.getcwd(), "drupal-build", args.distro)
    if not args.no_clean:
        log.info("Cleaning the drupal-build directory")
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
        os.makedirs(dest_dir)
    elif not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    info = {
        'title': args.title,
        'product-author': args.author,
        'product-version': args.version,
        'product': args.product,
        'distro': args.distro,
        'src_dir': src_dir,
        'dest_dir': dest_dir,
        'data': data,
        'book_nodes': book_nodes,
        'all_in_one': args.all_in_one,
        'preface-title': "",
        "upstream_branch": args.upstream_branch
    }

    # Build the master files
    log.info("Building the drupal files")
    build_master_files(info)

    # Copy the original data and reformat for drupal
    reformat_for_drupal(info)

    if has_errors:
        sys.exit(1)

    if args.push:
        # Parse the repo urls
        config_file = os.path.join(os.path.dirname(__file__), 'repos.ini')
        repo_urls = parse_repo_config(config_file, args.distro, args.version)

        # Make sure the base git dire exists
        base_git_dir = os.path.join(os.getcwd(), "gitlab-repos")
        ensure_directory(base_git_dir)

        # Checkout the gitlab repo, copy the changes and push them back up
        for book_dir, gitlab_repo_url in list(repo_urls.items()):
            build_book_dir = os.path.join(dest_dir, book_dir)
            git_dirname = gitlab_repo_url.split('/')[-1].replace(".git", "")
            git_dir = os.path.join(base_git_dir, git_dirname)

            try:
                log.info("Fetching " + book_dir + " sources from GitLab")
                fetch_sources(gitlab_repo_url, args.branch, base_git_dir, git_dirname)

                log.info("Syncing " + book_dir)
                sync_directories(build_book_dir, git_dir, ["docinfo.xml"])

                log.info("Pushing " + book_dir + " changes back to GitLab")
                commit_and_push_changes(git_dir, args.branch, args.upstream_branch)
            except subprocess.CalledProcessError as e:
                if e.output:
                    sys.stdout.write(e.output)
                raise

if __name__ == "__main__":
    main()
