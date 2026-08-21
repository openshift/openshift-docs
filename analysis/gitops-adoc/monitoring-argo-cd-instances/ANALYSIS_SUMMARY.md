# JTBD Analysis Summary: Monitoring Argo CD Instances

**Document:** cicd/gitops/monitoring-argo-cd-instances.adoc  
**Analysis Date:** 2026-04-06  
**Processing Method:** Direct AsciiDoc parsing (asciidoctor-reducer not available)

## Document Overview

- **Assembly Type:** ASSEMBLY
- **Title:** Monitoring Argo CD instances
- **Total Includes:** 1 module
- **Module Types:** PROCEDURE (1)
- **Document Size:** Small (~24 lines reduced)

## Files Analyzed

1. **Assembly:** `cicd/gitops/monitoring-argo-cd-instances.adoc`
2. **Included Module:** `modules/gitops-monitoring-argo-cd-health-using-prometheus-metrics.adoc` (PROCEDURE)

## JTBD Records Extracted

**Total Records:** 3

### Record Breakdown by Workflow Stage

- **Configure:** 1 record (33%)
- **Operate:** 1 record (33%)
- **Troubleshoot:** 1 record (33%)

### Priority Distribution

- **High:** 2 records (67%)
- **Medium:** 1 record (33%)

### Taxonomy Categories

- **Monitor and troubleshoot:** 2 records
- **Set up and configure:** 1 record

## Key Jobs Identified

### JTBD-001: Monitor Deployed Applications
**Job Statement:** "When I have deployed Argo CD applications, I want to monitor their health status, so that I can detect and respond to synchronization issues before they impact users"

- **Persona:** Platform Administrator
- **Workflow Stage:** Operate
- **Priority:** High
- **Key Feature:** Automatic monitoring integration via GitOps Operator

### JTBD-002: Investigate Application Issues
**Job Statement:** "When I need to investigate Argo CD application issues, I want to query Prometheus metrics for health status, so that I can understand which applications are unhealthy and why"

- **Persona:** Platform Administrator
- **Workflow Stage:** Troubleshoot
- **Priority:** High
- **Key Feature:** Prometheus metrics queries via Developer perspective

### JTBD-003: Automatic Monitoring Setup
**Job Statement:** "When I install GitOps Operator, I want monitoring to be automatically configured, so that I don't have to manually set up observability infrastructure"

- **Persona:** Platform Administrator
- **Workflow Stage:** Configure
- **Priority:** Medium
- **Key Feature:** Zero-configuration monitoring

## Technical Details

### Prometheus Metrics Referenced

- **Primary Metric:** `argocd_app_info`
- **Query Parameters:** 
  - `dest_namespace`: Filter by namespace
  - `health_status`: Application health state
- **Aggregation:** Grouped by health_status

### Prerequisites Identified

1. Cluster-admin privileges
2. Access to OpenShift web console
3. GitOps Operator installed
4. Argo CD application deployed in namespace (e.g., openshift-gitops)

## Output Files Generated

```
analysis/gitops-adoc/monitoring-argo-cd-instances/
├── monitoring-argo-cd-instances-jtbd.jsonl
├── monitoring-argo-cd-instances-jtbd.csv
├── monitoring-argo-cd-instances-include-graph.json
├── monitoring-argo-cd-instances-reduced.adoc
└── ANALYSIS_SUMMARY.md
```

## Quality Notes

- All 3 records have complete fields (persona, context, needs, success criteria)
- Evidence fields include specific line references and module types
- Cross-references capture related technical concepts
- Taxonomy categories align with monitoring and configuration themes
- No conditional content (ifdef blocks) present in source

## Recommendations for JTBD Restructuring

1. **Consolidation Opportunity:** This content is tightly focused on a single job (monitoring). Consider combining with other monitoring topics in a "Monitor GitOps deployments" section.

2. **Related Jobs:** This content likely relates to:
   - Configuring alerts for Argo CD
   - Viewing Argo CD metrics dashboards
   - Troubleshooting sync failures

3. **User Journey:** The jobs span the full lifecycle:
   - **Setup:** Auto-configuration (JTBD-003)
   - **Daily Operations:** Health monitoring (JTBD-001)
   - **Problem Resolution:** Metric queries (JTBD-002)

4. **Cross-References to Explore:**
   - OpenShift monitoring stack configuration
   - Prometheus alerting rules
   - Grafana dashboard creation for Argo CD

## Analysis Limitations

- **Asciidoctor-reducer not available:** Manual include resolution performed instead of automated reduction
- **JTBD CLI not available:** Direct analysis performed without CLI workflow
- **No variant processing:** No conditional content found in source, so variant (self-managed/cloud-service) not applicable
- **Single module:** Small document with only one included module, minimal complexity
