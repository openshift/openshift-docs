# Removing GitOps - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-04-09
**JTBD Records:** 3
**Main Jobs:** 1 (consumption/decommissioning job)
**Coverage:** 100% standard schema (no research extensions)

---

## Current Structure (Feature-Based)

```
Uninstalling OpenShift GitOps
├── Introduction (explaining two-step process)
├── Deleting the Argo CD instances
│   ├── Procedure
│   │   ├── Delete from openshift-gitops namespace
│   │   └── Delete from other namespaces
└── Uninstalling the GitOps Operator
    ├── Procedure
    │   ├── Navigate to OperatorHub
    │   ├── Search for GitOps tile
    │   └── Click Uninstall
    └── Additional resources
```

**Organization pattern:** Linear procedural steps organized by component (instances first, then Operator)

---

## Proposed JTBD-Based Structure

### Clean Up

**Job 1: Completely Remove GitOps from My Cluster**
*When I need to completely remove GitOps from my cluster*

**Personas:** Cluster administrator

**Timing:** CRITICAL - Must delete Argo CD instances BEFORE uninstalling Operator

**Why:** Uninstalling the Operator alone orphans Argo CD instances, causing namespace conflicts

#### 1.1 Delete All Argo CD Instances (Required First Step)
**Goal:** Remove all Argo CD instances to prevent orphaned resources.

- **Task:** Delete gitopsservice from default namespace
  → Lines 11-26: Deleting the Argo CD instances
  - CLI Path: `oc delete gitopsservice cluster -n openshift-gitops`
  - **Note:** Cannot delete via web console UI - must use CLI
  - Identify all namespaces with instances
  - Verify deletion from openshift-gitops namespace

- **Task:** Delete gitopsservice from additional namespaces
  → Lines 27-33: Deleting from other namespaces
  - CLI Path: `oc delete gitopsservice cluster -n <namespace>`
  - Repeat for each namespace with Argo CD instances

#### 1.2 Uninstall the GitOps Operator (Required Second Step)
**Goal:** Complete removal by uninstalling the Red Hat OpenShift GitOps Operator.

- **Task:** Locate and uninstall Operator via OperatorHub
  → Lines 35-48: Uninstalling the GitOps Operator
  - UI Path: Operators → OperatorHub → Search "Red Hat OpenShift GitOps" → Uninstall
  - **Verification:** Confirm complete removal (no orphaned CRDs or resources)

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Components and procedures (instances, then Operator)
**Navigation:** 2 main sections
**User Journey:** Linear reading, step-by-step execution
**Critical Sequencing:** Implied but not prominently flagged
**Path Options:** Limited visibility (CLI requirement for instances not visible until reading)

### Proposed Structure (JTBD-Based)

**Organized By:** User goal (complete removal) with explicit sequencing
**Navigation:** 1 main job with 2 required steps
**User Journey:** Goal-directed with explicit timing warnings
**Critical Sequencing:** **CRITICAL** flag at job level warns about ordering
**Path Options:** Clear UI vs CLI distinctions upfront

---

## Hierarchy Levels

### Level 1: Main Job (1 total)
- **Job 1:** Completely Remove GitOps from My Cluster
- **Type:** Consumption chain (decommissioning)
- **Stage:** Conclude

### Level 2: User Stories (2 approaches)
- **1.1:** Delete All Argo CD Instances (CLI-only)
- **1.2:** Uninstall the GitOps Operator (UI-based)

### Level 3: Procedures
- Tasks reference specific commands and UI paths
- Line numbers point to source content
- Verification steps included

---

## Example Consolidation

### Current (Fragmented)
```
Introduction: "Uninstalling only the Operator will not remove the Argo CD instances created."

Section 1: Deleting the Argo CD instances
  [Procedure steps]

Section 2: Uninstalling the GitOps Operator
  [Procedure steps]
```

