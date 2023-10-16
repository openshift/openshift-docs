for dir in */
do
    dir=${dir%*/}
    echo ${dir##*/}
    if [[ $dir == _* ]];
    then
      echo "Ignoring ${dir}"
      continue;
    fi
    cd $dir
    ln -s ../modules modules
    cd ..
done
