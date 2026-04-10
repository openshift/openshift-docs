# JTBD-Oriented Table of Contents
## Argo CD Applications

**Document**: argocd_applications  
**Distro**: openshift-gitops  
**Generated**: 2026-04-10

---

## Quick Navigation

| Job # | Job Title | Persona | Stage |
|-------|-----------|---------|-------|
| 1 | Deploy applications to OpenShift using Argo CD | Application Developer | EXECUTE |
| 2 | Manage Argo CD applications using the GitOps CLI | Platform Engineer | EXECUTE |
| 3 | Manage applications in non-control plane namespaces | Cluster Administrator | CONFIGURE |
| 4 | Manage application links in multi-instance Argo CD environments | Platform Architect | CONFIGURE |

---

## 1. Deploy Applications to OpenShift Using Argo CD

**Persona**: Application Developer  
**Stage**: EXECUTE

### User Stories

#### 1.1 Deploy via Argo CD Dashboard

**Story**: When I want to deploy my application using the Argo CD dashboard, I want to configure it through the UI, so I can visually set up my application deployment

**Tasks**:
- Create application via Argo CD dashboard
  - -> Lines 117-151: Creating an application by using the Argo CD dashboard
  - **Module**: gitops-creating-an-application-by-using-the-argo-cd-dashboard.adoc (PROCEDURE)
  - **Steps**:
    1. Log in to OpenShift cluster as administrator
    2. Install GitOps Operator
    3. Log in to Argo CD instance
    4. Create application with repository URL, path, and namespace settings
    5. Click CREATE to create application
    6. Label namespace for Argo CD management

#### 1.2 Deploy via Command Line

**Story**: When I want to deploy my application using command-line tools, I want to use the oc CLI, so I can automate and script my deployments

**Tasks**:
- Create application using oc CLI
  - -> Lines 164-207: Creating an application by using the oc tool
  - **Module**: gitops-creating-an-application-by-using-the-oc-tool.adoc (PROCEDURE)
  - **Steps**:
    1. Install GitOps Operator
    2. Log in to Argo CD instance
    3. Access oc CLI tool
    4. Download sample application
    5. Create application using oc
    6. Review created application

#### 1.3 Verify Application State

**Story**: When my application is deployed, I want to verify Argo CD's self-healing behavior, so I can ensure my application state is automatically corrected

**Tasks**:
- Test self-healing by modifying deployment
  - -> Lines 218-267: Verifying Argo CD self-healing behavior
  - **Module**: gitops-verifying-argo-cd-self-healing-behavior.adoc (PROCEDURE)
  - **Steps**:
    1. Verify application has Synced status in Argo CD dashboard
    2. Fork the GitOps repository
    3. Modify deployment and commit changes
    4. Scale deployment to test self-healing
    5. Observe Argo CD auto-heal the application
    6. Review events in Argo CD dashboard

---

## 2. Manage Argo CD Applications Using the GitOps CLI

**Persona**: Platform Engineer  
**Stage**: EXECUTE

### User Stories

#### 2.1 Use CLI in Default Mode

**Story**: When I want to use the Argo CD CLI in default mode, I want to authenticate and create applications, so I can manage deployments from the command line

**Tasks**:
- Create application using argocd CLI in default mode
  - -> Lines 384-483: Creating an application in the default mode by using the GitOps CLI
  - **Module**: gitops-argocd-cli-creating-an-application-in-default-mode.adoc (PROCEDURE)
  - **Steps**:
    1. Install GitOps Operator
    2. Install oc and argocd CLIs
    3. Get admin password for Argo CD server
    4. Get Argo CD server URL
    5. Log in to Argo CD server
    6. Verify argocd commands work
    7. Create application using argocd app create
    8. Label destination namespace
    9. Confirm application is created successfully

#### 2.2 Use CLI in Core Mode

**Story**: When I want to use the Argo CD CLI in core mode, I want to leverage my existing Kubernetes authentication, so I can avoid separate Argo CD login

**Tasks**:
- Create application using argocd CLI in core mode
  - -> Lines 497-597: Creating an application in core mode by using the GitOps CLI
  - **Module**: gitops-argocd-cli-creating-an-application-in-core-mode.adoc (PROCEDURE)
  - **Steps**:
    1. Log in to OpenShift cluster using oc CLI
    2. Check context is set correctly in kubeconfig
    3. Set default namespace to openshift-gitops
    4. Set environment variable to override Argo CD component names
    5. Verify argocd commands work in core mode
    6. Create application using argocd app create --core
    7. Label destination namespace
    8. Confirm application is created successfully

---

## 3. Manage Applications in Non-Control Plane Namespaces

**Persona**: Cluster Administrator  
**Stage**: CONFIGURE

### User Stories

#### 3.1 Enable Multitenancy with Target Namespaces

**Story**: When I want to enable multitenancy, I want to configure target namespaces in the ArgoCD CR, so I can allow teams to manage applications in their own namespaces

