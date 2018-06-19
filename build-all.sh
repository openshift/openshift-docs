#!/bin/bash
HOST_GIT_REPO_DIR="/Users/vikramgoyal/git-repo/openshift-docs/drupal-build/"
IMG_GIT_REPO_DIR="$1"

./build.py --distro $1 --product "$2" --version $3 --no-upstream-fetch

drupal_distro_dir="drupal_build/$1"

echo $drupal_distro_dir

if [ -z "$4" ]; then
  docker run -ti -v $HOST_GIT_REPO_DIR:/drupal_build ccutil:latest /bin/bash -c 'cd $drupal_distro_dir; for book in */;  do if [ "$book" == "rest_api/" ]; then echo -e "\n\n >>>> skipping rest_api <<<< "; continue; fi;  echo -e "\n\n>>> Working on ${book} <<<<"; cd $1; cd $book; ccutil compile --lang en-US --format html-single; cd ..; done'
else
  echo " >>>> Working on only ${4} <<<< "
  docker run -ti -v $HOST_GIT_REPO_DIR:/drupal_build ccutil:latest /bin/bash -c "cd drupal_build/$1/$4; ccutil compile --lang en-US --format html-single;"
fi
