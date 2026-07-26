# Multitenancy Support in GitOps
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Help cluster administrators understand, configure, and manage multitenant Argo CD deployments with appropriate isolation and access controls.

**Personas:** Cluster administrator, Platform engineer, Application delivery team

**Main Jobs:** 8 core jobs across 5 workflow stages

---

## Quick Navigation

**I want to:**
- Understand multitenancy architecture → Job 1 (Plan)
- Set up isolated tenant instances → Job 2 (Configure)
- Grant cluster-wide permissions → Job 3 (Configure)
- Use the default cluster instance → Job 4 (Administer)
- Prevent privilege escalation → Job 5 (Secure)
- Control what tenants can deploy → Job 6 (Administer)
- Enable tenant self-service namespace management → Job 7 (Configure)
- Delegate my namespaces to Argo CD → Job 8 (Configure)

---

# Table of Contents

## Understand Your Options

### Job 1: Understand Multitenancy Architecture and Instance Scopes
*When deploying applications for multiple teams*

**Personas:** Cluster administrator
**Why:** Choosing the wrong deployment model can lead to security risks and operational complexity

#### 1.1 Learn Core Multitenancy Concepts
**Goal:** Understand how single Argo CD instances serve multiple tenants with isolation.

→ Lines 1-17: Overview
  Source: Multitenancy support in GitOps

Key concepts:
- Single software instance serving multiple distinct user groups (tenants)
- Tenant autonomy without cluster-admin privileges
- Permission model for Argo CD Application Controller
- Three instance scope modes: namespace-scoped, cluster-scoped, and default cluster-scoped

#### 1.2 Compare Instance Scope Modes
**Goal:** Evaluate which instance scope fits your use cases.

→ Lines 19-24: Argo CD instance scopes
  Source: Instance scopes section

**Three modes available:**
- **Namespace-scoped instance** (Application delivery)
  - Best for: Tenant self-service, application delivery teams
  - Isolation: Namespace-level permissions
  - Use when: Teams need autonomy without cluster access

- **Cluster-scoped instance** (Custom cluster instance)
  - Best for: Shared instances managed by cluster admins
  - Isolation: Controlled via RBAC and AppProjects
  - Use when: Multiple teams share one instance, cluster resources needed

- **Default cluster-scoped instance** (openshift-gitops)
  - Best for: Cluster configuration only
  - Isolation: Read-only cluster access, limited deployment scope
  - Use when: Managing cluster-level configuration resources

---

## Set Up & Configure

### Job 2: Deploy Namespace-Scoped Argo CD Instances
*When providing GitOps capabilities to application teams*

**Personas:** Cluster administrator
**Timing:** After understanding architecture (Job 1)

#### 2.1 Deploy Basic Namespace-Scoped Instance
**Goal:** Establish tenant-isolated Argo CD instance.

→ Lines 25-38: Namespace-scoped instance (Application delivery instance)
  Source: Namespace-scoped instance section

- Create Argo CD custom resource in tenant namespace
- Instance has initial permission only for its own namespace
- GitOps Operator starts Argo CD in tenant namespace
- Tenant has full autonomy without admin permissions

**Note:** Default permissions are namespace-scoped only. Extend permissions using methods below.

#### 2.2 Extend Permissions Using Managed-By Label (Standard Approach)
**Goal:** Allow instance to deploy across multiple namespaces automatically.

→ Lines 40-48: How does this method work?
  Source: Namespace-scoped instance section

**Task:** Label target namespaces
- Add label: `argocd.argoproj.io/managed-by: <argo-cd-namespace>`
- GitOps Operator automatically creates roles and role bindings
- Controller gets permissions equivalent to Kubernetes `admin` cluster role

**Limitation:** Only works for same-cluster namespaces. For remote clusters, define permissions manually.

#### 2.3 Restrict Permissions Using Custom Cluster Roles (Secure Approach)
**Goal:** Enforce least-privilege access for Argo CD controllers.

→ Lines 49-55: Custom cluster role configuration
  Source: Namespace-scoped instance section

**Task:** Configure environment variables in Operator Subscription
- Set `CONTROLLER_CLUSTER_ROLE` for Application Controller
- Set `CONTROLLER_SERVER_ROLE` for Server component
- Operator creates role bindings (not default roles)
- Administrator creates cluster roles with precise permissions

**Requirements:**
- Custom cluster role must grant `view`, `get`, and `watch` for all resources Argo CD interacts with
- OR configure `resourceInclusions`/`resourceExclusions` in Argo CD CR to limit scope

**Limitation:** Cannot manage cluster-scoped resources (namespaces, CRDs, cluster roles) with namespace-scoped instance.