**Tasks**:
- Configure ArgoCD CR with source namespaces
  - -> Lines 763-869: Configuring the Argo CD CR of your user-defined cluster-scoped Argo CD instance with the target namespaces
  - **Module**: gitops-configuring-argo-cd-cr-of-your-user-defined-cluster-scoped-instance-with-target-namespaces.adoc (PROCEDURE)
  - **Steps**:
    1. Log in to OpenShift cluster as administrator
    2. Navigate to Installed Operators
    3. Select project with cluster-scoped Argo CD instance
    4. Go to Argo CD tab and select instance
    5. Edit YAML of ArgoCD CR
    6. Set sourceNamespaces parameter with target namespaces
    7. Save and reload
    8. Verify Operator adds managed-by-cluster-argocd label

#### 3.2 Define Project Policies

**Story**: When target namespaces are configured, I want to create an AppProject for those namespaces, so I can define deployment policies and permissions

**Tasks**:
- Create user-defined AppProject with source namespaces
  - -> Lines 882-939: Creating and configuring a user-defined AppProject instance with the target namespaces
  - **Module**: gitops-creating-and-configuring-user-defined-appproject-instance-with-target-namespaces.adoc (PROCEDURE)
  - **Steps**:
    1. Select openshift-gitops project
    2. Navigate to GitOps Operator and AppProject tab
    3. Click Create AppProject
    4. Enter configuration in YAML with sourceNamespaces field
    5. Specify destinations and source repos
    6. Click Create
    7. Verify AppProject is created

#### 3.3 Deploy to Target Namespaces

**Story**: When the AppProject is configured, I want to create Applications referencing the target namespace and project, so I can deploy to non-control plane namespaces

**Tasks**:
- Create Application CR in target namespace
  - -> Lines 950-1001: Creating and configuring the Application CR to reference the target namespace and user-defined AppProject instance
  - **Module**: gitops-creating-and-configuring-the-app-cr-to-reference-the-target-namespace-and-user-defined-appproject-instance.adoc (PROCEDURE)
  - **Steps**:
    1. Select target namespace from Project list
    2. Navigate to GitOps Operator and Application tab
    3. Click Create Application
    4. Enter configuration with metadata.namespace and spec.project fields
    5. Click Create
    6. Verify application is created and has Healthy and Synced status

---

## 4. Manage Application Links in Multi-Instance Argo CD Environments

**Persona**: Platform Architect  
**Stage**: CONFIGURE

### User Stories

#### 4.1 Understand Annotation Purpose

**Story**: When I have multiple Argo CD instances, I want to understand how the managed-by-url annotation works, so I can plan my architecture correctly

**Tasks**:
- Learn about managed-by-url annotation
  - -> Lines 1124-1142: Overview of the managed-by-url annotation
  - **Module**: gitops-overview-managed-by-url-annotation.adoc (CONCEPT)

#### 4.2 Configure Application Links

**Story**: When I use the app-of-apps pattern with multiple instances, I want to configure the managed-by-url annotation, so I can ensure child applications open in the correct Argo CD instance

**Tasks**:
- Add managed-by-url annotation to child applications
  - -> Lines 1154-1229: Configuring the managed-by-url annotation
  - **Module**: gitops-configuring-managed-by-url-annotation.adoc (PROCEDURE)
  - **Steps**:
    1. Create parent Application in primary Argo CD instance
    2. Add managed-by-url annotation to child Application definition in Git
    3. Specify secondary Argo CD instance URL in annotation
    4. Apply or sync parent Application
    5. Verify link opens in correct instance

#### 4.3 Validate Configuration

**Story**: When configuring the annotation, I want to understand the valid URL format, so I can avoid configuration errors

**Tasks**:
- Review annotation reference
  - -> Lines 1241-1288: Managed-by-url annotation reference
  - **Module**: gitops-managed-by-url-annotation-reference.adoc (REFERENCE)

#### 4.4 Fix Link Routing Issues

**Story**: When application links are not working, I want to troubleshoot the managed-by-url annotation, so I can fix link routing issues

**Tasks**:
- Diagnose managed-by-url annotation issues
  - -> Lines 1300-1359: Troubleshooting the managed-by-url annotation
  - **Module**: gitops-troubleshooting-managed-by-url-annotation.adoc (PROCEDURE)
  - **Steps**:
    1. Check if annotation is present using kubectl
    2. Verify URL is reachable from browser
    3. Check browser console for errors
    4. Ensure URL includes correct protocol
    5. Verify child Application exists in cluster
    6. Check parent Application sync status

---

## Workflow Coverage

### Covered Workflows

| Workflow Stage | Coverage | Jobs |
|----------------|----------|------|
| UNDERSTAND | ✓ | 4.1 |
| CONFIGURE | ✓✓✓ | 3.1, 3.2, 4.2, 4.3 |
| EXECUTE | ✓✓✓ | 1.1, 1.2, 2.1, 2.2, 3.3 |
| VERIFY | ✓ | 1.3 |
| TROUBLESHOOT | ✓ | 4.4 |

### Workflow Gaps

No significant gaps identified. The documentation covers a complete workflow from understanding concepts through execution and troubleshooting.

---

## Document Statistics

- **Total Jobs**: 4
- **Total User Stories**: 13
- **Total Tasks**: 13
- **Total Procedures**: 11
- **Total Concepts**: 1
- **Total References**: 1
- **Personas Identified**: 4 (Application Developer, Platform Engineer, Cluster Administrator, Platform Architect)
- **Source Document**: argocd_applications-combined.adoc (1365 lines)
