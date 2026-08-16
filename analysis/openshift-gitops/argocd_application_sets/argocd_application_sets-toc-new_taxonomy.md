# JTBD-Oriented Table of Contents
## Argo CD Application Sets

**Document**: argocd_application_sets  
**Distro**: openshift-gitops  
**Generated**: 2026-04-09  
**Total Jobs**: 3 main jobs, 21 total records

---

## Quick Navigation

### By Workflow Stage
- **LEARN** (2 jobs): Understanding strategies and concepts
- **PLAN** (1 job): Choosing deployment strategies
- **CONFIGURE** (12 jobs): Setting up ApplicationSets and Progressive Sync
- **EXECUTE** (2 jobs): Managing and controlling deployments
- **MONITOR** (1 job): Tracking deployment health
- **TROUBLESHOOT** (2 jobs): Resolving Progressive Sync issues

### By Persona
- **Cluster Administrator** (6 jobs): Infrastructure configuration and security
- **Platform Engineer** (14 jobs): Deployment orchestration and monitoring

---

## Table of Contents

### 1. [Manage ApplicationSets across multiple namespaces](#job-1)
Setup and Configuration for Multitenancy

### 2. [Control progressive application rollouts](#job-2)
Staged Deployment Orchestration

### 3. [Monitor progressive deployment health](#job-3)
Real-time Rollout Visibility

---

## Job Details

<a name="job-1"></a>
### 1. Manage ApplicationSets across multiple namespaces

**Main Job**  
**Persona**: Cluster Administrator  
**Stage**: EXECUTE  
**Why**: To support multitenancy and allow teams to manage their own ApplicationSet deployments in isolated namespaces

**Approach**: Enable ApplicationSet resources in non-control plane namespaces by configuring the ArgoCD CR

**Source**:
-> Lines 124-228: Managing the application set resources in non-control plane namespaces

**Notes**: Technology Preview feature. Source: modules/gitops-enabling-the-application-set-resources-in-non-control-plane-namespaces.adoc (PROCEDURE)

---

#### 1.1 Enable ApplicationSet resources in specific namespaces
**User Story** | **Stage**: CONFIGURE  
**Why**: To explicitly define which non-control plane namespaces can create and manage ApplicationSet resources

**Tasks**:
1. Set the sourceNamespaces parameter in the applicationSet spec of the ArgoCD CR
   - Source: Lines 176-228
   - Notes: Requires setting spec.applicationSet.sourceNamespaces. Creates RBAC resources automatically

---

#### 1.2 Control ApplicationSet permissions using namespace patterns
**User Story** | **Stage**: CONFIGURE  
**Why**: To grant permissions across multiple namespaces efficiently without listing each one individually

**Tasks**:
1. Use explicit names, glob patterns, or regex patterns in sourceNamespaces field
   - Source: Lines 239-253
   - Notes: Supports explicit names, glob-style wildcards, and regex patterns. Evaluated at reconcile time

---

#### 1.3 Enable ApplicationSet in a specific namespace by name
**User Story** | **Stage**: CONFIGURE  
**Why**: To grant ApplicationSet permissions to a single, well-known namespace

**Tasks**:
1. Add the namespace name directly to spec.applicationSet.sourceNamespaces
   - Source: Lines 264-288
   - Notes: Simplest approach for single namespace

---

#### 1.4 Grant ApplicationSet permissions using glob wildcards
**User Story** | **Stage**: CONFIGURE  
**Why**: To grant permissions across multiple namespaces that share a common naming convention

**Tasks**:
1. Use glob-style wildcard patterns like team-* in sourceNamespaces
   - Source: Lines 299-323
   - Notes: Example: team-* matches team-1, team-2

---

#### 1.5 Control ApplicationSet access using regular expressions
**User Story** | **Stage**: CONFIGURE  
**Why**: To precisely control which namespaces receive permissions using complex matching rules

**Tasks**:
1. Use regex patterns wrapped in forward slashes in sourceNamespaces field
   - Source: Lines 334-374
   - Notes: Patterns must be wrapped in /pattern/ format. Requires Apps in Any Namespace to be enabled

---

#### 1.6 Secure SCM Provider access for ApplicationSets
**User Story** | **Stage**: CONFIGURE  
**Why**: To prevent secret exfiltration through malicious API endpoints while enabling SCM Provider and PR generators

