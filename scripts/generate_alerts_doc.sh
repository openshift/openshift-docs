#!/bin/bash

# USE THIS SCRIPT TO GENERATE AN ASCIIDOC LIST OF ALERTS 
# INCLUDED IN A FRESH INSTALLATION OF THE CLUSTER.
# THE WRITER USED AWS CLUSTER

OUTPUT_FILE="openshift_cmo_alerts.adoc"

echo "Extracting CMO-managed alerts from the cluster..."

cat <<EOF > $OUTPUT_FILE
[options="header"]
|===
|Name |Severity |Duration |Description

EOF

# Extract alerts from openshift-monitoring PrometheusRules

# The jq filter performs the following operations:
# L46: Sorts alerts by name (case-insensitive)
# L47: Creates AsciiDoc table row with alert name, severity, duration, and description
# L48-L57: Clean up template syntax in descriptions, THE FOLLOWING LINES WERE CREATED WITH THE HELP OF AI:
#   - L48: Replace {{...$value...}} template patterns with simple "$value"
#   - L49: Extract label names from $labels.xxx patterns and replace with simplified format
#   - L50: Replace {{printf...}} function calls with "$value"
#   - L51: Replace nested template patterns {{...{...}...}} with "$value"
#   - L52: Remove any remaining {{...}} template patterns
#   - L53: Replace multiple consecutive "$value" occurrences with single "$value"
#   - L54: Replace "$values" with "$value" (singular form)
#   - L55: Replace multiple whitespace characters with single space
#   - L56: Trim leading and trailing whitespace
#   - L57: Escape pipe characters for AsciiDoc table format
oc get prometheusrules -n openshift-monitoring -o json | \
  jq -r '
    [
      .items[] |
      .spec.groups[]? |
      .rules[]? |
      select(.alert != null) |
      {
        name: .alert,
        severity: (.labels.severity // "n/a"),
        duration: (.for // "0s"),
        description: (.annotations.description // "No description")
      }
    ]
    | sort_by(.name | ascii_downcase)[] |
    "| `\(.name)` | \(.severity) | \(.duration) | \((.description
      | gsub("\\{\\{[^}]*\\$value[^}]*\\}\\}"; "$value")
      | (. as $text | [scan("\\{\\{[^}]*\\$labels\\.([a-zA-Z_]+)[^}]*\\}\\}") | .[0]] | unique as $labels | reduce $labels[] as $label ($text; gsub("\\{\\{[^}]*\\$labels\\." + $label + "[^}]*\\}\\}"; "$labels." + $label)))
      | gsub("\\{\\{\\s*printf[^}]*\\}\\}"; "$value")
      | gsub("\\{\\{[^{]*\\{[^}]*\\}[^}]*\\}\\}"; "$value")
      | gsub("\\{\\{[^}]*\\}\\}"; "")
      | gsub("\\$value\\$value\\$value"; "$value")
      | gsub("\\$values\\b"; "$value")
      | gsub("\\s+"; " ")
      | gsub("^\\s+|\\s+$"; "")
      | gsub("\\|"; "\\|")))"' \
  >> $OUTPUT_FILE

# Close the first table and start a new section for user workload monitoring
cat <<EOF >> $OUTPUT_FILE
|===

[options="header"]
|===
|Name |Severity |Duration |Description

EOF

# Extract alerts from openshift-user-workload-monitoring namespace, PrometheusRules
oc get prometheusrules -n openshift-user-workload-monitoring -o json | \
  jq -r '
    [
      .items[] |
      .spec.groups[]? |
      .rules[]? |
      select(.alert != null) |
      {
        name: .alert,
        severity: (.labels.severity // "n/a"),
        duration: (.for // "0s"),
        description: (.annotations.description // "No description")
      }
    ]
    | sort_by(.name | ascii_downcase)[] |
    "| `\(.name)` | \(.severity) | \(.duration) | \((.description
      | gsub("\\{\\{[^}]*\\$value[^}]*\\}\\}"; "$value")
      | (. as $text | [scan("\\{\\{[^}]*\\$labels\\.([a-zA-Z_]+)[^}]*\\}\\}") | .[0]] | unique as $labels | reduce $labels[] as $label ($text; gsub("\\{\\{[^}]*\\$labels\\." + $label + "[^}]*\\}\\}"; "$labels." + $label)))
      | gsub("\\{\\{\\s*printf[^}]*\\}\\}"; "$value")
      | gsub("\\{\\{[^{]*\\{[^}]*\\}[^}]*\\}\\}"; "$value")
      | gsub("\\{\\{[^}]*\\}\\}"; "")
      | gsub("\\$value\\$value\\$value"; "$value")
      | gsub("\\$values\\b"; "$value")
      | gsub("\\s+"; " ")
      | gsub("^\\s+|\\s+$"; "")
      | gsub("\\|"; "\\|")))"' \
  >> $OUTPUT_FILE

echo "|===" >> $OUTPUT_FILE

echo "Extraction completed. CMO-managed alerts are generated in $OUTPUT_FILE"
echo "This includes only alerts from:"
echo "  - openshift-monitoring namespace PrometheusRules"
echo "  - openshift-user-workload-monitoring namespace PrometheusRules"