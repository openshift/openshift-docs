#!/bin/bash
set -ev
#if [ "${TRAVIS_PULL_REQUEST}" = "true" ]; then
  echo -e "\e[32mHYPERLINKS CHECK\e[0m"
  COMMIT_HASH="$(git rev-parse @~)" #get the previous commit hash

  #run the loop for every modified or added file
  for i in $(git diff --name-only "${COMMIT_HASH}") ; do

      fileList[$N]="$i"
      echo "$(asciidoc-link-check $i -p)" #check all hyperlinks in this file
      echo $'\n'
      let "N= $N + 1"
  done
#fi
echo -e "\e[32mDONE!\e[0m"
