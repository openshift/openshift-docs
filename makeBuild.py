# converts books prepared for it from the build_for_portal.py or build.py
# scripts from AsciiDoc to DocBook XML

# uses a refactored Aura script which is an opensource port of ccutil

import sys
import os
import logging
import imp
imp.reload(sys)

from lxml.etree import XMLSyntaxError, XIncludeError

from aura import cli, utils
from aura.exceptions import InvalidInputException
from aura.transformers.tf_asciidoc import AsciiDocPublicanTransformer, XML_NS, LXML_XML_NS

#branch = os.system("git symbolic-ref -q --short HEAD")

#print(branch)

# function to convert XML ids to HTML 4 compatible ids from ccutil
def _fix_ids_for_html4(tree):
    """
    Fixes any id elements that aren't html4 compatible.

    :param tree:
    """
    xmlroot = tree.getroot()
    namespaces = {'xml': XML_NS}

    # Find all the elements with an id
    id_eles = xmlroot.findall(".//*[@xml:id]", namespaces=namespaces)
    ids = []

    # Filter the elements that start with an underscore
    underscore_id_eles = []
    for ele in id_eles:
        id_val = ele.get(LXML_XML_NS + 'id')
        if id_val.startswith("_"):
            underscore_id_eles.append(ele)
        else:
            ids.append(id_val)

    # Get the linkend and endterm eles
    old_linkend_eles = xmlroot.findall(".//*[@linkend]")
    old_endterm_eles = xmlroot.findall(".//*[@endterm]")

    # Fix each underscore id
    for id_ele in underscore_id_eles:
        id_val = id_ele.get(LXML_XML_NS + 'id')

        # Remove the underscore and if it now starts with a number, change the number to a word
        new_id = utils.create_xml_id(id_val)

        # Make sure the new id is unique, by adding a number to the end
        base_new_id = new_id
        count = 0
        while new_id in ids:
            count += 1
            new_id = base_new_id + "-" + str(count)

        # Set the new id
        if new_id != id_val:
            ids.append(new_id)
            id_ele.set(LXML_XML_NS + 'id', new_id)
            id_ele.set("remap", id_val)

            # update any old references
            for old_linkend in old_linkend_eles:
                if old_linkend.get("linkend") == id_val:
                    old_linkend.set('linkend', new_id)

            for old_endterm in old_endterm_eles:
                if old_endterm.get("endterm") == id_val:
                    old_endterm.set('endterm', new_id)

def build_book(book):
    validated = True
    starting_dir=os.getcwd()
    os.chdir(os.path.join("drupal-build", distro, book))
    #print(os.getcwd() + "\n")

    # Create the transformer instance
    transformer = AsciiDocPublicanTransformer()

    try:
        # Transform the AsciiDoc to DocBook XML
        print((">>> Working on " + book + " book in " + distro + " <<<"))
        if not transformer._build_docbook_src("master.adoc", "build"):
            logging.error(">>> Validation of book " + book + " in " + distro + " failed: master.adoc not found <<<")
            return False

        # Parse the transformed XML
        transformer._before_xml_parse("build/master.xml")

        # Parse the XML content
        tree = utils.parse_xml("build/master.xml")

        # Apply XML updates from aura/ccutil
        transformer._fix_uncoverted_xrefs_with_file_paths(tree)
        _fix_ids_for_html4(tree)

        # Validate the transformed XML
        if not transformer._validate_docbook_idrefs(tree):
            logging.error(">>> Validation of book " + book + " in " + distro + " failed <<<")
            validated = False
    except (XMLSyntaxError, XIncludeError, InvalidInputException) as e:
        logging.error(e)
        validated = False
    finally:
        print((">>> Finished with " + book + " book in " + distro + " <<<"))
        print("---------------------------------------")
        os.chdir(starting_dir)
        return validated



# all validated?
all_validated = True

# Initialize logging
cli.init_logging(False, False)

for distro in os.listdir("drupal-build"):

    print("---------------------------------------")
    print(("BUILDING " + distro + " BOOKS"))
    print("---------------------------------------")

    for book in os.listdir(os.path.join("drupal-build", distro)):

        #print(os.getcwd() + "\n")
        # skip any non-directory entries
        if not os.path.isdir("drupal-build/" + distro + "/" + book):
            continue
        # rest api book is a pain and doesn't convert well
        if book == "rest_api":
            continue

        if os.path.exists(os.path.join("drupal-build", distro, book,"hugeBook.flag")):
            for secondary_book in os.listdir(os.path.join("drupal-build", distro, book)):
                if os.path.isdir("drupal-build/" + distro + "/" + book + "/" + secondary_book):
                    all_validated = all_validated and build_book(book+"/"+secondary_book)
        else:
            all_validated = all_validated and build_book(book)
if not all_validated:
    sys.exit(-1)
else:
  print("All Successful")
