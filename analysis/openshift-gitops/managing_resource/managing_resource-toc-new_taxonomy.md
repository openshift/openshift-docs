# JTBD-Oriented Table of Contents
## Managing Resource Use Documentation

**Document:** managing_resource  
**Generated:** 2026-04-09  
**Total Jobs:** 17 (2 main jobs, 15 supporting jobs)

---

## Quick Navigation

| Workflow Stage | Jobs | User Stories | Tasks |
|----------------|------|--------------|-------|
| PLANNING | 0 | 1 | 1 |
| SETUP | 0 | 2 | 4 |
| OPERATIONS | 2 | 3 | 4 |

---

## 1. Resource Management for Argo CD Workloads

### Job 1: Manage Argo CD resource allocation
**Type:** MAIN_JOB | **Stage:** OPERATIONS  
**Persona:** Platform Administrator  
**Context:** Deploying and managing Argo CD instances in resource-constrained environments  
**Motivation:** ensure optimal performance and meet namespace resource quotas

> "With the Argo CD custom resource (CR), you can create, update, and delete resource requests and limits for Argo CD workloads."

**Source:** Lines 1-117 → Configuring resource quota or requests

#### Job 1.1: Configure resource requests and limits for initial deployment
**Type:** USER_STORY | **Stage:** SETUP  
**Persona:** Platform Administrator  
**Approach:** Define resources in Argo CD custom resource during instance creation  
**Alternatives:** Configure all components at once; Configure incrementally; Use default values  
**Acceptance Criteria:** All workload components have defined resource requirements; Instance deploys successfully in quota namespace; Resource allocation matches capacity planning

> "You can create Argo CD custom resource workloads with resource requests and limits. This is required when you want to deploy the Argo CD instance in a namespace that is configured with resource quotas."

**Source:** Lines 13-84 → Configuring workloads with resource requests and limits  
**Module Type:** REFERENCE

##### Task 1.1.1: Define Application Controller resource specifications
**Type:** TASK | **Stage:** SETUP  
**Context:** Configuring resource requirements in Argo CD custom resource  
**Steps:** Set CPU limits and requests; Set memory limits and requests  
**Tools:** Argo CD custom resource YAML

**Source:** Lines 13-84 → Configuring workloads with resource requests and limits

##### Task 1.1.2: Define ApplicationSet Controller resource specifications
**Type:** TASK | **Stage:** SETUP  
**Context:** Configuring resource requirements in Argo CD custom resource  
**Steps:** Set CPU limits and requests; Set memory limits and requests  
**Tools:** Argo CD custom resource YAML

**Source:** Lines 13-84 → Configuring workloads with resource requests and limits

##### Task 1.1.3: Define Server component resource specifications
**Type:** TASK | **Stage:** SETUP  
**Context:** Configuring resource requirements in Argo CD custom resource  
**Steps:** Set CPU limits and requests; Set memory limits and requests  
**Tools:** Argo CD custom resource YAML

**Source:** Lines 13-84 → Configuring workloads with resource requests and limits

#### Job 1.2: Update resource requirements post-installation
**Type:** USER_STORY | **Stage:** OPERATIONS  
**Persona:** Platform Administrator  
**Approach:** Use oc patch command with JSON patch operations  
**Alternatives:** Edit CR via web console; Apply updated YAML; Use GitOps approach  
**Acceptance Criteria:** Resource values updated without downtime; New limits applied to running pods; Performance meets expectations

> "You can update the resource requirements for all or any of the workloads post installation."

**Source:** Lines 86-103 → Patching Argo CD instance to update the resource requirements  
**Module Type:** PROCEDURE

##### Task 1.2.1: Patch Application Controller CPU request
**Type:** TASK | **Stage:** OPERATIONS  
**Context:** Modifying CPU allocation for running instance  
**Steps:** Run oc patch command with JSON path to CPU request field; Verify update  
**Tools:** oc CLI

**Source:** Lines 86-103 → Patching Argo CD instance to update the resource requirements

##### Task 1.2.2: Patch Application Controller memory request
**Type:** TASK | **Stage:** OPERATIONS  
**Context:** Modifying memory allocation for running instance  
**Steps:** Run oc patch command with JSON path to memory request field; Verify update  
**Tools:** oc CLI

**Source:** Lines 86-103 → Patching Argo CD instance to update the resource requirements

#### Job 1.3: Remove resource constraints
**Type:** USER_STORY | **Stage:** OPERATIONS  
**Persona:** Platform Administrator  
**Approach:** Use oc patch command with remove operation  
**Alternatives:** Apply CR without resource fields; Edit via web console  
**Acceptance Criteria:** Resource limits successfully removed; Workloads operate without constraints; No service interruption

> "You can also remove resource requirements for all or any of your workloads after installation."

**Source:** Lines 105-117 → Removing resource requests  
**Module Type:** PROCEDURE

##### Task 1.3.1: Remove Application Controller CPU constraint
**Type:** TASK | **Stage:** OPERATIONS  
**Context:** Removing CPU limits from running instance  
**Steps:** Run oc patch command with remove operation on CPU request path  
**Tools:** oc CLI

**Source:** Lines 105-117 → Removing resource requests

##### Task 1.3.2: Remove Application Controller memory constraint
**Type:** TASK | **Stage:** OPERATIONS  
**Context:** Removing memory limits from running instance  
**Steps:** Run oc patch command with remove operation on memory request path  
**Tools:** oc CLI

