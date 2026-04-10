# Removing GitOps — Consolidation Report

**Document:** removing_gitops-combined.adoc
**JTBD Records:** 3 records analyzed → 1 main job (2 user stories)

---

## Executive Summary

### What's Changing

The current "Removing GitOps" documentation organizes content by component (Argo CD instances, then Operator), presenting a linear two-section structure. While the procedural steps are clear, this organization buries critical sequencing information in the introduction. Users who skip directly to the "Uninstalling the GitOps Operator" section risk orphaning Argo CD instances by uninstalling the Operator first.

The proposed JTBD-based structure reorganizes the same content around the user's goal: "Completely Remove GitOps from My Cluster." This consolidates the two procedures under a single main job with explicit timing warnings that surface the critical ordering requirement at the point of decision, not buried in prose. The restructuring doesn't add or remove content — it elevates risk information to where users need it most.

### Key Improvements

- **Critical timing visibility:** Sequencing requirement (instances BEFORE Operator) moved from introduction prose to prominent job-level **TIMING** warning
- **Risk awareness:** Consequence of incorrect order (orphaned instances, namespace conflicts) stated in job-level **WHY** section
- **Method clarity:** UI vs CLI requirements labeled upfront (CLI-only for instances, UI-based for Operator)
- **Verification added:** Explicit verification task added to confirm complete removal (no orphaned CRDs/resources)
- **User confidence:** Step labels ("Required First Step" / "Required Second Step") make ordering impossible to miss
- **Navigation simplification:** 2 component-based sections → 1 goal-oriented job reduces top-level navigation by 50%

---

## Current Structure (Feature-Based)

- **Uninstalling OpenShift GitOps** — Assembly introduction
  - Introduction paragraph explaining two-step process
  - Warning that uninstalling only the Operator orphans instances
- **Deleting the Argo CD instances** — `[procedure]`
  - Procedure to delete from openshift-gitops namespace
  - Procedure to delete from other namespaces
  - Note: Cannot delete via web console UI
- **Uninstalling the GitOps Operator** — `[procedure]`
  - Procedure to navigate to OperatorHub
  - Search and locate GitOps tile
  - Click Uninstall
  - Additional resources section (link to general Operator deletion docs)

**Total:** 1 assembly with 2 main procedure sections (50 lines total), organized by component type (instances first, Operator second).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Clean Up**
  - Job 1: Completely Remove GitOps from My Cluster

### Detailed Job Descriptions

#### Clean Up

**Job 1: Completely Remove GitOps from My Cluster**

*When I need to completely remove GitOps from my cluster, I want to uninstall the Operator and all Argo CD instances, so I can ensure clean removal without orphaned resources.*

Prerequisites: Cluster administrator privileges, understand implications of removing GitOps workloads

**Timing:** CRITICAL — Must delete Argo CD instances BEFORE uninstalling Operator (uninstalling only the Operator orphans instances)

**Why:** Uninstalling the Operator alone does not remove Argo CD instances, causing orphaned resources and namespace conflicts in future installations

- **1.1. Delete All Argo CD Instances (Required First Step)** `[procedure]`
  - removing_gitops-combined.adoc, lines 11-33 (Section: Deleting the Argo CD instances): Delete gitopsservice resources from all namespaces using oc CLI
  - Context: Must use CLI — cannot delete Argo CD instances via web console UI
  - Steps:
    - Delete from openshift-gitops namespace: `oc delete gitopsservice cluster -n openshift-gitops`
    - Identify all other namespaces with Argo CD instances
    - Delete from each namespace: `oc delete gitopsservice cluster -n <namespace>`
    - Verify deletion complete before proceeding to step 1.2

- **1.2. Uninstall the GitOps Operator (Required Second Step)** `[procedure]`
  - removing_gitops-combined.adoc, lines 35-48 (Section: Uninstalling the GitOps Operator): Remove Red Hat OpenShift GitOps Operator via OperatorHub
  - Context: Use web console UI — simpler than CLI for Operator removal
  - Steps:
    - Navigate to Operators → OperatorHub
    - Search for "Red Hat OpenShift GitOps"
    - Click the Operator tile (indicates already installed)
    - Click Uninstall in descriptor page
  - Verification: Confirm Operator fully removed, check for no orphaned CRDs or resources
  - Additional resource: General Operator deletion documentation at https://docs.openshift.com/container-platform/latest/operators/admin/olm-deleting-operators-from-cluster.html

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By component type (instances, then Operator) | By user goal (complete removal) |
| **Top-level items** | 2 procedure sections | 1 main job with 2 required steps |
| **Critical timing** | Mentioned in introduction paragraph | Elevated to job-level **TIMING** warning |
| **Risk information** | Buried in prose ("will not remove") | Explicit **WHY** section (orphaned resources, namespace conflicts) |
| **UI vs CLI paths** | Discovered during reading | Labeled upfront in task descriptions |
| **Verification** | Not included | Explicit verification task in step 1.2 |
| **Step sequencing** | Implied by section order | Explicit labels: "Required First Step" / "Required Second Step" |

### Job List Adjustments from Suggested Input

The suggested 3 JTBD records were consolidated to **1 main job with 2 user stories** for the following reasons:

1. **Records 2 and 3 (both procedures) nested as user stories** → Both "Deleting instances" and "Uninstalling Operator" are implementation steps of the higher-level goal "Completely remove GitOps." Promoting them to separate main jobs would fragment a tightly coupled two-step process.

