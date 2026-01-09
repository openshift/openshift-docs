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

oc -n openshift-monitoring exec -c prometheus prometheus-k8s-0 -- \
  curl -s 'http://localhost:9090/api/v1/rules' | \
  jq -r '[ .data.groups[].rules[] | select(.type == "alerting") ] 
  | sort_by(.name | ascii_downcase)[]| 
  "| `\(.name)` | \(.labels.severity // "n/a") | \(.duration)s | \((.annotations.description // "No description") | gsub("\\|"; "\\|"))"' \
  >> $OUTPUT_FILE

echo "|===" >> $OUTPUT_FILE

echo "Extraction is completed. AsciiDoc table is generated in $OUTPUT_FILE"