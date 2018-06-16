import sys
import os
import logging

from lxml.etree import XMLSyntaxError, XIncludeError

from aura import cli, utils
from aura.exceptions import InvalidInputException
from aura.transformers.tf_asciidoc import AsciiDocPublicanTransformer

branch = os.system("git symbolic-ref -q --short HEAD")

print(branch)

# list of books - CHANGE HERE
book_list = ['admin_guide', 'apb_devel', 'architecture', 
  'creating_images', 'day_two_guide', 'dev_guide', 
  'getting_started', 'install_config', 'release_notes', 'scaling_performance', 
  'security', 'upgrading', 'using_images']

# all validated?
all_validated = True

# Initialize logging
cli.init_logging(False, False)

for distro in os.listdir("drupal-build"):
    
    print("---------------------------------------")
    print("BUILDING " + distro + " BOOKS")
    print("---------------------------------------")
    
    for book in os.listdir(os.path.join("drupal-build", distro)):

      #print(os.getcwd() + "\n")
      #if not os.path.isdir("drupal-build/" + distro + "/" + book):
        #print("---------------------------------------")
        #print(">>> No Book " + book + " in this repo. Skipping <<<")
        #print("---------------------------------------")
        
        #continue
        
      # rest api book is a pain and doesn't convert well
      if book == "rest_api":
          continue
          
      os.chdir("drupal-build/" + distro + "/" + book)
      #print(os.getcwd() + "\n")

      # Create the transformer instance
      transformer = AsciiDocPublicanTransformer()

      # Transform the AsciiDoc to DocBook XML
      print(">>> Working on " + book + " book <<<")
      if not transformer._build_docbook_src("master.adoc", "build"):
        print("Could not transform book " + book)
        sys.exit(-1)
      
      # Parse the transformed XML
      try:
                
        transformer._before_xml_parse("build/master.xml")
        
        # Parse the XML content
        tree = utils.parse_xml("build/master.xml")
        
        transformer._fix_uncoverted_xrefs_with_file_paths(tree)

        # Validate the transformed XML
        if not transformer._validate_docbook_idrefs(tree):
          logging.error(">>> Validation of book " + book + " failed <<<")
          all_validated = False
          # sys.exit(-1)
        
        print(">>> Finished with " + book + " book <<<")
        print("---------------------------------------")
        
        os.chdir("../../../")
        
      except (XMLSyntaxError, XIncludeError, InvalidInputException) as e:
        logging.error(e)
        all_validated = False
        print(">>> Finished with " + book + " book <<<")
        print("---------------------------------------")    
        os.chdir("../../../")

if not all_validated:
    sys.exit(-1)
else: 
  print("All Successful")