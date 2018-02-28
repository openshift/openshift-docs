#!/bin/bash
set -ev

git diff --name-only HEAD...$TRAVIS_BRANCH

asciidoc-link-check -p creating_images/custom.adoc

#if [ "${TRAVIS_PULL_REQUEST}" = "true" ]; then
  echo -e "\e[32mHYPERLINKS CHECK\e[0m"
  #run the loop for every modified or added file
  for i in $(git diff --name-only --diff-filter=AM HEAD...$TRAVIS_BRANCH) ; do

      fileList[$N]="$i"
      echo "$(asciidoc-link-check $i -p)" #check all hyperlinks in this file
      echo $'\n'
      let "N= $N + 1"
  done
#fi
echo -e "\e[32mDONE!\e[0m"
