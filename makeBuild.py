import sys
import os
import logging

from lxml.etree import XMLSyntaxError, XIncludeError

from aura import cli, utils
from aura.transformers.tf_asciidoc import AsciiDocPublicanTransformer

# list of books - CHANGE HERE
book_list = ['admin_guide', 'architecture', 'cli_reference', 'dev_guide', 
  'getting_started', 'install_config', 'release_notes', 'scaling_performance', 
  'security', 'using_images']

# all validated?
all_validated = True

# Initialize logging
cli.init_logging(False, False)

for book in book_list:

  #print(os.getcwd() + "\n")
  os.chdir("drupal-build/" + book)
  #print(os.getcwd() + "\n")

  # Create the transformer instance
  transformer = AsciiDocPublicanTransformer()

  # Transform the AsciiDoc to DocBook XML
  if not transformer._build_docbook_src("master.adoc", "build"):
    print("Could not transform book " + book)
    sys.exit(-1)
  
  transformer._before_xml_parse("build/master.xml")

  # Parse the transformed XML
  try:
    
    # Parse the XML content
    tree = utils.parse_xml("build/master.xml")
    
    transformer._fix_uncoverted_xrefs_with_file_paths(tree)

    # Validate the transformed XML
    if not transformer._validate_docbook_idrefs(tree):
      logging.error(">> Validation of book " + book + " failed <<")
      all_validated = False
      # sys.exit(-1)
    
    os.chdir("../../")
    
  except (XMLSyntaxError, XIncludeError) as e:
    logging.error(e)
    logging.error("Unable to parse the AsciiDoc built DocBook XML")    
    os.chdir("../../")

if not all_validated:
    sys.exit(-1)
else: 
  print("Successful")