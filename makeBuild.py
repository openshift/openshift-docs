import sys

from lxml.etree import XMLSyntaxError, XIncludeError

from aura import utils
from aura.transformers.tf_asciidoc import AsciiDocPublicanTransformer

# Create the transformer instance
transformer = AsciiDocPublicanTransformer()

# Transform the AsciiDoc to DocBook XML
transformer._build_docbook_src("master.adoc", "build")
transformer._before_xml_parse("build/master.xml")

# Parse the transformed XML
try:
    # Parse the XML content
    tree = utils.parse_xml(asciidoc_xml_file)
except (XMLSyntaxError, XIncludeError) as e:
    print("Validation failed")
    sys.exit(-1)

# Validate the transformed XML
if not transformer._validate_docbook_xml_basic("build", tree):
    print("Validation failed")
    sys.exit(-1)
