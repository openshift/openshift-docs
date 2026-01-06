#!/bin/bash

# pull down docs.kuadrant.io docs
branch=main
echo "info: fetching upstream content from docs.kuadrant.io branch: $branch"
echo 
# -L = follow redirects
curl -L -o $branch.zip https://github.com/kuadrant/docs.kuadrant.io/archive/$branch.zip

# -o = overwrite, -j = flatten directory structure, -q = quiet
unzip -qo $branch.zip "docs.kuadrant.io-$branch/docs/*"

# perform processing with sed or python scripts
# TBD

rm $branch.zip

echo "info: completed fetching docs.kuadrant.io branch: $branch"
echo


# pull down kuadrant operator docs
operator_branch=main

echo "info: fetching upstream content from kuadrant operator branch: $operator_branch"

# -L = follow redirects
curl -L -o $operator_branch.zip https://github.com/kuadrant/kuadrant-operator/archive/$operator_branch.zip

# -o = overwrite, -j = flatten directory structure, -q = quiet
unzip -qo $operator_branch.zip "kuadrant-operator-$operator_branch/doc/*"

# perform processing with sed or python scripts
# TBD

rm $operator_branch.zip

echo "info: completed fetching kuadrant operator branch: $operator_branch"
echo


# pull down kuadrantctl CLI docs
cli_branch=main

echo "info: fetching upstream content from kuadrantctl branch: $cli_branch"

# -L = follow redirects
curl -L -o $cli_branch.zip https://github.com/kuadrant/kuadrantctl/archive/$cli_branch.zip

# -o = overwrite, -j = flatten directory structure, -q = quiet
unzip -qo $cli_branch.zip "kuadrantctl-$cli_branch/doc/*"

# perform processing with sed or python scripts
# TBD 

rm $cli_branch.zip

echo "info: completed fetching kuadrantcl branch: $cli_branch"
echo