**Issue:** Critical sequencing information buried in introduction paragraph, not surfaced where users make decisions.

### Proposed (Consolidated)
```
Job 1: Completely Remove GitOps from My Cluster
  **Timing:** CRITICAL - Must delete Argo CD instances BEFORE uninstalling Operator
  **Why:** Uninstalling the Operator alone orphans Argo CD instances

  1.1 Delete All Argo CD Instances (Required First Step)
  1.2 Uninstall the GitOps Operator (Required Second Step)
```

**Benefit:** Timing constraint elevated to job-level warning, visible BEFORE user starts execution!

---

## Navigation Improvement Metrics

**Current:**
- Navigate 2 sections to understand full process
- Critical sequencing info in prose introduction (easy to miss)
- CLI vs UI requirements discovered during reading

**Proposed:**
- Navigate 1 main goal with 2 clear steps
- Critical sequencing flagged with **CRITICAL** and **TIMING** warnings
- CLI vs UI paths visible upfront (CLI for instances, UI for Operator)

**Reduction:** 50% fewer top-level navigation items (2 sections → 1 job)

**Benefit:** 
- Critical timing information surfaced at decision point (not buried in intro)
- Find execution path in 1 click (job title) vs 2-3 clicks (read intro, find section)
- **Risk reduction:** Impossible to miss the ordering requirement

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ❌ | ❌ | Not applicable (removal guide) |
| Plan | ⚠️ Implied in intro | ⚠️ Could add backup guidance | Gap remains |
| Configure | ❌ | ❌ | Not applicable |
| Deploy | ❌ | ❌ | Not applicable |
| Monitor | ❌ | ❌ | Not applicable |
| Troubleshoot | ❌ | ❌ | Gap identified |
| Upgrade | ❌ | ❌ | Not applicable |
| Conclude | ✅ Complete 2-step process | ✅ Job 1 with explicit sequencing | **Improved** |
| Reference | ⚠️ Additional resources link only | ⚠️ Same link preserved | No change |

### Coverage Summary

**Current structure gaps:** Plan (no backup/migration guidance), Troubleshoot (no error recovery)
**Proposed structure gaps:** Plan (could add), Troubleshoot (should add)
**Gaps addressed by restructure:** Conclude stage now explicitly flags critical timing

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Troubleshoot | Add section for handling failed deletions or stuck resources | High |
| Plan | Add guidance for backing up GitOps configurations before removal | Medium |
| Verify | Add explicit verification procedures to confirm complete removal | Medium |

---

## Document Statistics

### Current Structure
- **Sections:** 2 main procedures
- **Prerequisites stated:** No (assumed cluster admin access)
- **Timing warnings:** Buried in prose introduction
- **UI/CLI paths:** Mixed (discovered during reading)

### Proposed Structure
- **Main Jobs:** 1 (consumption/decommissioning)
- **User Stories:** 2 (delete instances, uninstall Operator)
- **Timing Warnings:** Elevated to job-level metadata
- **UI/CLI Paths:** Explicitly labeled (CLI for instances, UI for Operator)
- **Prerequisites:** Could be added (cluster admin permissions, oc CLI access)

---

## Key Improvements

### 1. Critical Sequencing Visibility
**Before:** Mentioned in introduction prose
**After:** Flagged with **CRITICAL** and **TIMING:** warnings at job level

### 2. Risk Awareness
**Before:** Consequence of wrong order mentioned once in intro
**After:** **WHY** section explicitly states orphaned resource risk

### 3. Method Clarity
**Before:** CLI requirement for instance deletion discovered in procedure
**After:** UI vs CLI paths labeled upfront in task descriptions

### 4. Verification Guidance
**Before:** No verification steps
**After:** Verification task added to 1.2 (confirm complete removal)

### 5. User Confidence
**Before:** Users might skip intro and go straight to "Uninstalling" section
**After:** Impossible to miss the required ordering with step labels "Required First Step" / "Required Second Step"