---

### Job 3: Deploy Cluster-Scoped Argo CD Instance
*When managing cluster-level resources or supporting Applications in any namespace*

**Personas:** Cluster administrator
**Timing:** After understanding architecture (Job 1)
**Why:** Prevents self-elevation security risk while enabling cluster-wide management

#### 3.1 Understand Cluster-Scoped Instance Use Cases
**Goal:** Validate need for cluster-level permissions.

→ Lines 57-64: Cluster-scoped instance
  Source: Cluster-scoped instance section

**Use when:**
- Need to deploy and manage resources across cluster
- Using "Applications in any namespace" feature
- Managing cluster configuration (typically, but not always)
- Shared instance managed by cluster admins for multiple teams

**Important:** Do NOT elevate instances self-managed by application delivery teams - severe security risk.

#### 3.2 Elevate Instance Using Environment Variable
**Goal:** Safely grant cluster-level permissions.

→ Lines 65-73: How does this method work?
  Source: Cluster-scoped instance section

**Task:** Configure ARGOCD_CLUSTER_CONFIG_NAMESPACES
- Modify GitOps Operator Subscription resource
- Set `ARGOCD_CLUSTER_CONFIG_NAMESPACES` environment variable
- Identify namespaces allowed to have cluster privileges
- Non-cluster admins cannot access Subscription, preventing self-elevation

**Result:**
- Operator creates cluster role and cluster role bindings
- Default role is NOT equivalent to `cluster-admin`
- Much smaller set of permissions granted
- Extend permissions by creating additional cluster roles/bindings as needed

---

### Job 4: Use the Default Cluster-Scoped Instance
*When managing cluster configuration resources*

**Personas:** Cluster administrator
**Requires:** OpenShift GitOps Operator installed

#### 4.1 Understand Default Instance Purpose
**Goal:** Recognize intended use and limitations.

→ Lines 75-84: Default cluster-scoped instance
  Source: Default cluster-scoped instance section

**Automatic instantiation:**
- Created in `openshift-gitops` namespace on Operator install
- Opinionated setup for cluster configuration
- Does NOT have full `cluster-admin` privileges
- Read access to all cluster resources
- Can deploy only limited set of resources

**Critical restrictions:**
- Do NOT use for application delivery
- Do NOT grant access to non-cluster-admin users
- Delegate tenant use cases to separate instances in other namespaces

---

## Secure Your Environment

### Job 5: Understand the Two-Level RBAC Model
*When designing multitenancy solutions*

**Personas:** Cluster administrator, Platform engineer
**Why:** Privilege escalation risk when tenants leverage controller's elevated permissions

#### 5.1 Learn the Two Permission Layers
**Goal:** Recognize how Kubernetes and Argo CD RBAC interact.

→ Lines 89-96: Argo CD role-based access control (RBAC)
  Source: Argo CD RBAC section

**Two distinct levels:**

1. **Kubernetes level**
   - Argo CD Application Controller uses single service account per cluster
   - Service account needs permissions for all tenants and use cases
   - Managed by standard Kubernetes RBAC

2. **Argo CD level**
   - Argo CD has its own RBAC permissions model
   - Independent of Kubernetes permissions
   - Can provide access to applications beyond Kubernetes permissions

**Risk:** Privilege escalation occurs when tenant uses controller's elevated privileges to perform unauthorized actions.

#### 5.2 Mitigate Privilege Escalation
**Goal:** Prevent tenants from bypassing multitenancy restrictions.

→ Lines 97-101: Privilege escalation mitigation
  Source: Argo CD RBAC section

**Mitigation strategies:**
- Use Argo CD RBAC model to restrict user-level access
- Use separate Argo CD instances for complete isolation
- Configure both permission layers appropriately

**Related:** See Job 6 for AppProject restrictions.

---

## Administer Platform

### Job 6: Define AppProject Custom Resources for Tenant Management
*When managing multiple tenants with an Argo CD instance*

**Personas:** Cluster administrator
**Requires:** Understanding of Argo CD projects concept

#### 6.1 Understand Argo CD Projects Purpose
**Goal:** Learn how projects group applications and enforce restrictions.

→ Lines 103-112: Argo CD projects
  Source: Argo CD projects section

**What are Argo CD projects:**
- Not to be confused with OpenShift Container Platform projects
- Group applications together
- Specify restrictions on what resources can be deployed and where
- Enable granular RBAC at project level (vs global in Argo CD CR)

**Why use projects:**
- Define tenant RBAC with restrictions in `AppProject` CR
- Avoid repetition when managing large number of tenants
- Manage tenants more effectively than global RBAC

