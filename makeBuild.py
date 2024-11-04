# converts books prepared for it from the build_for_portal.py or build.py
# scripts from AsciiDoc to DocBook XML

# Update Nov 2024: Remove outdated dependency on aura/ccutil package

import sys
import os
import logging
from lxml import etree
from lxml.etree import XMLSyntaxError, XIncludeError

# Namespace constants for XML processing
XML_NS = "http://www.w3.org/XML/1998/namespace"
LXML_XML_NS = f"{{{XML_NS}}}"

# Creates an HTML4 compatible XML ID by removing any leading underscore.
    Converts a starting digit to a corresponding word.
def create_xml_id(id_val):
    id_val = id_val.lstrip('_')
    if id_val[0].isdigit():
        id_val = f"num_{id_val}"
    return id_val

# Parses an XML file into an etree element tree, handling unescaped ampersands.
def parse_xml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    # Replace unescaped ampersands with &amp;
    xml_content = xml_content.replace("&", "&amp;")
    
    # Parse modified XML content
    try:
        return etree.fromstring(xml_content)
    except XMLSyntaxError as e:
        logging.error(f"XML parsing error in {file_path}: {e}")
        raise

# Fixes any id elements that aren't HTML4 compatible.
def _fix_ids_for_html4(tree):
    xmlroot = tree.getroot()
    id_eles = xmlroot.findall(f".//*[@{{{XML_NS}}}id]", namespaces={'xml': XML_NS})
    ids = []

    underscore_id_eles = [ele for ele in id_eles if ele.get(LXML_XML_NS + 'id').startswith('_')]
    ids.extend(ele.get(LXML_XML_NS + 'id') for ele in id_eles if not ele.get(LXML_XML_NS + 'id').startswith('_'))

    old_linkend_eles = xmlroot.findall(".//*[@linkend]")
    old_endterm_eles = xmlroot.findall(".//*[@endterm]")

    for id_ele in underscore_id_eles:
        id_val = id_ele.get(LXML_XML_NS + 'id')
        new_id = create_xml_id(id_val)
        base_new_id = new_id
        count = 0
        while new_id in ids:
            count += 1
            new_id = f"{base_new_id}-{count}"

        if new_id != id_val:
            ids.append(new_id)
            id_ele.set(LXML_XML_NS + 'id', new_id)
            id_ele.set("remap", id_val)

            for old_linkend in old_linkend_eles:
                if old_linkend.get("linkend") == id_val:
                    old_linkend.set('linkend', new_id)

            for old_endterm in old_endterm_eles:
                if old_endterm.get("endterm") == id_val:
                    old_endterm.set('endterm', new_id)

def build_book(book, distro):
    validated = True
    starting_dir = os.getcwd()
    os.chdir(os.path.join("drupal-build", distro, book))

    try:
        print(f">>> Working on {book} book in {distro} <<<")
        if not os.path.exists("master.adoc"):
            logging.error(f">>> Validation of book {book} in {distro} failed: master.adoc not found <<<")
            return False

        # Simulate transformation and parse XML
        tree = parse_xml("build/master.xml")

        # Fix IDs for HTML4 compatibility
        _fix_ids_for_html4(tree)

        # Example validation: Check ID uniqueness (dummy example for refactor)
        all_ids = [elem.get(f"{LXML_XML_NS}id") for elem in tree.xpath(".//*[@xml:id]")]
        if len(all_ids) != len(set(all_ids)):
            logging.error(f">>> Validation failed: Duplicate IDs found in {book} <<<")
            validated = False
    except (XMLSyntaxError, XIncludeError) as e:
        logging.error(e)
        validated = False
    finally:
        print(f">>> Finished with {book} book in {distro} <<<")
        print("---------------------------------------")
        os.chdir(starting_dir)
        return validated

all_validated = True
for distro in os.listdir("drupal-build"):
    print("---------------------------------------")
    print(f"BUILDING {distro} BOOKS")
    print("---------------------------------------")

    for book in os.listdir(os.path.join("drupal-build", distro)):
        if not os.path.isdir(f"drupal-build/{distro}/{book}") or book == "rest_api":
            continue

        if os.path.exists(os.path.join("drupal-build", distro, book, "hugeBook.flag")):
            for secondary_book in os.listdir(os.path.join("drupal-build", distro, book)):
                if os.path.isdir(f"drupal-build/{distro}/{book}/{secondary_book}"):
                    all_validated &= build_book(f"{book}/{secondary_book}", distro)
        else:
            all_validated &= build_book(book, distro)

if not all_validated:
    sys.exit(-1)
else:
    print("All Successful")
