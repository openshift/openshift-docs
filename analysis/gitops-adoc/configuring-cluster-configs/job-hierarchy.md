# Job Hierarchy: Configuring Cluster with GitOps

## Main Job 1: Configure Argo CD Permissions
**Stage**: Configure  
**Persona**: Cluster Administrator

### User Stories:
1. Use web console to edit Subscription (Cluster Administrator)
2. Verify cluster role configuration via UI or CLI (Cluster Administrator)

---

## Main Job 2: Understand Permission Model
**Stage**: Plan  
**Persona**: Cluster Administrator

### User Stories:
1. Review in-built permissions for cluster configuration (Cluster Administrator)

---

## Main Job 3: Run Argo CD on Infrastructure Nodes
**Stage**: Configure  
**Persona**: Platform Engineer

### User Stories:
- None (main procedure)

---

## Main Job 4: Create Argo CD Application
**Stage**: Deploy  
**Persona**: Cluster Administrator

### User Stories:
1. Use Argo CD dashboard to create application (Cluster Administrator)
2. Use oc CLI to create application (Platform Engineer)
3. Label namespace for Argo CD management (Cluster Administrator) - *Related Job*

---

## Main Job 5: Synchronize Application with Git
**Stage**: Execute  
**Persona**: Cluster Administrator

### User Stories:
1. Verify changes in OpenShift console after sync (Cluster Administrator)

---

## Main Job 6: Create Custom Cluster Roles
**Stage**: Configure  
**Persona**: Cluster Administrator

### User Stories:
1. Use web console to create RBAC resources (Cluster Administrator)

---

## Main Job 7: Automate Operator Installation
**Stage**: Deploy  
**Persona**: Cluster Administrator

### User Stories:
1. Install cluster-scoped Operators with Subscription only (Cluster Administrator)
2. Install namespace-scoped Operators with OperatorGroup + Subscription (Cluster Administrator)
3. Avoid OperatorGroup conflicts when deploying multiple Operators (Cluster Administrator) - *Related Job*

---

## Workflow Sequence

```
┌─────────────────────────────────────────────────────────────┐
│ Prerequisites:                                               │
│ - Install GitOps Operator                                   │
│ - Deploy Argo CD instance                                   │
│ - Have cluster admin access                                 │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ PLAN Stage                                                   │
│ Main Job 2: Understand Permission Model                     │
│ - Review default permissions                                │
│ - Identify additional permission needs                      │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ CONFIGURE Stage                                              │
│ Main Job 1: Configure Argo CD Permissions                   │
│ - Edit Subscription to add namespace                        │
│ - Verify cluster role                                       │
│                                                              │
│ Main Job 3: Run Argo CD on Infrastructure Nodes (Optional)  │
│ - Label nodes, add taints                                   │
│ - Configure GitOpsService CR                                │
│                                                              │
│ Main Job 6: Create Custom Cluster Roles (If Needed)         │
│ - Create ClusterRole                                        │
│ - Create ClusterRoleBinding                                 │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ DEPLOY Stage                                                 │
│ Main Job 4: Create Argo CD Application                      │
│ - Create application via Dashboard or CLI                   │
│ - Label target namespace                                    │
│                                                              │
│ Main Job 7: Automate Operator Installation (Optional)       │
│ - Add Operator Subscriptions to Git                         │
│ - Add OperatorGroups for namespace-scoped Operators         │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ EXECUTE Stage                                                │
│ Main Job 5: Synchronize Application with Git                │
│ - Trigger sync from Argo CD dashboard                       │
│ - Review changes before applying                            │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ CONFIRM Stage                                                │
│ - Verify configurations in OpenShift console                │
│ - Check application status in Argo CD                       │
│ - Monitor Operator installation (if applicable)             │
└─────────────────────────────────────────────────────────────┘
```

## Key Decision Points

### Decision 1: Infrastructure Nodes
**Question**: Is this a production cluster requiring workload isolation?
- **Yes** → Execute Main Job 3: Run Argo CD on Infrastructure Nodes
- **No** → Skip to application creation

### Decision 2: Additional Permissions
**Question**: Do default permissions cover all required resources?
- **Yes** → Proceed to application creation
- **No** → Execute Main Job 6: Create Custom Cluster Roles

### Decision 3: Application Creation Method
**Question**: Prefer UI or automation?
- **UI** → Use Argo CD Dashboard
- **CLI/Automation** → Use oc tool

### Decision 4: Operator Installation
**Question**: Installing Operators via GitOps?
- **Cluster-scoped** → Only Subscription needed
- **Namespace-scoped** → Subscription + OperatorGroup (ONE per namespace!)

## Critical Success Factors

1. **Namespace Labeling**: MUST label namespace with `argocd.argoproj.io/managed-by=openshift-gitops`
2. **OperatorGroup Constraint**: ONLY one OperatorGroup per namespace for namespace-scoped Operators
3. **Permission Verification**: Always verify permissions before deploying applications
4. **Sync Policy**: Choose Manual or Automatic based on change control requirements
5. **Directory Recursion**: Enable for hierarchical Git repository structures