2. **Record 1 (assembly introduction) elevated to main job** → The assembly-level job statement captures the complete user goal. The two procedures become sub-steps (1.1 and 1.2) under this main job.

---

## Consolidation Examples

### Example 1: Critical Sequencing (Timing information scattered → Unified job-level warning)

**Current (Fragmented):**
- Introduction paragraph: "Uninstalling only the Operator will not remove the Argo CD instances created."
- Section 1: Deleting the Argo CD instances (no explicit timing warning)
- Section 2: Uninstalling the GitOps Operator (no reminder of ordering requirement)

**User Pain:** Users who skip the introduction and navigate directly to "Uninstalling the GitOps Operator" will orphan Argo CD instances. The critical ordering requirement is easy to miss.

**Proposed (Consolidated):**
- **Job 1: Completely Remove GitOps from My Cluster**
  - **TIMING:** CRITICAL — Must delete Argo CD instances BEFORE uninstalling Operator
  - **WHY:** Uninstalling the Operator alone orphans instances, causing namespace conflicts
  - 1.1. Delete All Argo CD Instances (Required First Step)
  - 1.2. Uninstall the GitOps Operator (Required Second Step)

**Benefit:** Timing constraint is impossible to miss — flagged at job level with CRITICAL marker, WHY section explaining consequences, and explicit step labels.

### Example 2: Method Requirements (UI/CLI paths discovered during reading → Labeled upfront)

**Current (Fragmented):**
- Section 1 (Deleting instances): User discovers CLI requirement in Note block during procedure execution
- Section 2 (Uninstalling Operator): Procedure assumes web console access

**User Pain:** Users planning their approach must read into each section to discover CLI vs UI requirements.

**Proposed (Consolidated):**
- **1.1. Delete All Argo CD Instances** 
  - Context: Must use CLI — cannot delete via web console UI
- **1.2. Uninstall the GitOps Operator**
  - Context: Use web console UI — simpler than CLI for Operator removal

**Benefit:** Method requirements visible before starting execution, enabling better planning (e.g., "I need oc CLI access before I can start").

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Troubleshooting failed deletions | Job 1.1 (Delete instances) | None — assumes commands succeed | **High** — Users with stuck resources or finalizers have no guidance; likely support ticket |
| Pre-removal backup guidance | Job 1 (Complete removal) | None — no mention of backing up configs | **Medium** — Users may lose GitOps application definitions; workaround: manual backup before starting |
| Explicit verification procedures | Job 1.2 (Uninstall Operator) | Generic "verify" mentioned, no specific steps | **Medium** — Users uncertain if removal is complete; workaround: check oc get operators |
| Identifying all namespaces with instances | Job 1.1 (Delete instances) | None — assumes user knows all namespaces | **Medium** — Users may miss Argo CD instances in non-default namespaces; partial removal risk |
| Handling applications managed by GitOps | Job 1 (Complete removal) | None — no guidance on application lifecycle | **Medium** — Users uncertain what happens to applications managed by Argo CD; workaround: check application resources first |
| CRD cleanup confirmation | Job 1.2 (Uninstall Operator) | Mentioned in verification, no specific commands | **Low** — Advanced users can check manually with oc get crds; nice-to-have explicit steps |
| Reinstallation considerations | Job 1 (Complete removal) | None — no guidance for future reinstalls | **Low** — Users planning to reinstall later have no namespace preparation guidance; workaround: wait for next install guide |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 2 sections (Deleting instances, Uninstalling Operator) | 1 job (Complete removal) | 50% reduction |
| Clicks to find "How to remove GitOps" | 2-3 (read intro, choose section) | 1 (Job 1 title) | ~60% reduction |
| Timing warning visibility | Buried in introduction prose (easy to skip) | Job-level CRITICAL flag (impossible to miss) | Risk awareness: 100% improvement |
| UI vs CLI path discovery | Must read into each section | Labeled in Context lines upfront | Planning efficiency: immediate visibility |
| Verification guidance | Not provided | Explicit verification task | Confidence: goes from implicit to explicit |

**Final job count: 1** (reduced from suggested 3 records). **Consolidation rationale:** The two procedures (deleting instances, uninstalling Operator) are tightly coupled steps in a single user goal (complete removal). Separating them would fragment a sequential process where step order is critical. By consolidating under one main job with two required sub-steps, the structure reflects the user's mental model ("I need to fully remove GitOps") and makes the ordering requirement explicit.

---

## Document Statistics

### Current Structure
- **Sections:** 2 main procedure sections
- **Line count:** 50 lines (combined document)
- **Modules:** 2 procedures (PROCEDURE type)
- **Timing warnings:** 1 (in prose introduction)

### Proposed Structure
- **Main Jobs:** 1 (consumption/decommissioning)
- **User Stories:** 2 (delete instances, uninstall Operator)
- **Total JTBD records analyzed:** 3
- **Timing warnings:** 3 (job-level TIMING, job-level WHY, step labels)
- **Verification steps:** 1 (added explicit verification task)

### Coverage by Workflow Stage
- **Conclude (Clean Up):** ✅ Fully covered
- **All other stages:** ❌ Not applicable (this is a removal guide)

### Content Type Distribution
- **Procedures:** 100% (both steps are procedural)
- **Concepts:** 0%
- **Reference:** 1 external link (general Operator deletion docs)
