#!/bin/bash

# USE THIS SCRIPT TO GENERATE AN ASCIIDOC LIST OF ALERTS 
# INCLUDED IN A FRESH INSTALLATION OF THE CLUSTER.
# THE WRITER USED AWS CLUSTER FOR THE 4.20 OCP VERSION.

OUTPUT_FILE="openshift_alerts.adoc"

echo "Extracting alerts from the cluster..."

cat <<EOF > $OUTPUT_FILE
|===
|Name |Severity |Duration |Description

EOF

# The oc command: connect to Prometheus pod and fetch alerting rules via API
# The jq filter performs the following operations:
# L35: Extracts all alerting rules from Prometheus API response
# L36: Sorts alerts by name (case-insensitive)
# L37: Creates AsciiDoc table row with alert name, severity, duration, and description
# L38-L47: Clean up Prometheus template syntax in descriptions, THE FOLLOWING LINES WERE CREATED WITH THE HELP OF AI:
#   - L38: Replace {{...$value...}} template patterns with simple "$value"
#   - L39: Extract label names from $labels.xxx patterns and replace with simplified format
#   - L40: Replace {{printf...}} function calls with "$value"
#   - L41: Replace nested template patterns {{...{...}...}} with "$value"
#   - L42: Remove any remaining {{...}} template patterns
#   - L43: Replace multiple consecutive "$value" occurrences with single "$value"
#   - L44: Replace "$values" with "$value" (singular form)
#   - L45: Replace multiple whitespace characters with single space
#   - L46: Trim leading and trailing whitespace
#   - L47: Escape pipe characters for AsciiDoc table format
oc -n openshift-monitoring exec -c prometheus prometheus-k8s-0 -- \
  curl -s 'http://localhost:9090/api/v1/rules' | \
  jq -r '[ .data.groups[].rules[] | select(.type == "alerting") ]
  | sort_by(.name | ascii_downcase)[]|
  "| `\(.name)` | \(.labels.severity // "n/a") | \(.duration)s | \((.annotations.description // "No description")
    | gsub("\\{\\{[^}]*\\$value[^}]*\\}\\}"; "$value")
    | (. as $text | [scan("\\{\\{[^}]*\\$labels\\.([a-zA-Z_]+)[^}]*\\}\\}") | .[0]] | unique as $labels | reduce $labels[] as $label ($text; gsub("\\{\\{[^}]*\\$labels\\." + $label + "[^}]*\\}\\}"; "$labels." + $label)))
    | gsub("\\{\\{\\s*printf[^}]*\\}\\}"; "$value")
    | gsub("\\{\\{[^{]*\\{[^}]*\\}[^}]*\\}\\}"; "$value")
    | gsub("\\{\\{[^}]*\\}\\}"; "")
    | gsub("\\$value\\$value\\$value"; "$value")
    | gsub("\\$values\\b"; "$value")
    | gsub("\\s+"; " ")
    | gsub("^\\s+|\\s+$"; "")
    | gsub("\\|"; "\\|"))"' \
  >> $OUTPUT_FILE

echo "|===" >> $OUTPUT_FILE

echo "Extraction is completed. AsciiDoc table is generated in $OUTPUT_FILE"