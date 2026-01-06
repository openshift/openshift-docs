#!/bin/bash


function swizzle-images {
    ASSEMBLY_FILES=`ls assemblies/*/as_*.adoc`
    PROC_FILES=`ls modules/*/p_*.adoc`
    CONCEPT_FILES=`ls modules/*/c_*.adoc`
    REFERENCE_FILES=`ls modules/*/r_*.adoc`
    ALL_FILES="$ASSEMBLY_FILES $PROC_FILES $CONCEPT_FILES $REFERENCE_FILES"
    for FILE in $ALL_FILES
    do
        sed -e "s/image:[\.\/]*images/image:images/" $FILE > $FILE.sed
        mv -f $FILE.sed $FILE
    done
}

swizzle-images

