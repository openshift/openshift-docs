# Removing GitOps
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Remove Red Hat OpenShift GitOps from an OpenShift cluster completely and cleanly.

**Personas:** Cluster administrator

**Main Jobs:** 1 core consumption job across the Conclude workflow stage

---

## Quick Navigation

**I want to:**
- Remove GitOps from my cluster → Job 1 (Conclude)
- Delete Argo CD instances → Job 1 (Conclude)
- Uninstall the GitOps Operator → Job 1 (Conclude)

---

# Table of Contents

## Clean Up

### Job 1: Completely Remove GitOps from My Cluster
*When I need to completely remove GitOps from my cluster*

**Personas:** Cluster administrator

**Timing:** CRITICAL - Must delete Argo CD instances BEFORE uninstalling Operator - uninstalling only the Operator will orphan Argo CD instances

**Why:** Uninstalling the Operator alone does not remove Argo CD instances, which can cause orphaned resources and namespace conflicts in future installations

#### 1.1 Delete All Argo CD Instances (Required First Step)
**Goal:** Remove all Argo CD instances to prevent orphaned resources when the Operator is removed.

- **Task:** Delete gitopsservice from default namespace
  → Lines 11-26: Deleting the Argo CD instances
    Source: removing_gitops-combined.adoc, Section "Deleting the Argo CD instances"
  - Run `oc delete gitopsservice cluster -n openshift-gitops`
  - Note: Cannot delete via web console UI - must use CLI
  - Verify instances are deleted from openshift-gitops namespace

- **Task:** Delete gitopsservice from additional namespaces
  → Lines 27-33: Deleting from other namespaces
    Source: removing_gitops-combined.adoc, Section "Deleting the Argo CD instances"
  - Identify all namespaces with Argo CD instances
  - Run `oc delete gitopsservice cluster -n <namespace>` for each

#### 1.2 Uninstall the GitOps Operator (Required Second Step)
**Goal:** Complete the removal process by uninstalling the Red Hat OpenShift GitOps Operator.

- **Task:** Locate and uninstall Operator via OperatorHub
  → Lines 35-48: Uninstalling the GitOps Operator
    Source: removing_gitops-combined.adoc, Section "Uninstalling the GitOps Operator"
  - Navigate to Operators → OperatorHub in web console
  - Search for "Red Hat OpenShift GitOps"
  - Click the Operator tile and select Uninstall

- **Verification:** Confirm complete removal
  - Verify Operator is fully removed
  - Check for remaining CRDs or resources
  - Ensure no namespace conflicts exist

---

## Appendices

### A. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ❌ | - | Not applicable for removal guide |
| Plan | ❌ | - | No planning/decision content |
| Configure | ❌ | - | No configuration content |
| Deploy | ❌ | - | Not applicable for removal guide |
| Monitor | ❌ | - | No monitoring content |
| Troubleshoot | ❌ | - | No troubleshooting content |
| Upgrade | ❌ | - | Not applicable for removal guide |
| Conclude | ✅ | Job 1 | Complete decommissioning workflow |

### B. Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Troubleshoot | No troubleshooting for removal issues | Add section for handling failed deletions or stuck resources |
| Plan | No backup/migration guidance | Add section for backing up configurations before removal |
| Verify | No verification procedures | Add explicit verification steps to confirm complete removal |

### C. Additional Resources

**Related Documentation:**
- General Operator deletion on OpenShift: https://docs.openshift.com/container-platform/latest/operators/admin/olm-deleting-operators-from-cluster.html

**Common Next Steps:**
- Back up GitOps configurations before removal
- Document applications managed by GitOps
- Plan alternative deployment approaches if needed

---

## Navigation Guide

### By User Journey

**Cluster Administrator removing GitOps:**
1. Job 1.1: Delete all Argo CD instances (CLI required)
2. Job 1.2: Uninstall the GitOps Operator (web console)
3. Verify complete removal (no orphaned resources)

---

## Document Statistics

**Workflow Coverage:**
- Conclude: 1 job (Complete)
- All other stages: Not applicable (removal guide)

**Main Jobs:** 1

**User Stories/Approaches:** 2 (Delete instances, Uninstall Operator)

**Source Sections:** 3 (Assembly introduction, 2 procedures)

**Critical Sequencing:** 1 (instances MUST be deleted before Operator)
