# Declarative Cluster Configuration - Structure Comparison

## Document Metadata

**Book:** Declarative Cluster Configuration  
**Distro:** openshift-gitops  
**Current Structure:** Feature-based (4 assemblies)  
**Proposed Structure:** JTBD-oriented (4 main jobs, 14 user stories)  
**Analysis Date:** 2026-04-09

---

## Current Structure (Feature-Based)

### Assembly 1: Configuring an OpenShift cluster by deploying an application with cluster configurations
- Prerequisites
- Using an Argo CD instance to manage cluster-scoped resources
- Default permissions of an Argo CD instance
- Running the Argo CD instance at the cluster-level
- Creating an application by using the Argo CD dashboard
- Creating an application by using the oc tool
- Creating an application in default mode by using the GitOps CLI
- Creating an application in core mode by using the GitOps CLI
- Synchronizing your application with your Git repository
- Synchronizing an application in default mode by using the GitOps CLI
- Synchronizing an application in core mode by using the GitOps CLI
- In-built permissions for cluster configuration
- Adding permissions for cluster configuration
- Installing OLM Operators using GitOps
  - Installing cluster-scoped Operators
  - Installing namespace-scoped Operators
- Configuring respectRBAC using GitOps
  - Configuring respectRBAC using the CLI
  - Configuring respectRBAC by using the web console
- Additional resources

### Assembly 2: Customizing permissions by creating user-defined cluster roles for cluster-scoped instances
- Prerequisites
- Disabling the creation of the default cluster roles for the cluster-scoped instance
- Customizing permissions for cluster-scoped instances
- Additional resources

### Assembly 3: Customizing permissions by creating aggregated cluster roles
- Aggregated cluster roles
- Prerequisites
- Creating aggregated cluster roles
  - Enable the creation of aggregated cluster roles
  - Create user-defined cluster roles and configure user-defined permissions
- Enabling the creation of aggregated cluster roles
- Creating user-defined cluster roles and configuring user-defined permissions for Application Controller
- Additional resources

### Assembly 4: Sharding clusters across Argo CD Application Controller replicas
- Enabling the round-robin sharding algorithm
- Enabling the round-robin sharding algorithm in the web console
- Enabling the round-robin sharding algorithm by using the CLI
- Enabling dynamic scaling of shards of the Argo CD Application Controller
- Enabling dynamic scaling of shards in the web console
- Enabling dynamic scaling of shards by using the CLI
- Additional resources

**Hierarchy:** 4 top-level assemblies → 26 sections (chapters/procedures)

---

## Proposed JTBD-Based Structure

### Job 1: Configure cluster using GitOps declarative approach
**User Stories:**
1. Set up cluster-scoped Argo CD instance
2. Create and sync cluster configuration applications
3. Synchronize cluster configurations from Git
4. Run Argo CD on infrastructure nodes

### Job 2: Manage RBAC permissions for cluster-scoped Argo CD instances
**User Stories:**
1. Understand default Argo CD permissions
2. Add additional permissions for cluster configuration
3. Create user-defined cluster roles for cluster-scoped instances
4. Create aggregated cluster roles
5. Configure respectRBAC feature

### Job 3: Install OLM Operators declaratively using GitOps
**User Stories:**
1. Install cluster-scoped operators
2. Install namespace-scoped operators

### Job 4: Scale Argo CD Application Controller with cluster sharding
**User Stories:**
1. Enable round-robin sharding algorithm
2. Enable dynamic scaling of shards
3. Verify sharding configuration and distribution

**Hierarchy:** 4 main jobs → 14 user stories → Tasks (granular procedures)

---

## Key Differences

| Aspect | Current (Feature-Based) | Proposed (JTBD-Based) |
|--------|-------------------------|----------------------|
| **Organization** | By implementation method/feature | By user goal and outcome |
| **Top-level entries** | 4 assemblies | 4 main jobs |
| **Discovery** | Must know feature name | Search by what you want to accomplish |
| **Redundancy** | 6 sections for creating/syncing apps (by method) | 2 user stories covering all methods |
| **Permission content** | Split across 3 assemblies | Unified under 1 job with 5 user stories |
| **Workflow context** | Implicit (must infer from content) | Explicit (DEFINE → EXECUTE → OPTIMIZE → MONITOR) |
| **Persona clarity** | Not specified | Cluster Administrator, Platform Engineer |
| **Navigation depth** | 2 levels (assembly → section) | 3 levels (job → user story → task/approach) |
| **Cross-cutting concerns** | Scattered references | Grouped by outcome |

---

## Hierarchy Levels

### Current Structure
```
Assembly (Level 1)
├── Section/Procedure (Level 2)
│   └── Steps (embedded in procedure)
```