#### 6.2 Define Tenant AppProject CRs
**Goal:** Control tenant deployment permissions.

→ Lines 112-117: AppProject best practices
  Source: Argo CD projects section

**Best practices:**
- Always define your own projects
- Never use default project created by Operator
- Define tenant RBAC along with restrictions in AppProject CR
- For many tenants, use global projects for common configuration
- Inherit global projects in tenant projects to reduce duplication

---

### Job 7: Enable Tenant Self-Service for Namespace Management
*When enabling tenant self-service for namespace management*

**Personas:** Cluster administrator
**Timing:** After deploying namespace-scoped instances (Job 2)
**Why:** Default label-based approach requires cluster-admin privileges, unsuitable for tenant self-service

#### 7.1 Understand NamespaceManagement CR Feature
**Goal:** Learn how NamespaceManagement CR enables tenant delegation.

→ Lines 119-133: Enable tenant namespace management with NamespaceManagement CR
  Source: NamespaceManagement CR section

**Feature overview:**
- New `NamespaceManagement` custom resource
- Allows tenants to delegate control without cluster admin action
- Disabled by default for security
- Must be explicitly enabled by cluster administrator

**How it works:**
- Argo CD admins configure namespace management using glob patterns (`/*`, `tenant-/*`)
- Tenants create NamespaceManagement CR in target namespace
- GitOps Operator automatically provisions RBAC resources
- Operator updates Argo CD cluster secret

#### 7.2 Enable Feature in Subscription
**Goal:** Allow namespace management for namespace-scoped instances.

→ Lines 155-176: Procedure step 1
  Source: Configuring namespace management section

**Task:** Edit GitOps Operator Subscription CR

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: argocd-operator
  namespace: argocd
spec:
  config:
    env:
    - name: ALLOW_NAMESPACE_MANAGEMENT_IN_NAMESPACE_SCOPED_INSTANCES
      value: "true"
```

**Field descriptions:**
- `spec.config.env[].name`: Environment variable enabling namespace management
- `spec.config.env[].value`: Set to `"true"` to enable

#### 7.3 Configure Argo CD CR with Namespace Patterns
**Goal:** Define which namespaces Argo CD can manage.

→ Lines 177-192: Procedure step 2
  Source: Configuring namespace management section

**Task:** Update Argo CD instance

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  namespace: <argocd-ns>
spec:
  namespaceManagement:
    - name: <tenant-ns>
      allowManagedBy: true
```

**Field descriptions:**
- `<metadata.namespace>`: Argo CD instance namespace
- `<spec.namespaceManagement.name>`: Namespace to manage, supports glob patterns (`/*`, `dev-/*`, `?`)

**Pattern matching:**
- `/*`: Matches all namespaces
- `tenant-/*`: Matches namespaces with `tenant-` prefix
- Use wildcards for flexible matching

#### 7.4 Understand NamespaceManagement CR Lifecycle
**Goal:** Predict operator behavior during CR operations.

→ Lines 145-153: Effects of NamespaceManagement CR
  Source: NamespaceManagement CR effects section

**Lifecycle responses:**

1. **Creation**
   - Role and RoleBinding created in target namespace
   - Namespace added to Argo CD cluster secret

2. **Update**
   - RBAC and cluster secret entries updated when `.spec.managedBy` changes

3. **Deletion**
   - Associated RBAC resources removed
   - Cluster secret entries removed

**Automatic cleanup:** If feature disabled at Subscription level, all NamespaceManagement configuration cleaned up.

---

### Job 8: Delegate My Namespaces to Argo CD (Tenant Perspective)
*When I need my Argo CD instance to manage my namespaces*

**Personas:** Application delivery team
**Requires:** Cluster admin has enabled namespace management (Job 7), permissions to create NamespaceManagement CR

#### 8.1 Create NamespaceManagement CR
**Goal:** Delegate control to Argo CD instance without cluster-admin approval.

→ Lines 193-209: Procedure step 3 and Verification
  Source: Configuring namespace management section

**Task:** Create CR in tenant namespace

```yaml
apiVersion: argoproj.io/v1beta1
kind: NamespaceManagement
metadata:
  name: ui-team-namespace
  namespace: <tenant-ns>
spec:
  managedBy: <argocd-ns>
```

**Field descriptions:**
- `<metadata.namespace>`: Namespace to be managed by Argo CD
- `<spec.managedBy>`: Namespace where Argo CD instance runs (must exactly match)

**Verification:**
After CR creation, GitOps Operator automatically:
- Creates Role and RoleBinding in tenant namespace
- Updates Argo CD cluster secret