**Source:** Lines 105-117 → Removing resource requests

---

## 2. Resource Management for GitOps Console Plugin

### Job 2: Configure GitOps plugin resource allocation
**Type:** MAIN_JOB | **Stage:** OPERATIONS  
**Persona:** Platform Administrator  
**Context:** Managing OpenShift GitOps console plugin resource consumption  
**Motivation:** control memory usage and ensure stable performance

> "You can configure CPU and memory resource requests and limits for the {gitops-shortname} console plugin and its backend cluster components."

**Source:** Lines 119-260 → Configure resource requests and limits for GitOps plugin components

#### Job 2.1: Configure plugin component resource limits
**Type:** USER_STORY | **Stage:** SETUP  
**Persona:** Platform Administrator  
**Approach:** Edit GitOpsService custom resource to specify backend and plugin resources  
**Alternatives:** Use default values; Configure during operator installation  
**Acceptance Criteria:** Backend resources configured; Plugin resources configured; GitOpsService controller applies settings; Components run with specified limits

> "To enable resource configuration for the {gitops-shortname} plugin components, specify the .spec.consolePlugin.backend.resources field for the backend component and the .spec.consolePlugin.gitopsPlugin.resources field."

**Source:** Lines 141-217 → Enabling the GitOpsService custom resource  
**Module Type:** PROCEDURE

##### Task 2.1.1: Locate GitOpsService custom resource
**Type:** TASK | **Stage:** SETUP  
**Context:** Identifying the CR to configure  
**Steps:** Run oc get gitopsservice -A; Note namespace and name  
**Tools:** oc CLI

**Source:** Lines 141-217 → Enabling the GitOpsService custom resource

##### Task 2.1.2: Edit GitOpsService CR with resource specifications
**Type:** TASK | **Stage:** SETUP  
**Context:** Adding resource limits to console components  
**Steps:** Run oc edit command; Add backend.resources section; Add gitopsPlugin.resources section; Save changes  
**Tools:** oc CLI; Text editor

**Source:** Lines 141-217 → Enabling the GitOpsService custom resource

##### Task 2.1.3: Verify resource configuration applied
**Type:** TASK | **Stage:** SETUP  
**Context:** Validating resource limits are active  
**Steps:** Describe plugin pod; Check Limits section; Check Requests section; Confirm values match configuration  
**Tools:** oc CLI

**Source:** Lines 141-217 → Enabling the GitOpsService custom resource

#### Job 2.2: Understand resource configuration behavior
**Type:** USER_STORY | **Stage:** PLANNING  
**Persona:** Platform Administrator  
**Approach:** Review documentation on GitOpsService controller behavior  
**Alternatives:** Trial and error; Contact support  
**Acceptance Criteria:** Understand specified value behavior; Know default values; Can predict controller behavior

> "The following information describes how the GitOpsService controller applies resource values defined in the GitOpsService custom resource (CR)."

**Source:** Lines 219-260 → Behavior of resource configuration  
**Module Type:** CONCEPT

##### Task 2.2.1: Review default resource values
**Type:** TASK | **Stage:** PLANNING  
**Context:** Understanding baseline resource allocation  
**Steps:** Consult default values table; Note backend defaults (250m CPU, 128Mi memory requests); Note plugin defaults (250m CPU, 128Mi memory requests); Compare to requirements  
**Tools:** Documentation reference

**Source:** Lines 219-260 → Behavior of resource configuration

---

## Workflow Coverage

This documentation covers the complete lifecycle of resource management for GitOps components:

1. **PLANNING** ✓ — Understanding resource configuration behavior and defaults
2. **SETUP** ✓ — Initial resource allocation for new instances
3. **OPERATIONS** ✓ — Updating and removing resource constraints
4. **MONITORING** ⚠ — **Gap:** No coverage for monitoring actual resource consumption vs limits
5. **TROUBLESHOOTING** ⚠ — **Gap:** No guidance for diagnosing resource-related issues (OOMKilled pods, throttling)
6. **OPTIMIZATION** ⚠ — **Gap:** No guidance for right-sizing resources based on workload patterns

---

## Document Statistics

- **Total Sections:** 5
- **Main Jobs:** 2
- **User Stories:** 5
- **Tasks:** 10
- **Module Types:** 3 PROCEDURE, 1 REFERENCE, 1 CONCEPT
- **Workflow Coverage:** 3 of 6 stages (50%)
- **Primary Persona:** Platform Administrator (100%)
- **Average User Stories per Job:** 2.5
- **Average Tasks per User Story:** 2.0

---

## Content Gaps Identified

| Gap Area | Impact | Recommendation |
|----------|--------|----------------|
| Resource monitoring | High | Add procedures for viewing actual resource usage via metrics |
| Troubleshooting OOMKilled pods | High | Add procedure for diagnosing and resolving memory issues |
| Performance tuning | Medium | Add guidance for optimizing resource allocations based on usage patterns |
| Capacity planning | Medium | Add reference material on recommended resource values by cluster size |
| Multi-instance coordination | Low | Add guidance for managing resources across multiple Argo CD instances |

---

**Note:** This TOC reflects a JTBD-oriented reorganization of the content. The original structure groups content by technical components (Argo CD CR, GitOpsService CR), while this structure groups by user goals (manage Argo CD allocation, configure plugin allocation).
