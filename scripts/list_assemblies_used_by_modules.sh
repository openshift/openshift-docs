#!/bin/bash
#
# THIS SCRIPT IS INTENDED FOR LOCAL GIT CLONE TEST ENVIRONMENTS ONLY. REVIEW THIS SCRIPT THOROUGHLY TO DETERMINE SUITABILITY FOR YOUR TEST ENVIRONMENT.

function intro ()
{
echo; echo "###########################################################
#                                                         #
#    THIS SCRIPT IS INTENDED FOR LOCAL GIT CLONE TEST     #
#   ENVIRONMENTS ONLY. REVIEW THIS SCRIPT THOROUGHLY TO   #
#     DETERMINE SUITABILITY FOR YOUR TEST ENVIRONMENT.    #
#                                                         #
#  This script lists which AsciiDoc assemblies in a Git   #
#  repository include a particular module. You can use    #
#  the output to check that the assembly references at    #
#  the top of modules are up to date. The script can be   #
#  run for one module or for all modules updated in a Git #
#  commit.                                                #
#                                                         #
#  For the latter, the script assumes that all modules    #
#  are stored in a './module' directory and that all      #
#  assemblies are outside of that.                        #
#                                                         #
###########################################################"; echo
}

function get_repo ()
{
# Request the absolute path of the Git repository:
read -p "Input the absolute path of your local Git repository (e.g. /home/myusername/github-repos/myrepo). You can use tab to auto-complete: " -e REPODIR
# Check that the directory exists:
if [[ -d "${REPODIR}" ]]; then
  GITDIRCHECK="${REPODIR}/.git"
  if [[ -d "${GITDIRCHECK}" ]]; then
    echo; echo "${REPODIR} is a Git repository."
    # Change to the Git repo directory:
    cd ${REPODIR}
    # List the current branch:
    BRANCH=$(git branch --show-current)
    echo; echo "The current branch is ${BRANCH}. You can change branches by exiting this script with ctrl+c, running 'git checkout <branch>' from ${REPODIR} in another terminal window and then running this script again."
  else
    echo; echo "${REPODIR} is not a Git repository."
    exit 0
  fi
else
  echo "Directory does not exist."
  exit 0
fi
}

# Clarify if the user wants to run the script for one module or for all modules updated in a Git commit:
function module_check ()
{
  SWITCH="off"
  while [ "${SWITCH}" = "off"  ]; do
    echo
    echo "Please select an option:"
    echo ""
    echo "1. Run the script for one module"
    echo "2. Run the script for all modules updated in a Git commit"
    echo ""
    echo -e "Please select a number from the list above (or 'q' to quit): \c"
    read MODULESELECT
    echo

    case "${MODULESELECT}" in
      1)   one_module; break ;;
      2)   commit_modules; break ;;
      q|Q) exit 0 ;;
      *)  echo -e "Answer must be either '1', '2', 'q' or 'Q' (or 'ctrl+c')..."; sleep 3;;
    esac
  done
}

# Obtain the Git commit ID for your pull request:
function commit_modules ()
{
read -p "Input your local Git commit ID (e.g. b3e939f1365c95a2969ec09eee59664c597275e5). The commit ID can be obtained by running 'git log' from ${REPODIR}: " COMMITID
}

# Set the commit ID to "None" when the script is to be run against one module only:
function one_module ()
{
COMMITID="None"
}

function get_adocs ()
{
# Get a list of all assembly files in the repo:
ASSEMBLIES=$(find . -iname "*.adoc" -not -path "./modules/*" -not -path "./_preview/*")
# Get a list of modules:
if [[ "${COMMITID}" = "None" ]]; then
  read -p "Input the relative path to your module (e.g. modules/mymodule.adoc). You can use tab to auto-complete: " -e MODULEPATH
  # Remove preceding `./` characters if they exist:
  MODULES=$(echo ${MODULEPATH} | sed s/"^.\/"/" "/g)
  echo ; echo "Listing the assemblies that include ${MODULES}..."; echo
else
  MODULES=$(git show ${COMMITID} --name-only | grep -is '^modules/')
  echo ; echo "Listing the assemblies that include each module updated in Git commit ${COMMITID}..."; echo
fi
}

# List the assemblies in the repo that include each module that is updated in the commit:
function list_assemblies ()
{
for i in ${MODULES}
do
  echo "###${i}"
  echo "// Module included in the following assemblies:"
  echo "//"
  for j in ${ASSEMBLIES}
  do
    RESULT=$(grep -is ${i} ${j} | grep -is '^include::')
    if [[ -z ${RESULT} ]]; then
      :
    else
      TRUNCJ=$(echo ${j} | sed s/"^.\/"/" "/g)
      echo "// *${TRUNCJ}"
    fi
  done
  echo
done

if [[ "${COMMITID}" = "None" ]]; then
  echo "You can use this output to check that the assembly references at the top of ${MODULES} are up to date in your local Git repository."; echo
else
  echo "You can use this output to check that the assembly references at the top of each module file are up to date in your local Git repository."; echo
fi
}

# Main:
intro
get_repo
module_check
get_adocs
list_assemblies
