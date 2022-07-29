#!/usr/bin/env python
#
# **** Before running this script, review it for suitability in your own environment. ****
#
# This script builds previews only for openshift-docs pages that are changed in the latest commit in a branch. The script creates a list of active assemblies that are referenced in the topic maps in a branch of a clone of the openshift-docs repo. It also creates a list of the modules and snippets that are included in the active assemblies. This information is used to determine what active pages are updated by the commit. It also builds any pages that include modules that are changed in the commit, even if the assembly is not itself updated.
#
# Prerequisites:
#
# * You have installed Python 3 on your local host.
# * You have installed AsciiBinder on your local host.
# * You have a local clone of your openshift-docs fork.
# * You have a feature branch in your local clone and your changes are in the HEAD commit only.
#
# Usage:
#
# You can run the script as follows:
#
# $ python build-changed-pages.py -c <clone_directory_path> -b <branch>
#
# For example:
#
# $ python build-changed-pages.py -c /var/tmp/clones/openshift-docs/ -b my-feature-branch
#
# Because this script exists in the top level directory in the openshift-docs repo, you can run the script from that directory and specify '.' as the clone dir. If you don't specify the `-c` option, the directory that contains the script is used by default. For example:
#
# $ python build-changed-pages.py -b my-feature-branch
#
# Note: the script changes to the specified branch before processing the data. If the branch does not exist, the script exits with an error message.
#
# Author: Paul Needle <pneedle@redhat.com>

import tempfile
import shutil
import subprocess
import os
import sys
import yaml
import git
import re
import argparse
import time
from git import InvalidGitRepositoryError,NoSuchPathError,GitCommandError

# Create a global dictionary:
d = {}

# Add a help menu:
def help_menu():
    global clone_dir
    global git_branch
    parser=argparse.ArgumentParser(
        description='''This script creates a list of assemblies and modules that are active in an openshift-docs branch.''')
    parser.add_argument('-c', '--clone-path', dest='clone', type=str, required=False, help='Specify the path to the local clone to examine. The current working directory is the default.')
    parser.add_argument('-b', '--branch', dest='branch', type=str, required=True, help='Specify the Git branch to examine in the local clone.')
    args=parser.parse_args()
    # If the clone directory is not specified, use the current working directory by default:
    if args.clone is None:
        clone_dir = "."
    else:
        clone_dir = args.clone
    # Remove any trailing `/` characters from the end of the clone directory path:
    while "/" in clone_dir[-1:]:
        clone_dir = clone_dir.removesuffix('/')
    git_branch = args.branch

# Create a temp directory:
def create_tmpdir():
    global tmpdir
    tmpdir = tempfile.mkdtemp()

# Validate the local openshift-docs Git clone and checkout the specified branch:
def git_check():
    global repo
    try:
        repo = git.Repo(clone_dir)
    except (InvalidGitRepositoryError, NoSuchPathError):
        print(f"{clone_dir} does not look like a Git repository. Exiting.")
        sys.exit()
    if ".git" in repo.git_dir:
        print(f"{clone_dir} is a Git repo.")
    else:
        print(f"{clone_dir} is not a Git repo. Exiting.")
    try:
        print(f"Checking out to {git_branch}.")
        repo.git.checkout(git_branch)
    except GitCommandError:
        print(f"Failed to check out to {git_branch}. Attempt a manual checkout in the repo by running 'git checkout {git_branch}' and review the Git error to resolve. Then, re-run this script. Exiting.")
        sys.exit()
    current_branch = repo.active_branch.name
    if current_branch == git_branch:
        print(f"The active branch is {current_branch}.")
    else:
        print(f"Failed to checkout to {git_branch}. Exiting.")
        sys.exit()

# Create a temporary combined topic map:
def find_build_config_file():
    global build_config
    topic_map_list = os.listdir(clone_dir + "/_topic_maps/")
    time_string = time.strftime("%Y%m%d%H%M%S")
    tmp_topic_map = tmpdir + "/tmp_topic_map_" + time_string + ".yml"
    with open(tmp_topic_map, 'w') as outfile:
        for i in topic_map_list:
            with open(clone_dir + "/_topic_maps/" + i) as infile:
                outfile.write(infile.read())
    build_config = os.path.abspath(os.path.join(tmp_topic_map))
    if not os.path.isfile(build_config):
        build_config = os.path.abspath(os.path.join(clone_dir, "_build_cfg.yml"))

# Load the topic map into a list:
def parse_build_config():
    global data
    with open(build_config, "r") as f:
        data = list(yaml.load_all(f,Loader=yaml.FullLoader))

