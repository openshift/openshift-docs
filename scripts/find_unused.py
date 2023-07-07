#!/usr/bin/env python

"""
This script goes through and searches the OpenShift docs repository for any modules
that are not included in assemblies.

__author__      = "Christian Huffman"
__version__     = "1 July, 2019"

Updated September 2022 to run with Python 3.

Run with `python scripts/find_unused.py .` at the repo root level to run against the entire repo.
"""

from __future__ import print_function

from os.path import join
import argparse
import os
import shutil
import sys

class FindUnused():
    unused_directory = "_unused_topics"     # Edit this to adjust the target path.
    modules_directory = "/modules"          # Edit this to adjust the modules subdirectory
    ignored_prefixes = ["virt","ossm"]       # Add any prefixes to ignore here
    
    def __init__(self, args):
        self.args = args
    
    def process(self):
        """
        This function is responsible for obtaining the list of modules, the list of assemblies,
        and then either moving or displaying any modules not being included.
        """
        modules = {}
        assemblies = []
        # Build up a dictionary from the elements in the modules subdirectory, storing their path as the value.
        for root, directories, files in os.walk(self.args.path + self.modules_directory):
            for filename in files:
                for prefix in self.ignored_prefixes:
                    # Search through all provided prefixes. If one is found, skip including it.
                    if filename.startswith(prefix):
                        break
                    modules[filename] = os.path.join(root,filename)
        # Since modules can also include other modules, we include them in the list of assemblies.
        for root, directories, files in os.walk(self.args.path):
            for filename in files:
                if filename.endswith(".adoc"):
                    assemblies.append(os.path.join(root,filename))
        remaining_modules = self.check_assemblies(assemblies,modules)
        # Determine if we should move the files or simply print the list
        if self.args.move:
            self.move_files(self.args.path,remaining_modules)
        else:
            for filename in remaining_modules:
                print(remaining_modules[filename])
    
    def check_assemblies(self,assemblies,modules):
        """
        Because we can't modify dictionaries while they're being iterated over, we're
        forced to create a new list to collect any files that are found. Once this process
        completes, we then go through the original list and remove the found files.
        
        This process leaves us with a dictionary containing the unused files and their paths,
        which is returned.
        """
        included_modules = {}
        for filename in assemblies:
            currentfile = open(filename,"r")
            for line in currentfile.readlines():
                for key in modules:
                    if key in line:
                        included_modules[key] = ""
            currentfile.close()
        for key in included_modules:
            del modules[key]
        return modules
    
    def move_files(self,root,remaining_modules):
        """
        Goes through each path in the dictionary and moves it to "root/self.unused_directory/"
        Once finished it prints out the total number of files moved.
        """
        try:
            for key in remaining_modules:
                os.rename(remaining_modules[key],root + "/" + self.unused_directory + "/" + key)
            print("Moved %d files" % len(remaining_modules))
        except OSError as err:
            print("Unable to move files: {0}".format(err))
            print("Target destination: " + self.unused_directory)
    
    
def main():
  usage = """
  Identifies any modules in the `<docs_repo>/modules` directory and subdirectories
  that are not currently included in any assembly or module.
  """
  
  parser = argparse.ArgumentParser(description=usage)
  parser.add_argument('path', help="path to the root of the github repository.")
  parser.add_argument('-m', dest='move', action='store_true', help="moves the files instead of displaying them.")
  args = parser.parse_args()
  
  parser = FindUnused(args)
  parser.process()

if __name__ == "__main__":
    main()