**Resources to verify:**
- **Roles:** `<argocd-instance-name>-argocd-server`, `<argocd-instance-name>-argocd-application-controller`
- **RoleBindings:** `<argocd-instance-name>-argocd-server`, `<argocd-instance-name>-argocd-application-controller`
- **Cluster secret:** `<argocd-instance-name>-cluster`

---

## Appendices

### A. Instance Scope Comparison Matrix

| Instance Scope | Best For | Permissions | Isolation | Elevation Control |
|----------------|----------|-------------|-----------|-------------------|
| Namespace-scoped | Tenant self-service, application delivery | Namespace-level (extendable) | High (namespace boundaries) | Not applicable |
| Cluster-scoped | Shared instances, cluster resources | Cluster-level (limited set) | Medium (via RBAC + AppProjects) | ARGOCD_CLUSTER_CONFIG_NAMESPACES |
| Default cluster-scoped | Cluster configuration only | Read-only cluster + limited deploy | High (cluster admin only) | Not elevatable |

**Choose based on:**
- **Namespace-scoped:** Tenant teams managing their own applications
- **Cluster-scoped:** Cluster admins managing shared instance for multiple teams
- **Default cluster-scoped:** Only for cluster configuration, never for application delivery

---

### B. Permission Extension Methods Comparison

| Method | Use Case | Scope | Automation | Security Control |
|--------|----------|-------|------------|------------------|
| managed-by label | Standard namespace extension | Same cluster only | High (auto-provisioning) | Admin cluster role by default |
| Custom cluster roles | Least-privilege access | Same cluster + custom | Medium (manual role creation) | Fine-grained control |
| ARGOCD_CLUSTER_CONFIG_NAMESPACES | Elevate to cluster-scoped | Cluster-wide | Medium (Subscription edit) | Prevents self-elevation |
| NamespaceManagement CR | Tenant self-service | Pattern-matched namespaces | High (tenant-initiated) | Cluster admin enablement required |

---

### C. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Plan | ✅ | Job 1 | Architecture understanding and instance scope selection |
| Configure | ✅ | Jobs 2, 3, 7, 8 | Instance deployment, permission extension, namespace management |
| Administer | ✅ | Jobs 4, 6 | Default instance usage, AppProject management |
| Secure | ✅ | Job 5 | RBAC model understanding, privilege escalation mitigation |
| Deploy | ⚠️ Limited | - | Application deployment referenced but not detailed |
| Monitor | ❌ | - | No observability or monitoring content |
| Troubleshoot | ❌ | - | No troubleshooting guidance |
| Upgrade | ❌ | - | No upgrade or migration procedures |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Deploy | No application deployment procedures | Link to application deployment guides |
| Monitor | No observability for multitenancy | Add monitoring best practices for tenant isolation |
| Troubleshoot | No troubleshooting guidance | Add common permission issues and resolutions |
| Upgrade | No upgrade procedures | Add instance upgrade and migration procedures |

---

## Navigation Guide

### By User Journey

**Cluster Administrator setting up multitenancy:**
1. Job 1: Understand multitenancy architecture
2. Job 2: Deploy namespace-scoped instances for tenants
3. Job 5: Understand RBAC model
4. Job 6: Define AppProjects for tenant restrictions
5. Job 7: Enable tenant self-service namespace management

**Cluster Administrator managing cluster configuration:**
1. Job 1: Understand multitenancy architecture
2. Job 4: Use default cluster-scoped instance
3. Job 5: Understand RBAC model

**Cluster Administrator deploying shared instance:**
1. Job 1: Understand multitenancy architecture
2. Job 3: Deploy cluster-scoped instance
3. Job 5: Understand RBAC model
4. Job 6: Define AppProjects for tenant restrictions

**Application Delivery Team (tenant) delegating namespaces:**
1. Job 8: Create NamespaceManagement CR in tenant namespace
2. Verify automatic RBAC provisioning
3. Deploy applications to managed namespaces

---

## Document Statistics

**Workflow Coverage:**
- Plan: 1 job
- Configure: 4 jobs
- Administer: 2 jobs
- Secure: 1 job
- Deploy: 0 jobs (gap)
- Monitor: 0 jobs (gap)
- Troubleshoot: 0 jobs (gap)
- Upgrade: 0 jobs (gap)

**Main Jobs:** 8
**User Stories/Paths:** 14
**Source Sections:** 12
**Instance Scope Variations:** 3 (namespace-scoped, cluster-scoped, default cluster-scoped)
**Permission Extension Methods:** 4 (managed-by label, custom cluster roles, ARGOCD_CLUSTER_CONFIG_NAMESPACES, NamespaceManagement CR)
