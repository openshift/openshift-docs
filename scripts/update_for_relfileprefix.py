# Usage: python ./scripts/update-relfileprefix.py <path_to_assembly>
#
# Use this script to update an assembly and included modules with relfileprefix changes. The script adds ":relfileprefix: <appropriate_dot_path_prefix>" to the assembly file metadata if it doesn't already exist and cleans all path prefixes from xrefs in the assembly and included modules.

import re
import os
import sys
import git

xref_re = re.compile(r"xref:((\.\.\/)+)", re.DOTALL)
relfileprefix_re = re.compile(r":relfileprefix: ((\.\.\/)*)", re.DOTALL)
modules_include_re = re.compile(r"^include::(modules/.+)\[.*\]$", re.MULTILINE)

# Calculate the root dir
git_repo = git.Repo(os.path.abspath(os.getcwd()), search_parent_directories=True)
git_root = git_repo.git.rev_parse("--show-toplevel")

def update_files(assembly):
    with open(assembly, "r+") as f:
        assembly_content = f.read()

        relfileprefix_match = re.search(relfileprefix_re, assembly_content)
        if relfileprefix_match:
            print("relfileprefix attribute already exists! There is no need to process this assembly. 😕")
            exit()

        # Calculate the relative path dot value for xref_prefix
        assembly_dir = os.path.dirname(os.path.abspath(assembly))
        xref_prefix = os.path.relpath(git_root, assembly_dir) + "/"

        # Add :relfileprefix: to the top of the assembly
        assembly_content = f":relfileprefix: {xref_prefix}\n{assembly_content}"
        # Update assembly xrefs
        assembly_content = re.sub(xref_re, "xref:", assembly_content)
        f.seek(0)
        f.write(assembly_content)
        f.truncate()

    # Update included modules xrefs
    included_files = re.findall(modules_include_re, assembly_content)
    for included_file in included_files:
        include_path = os.path.join(git_root, included_file)
        with open(include_path, "r+") as f:
            module_content = f.read()
            module_content = re.sub(xref_re, "xref:", module_content)
            f.seek(0)
            f.write(module_content)
            f.truncate()

    print(f"Updated xrefs in {assembly} and included modules 🥳")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_for_relfileprefix.py <path_to_assembly>")
    else:
        assembly = sys.argv[1]
        update_files(assembly)
