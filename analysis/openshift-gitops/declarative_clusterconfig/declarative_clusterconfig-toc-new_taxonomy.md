# Declarative Cluster Configuration - JTBD-Oriented Table of Contents

## Document Overview

**Book:** Declarative Cluster Configuration  
**Distro:** openshift-gitops  
**Analysis Date:** 2026-04-09  
**Source Assemblies:** 4  
**JTBD Records:** 18 (4 main jobs, 14 user stories)

---

## Quick Navigation

### By Workflow Stage
- **DEFINE:** Jobs 1, 2
- **EXECUTE:** Jobs 1, 2, 3
- **OPTIMIZE:** Jobs 1, 2, 4
- **MONITOR:** Job 4

### By Persona
- **Cluster Administrator:** Jobs 1, 2, 3
- **Platform Engineer:** Job 4

---

## JTBD-Oriented Structure

### Job 1: Configure cluster using GitOps declarative approach

**When** managing OpenShift cluster configurations, **I want** to use GitOps to deploy and sync cluster-wide resources from Git repositories, **so I can** maintain consistency and version control for cluster settings.

**User Stories:**

#### 1.1 Set up cluster-scoped Argo CD instance
**When** setting up GitOps for cluster management, **I want** to configure Argo CD with cluster-scoped permissions, **so it can** manage cluster-wide resources like operators and RBAC.

- **Approach:** Configure Operator subscription to enable cluster scope
- **Source:** Lines 137-195: Using an Argo CD instance to manage cluster-scoped resources
- **Key Actions:**
  - Update ARGOCD_CLUSTER_CONFIG_NAMESPACES environment variable in Subscription
  - Verify cluster role creation for argocd-application-controller
  - Test permissions with `oc auth can-i` commands
- **Security Note:** Requires cluster-admin privileges; includes privilege escalation warning

#### 1.2 Create and sync cluster configuration applications
**When** deploying cluster configurations, **I want** to create Argo CD applications that sync Git repository contents to the cluster, **so** configuration changes are automatically applied.

- **Approach:** Create applications via dashboard, oc tool, or GitOps CLI
- **Source:** 
  - Lines 333-384: Creating an application by using the Argo CD dashboard
  - Lines 402-462: Creating an application by using the oc tool
  - Lines 480-612: Creating an application in default mode by using the GitOps CLI
  - Lines 629-763: Creating an application in core mode by using the GitOps CLI
- **Key Configuration:**
  - Application Name: cluster-configs
  - Repository URL: Git repository with cluster configurations
  - Path: cluster (or custom path)
  - Namespace: Target namespace with appropriate labels
  - Directory Recurse: Enabled for hierarchical configs
- **Methods:** Dashboard (UI), oc CLI, argocd CLI (default and core modes)

#### 1.3 Synchronize cluster configurations from Git
**When** cluster configurations change in Git, **I want** to synchronize them to the cluster either manually or automatically, **so** the cluster state matches the desired state in Git.

- **Approach:** Manual or automated sync policy
- **Source:**
  - Lines 772-790: Synchronizing your application with your Git repository
  - Lines 800-864: Synchronizing an application in default mode
  - Lines 875-939: Synchronizing an application in core mode
- **Sync Policies:**
  - **Manual:** Review changes before applying (default)
  - **Automated:** Continuous sync with self-heal option
- **Verification:** Check application status (Healthy + Synced)

#### 1.4 Run Argo CD on infrastructure nodes
**When** managing Argo CD deployment, **I want** to run Argo CD instances on infrastructure nodes with appropriate tolerations, **so** workloads are properly isolated and scheduled.

- **Approach:** Configure GitOpsService resource with runOnInfra toggle
- **Source:** Lines 250-310: Running the Argo CD instance at the cluster-level
- **Configuration:**
  - Label nodes with node-role.kubernetes.io/infra
  - Optional: Apply taints for workload isolation
  - Set runOnInfra: true in GitOpsService CR
  - Add tolerations if taints are configured
- **Verification:** Check pod placement in openshift-gitops namespace

---

### Job 2: Manage RBAC permissions for cluster-scoped Argo CD instances

**When** operating Argo CD at cluster scope, **I want** to control and customize permissions for cluster resources, **so I can** grant appropriate access while maintaining security boundaries.

**User Stories:**

#### 2.1 Understand default Argo CD permissions
**When** deploying Argo CD, **I want** to understand its default permission model, **so I can** assess security implications and plan necessary customizations.

- **Approach:** Review default RBAC configuration
- **Source:** Lines 204-241: Default permissions of an Argo CD instance
- **Default Permissions:**
  - **Namespace-scoped:** Admin privileges in deployment namespace
  - **Cluster-scoped:** Read-only (get/list/watch) on all resources
  - **API Groups:** get/list on nonResourceURLs
