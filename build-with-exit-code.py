#!/usr/bin/env python
#
# **** Before running this script, review it for suitability in your own environment. ****
#
# This script builds an AsciiBinder preview and generates an error code on exit if there are AsciiDoc errors in the build. If you run `asciibinder build` directly in a terminal, it does not produce an error code when AsciiDoc errors are seen.
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
# $ python build-changed-pages.py -c <clone_directory_path> -b <branch> -d <distro>
#
# For example:
#
# $ python build-changed-pages.py -c /var/tmp/clones/openshift-docs/ -b my-feature-branch -d openshift-enterprise
#
# Because this script exists in the top level directory in the openshift-docs repo, you can run the script from that directory and specify '.' as the clone dir. If you don't specify the `-c` option, the directory that contains the script is used by default. For example:
#
# $ python build-changed-pages.py -b my-feature-branch -d openshift-enterprise
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
    global distro
    parser=argparse.ArgumentParser(
        description='''This script creates a list of assemblies and modules that are active in an openshift-docs branch.''')
    parser.add_argument('-c', '--clone-path', dest='clone', type=str, required=False, help='Specify the path to the local clone to examine. The current working directory is the default.')
    parser.add_argument('-b', '--branch', dest='branch', type=str, required=True, help='Specify the Git branch to examine in the local clone.')
    parser.add_argument('-d', '--distro', dest='distro', type=str, required=True, help='Specify the distro to build. For example, openshift-enterprise, openshift-osd, or osd-rosa.')
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
    distro = args.distro

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

# Build a preview for the specified distro and exit with an error code if there are any unexpected AsciiDoc errors or warnings:
def build_preview():
    asciibinder_command = ["asciibinder", "build", "-d", distro]
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
    build_preview()

# Run the main function:
if __name__ == "__main__":
    main()