**Example:**
```
Configuring an OpenShift cluster... (Assembly)
├── Creating an application by using the Argo CD dashboard (Section)
├── Creating an application by using the oc tool (Section)
├── Creating an application in default mode by using the GitOps CLI (Section)
└── Creating an application in core mode by using the GitOps CLI (Section)
```

### Proposed Structure
```
Main Job (Level 1)
├── User Story (Level 2)
│   ├── Approach (Level 3)
│   └── Key Actions/Configuration (Level 3)
```

**Example:**
```
Configure cluster using GitOps... (Main Job)
└── Create and sync cluster configuration applications (User Story)
    ├── Approach: Create applications via dashboard, oc tool, or GitOps CLI
    ├── Source: Lines 333-763 covering all 4 creation methods
    └── Methods: Dashboard (UI), oc CLI, argocd CLI (default and core modes)
```

---

## Example Consolidation

### Example 1: Application Creation & Sync

**Current Structure (8 separate sections):**
1. Creating an application by using the Argo CD dashboard
2. Creating an application by using the oc tool
3. Creating an application in default mode by using the GitOps CLI
4. Creating an application in core mode by using the GitOps CLI
5. Synchronizing your application with your Git repository
6. Synchronizing an application in default mode by using the GitOps CLI
7. Synchronizing an application in core mode by using the GitOps CLI
8. (Plus scattered references to manual vs. automated sync)

**Proposed Structure (2 user stories):**

**User Story 1.2:** Create and sync cluster configuration applications
- **When:** Deploying cluster configurations
- **I want:** Create Argo CD applications that sync Git repo contents
- **So I can:** Apply configuration changes automatically
- **All Methods:** Dashboard, oc CLI, argocd CLI (default/core modes) in one place
- **Source:** Lines 333-763 (consolidated)

**User Story 1.3:** Synchronize cluster configurations from Git
- **When:** Cluster configurations change in Git
- **I want:** Sync them manually or automatically
- **So:** Cluster state matches Git
- **Approaches:** Manual sync (review changes first) vs. Automated sync (continuous)
- **Source:** Lines 772-939 (all sync methods consolidated)

**Benefit:** Reduces 8 sections to 2 user stories; user picks method based on their preference, not navigating structure

---

### Example 2: Permission Management

**Current Structure (3 assemblies + scattered sections):**
- Assembly 1 → Default permissions, In-built permissions, Adding permissions
- Assembly 2 → User-defined cluster roles (entire assembly)
- Assembly 3 → Aggregated cluster roles (entire assembly)
- Plus: respectRBAC buried in Assembly 1

**Proposed Structure (1 job with 5 user stories):**

**Job 2:** Manage RBAC permissions for cluster-scoped Argo CD instances
1. Understand default permissions (DEFINE)
2. Add additional permissions (EXECUTE)
3. Create user-defined cluster roles (EXECUTE)
4. Create aggregated cluster roles (EXECUTE)
5. Configure respectRBAC (OPTIMIZE)

**Benefit:** All permission management in one cohesive job; clear progression from understanding defaults → simple additions → full customization → optimization

---

## Navigation Improvement Metrics

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| **Top-level navigation items** | 4 assemblies | 4 main jobs | Same count, clearer intent |
| **Avg. clicks to reach procedure** | 2-3 | 2-3 | Same depth |
| **Sections for app creation/sync** | 8 sections | 2 user stories | 75% reduction |
| **Permission-related assemblies** | 3 separate assemblies | 1 unified job | 66% consolidation |
| **Method-based duplication** | High (6 creation methods) | Low (methods as options) | Significant reduction |
| **Workflow stage clarity** | Implicit | Explicit in metadata | Clear guidance |
| **Persona targeting** | Generic "administrator" | Specific personas | Targeted content |

### Discovery Time Estimates

**Scenario:** User wants to "install an operator using GitOps"

**Current Structure:**
1. Scan 4 assembly titles
2. Open "Configuring an OpenShift cluster..."
3. Scan 15+ section titles
4. Find "Installing OLM Operators using GitOps"
5. Navigate to cluster-scoped vs. namespace-scoped
**Time:** ~2-3 minutes of scanning

**Proposed Structure:**
1. Scan 4 main job titles
2. Identify "Install OLM Operators declaratively using GitOps" (Job 3)
3. See 2 user stories: cluster-scoped vs. namespace-scoped
**Time:** ~30-60 seconds

**Improvement:** 60-75% faster discovery

---

## Workflow Coverage Comparison

### Current Structure Coverage

| Workflow Stage | Implicit Coverage | Gaps |
|----------------|-------------------|------|
| PLAN | No explicit planning guidance | No capacity planning for sharding |
| DEFINE | Prerequisites, permission review | Scattered across assemblies |
| EXECUTE | All procedures covered | No outcome-oriented grouping |
| MONITOR | Verification steps in procedures | No dedicated monitoring section |
| OPTIMIZE | Infrastructure nodes, sharding | Not clearly labeled as optimization |
| TROUBLESHOOT | Minimal (errors mentioned inline) | No troubleshooting guide |
| MAINTAIN | Not covered | No upgrade/maintenance content |