- **Customization:** Edit argocd-server and argocd-application-controller cluster roles

#### 2.2 Add additional permissions for cluster configuration
**When** Argo CD needs access to additional cluster resources, **I want** to create custom cluster roles and bindings, **so** Argo CD can manage those resources declaratively.

- **Approach:** Create ClusterRole and ClusterRoleBinding resources
- **Source:** Lines 980-1043: Adding permissions for cluster configuration
- **Steps:**
  1. Create ClusterRole with required permissions (e.g., secrets access)
  2. Create ClusterRoleBinding for service account
  3. Bind to openshift-gitops-argocd-application-controller service account
- **Prerequisites:** cluster-admin access

#### 2.3 Create user-defined cluster roles for cluster-scoped instances
**When** default operator-managed permissions don't fit my requirements, **I want** to disable default cluster roles and create custom ones, **so I can** precisely control Argo CD's cluster access.

- **Approach:** Disable default roles and create custom RBAC
- **Source:** Lines 1374-1609: Customizing permissions by creating user-defined cluster roles
- **Steps:**
  1. Set spec.defaultClusterScopedRoleDisabled: true in Argo CD CR
  2. Verify operator deleted default cluster roles
  3. Create custom ClusterRole with specific permissions
  4. Find service account from pod spec
  5. Create ClusterRoleBinding for service account
- **Naming Convention:** <argocd_name>-<argocd_namespace>-<control_plane_component>

#### 2.4 Create aggregated cluster roles
**When** I want to extend Argo CD permissions without creating roles from scratch, **I want** to use aggregated cluster roles, **so I can** compose permissions from multiple role definitions.

- **Approach:** Enable aggregation and create labeled roles
- **Source:** Lines 1739-2340: Customizing permissions by creating aggregated cluster roles
- **Steps:**
  1. Set spec.aggregatedClusterRoles: true in Argo CD CR
  2. Operator creates aggregated cluster role with aggregationRule
  3. Operator creates view and admin child roles
  4. Create user-defined ClusterRole with label argocd/aggregate-to-admin: 'true'
  5. Verify permissions propagate to aggregated role
- **Label Selectors:**
  - argocd/aggregate-to-controller: "true" (for aggregated role)
  - argocd/aggregate-to-admin: "true" (for user-defined roles)
- **Version:** GitOps 1.14+, Application Controller only

#### 2.5 Configure respectRBAC feature
**When** I want to restrict Argo CD's resource discovery, **I want** to enable respectRBAC, **so** the controller only watches resources it has permissions to access.

- **Approach:** Set respectRBAC in Argo CD resource
- **Source:** Lines 1137-1242: Configuring respectRBAC using GitOps
- **Configuration:**
  - **normal:** Balance accuracy and speed (lightweight operation)
  - **strict:** More accurate, higher API call count
- **Verification:** Check resource.respectRBAC parameter in argocd-cm ConfigMap
- **Benefit:** Prevents errors when controller lacks permissions for specific resources

---

### Job 3: Install OLM Operators declaratively using GitOps

**When** managing operator lifecycle, **I want** to use GitOps to install and configure OLM operators from Git, **so** operator deployments are version-controlled and repeatable.

**User Stories:**

#### 3.1 Install cluster-scoped operators
**When** deploying cluster-scoped operators, **I want** to place Subscription resources in Git, **so** Argo CD automatically installs operators in the openshift-operators namespace.

- **Approach:** Store Subscription manifests in Git
- **Source:** Lines 1062-1083: Installing cluster-scoped Operators
- **Configuration:**
  - **Namespace:** openshift-operators (default)
  - **OperatorGroup:** Not required (uses global-operators)
  - **Subscription:** Define channel, installPlanApproval, name, source
- **Example:** Grafana Operator with channel v4, automatic install plan approval

#### 3.2 Install namespace-scoped operators
**When** deploying namespace-scoped operators, **I want** to place Subscription and OperatorGroup resources in Git, **so** operators are installed in specific namespaces with proper scope.

- **Approach:** Store Namespace, OperatorGroup, and Subscription in Git
- **Source:** Lines 1085-1128: Installing namespace-scoped Operators
- **Configuration:**
  - Create Namespace resource
  - Create OperatorGroup with targetNamespaces
  - Create Subscription in the same namespace
- **Critical:** Only one OperatorGroup per namespace (TooManyOperatorGroups error)
- **Example:** Ansible Automation Platform Resource Operator in ansible-automation-platform namespace
- **Recovery:** If CSV fails due to multiple OperatorGroups, manually approve pending install plan after fixing

