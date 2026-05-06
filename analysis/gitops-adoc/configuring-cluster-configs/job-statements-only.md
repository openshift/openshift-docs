# All Job Statements: Configuring Cluster with GitOps

## Main Jobs (7)

### 1. Configure Argo CD Permissions
When I need to manage cluster-scoped resources with GitOps, I want to configure my Argo CD instance with appropriate permissions, so I can automate cluster configuration through Git without manual intervention.

**Persona**: Cluster administrator  
**Stage**: Configure

---

### 2. Understand Permission Model
When planning my Argo CD deployment, I want to understand the default permission model, so I can determine what additional permissions I need to configure.

**Persona**: Cluster administrator  
**Stage**: Plan

---

### 3. Run Argo CD on Infrastructure Nodes
When operating a production cluster with infrastructure nodes, I want to run Argo CD on dedicated infrastructure nodes, so I can isolate GitOps workloads from application workloads and ensure predictable performance.

**Persona**: Platform engineer  
**Stage**: Configure

---

### 4. Create Argo CD Application
When I need to deploy cluster configurations via GitOps, I want to create an Argo CD application pointing to my Git repository, so I can manage cluster state declaratively.

**Persona**: Cluster administrator  
**Stage**: Deploy

---

### 5. Synchronize Application with Git
When my Argo CD application is created with manual sync policy, I want to trigger synchronization, so I can apply Git repository changes to the cluster in a controlled manner.

**Persona**: Cluster administrator  
**Stage**: Execute

---

### 6. Create Custom Cluster Roles
When default Argo CD permissions are insufficient, I want to create custom cluster roles and bindings, so I can enable Argo CD to manage additional cluster resources securely.

**Persona**: Cluster administrator  
**Stage**: Configure

---

### 7. Automate Operator Installation
When managing cluster configuration as code, I want to automate Operator installation via GitOps, so I can eliminate manual Operator installation procedures and ensure consistent Operator deployments across clusters.

**Persona**: Cluster administrator  
**Stage**: Deploy

---

## User Stories (11)

### Configure Argo CD Permissions

#### US1: Use Web Console for Configuration
As a cluster administrator, when configuring Argo CD for cluster-scoped management, I want to use the web console to edit the Subscription, so I can visually configure permissions without writing YAML.

**Parent Job**: Configure my Argo CD instance with appropriate permissions

---

#### US2: Verify Cluster Role Configuration
As a cluster administrator, when I've configured Argo CD permissions, I want to verify the cluster role assignment, so I can confirm Argo CD can manage cluster-scoped resources before deploying applications.

**Parent Job**: Configure my Argo CD instance with appropriate permissions

---

### Understand Permission Model

#### US3: Review In-Built Permissions
When planning cluster configuration via GitOps, I want to understand what cluster-scoped resources Argo CD can manage by default, so I can determine if additional permissions are needed.

**Parent Job**: Understand the default permission model

---

### Create Argo CD Application

#### US4: Use Dashboard for Application Creation
As a cluster administrator, when creating an Argo CD application, I want to use the web dashboard, so I can configure the application visually without writing YAML manifests.

**Parent Job**: Create an Argo CD application pointing to my Git repository

---

#### US5: Label Namespace for Management (Related Job)
As a cluster administrator, after creating an Argo CD application, I want to label the target namespace for management, so I can ensure the Argo CD instance has permission to deploy resources there.

**Parent Job**: Create an Argo CD application pointing to my Git repository  
**Type**: Related

---

#### US6: Use CLI for Application Creation
As a platform engineer, when creating an Argo CD application, I want to use the oc CLI tool, so I can automate application creation and manage it as code.

**Parent Job**: Create an Argo CD application pointing to my Git repository

---

### Synchronize Application with Git

#### US7: Verify Changes in Console
As a cluster administrator, after synchronizing cluster configurations, I want to verify the changes in the OpenShift console, so I can confirm the configurations were applied correctly.

**Parent Job**: Trigger synchronization to apply Git repository changes

---

### Create Custom Cluster Roles

#### US8: Use Web Console for RBAC
As a cluster administrator, when granting additional permissions, I want to use the web console to create cluster roles and bindings, so I can configure permissions without writing RBAC YAML.

**Parent Job**: Create custom cluster roles and bindings

---

### Automate Operator Installation

#### US9: Install Cluster-Scoped Operators
As a cluster administrator, when installing cluster-scoped Operators via GitOps, I want to only manage the Subscription resource in Git, so I can leverage the default global-operators OperatorGroup and simplify my GitOps repository.

**Parent Job**: Automate Operator installation via GitOps

---

#### US10: Install Namespace-Scoped Operators
As a cluster administrator, when installing namespace-scoped Operators via GitOps, I want to manage both Subscription and OperatorGroup resources in Git, so I can ensure Operators are installed in the correct namespace with proper targeting.

**Parent Job**: Automate Operator installation via GitOps

---

#### US11: Avoid OperatorGroup Conflicts (Related Job)
When deploying multiple Operators to the same namespace via GitOps, I want to ensure only one OperatorGroup exists, so I can prevent CSV transition failures and ensure successful Operator installation.

**Parent Job**: Automate Operator installation via GitOps  
**Type**: Related  
**Stage**: Troubleshoot

---

## Quick Reference by Persona

### Cluster Administrator (13 jobs)
- Configure Argo CD Permissions (Main + 2 User Stories)
- Understand Permission Model (Main + 1 User Story)
- Create Argo CD Application (Main + 3 User Stories)
- Synchronize Application with Git (Main + 1 User Story)
- Create Custom Cluster Roles (Main + 1 User Story)
- Automate Operator Installation (Main + 3 User Stories)

### Platform Engineer (2 jobs)
- Run Argo CD on Infrastructure Nodes (Main)
- Use CLI for Application Creation (User Story)

---

## Quick Reference by Stage

### Plan (2)
- Understand Permission Model
- Review In-Built Permissions

### Configure (7)
- Configure Argo CD Permissions (+ 2 US)
- Run Argo CD on Infrastructure Nodes
- Create Custom Cluster Roles (+ 1 US)
- Label Namespace for Management

### Confirm (2)
- Verify Cluster Role Configuration
- Verify Changes in Console

### Deploy (7)
- Create Argo CD Application (+ 3 US)
- Automate Operator Installation (+ 2 US)

### Execute (1)
- Synchronize Application with Git

### Troubleshoot (1)
- Avoid OperatorGroup Conflicts