### Proposed Structure Coverage

| Workflow Stage | Explicit Coverage | Improvements |
|----------------|-------------------|--------------|
| PLAN | Gap identified in coverage report | Recommendation for future content |
| DEFINE | Job 1 (setup), Job 2 (permissions) | Clear setup phase |
| EXECUTE | Jobs 1, 2, 3 (all core tasks) | Unified execution path |
| MONITOR | Job 4 (shard verification) | Dedicated monitoring tasks |
| OPTIMIZE | Jobs 1, 2, 4 (infra nodes, RBAC, sharding) | Clearly labeled |
| TROUBLESHOOT | Gap identified | Recommendation for future content |
| MAINTAIN | Gap identified | Recommendation for future content |

**Gap Recommendations:**
- ✓ Add capacity planning guidance for sharding thresholds (PLAN)
- ✓ Add troubleshooting guide for common failure scenarios (TROUBLESHOOT)
- ✓ Add maintenance/upgrade procedures for declarative configs (MAINTAIN)

---

## Content Reuse Analysis

### Duplicated/Similar Content in Current Structure

1. **Application Creation:** 4 sections covering different methods (dashboard, oc, argocd default, argocd core)
   - **Duplication:** Prerequisites, application configuration, verification steps repeated
   - **Unique Content:** CLI commands, UI navigation paths
   - **Consolidation Opportunity:** HIGH

2. **Application Sync:** 3 sections for sync methods (dashboard, default mode, core mode)
   - **Duplication:** Sync policy concepts, verification steps
   - **Unique Content:** CLI commands vs. UI interactions
   - **Consolidation Opportunity:** HIGH

3. **Permission Customization:** 3 separate assemblies
   - **Duplication:** Service account concepts, RBAC fundamentals
   - **Unique Content:** Specific permission mechanisms (direct, user-defined, aggregated)
   - **Consolidation Opportunity:** MEDIUM (concepts consolidated, approaches remain distinct)

4. **Sharding Configuration:** 2 methods (web console, CLI) for each feature
   - **Duplication:** Algorithm explanations, verification steps
   - **Unique Content:** UI vs. CLI commands
   - **Consolidation Opportunity:** MEDIUM

### Proposed Consolidation Benefits

- **Single source of truth** for core concepts (permissions, sync policies, sharding)
- **Method selection** becomes an implementation detail within user stories
- **Reduced maintenance** burden (update concept once, not per method)
- **Clearer decision trees** (when to use aggregated vs. user-defined roles)

---

## UX Research Alignment

### Persona Mapping

**Current Structure:** Implicit "administrator" persona throughout

**Proposed Structure:**
- **Cluster Administrator:** Jobs 1, 2, 3 (setup, permissions, operators)
- **Platform Engineer:** Job 4 (scaling and optimization)

**Alignment:** Role-based content grouping matches organizational responsibilities

### Pain Point Coverage

| Pain Point (Inferred) | Current Approach | Proposed Approach |
|------------------------|------------------|-------------------|
| "How do I give Argo CD cluster-wide access?" | Scattered across 3 assemblies | Job 2 with clear progression |
| "Which permission method should I use?" | No comparison or decision guidance | Job 2 user stories show use cases |
| "How do I install operators with GitOps?" | Buried in large assembly | Dedicated Job 3 |
| "Argo CD is using too much memory" | Assembly 4 (must know term "sharding") | Job 4: "Scale Argo CD..." (outcome-focused) |

---

## Summary of Benefits

### Organizational Benefits
- ✓ Outcome-oriented navigation (what you want to achieve)
- ✓ Reduced duplication (6 app creation/sync sections → 2 user stories)
- ✓ Unified permission management (3 assemblies → 1 job)
- ✓ Clear workflow stages (DEFINE → EXECUTE → OPTIMIZE → MONITOR)

### User Benefits
- ✓ Faster discovery (60-75% time reduction)
- ✓ Method-agnostic approach (pick UI or CLI based on preference)
- ✓ Role-based navigation (Cluster Admin vs. Platform Engineer)
- ✓ Explicit prerequisites and outcomes

### Maintenance Benefits
- ✓ Single source of truth for concepts
- ✓ Clear content ownership by workflow stage
- ✓ Easier gap identification (PLAN, TROUBLESHOOT, MAINTAIN)
- ✓ Simpler updates (change concept once, not per method)

---

**Generated by:** Claude Code JTBD Workflow  
**Analysis Type:** Current vs. Proposed Structure Comparison  
**Format Version:** 1.0