---

### Job 4: Scale Argo CD Application Controller with cluster sharding

**When** Argo CD manages many clusters with high memory usage, **I want** to distribute clusters across multiple controller replicas using sharding, **so** resource usage is balanced and performance is optimized.

**User Stories:**

#### 4.1 Enable round-robin sharding algorithm
**When** enabling sharding, **I want** to use the round-robin algorithm instead of legacy hash-based, **so** clusters are distributed evenly across shards.

- **Approach:** Configure sharding with round-robin algorithm
- **Source:** Lines 2484-2786: Enabling the round-robin sharding algorithm
- **Configuration:**
  - Set spec.controller.sharding.enabled: true
  - Set spec.controller.sharding.replicas: <count>
  - Set env ARGOCD_CONTROLLER_SHARDING_ALGORITHM: round-robin
  - Set spec.controller.logLevel: debug (for verification)
- **Benefits:**
  - Balanced workload distribution
  - Prevents shard overload/underutilization
  - Optimizes compute resources
  - Reduces bottlenecks
  - Improves performance and reliability
- **Status:** Technology Preview feature

#### 4.2 Enable dynamic scaling of shards
**When** cluster count fluctuates, **I want** shards to scale dynamically based on configured thresholds, **so** shard distribution remains optimal without manual intervention.

- **Approach:** Configure dynamic scaling parameters
- **Source:** Lines 2794-3010: Enabling dynamic scaling of shards
- **Configuration:**
  - Set spec.controller.sharding.dynamicScalingEnabled: true
  - Set spec.controller.sharding.minShards: <value> (>= 1)
  - Set spec.controller.sharding.maxShards: <value> (> minShards)
  - Set spec.controller.sharding.clustersPerShard: <value> (>= 1)
- **Behavior:** System automatically adjusts shard count based on cluster count
- **Constraint:** Cannot manually modify shard count when dynamic scaling is enabled
- **Status:** Technology Preview feature

#### 4.3 Verify sharding configuration and distribution
**When** sharding is enabled, **I want** to verify which clusters are assigned to which shards, **so I can** confirm even distribution and troubleshoot issues.

- **Approach:** Check logs and pod status
- **Source:** Lines 2594-2650, 2744-2785: Verification steps
- **Verification Steps:**
  1. Check StatefulSet pod count matches replicas
  2. View controller pod logs for "Using filter function: round-robin"
  3. Search logs for "processed by shard" to see cluster assignments
  4. Verify even distribution: C (clusters) / R (replicas) = N (clusters per shard)
- **Log Level:** Must set to debug to observe shard assignments
- **Example:** 3 clusters with 3 replicas = 1 cluster per shard (shard 0, 1, 2)

---

## Workflow Coverage

### DEFINE Stage
- ✓ Cluster-scoped Argo CD setup and security model
- ✓ RBAC permission planning and assessment
- ✓ Default permission review

### EXECUTE Stage
- ✓ Application creation and configuration sync
- ✓ Permission customization (cluster roles, aggregated roles)
- ✓ OLM operator installation (cluster-scoped and namespace-scoped)

### OPTIMIZE Stage
- ✓ Infrastructure node placement for Argo CD
- ✓ Resource discovery optimization (respectRBAC)
- ✓ Sharding for scalability (round-robin, dynamic scaling)

### MONITOR Stage
- ✓ Shard distribution verification
- ✓ Sync status monitoring

### Coverage Gaps
- **PLAN:** No explicit capacity planning guidance for sharding thresholds
- **TROUBLESHOOT:** Limited troubleshooting content for common failure scenarios
- **MAINTAIN:** No content on upgrading or maintaining declarative configs over time

---

## Document Statistics

| Metric | Count |
|--------|-------|
| Main Jobs | 4 |
| User Stories | 14 |
| Source Assemblies | 4 |
| Combined Lines | 3,017 |
| Modules Referenced | 29 |
| Procedures | 12 |
| Concepts | 3 |
| References | 3 |

---

## Additional Resources

### Cross-References
- Installing GitOps
- Argo CD instance configuration
- GitOps CLI reference
- Multitenancy support
- Setting up Argo CD instance

### External Links
- Argo CD upstream documentation (declarative setup, RBAC)
- Kubernetes aggregated cluster roles
- OpenShift node scheduling (taints and tolerations)
- OpenShift infrastructure machine sets
- Technology Preview features support scope

---

**Generated by:** Claude Code JTBD Workflow  
**Methodology:** Jobs-To-Be-Done framework with workflow stage taxonomy  
**Format Version:** 1.0