**Tasks**:
1. Define allowed SCM Provider URLs in spec.applicationSet.scmProviders
   - Source: Lines 385-427
   - Notes: SCM Provider and PR generators disabled by default for security. Must explicitly allow URLs

---

<a name="job-2"></a>
### 2. Control progressive application rollouts

**Main Job**  
**Persona**: Platform Engineer  
**Stage**: EXECUTE  
**Why**: To orchestrate safe, staged rollouts of changes across multiple clusters with visibility into health and progress

**Approach**: Enable and configure Progressive Sync with ApplicationSet strategies

**Source**:
-> Lines 443-623: Using Progressive Sync in OpenShift GitOps

**Notes**: Technology Preview feature. Manages synchronization across multiple clusters

---

#### 2.1 Enable Progressive Sync feature in GitOps
**User Story** | **Persona**: Cluster Administrator | **Stage**: CONFIGURE  
**Why**: To activate Progressive Sync functionality for ApplicationSet controllers

**Tasks**:
1. Add extraCommandArgs or set env variable in Argo CD CR to enable Progressive Sync
   - Source: Lines 642-744
   - Notes: Two methods: extraCommandArgs with --enable-progressive-syncs, or env variable ARGOCD_APPLICATIONSET_CONTROLLER_ENABLE_PROGRESSIVE_SYNCS

---

#### 2.2 Enable Progressive Sync using command arguments
**User Story** | **Persona**: Cluster Administrator | **Stage**: CONFIGURE  
**Why**: To enable Progressive Sync using the command argument method

**Tasks**:
1. Add --enable-progressive-syncs to spec.applicationSet.extraCommandArgs in ArgoCD CR
   - Source: Lines 660-696
   - Notes: Operator automatically reconciles and updates ApplicationSet controller deployment

---

#### 2.3 Enable Progressive Sync using environment variable
**User Story** | **Persona**: Cluster Administrator | **Stage**: CONFIGURE  
**Why**: To enable Progressive Sync using the environment variable method

**Tasks**:
1. Set ARGOCD_APPLICATIONSET_CONTROLLER_ENABLE_PROGRESSIVE_SYNCS=true in spec.applicationSet.env
   - Source: Lines 707-744
   - Notes: Alternative to extraCommandArgs. Operator automatically reconciles

---

#### 2.4 Understand ApplicationSet lifecycle strategies
**User Story** | **Stage**: LEARN  
**Why**: To choose appropriate strategies for controlling application deployment patterns and cleanup sequences

**Tasks**:
1. Review creation and deletion strategy options for ApplicationSets
   - Source: Lines 755-773
   - Notes: Two components: creation strategy (type field) and deletion strategy (deletionOrder field). Finalizer prevents removal until all apps deleted

---

#### 2.5 Choose between AllAtOnce and RollingSync creation
**User Story** | **Stage**: PLAN  
**Why**: To select the creation strategy that matches deployment risk tolerance and dependency requirements

**Tasks**:
1. Evaluate AllAtOnce for simultaneous updates vs RollingSync for staged rollouts
   - Source: Lines 784-803
   - Notes: AllAtOnce = default, all apps simultaneously. RollingSync = staged by labels. Apps not matched by any step must be manually synced

---

#### 2.6 Deploy applications simultaneously with AllAtOnce
**User Story** | **Stage**: CONFIGURE  
**Why**: To update all applications managed by the ApplicationSet at the same time

**Tasks**:
1. Set spec.strategy.type to AllAtOnce in ApplicationSet
   - Source: Lines 815-946
   - Notes: Default behavior. Suitable for independent applications without dependencies

---

#### 2.7 Deploy applications in stages with RollingSync
**User Story** | **Stage**: CONFIGURE  
**Why**: To control deployment progression through environment stages and reduce risk with staged rollouts

**Tasks**:
1. Set spec.strategy.type to RollingSync and define steps with label selectors
   - Source: Lines 957-1144
   - Notes: Requires labels on generated apps. Steps process sequentially. maxUpdate controls concurrent updates within a step. Progressive Sync panel displays rollout status in UI

---

#### 2.8 Understand deletion order strategies
**User Story** | **Stage**: LEARN  
**Why**: To choose appropriate strategy for tearing down applications in the correct order