# Get the relative path for all active assembly files referenced in the combined topic map:
def list_active_assembly_files():
    global assembly_list_raw
    global assembly_list
    assembly_list = []
    for i in data:
        book = i['Name']
        dir1 = i['Dir']
        for j in i['Topics']:
            if "Dir" in j:
                for k in j['Topics']:
                    dir2 = j['Dir']
                    if "Dir" in k:
                        for l in k['Topics']:
                            dir3 = k['Dir']
                            assembly_file = l['File']
                            filepath = dir1 + "/" + dir2 + "/" + dir3 + "/" + assembly_file + ".adoc"
                            assembly_list.append(filepath)
                    else:
                        assembly_file = k['File']
                        filepath = dir1 + "/" + dir2 + "/" + assembly_file + ".adoc"
                        assembly_list.append(filepath)
            else:
                assembly_file = j['File']
                filepath = dir1 + "/" + assembly_file + ".adoc"
                assembly_list.append(filepath)
    # Create a raw copy of the assembly list to print for verification purposes. The raw list is in the same order as the topic map file entries and not deduplicated:
    assembly_list_raw = assembly_list
    # Sort and deduplicate the assembly list:
    assembly_list.sort()
    assembly_list = list(dict.fromkeys(assembly_list))

# Get the relative path for all active modules referenced in the active assembly files:
def list_active_module_files():
    global module_list
    module_list = []
    for a in assembly_list:
        assembly_path = clone_dir + "/" + a
        try:
            with open(assembly_path) as f:
                for line in f:
                    if line.startswith("include::") and "modules/" in line:
                        module_path = re.search('modules/[^"\r\n]*.adoc', line)[0]
                        module_list.append(module_path)
        except FileNotFoundError:
            print(f"{assembly_path} is active in at least one topic map, but the the file is not found.")
            sys.exit(1)
    # Sort and deduplicate the module list entries:
    module_list.sort()
    module_list = list(dict.fromkeys(module_list))

# Get the relative path for all active snippets referenced in the active assembly files:
def list_active_snippet_files():
    global snippet_list
    snippet_list = []
    for a in assembly_list:
        assembly_path = clone_dir + "/" + a
        try:
            with open(assembly_path) as f:
                for line in f:
                    if line.startswith("include::") and "snippets/" in line:
                        snippet_path = re.search('snippets/[^"\r\n]*.adoc', line)[0]
                        snippet_list.append(snippet_path)
        except FileNotFoundError:
            print(f"{assembly_path} is active in at least one topic map, but the the file is not found.")
            sys.exit(1)
    # Sort and deduplicate the module list entries:
    snippet_list.sort()
    snippet_list = list(dict.fromkeys(snippet_list))

# Create a list of pages that are changed by the latest commit in the specified branch. Then, build previews only for those changed pages:
def list_changed_files_in_pr():
    # Create an empty pages to build list:
    pages_to_build = []
    # Create a dictionary of files changed in the HEAD commit for the current branch. In the dictionary, each key is the changed file name and the value is the change type:
    head_commit = repo.head.commit
    for i in head_commit.diff("HEAD~1"):
        d.update({i.a_path: i.change_type})
    # For each changed file in HEAD, check if the files are active and compile a list of pages to build:
    for key, value in d.items():
        # If a changed file is an assembly file that is active in the topic map, add it to the list of pages to build:
        if ".adoc" in key and key in assembly_list and "D" not in value:
            pages_to_build.append(key.replace('.adoc',''))
        # Check if each changed module file is in an active assembly:
        if ".adoc" in key and key in module_list and "D" not in value:
            include_string = "include::" + key + "["
            for i in assembly_list:
                with open(clone_dir + "/" + i, 'r') as file:
                    content = file.read()
                    if key in content:
                        pages_to_build.append(i.replace('.adoc',''))
    # Sort and deduplicate the list of pages that are changed in the HEAD commit:
    pages_to_build.sort()
    pages_to_build = list(dict.fromkeys(pages_to_build))
    # Run 'asciibinder build' for each page that is changed in the HEAD commit, including any unchanged assemblies that include changed modules:
    print(f"Attempting to build the pages changed in the HEAD commit:")
    for i in pages_to_build:
        asciibinder_command = ["asciibinder", "build", "-p", i]
        try:
            asciibinder_output = subprocess.run(asciibinder_command, cwd=clone_dir, capture_output=True, text=True)
            # It looks like all of the AsciiDoctor errors and warnings are output to stderr. The expected AsciiBinder warnings about the topic map, however, are sent to stdout. If there any outputs in stderr, print them and exit the script with an error code:
            if len(asciibinder_output.stderr.splitlines()) > 0:
                for i in asciibinder_output.stderr.splitlines():
                    print(i)
                sys.exit(1)
            # If there is no output to stderr, print the stdout messages:
            for i in asciibinder_output.stdout.splitlines():
                print(i)
        except subprocess.CalledProcessError as e:
            print(e)
            sys.exit(e.returncode)

# Main funciton:
def main():
    help_menu()
    create_tmpdir()
    git_check()
    find_build_config_file()
    parse_build_config()
    list_active_assembly_files()
    list_active_module_files()
    list_active_snippet_files()
    list_changed_files_in_pr()

# Run the main function:
if __name__ == "__main__":
    main()
