# JTBD Analysis Summary: Installing OpenShift GitOps

**Analysis Date:** 2026-04-06  
**Source Assembly:** `cicd/gitops/installing-openshift-gitops.adoc`  
**Processing Method:** Single-pass analysis (document < 500 lines)

## Document Overview

This assembly covers the installation and initial setup of OpenShift GitOps Operator, which provides Argo CD capabilities for declarative GitOps-based cluster and application management.

### Source Modules Analyzed

1. **modules/installing-gitops-operator-in-web-console.adoc** (PROCEDURE)
   - Installation via OperatorHub web UI
   - Channel and version selection
   - Namespace configuration and monitoring

2. **modules/installing-gitops-operator-using-cli.adoc** (PROCEDURE)
   - CLI-based installation workflow
   - Namespace, OperatorGroup, and Subscription creation
   - Pod verification steps

3. **modules/logging-in-to-the-argo-cd-instance-by-using-the-argo-cd-admin-account.adoc** (PROCEDURE)
   - Argo CD UI access methods
   - OpenShift SSO integration
   - Admin password retrieval

## JTBD Extraction Results

**Total Jobs Extracted:** 13

### Distribution by Workflow Stage
- **Setup:** 11 jobs (85%)
- **Planning:** 2 jobs (15%)

### Distribution by Importance
- **Critical:** 8 jobs (62%)
- **Medium:** 5 jobs (38%)

### Distribution by Job Performer
- **Cluster administrator:** 7 jobs (54%)
- **Cluster administrator, Platform engineer:** 3 jobs (23%)
- **Cluster administrator, Developer:** 2 jobs (15%)
- **Cluster administrator, SRE, Platform engineer:** 1 job (8%)

## Key Job Categories

### 1. Installation Jobs (Primary)
- Install via web console
- Install via CLI
- Select update channel and version
- Choose installation namespace
- Verify installation success

### 2. Prerequisites and Planning
- Understand prerequisites
- Remove community Argo CD Operator (if applicable)

### 3. CLI-Specific Setup
- Create namespace and OperatorGroup
- Create and apply Subscription
- Verify pod status

### 4. Access and Authentication
- Access Argo CD UI from console
- Log in with OpenShift credentials
- Retrieve admin password from secrets

## Key Insights

### User Personas
- **Primary:** Cluster administrators responsible for platform setup
- **Secondary:** Platform engineers automating deployments
- **Tertiary:** Developers accessing GitOps UI

### Critical User Needs
1. **Choice of installation method:** Web console vs CLI (different use cases)
2. **Version control:** Ability to select specific Operator versions via channels
3. **Verification:** Clear steps to confirm successful installation
4. **Access flexibility:** Multiple login methods (SSO vs admin credentials)

### Documentation Gaps Identified
1. **Community Operator removal:** Warning present but no removal procedure provided
2. **Troubleshooting:** No guidance for installation failures
3. **Post-installation:** Limited guidance on next steps after login

## Workflow Observations

### Installation Decision Tree
```
Prerequisites Check
    ↓
Remove Community Operator (if present)
    ↓
Choose Installation Method
    ├─→ Web Console (interactive)
    │   └─→ Select channel/version
    │       └─→ Choose namespace
    │           └─→ Enable monitoring
    │               └─→ Verify in UI
    │
    └─→ CLI (automation)
        └─→ Create namespace
            └─→ Create OperatorGroup
                └─→ Create Subscription
                    └─→ Verify pods
    ↓
Access Argo CD
    ├─→ OpenShift SSO login
    └─→ Admin password login
```

### Frequency Patterns
- **One-time setup:** Installation, prerequisite checks (most jobs)
- **Per-session:** Logging in to Argo CD UI
- **Rare:** Retrieving admin password (troubleshooting)

## Files Generated

1. **installing-openshift-gitops-reduced.adoc** (162 lines)
   - Flattened assembly with all includes resolved
   
2. **installing-openshift-gitops-jtbd.jsonl** (13 records)
   - Complete JTBD records in JSON Lines format
   
3. **installing-openshift-gitops-jtbd.csv** (14 lines including header)
   - Spreadsheet-friendly format for review
   
4. **installing-openshift-gitops-include-graph.json**
   - Source module mapping and metadata

## Recommended Next Steps

1. **Generate JTBD TOC:** Run `/jtbd-toc` to create user-goal-oriented structure
2. **Compare structures:** Run `/jtbd-compare` to contrast with current organization
3. **Identify consolidation opportunities:** Look for overlapping jobs between web console and CLI methods
4. **Gap analysis:** Address missing content for community operator removal

## Quality Notes

- All job statements follow "When [situation], I want to [motivation], so I can [outcome]" format
- Evidence fields include line numbers and source module references
- Module types (PROCEDURE) correctly identified
- Jobs properly categorized by workflow stage and importance
- Performer roles aligned with prerequisite requirements (cluster-admin)