**Tasks**:
1. Review AllAtOnce and Reverse deletion strategies
   - Source: Lines 1155-1177
   - Notes: AllAtOnce = default, all deleted simultaneously. Reverse = delete in reverse order of rollingSync.steps. Useful for dependent services

---

#### 2.9 Delete applications simultaneously with AllAtOnce
**User Story** | **Stage**: CONFIGURE  
**Why**: To remove all applications at the same time when they don't have deletion dependencies

**Tasks**:
1. Set spec.strategy.deletionOrder to AllAtOnce
   - Source: Lines 1189-1328
   - Notes: Default deletion behavior. Works with both AllAtOnce and RollingSync creation strategies. Finalizer ensures cleanup before ApplicationSet removed

---

#### 2.10 Delete applications in reverse order
**User Story** | **Stage**: CONFIGURE  
**Why**: To ensure dependent services are deleted in the correct sequence (e.g., frontend before backend)

**Tasks**:
1. Set spec.strategy.deletionOrder to Reverse with RollingSync type
   - Source: Lines 1339-1490
   - Notes: Requires type: RollingSync with defined rollingSync.steps. Deletes in reverse order of steps

---

#### 2.11 Troubleshoot Progressive Sync visibility issues
**User Story** | **Stage**: TROUBLESHOOT  
**Why**: To diagnose why the Progressive Sync panel is not appearing in the Application details view

**Tasks**:
1. Verify Progressive Sync is enabled and ApplicationSet uses RollingSync strategy
   - Source: Lines 1501-1539
   - Notes: Common issues: section not appearing or Unknown state. Verify RollingSync strategy and Progressive Sync enabled in ArgoCD CR

---

#### 2.12 Diagnose Unknown application state in Progressive Sync
**User Story** | **Stage**: TROUBLESHOOT  
**Why**: To resolve Unknown state errors in Progressive Sync status

**Tasks**:
1. Check labels, annotations, namespace location, and ApplicationSet controller logs
   - Source: Lines 1550-1558
   - Notes: Verify labels/annotations, same namespace as ArgoCD instance, and check controller logs

---

<a name="job-3"></a>
### 3. Monitor progressive deployment health

**Main Job**  
**Persona**: Platform Engineer  
**Stage**: MONITOR  
**Why**: To track rollout progress, identify bottlenecks, and ensure compliance with deployment policies

**Approach**: Use the Progressive Sync status panel in Argo CD Web UI

**Source**:
-> Lines 611-623: Overview of enabling Progressive Sync

**Notes**: Displays rollout wave, health, and messages for each application. Available when RollingSync strategy configured

---

## Workflow Coverage

### Complete Workflows
- **ApplicationSet Multitenancy Setup**: CONFIGURE → EXECUTE (Jobs 1.1-1.6)
- **Progressive Rollout Lifecycle**: LEARN → PLAN → CONFIGURE → EXECUTE → MONITOR → TROUBLESHOOT (Jobs 2.1-2.12, 3)

### Partial Workflows
- None identified

### Coverage Gaps
- **GET STARTED**: No onboarding or prerequisites guide
- **DEFINE**: No capacity planning or architecture design guidance
- **VALIDATE**: Limited testing or verification procedures

---

## Document Statistics

| Metric | Count |
|--------|-------|
| Main Jobs | 3 |
| User Stories | 18 |
| Total Records | 21 |
| Unique Personas | 2 |
| Workflow Stages | 6 |
| Source Lines Covered | ~1566 |
| Assemblies Analyzed | 2 |
| Modules Referenced | 24 |

### Module Type Distribution
- **PROCEDURE**: 12 modules
- **CONCEPT**: 8 modules
- **REFERENCE**: 4 modules

---

## Navigation Patterns

### Primary Paths
1. **Multitenancy Administrator**: Jobs 1.1 → 1.2 → 1.3/1.4/1.5 → 1.6
2. **Progressive Deployment Engineer**: Jobs 2.1/2.2/2.3 → 2.4 → 2.5 → 2.6/2.7 → 3
3. **Lifecycle Manager**: Jobs 2.8 → 2.9/2.10

### Cross-cutting Concerns
- **Security**: Job 1.6 (SCM Provider access control)
- **Troubleshooting**: Jobs 2.11, 2.12
- **Monitoring**: Job 3

---

*Generated by JTBD Workflow - Topic Map Analysis*
