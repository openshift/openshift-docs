import sys
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

print(os.getcwd() + "\n")
os.chdir("drupal-build/install_config/")
#print(os.getcwd() + "\n")

from lxml.etree import XMLSyntaxError, XIncludeError

from aura import utils
from aura.transformers.tf_asciidoc import AsciiDocPublicanTransformer

# Create the transformer instance
transformer = AsciiDocPublicanTransformer()

logging.Logger.verbose = logging.Logger.debug
# Transform the AsciiDoc to DocBook XML
#os.chdir("drupal-build/install_config/")
transformer._build_docbook_src("master.adoc", "build")
transformer._before_xml_parse("build/master.xml")

# Parse the transformed XML
try:
    # Parse the XML content
    tree = utils.parse_xml("build/master.xml")
except (XMLSyntaxError, XIncludeError) as e:
    logging.error(e)
    logging.error("Unable to parse the AsciiDoc built DocBook XML")
    print("Validation failed")
    sys.exit(-1)

# Validate the transformed XML
if not transformer._validate_docbook_xml_basic("build", tree):
    print("Validation failed")
    sys.exit(-1)
