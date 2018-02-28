#!/bin/bash
set -ev

#git diff --name-only HEAD...$TRAVIS_BRANCH

#asciidoc-link-check -p creating_images/custom.adoc
echo "${TRAVIS_PULL_REQUEST}"
#COMMIT_HASH="$(git log -n 1 --skip 1 --pretty=format:"%H")" #get the second last commit hash because Travis merges PR and creates a new commit
if [ "${TRAVIS_PULL_REQUEST}" != "false" ]; then
  echo -e "\e[32mHYPERLINKS CHECK\e[0m"
  #run the loop for every modified or added file
  for i in $(git diff --name-only "${TRAVIS_PULL_REQUEST_SHA}") ; do
      fileList[$N]="$i"
      echo "$(asciidoc-link-check $i)" #check all hyperlinks in this file
      echo $'\n'
      let "N= $N + 1"
  done
fi
echo -e "\e[32mDONE!\e[0m"
