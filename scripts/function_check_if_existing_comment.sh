#!/bin/bash

# Define the check_if_existing_comment function
function check_if_existing_comment {
    echo "Checking if existing comment..."

    local vale_json="$1"
    #local pull_comment_json="$2"

    # Outer loop to iterate through Vale alert JSON
    echo "$vale_json" | jq -c '.[]' | while read object; do
        echo "$object"
        BODY_VALE=$(jq -r '.body' <<< "$object")
        echo $BODY_VALE
        PATH_VALE=$(jq -r '.path' <<< "$object")
        LINE_VALE=$(jq -r '.line' <<< "$object")
        echo $LINE_VALE

        # Inner loop to iterate through pull comment JSON to see if a comment exists
        echo "$pull_comment_json" | jq -c '.[]' | while IFS= read -r object2; do
            echo "$object2"
            BODY_COMMENT=$(jq -r '.body' <<< "$object2")
            PATH_COMMENT=$(jq -r '.path' <<< "$object2")
            LINE_COMMENT=$(jq -r '.line' <<< "$object2")
            echo "Inner loop"

            # If there's a comment that matches the Vale body, line, and path, remove it from both files
            if [ "$BODY_VALE" == "$BODY_COMMENT" ] && [ "$PATH_VALE" == "$PATH_COMMENT" ] && [ "$LINE_VALE" == "$LINE_COMMENT" ]; then
                echo "Found existing comment for $object"
                echo "Removing alert because review comment already exists... "

                # Remove the matching object from vale_json and pull_comment_json
                vale_json=$(echo "$vale_json" | jq --argjson obj "$object" '. | del(.[index($obj)])')
                pull_comment_json=$(echo "$pull_comment_json" | jq --argjson obj "$object2" '. | del(.[index($obj)])')

                break
            fi
        done
    done
}

# Construct vale_json variable
# vale_json='[
#     {
#         "body": "[error] OpenShiftAsciiDoc.ModuleContainsContentType: Module is missing the _mod-docs-content-type variable.",
#         "path": "modules/private-clusters-about-gcp.adoc",
#         "line": 1
#     },
#     {
#         "body": "[error] RedHat.TermsErrors: Use '\''consist of'\'' rather than '\''comprised of'\''.",
#         "path": "modules/private-clusters-about-gcp.adoc",
#         "line": 26
#     },
#     {
#         "body": "[error] RedHat.Spacing: Keep one space between words in '\''p.T'\''.",
#         "path": "modules/private-clusters-about-gcp.adoc",
#         "line": 26
#     }
# ]'

# Construct vale_json variable
vale_json=$(cat <<EOF
[{ "body": "[error] OpenShiftAsciiDoc.ModuleContainsContentType: Module is missing the '_mod-docs-content-type' variable.", "path": "modules/private-clusters-about-gcp.adoc", "line": 1 } ,{ "body": "[error] RedHat.TermsErrors: Use 'consist of' rather than 'comprised of'.", "path": "modules/private-clusters-about-gcp.adoc", "line": 26 } ,{ "body": "[error] RedHat.Spacing: Keep one space between words in 'p.T'.", "path": "modules/private-clusters-about-gcp.adoc", "line": 26 } ]
EOF
)


#  [{
#   body: "[error] OpenShiftAsciiDoc.ModuleContainsContentType: Module is missing the _mod-docs-content-type variable.",
#   path: "modules/private-clusters-about-gcp.adoc",
#   line: 1
# },
# {
#   body: "[error] RedHat.TermsErrors: Use 'consist of' rather than 'comprised of'.",
#   path: "modules/private-clusters-about-gcp.adoc",
#   line: 26
# },
# {
#   body: "[error] RedHat.Spacing: Keep one space between words in 'p.T'.",
#   path: "modules/private-clusters-about-gcp.adoc",
#   line: 26
# }]')

# Set pull_comment_json (for testing)
#pull_comment_json="test"

# Call the check_if_existing_comment function with vale_json and pull_comment_json as arguments
check_if_existing_comment "$vale_json"
