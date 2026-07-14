# JTBD-Oriented Table of Contents
## Argo CD Instance Documentation

**Document:** argocd_instance  
**Generated:** 2026-04-09  
**Total Jobs:** 33 (15 main jobs, 18 supporting jobs)

---

## Quick Navigation

| Workflow Stage | Jobs | User Stories | Tasks |
|----------------|------|--------------|-------|
| DEFINE | 1 | 0 | 0 |
| PROVISION | 0 | 1 | 2 |
| CONFIGURE | 7 | 8 | 0 |
| SECURE | 1 | 3 | 0 |
| SCALE | 1 | 3 | 0 |
| EXTEND | 0 | 1 | 0 |
| MONITOR | 1 | 3 | 3 |
| REFERENCE | 1 | 5 | 0 |

---

## 1. Setup and Provisioning

### Job 1: Set up Argo CD instances
**Type:** MAIN_JOB | **Stage:** DEFINE  
**Persona:** Platform Administrator  
**Context:** Managing GitOps deployment infrastructure  
**Motivation:** establish continuous deployment capabilities using GitOps

> "By default, {gitops-title} installs an instance of Argo CD in the `openshift-gitops` namespace... To manage cluster configurations or deploy applications, you can install and deploy a new user-defined Argo CD instance."

**Source:** Lines 1-379 → Setting up an Argo CD instance

#### Job 1.1: Install a user-defined Argo CD instance
**Type:** USER_STORY | **Stage:** PROVISION  
**Persona:** Platform Administrator  
**Approach:** Use the OpenShift web console to create an ArgoCD custom resource  
**Alternatives:** YAML-based configuration; CLI-based installation  
**Acceptance Criteria:** Argo CD instance is running; Route is created; Admin credentials are accessible

> "To manage cluster configurations or deploy applications, you can install and deploy a new user-defined Argo CD instance. By default, any new user-defined instance has permissions to manage resources only in the namespace where it is deployed."

**Source:** Lines 42-131 → Installing a user-defined Argo CD instance  
**Module Type:** PROCEDURE

##### Task 1.1.1: Create ArgoCD custom resource via web console
**Type:** TASK | **Stage:** PROVISION  
**Context:** Installing Argo CD instance through UI  
**Steps:** Log in to web console; Navigate to Operators > Installed Operators; Select project; Click Create ArgoCD; Configure parameters; Enable Route; Create instance  
**Tools:** OpenShift web console

**Source:** Lines 42-131 → Installing a user-defined Argo CD instance

##### Task 1.1.2: Access Argo CD web UI
**Type:** TASK | **Stage:** VALIDATE  
**Context:** After creating Argo CD instance  
**Steps:** Go to Networking > Routes; Find instance route; Click web UI link; Authenticate using OpenShift or admin credentials  
**Tools:** OpenShift web console; Argo CD UI

**Source:** Lines 97-120 → Installing a user-defined Argo CD instance

#### Job 1.2: Disable default Argo CD instance
**Type:** USER_STORY | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Approach:** Set DISABLE_DEFAULT_ARGOCD_INSTANCE environment variable in operator subscription  
**Acceptance Criteria:** Default Argo CD instance does not start in openshift-gitops namespace

> "To prevent the default Argo CD instance from starting in the `openshift-gitops` namespace, you can use the `openshift-gitops-operator` subscription and configure the `DISABLE_DEFAULT_ARGOCD_INSTANCE` environment variable"

**Source:** Lines 14-37 → Setting up an Argo CD instance

#### Job 1.3: Customize Argo CD console link in multitenant clusters
**Type:** USER_STORY | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Approach:** Set DISABLE_DEFAULT_ARGOCD_CONSOLELINK environment variable  
**Acceptance Criteria:** Console link behavior matches administrator intent (enabled or disabled)

> "In a multitenant cluster, users might have to deal with many instances of Argo CD. After installing an Argo CD instance in your namespace, the Argo CD console link in the Console Application Launcher might open another Argo CD instance"

**Source:** Lines 260-293 → Customizing the Argo CD console link  
**Module Type:** PROCEDURE

---

## 2. Security and Permissions

### Job 6: Configure Argo CD permissions and security
**Type:** MAIN_JOB | **Stage:** SECURE  
**Persona:** Platform Administrator  
**Context:** Multi-tenant cluster environments  
**Motivation:** reduce security risks and prevent privilege escalation

> "When you give namespaces to non-administrator users, for example, development teams, they can use the `namespace-admin` privileges... These roles are highly privileged and can delete all resources. To reduce this risk, configure common cluster roles with limited permissions"

**Source:** Lines 135-199 → Configuring common cluster roles

#### Job 6.1: Configure custom cluster roles for namespace-scoped instances
**Type:** USER_STORY | **Stage:** SECURE  
**Persona:** Platform Administrator  
**Approach:** Specify CONTROLLER_CLUSTER_ROLE and SERVER_CLUSTER_ROLE environment variables in operator subscription  
**Alternatives:** Inject variables directly into Operator Deployment object  
**Acceptance Criteria:** User-defined cluster roles are applied instead of default admin role

> "To configure common cluster roles for all managed namespaces, you can specify user-defined cluster roles for the `CONTROLLER_CLUSTER_ROLE` and `SERVER_CLUSTER_ROLE` environment variables"

**Source:** Lines 135-199 → Configuring common cluster roles by specifying user-defined cluster roles for namespace-scoped instances  
**Module Type:** PROCEDURE

---

## 3. Namespace Management

### Job 10: Configure Argo CD namespace management
**Type:** MAIN_JOB | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Context:** Managing resources across multiple namespaces  
**Motivation:** allow Argo CD to manage resources outside its installation namespace

> "To allow Argo CD to manage resources in other namespaces apart from where it is installed, configure the target namespace with a `argocd.argoproj.io/managed-by` label"

**Source:** Lines 238-256 → Deploying resources to a different namespace

#### Job 10.1: Label namespaces for Argo CD management
**Type:** USER_STORY | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Approach:** Apply argocd.argoproj.io/managed-by label to target namespace  
**Acceptance Criteria:** Argo CD can deploy and manage resources in labeled namespace

> "Configure the target namespace by running the following command: $ oc label namespace <target_namespace> argocd.argoproj.io/managed-by=<argocd_namespace>"

**Source:** Lines 238-256 → Deploying resources to a different namespace  
**Module Type:** PROCEDURE

---

## 4. Scaling and High Availability

### Job 8: Scale Argo CD components for high availability
**Type:** MAIN_JOB | **Stage:** SCALE  
**Persona:** Platform Administrator  
**Context:** Production deployments requiring high availability  
**Motivation:** distribute workloads and ensure service availability

> "To better distribute your workloads among pods, you can increase the number of Argo CD-server and Argo CD-repo-server replicas"

**Source:** Lines 203-235 → Enabling replicas

#### Job 8.1: Enable replicas for Argo CD server and repo server
**Type:** USER_STORY | **Stage:** SCALE  
**Persona:** Platform Administrator  
**Approach:** Set replicas parameters in ArgoCD custom resource spec  
**Acceptance Criteria:** Multiple replicas are running for server and repo-server components

> "Set the `replicas` parameters for the `repo` and `server` spec to the number of replicas you want to run"

**Source:** Lines 203-235 → Enabling replicas for Argo CD server and repo server  
**Module Type:** PROCEDURE  
**Note:** Autoscaler overrides manual replica count if enabled

#### Job 17.1: Enable controller sharding for large-scale deployments
**Type:** USER_STORY | **Stage:** SCALE  
**Persona:** Platform Administrator  
**Approach:** Configure sharding properties in controller spec  
**Alternatives:** Enable dynamic scaling based on cluster count  
**Acceptance Criteria:** Controller replicas are sharded; Memory pressure is reduced

> "sharding.enabled - Enable sharding on the Argo CD Application Controller component. Use this property to manage a large number of clusters and relieve memory pressure on the controller component"

**Source:** Lines 393-578 → Argo CD custom resource properties  
**Note:** Supports static replicas or dynamic scaling based on clusters per shard

#### Job 18.1: Configure high availability with Redis
**Type:** USER_STORY | **Stage:** SCALE  
**Persona:** Platform Administrator  
**Approach:** Enable HA mode in ArgoCD CR  
**Acceptance Criteria:** Redis HA proxy is deployed; HA is enabled globally

> "ha - High-availability options... enabled - Toggle high-availability support globally for Argo CD"

**Source:** Lines 462-466 → Argo CD custom resource properties  
**Note:** Includes Redis HAProxy configuration options

---

## 5. Configuration Management

### Job 13: Configure image pull policies
**Type:** MAIN_JOB | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Context:** Managing container image updates and caching  
**Motivation:** control how and when container images are pulled

> "The {gitops-shortname} Operator lets administrators configure `imagePullPolicy` at multiple levels to control how Argo CD components pull container images"

**Source:** Lines 297-378 → Configuring ImagePullPolicy  
**Module Type:** CONCEPT  
**Note:** Hierarchical precedence: instance > global > default

#### Job 13.1: Set global image pull policy
**Type:** USER_STORY | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Approach:** Set IMAGE_PULL_POLICY environment variable in operator subscription  
**Alternatives:** Set at instance level using spec.imagePullPolicy  
**Acceptance Criteria:** All Argo CD instances use the configured pull policy

> "You can define a global image pull policy for all Argo CD instances managed by the Operator by setting the `IMAGE_PULL_POLICY` environment variable"

**Source:** Lines 297-378 → Configuring ImagePullPolicy  
**Module Type:** CONCEPT

---

## 6. Custom Resource Configuration

### Job 15: Understand Argo CD custom resource structure
**Type:** MAIN_JOB | **Stage:** REFERENCE  
**Persona:** Platform Administrator; Application Developer  
**Context:** Configuring Argo CD instances  
**Motivation:** understand available configuration options

> "The `Argo CD` custom resource is a Kubernetes Custom Resource (CRD) that describes the desired state for a given Argo CD cluster and allows you to configure the components which make up an Argo CD cluster"

**Source:** Lines 380-578 → Argo CD custom resource properties  
**Module Type:** REFERENCE

#### Job 15.1: Configure ApplicationSet controller
**Type:** USER_STORY | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Approach:** Configure applicationSet property in ArgoCD CR  
**Acceptance Criteria:** ApplicationSet controller is enabled and configured

> "ApplicationSet Controller configuration options... enabled - The flag to use to enable the ApplicationSet Controller during the Argo CD installation"

**Source:** Lines 406-424 → Argo CD custom resource properties  
**Note:** Supports annotations, resources, log levels, source namespaces, webhook server

#### Job 15.2: Configure RBAC policies
**Type:** USER_STORY | **Stage:** SECURE  
**Persona:** Platform Administrator  
**Approach:** Define RBAC properties in ArgoCD CR  
**Acceptance Criteria:** RBAC policies are enforced; Users have appropriate permissions

> "rbac - RBAC configuration options... defaultPolicy - The name of the default role that Argo CD falls back to when authorizing API requests... policy - CSV data about user-defined RBAC policies and role definitions"

**Source:** Lines 515-520 → Argo CD custom resource properties  
**Note:** Supports policy matcher modes (glob or regex) and OIDC scope configuration

#### Job 15.3: Configure TLS and certificate management
**Type:** USER_STORY | **Stage:** SECURE  
**Persona:** Platform Administrator  
**Approach:** Configure TLS and initialSSHKnownHosts in ArgoCD CR  
**Acceptance Criteria:** TLS certificates are configured; SSH known hosts are defined

> "tls - TLS configuration options... ca.configMapName - The name of the `ConfigMap` which contains the CA certificate... initialSSHKnownHosts - Defines the initial SSH Known Hosts data for Argo CD"

**Source:** Lines 570-574, 479-482 → Argo CD custom resource properties  
**Note:** Supports both HTTPS (TLS certs) and SSH (known hosts) connections

---

## 7. Repo Server Configuration

### Job 21: Configure Argo CD repo server
**Type:** MAIN_JOB | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Context:** Customizing repo server behavior and capabilities  
**Motivation:** optimize manifest generation and repository interactions

> "The following properties are available for configuring the repo server component"

**Source:** Lines 582-612 → Repo server properties  
**Module Type:** REFERENCE

#### Job 21.1: Configure TLS trust for repo server
**Type:** USER_STORY | **Stage:** SECURE  
**Persona:** Platform Administrator  
**Approach:** Inject custom TLS certificates via secrets and config maps using systemCATrust  
**Acceptance Criteria:** Repo server trusts custom CAs; Plugin workflows can access TLS-enabled resources

> "You can configure the repo server to trust additional certificate authorities (CAs) by injecting custom TLS certificates into the repo server container and its Config Management Plugin sidecar containers"

**Source:** Lines 614-665 → Configure TLS trust for the repo server  
**Module Type:** CONCEPT  
**Note:** Supports wildcard certificates; Enables advanced plugin workflows

#### Job 21.2: Configure execution timeout for rendering tools
**Type:** USER_STORY | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Approach:** Set execTimeout property in repo spec  
**Acceptance Criteria:** Rendering tools have sufficient time to complete

> "execTimeout - Execution timeout in seconds for rendering tools, for example, Helm or Kustomize"

**Source:** Lines 594 → Repo server properties  
**Note:** Default is 180 seconds

---

## 8. Notifications and Monitoring

### Job 24: Set up notifications for Argo CD events
**Type:** MAIN_JOB | **Stage:** MONITOR  
**Persona:** Platform Administrator; Application Developer  
**Context:** Tracking application sync status and failures  
**Motivation:** receive alerts when important events occur

> "Argo CD notifications allow you to send notifications to external services when events occur in your Argo CD instance. For example, you can send notifications to Slack or email when a sync operation fails"

**Source:** Lines 668-716 → Enabling notifications  
**Note:** Notifications are disabled by default

#### Job 24.1: Enable notifications for Argo CD instance
**Type:** USER_STORY | **Stage:** MONITOR  
**Persona:** Platform Administrator  
**Approach:** Set spec.notifications.enabled to true in ArgoCD CR  
**Alternatives:** Use oc patch command  
**Acceptance Criteria:** Notifications controller is enabled and running

> "To enable notifications for an Argo CD instance using the {OCP} web console... set the `spec.notifications.enabled` parameter to `true`"

**Source:** Lines 668-716 → Enabling notifications with an Argo CD instance  
**Module Type:** PROCEDURE

#### Job 24.2: Configure notification templates and triggers
**Type:** USER_STORY | **Stage:** MONITOR  
**Persona:** Platform Administrator  
**Approach:** Configure NotificationsConfiguration CR with templates, triggers, services, and subscriptions  
**Acceptance Criteria:** Notification templates are defined; Triggers are configured; Services are integrated

> "The `NotificationsConfiguration` resource is a Kubernetes custom resource (CR) that manages notifications... you can add templates, triggers, services, and subscription resources"

**Source:** Lines 767-894 → NotificationsConfiguration custom resource properties  
**Module Type:** CONCEPT  
**Note:** default-notifications-configuration CR is created automatically

##### Task 24.2.1: Add notification template
**Type:** TASK | **Stage:** MONITOR  
**Steps:** Edit NotificationsConfiguration CR; Add template under spec.templates; Define message format using Go templating  
**Tools:** OpenShift web console; oc CLI

> "Templates are used to generate the notification template message... spec.templates: template.my-custom-template"

**Source:** Lines 807-824 → NotificationsConfiguration custom resource properties  
**Note:** Uses Go templating with context variables like .app.metadata.name

##### Task 24.2.2: Add notification trigger
**Type:** TASK | **Stage:** MONITOR  
**Steps:** Edit NotificationsConfiguration CR; Add trigger under spec.triggers; Define condition and templates to send  
**Tools:** OpenShift web console; oc CLI

> "Triggers are used to define the condition when a notification is sent to the user and the list of templates required to generate the message"

**Source:** Lines 826-844 → NotificationsConfiguration custom resource properties  
**Note:** Conditions use CEL-like expressions (e.g., app.status.sync.status == 'Unknown')

##### Task 24.2.3: Configure notification service
**Type:** TASK | **Stage:** MONITOR  
**Steps:** Edit NotificationsConfiguration CR; Add service under spec.services; Configure service credentials and settings  
**Tools:** OpenShift web console; oc CLI

> "Services are used to deliver a message... service.slack: token, username, icon"

**Source:** Lines 845-864 → NotificationsConfiguration custom resource properties  
**Note:** Supports Slack, email, and other notification services

#### Job 24.3: Configure notifications in delegated namespaces
**Type:** USER_STORY | **Stage:** MONITOR  
**Persona:** Platform Administrator  
**Approach:** Configure sourceNamespaces and notifications.sourceNamespaces in ArgoCD CR  
**Acceptance Criteria:** Teams can manage notification configuration in their namespaces

> "By default, Argo CD manages notification configuration only within the control plane namespace. With {gitops-title} Operator, cluster administrators can enable teams to manage notification settings for their applications from additional namespaces"

**Source:** Lines 982-1036 → Configuring notifications in any Namespace  
**Module Type:** PROCEDURE  
**Note:** Operator creates NotificationsConfiguration CR in each delegated namespace

---

## 9. Extensions and Plugins

### Job 31: Enable Config Management Plugins
**Type:** USER_STORY | **Stage:** EXTEND  
**Persona:** Platform Administrator  
**Context:** Need to use tools beyond Helm, Jsonnet, and Kustomize  
**Approach:** Configure sidecar container in ArgoCD CR repo spec  
**Acceptance Criteria:** Config Management Plugin is running as sidecar; Custom tool is available

> "Argo CD provides support for Helm, Jsonnet, and Kustomize as built-in config management tools. To use a different config management tool, or to enable features not provided by the built-in config management tools, you can use the Config Management Plugin (CMP)"

**Source:** Lines 720-764 → Enabling Config Management Plugins in an Argo CD CR  
**Module Type:** CONCEPT  
**Note:** Plugin runs as sidecar container in repo server

---

## 10. Multi-Instance Management

### Job 32: Configure multi-instance Argo CD deployments
**Type:** MAIN_JOB | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Context:** Multiple Argo CD instances managing resources  
**Motivation:** prevent conflicts and enable parallel operation of multiple instances

> "{gitops-title} Operator enhances multi-instance support by improving annotation-based resource tracking in Argo CD.Multiple Argo CD instances can use annotation-based tracking by assigning each instance a unique `installationID`"

**Source:** Lines 1052-1069 → Enabling annotation-based resource tracking  
**Module Type:** CONCEPT

#### Job 32.1: Configure annotation-based tracking in multiple instances
**Type:** USER_STORY | **Stage:** CONFIGURE  
**Persona:** Platform Administrator  
**Approach:** Set unique installationID and resourceTrackingMethod in each ArgoCD CR  
**Acceptance Criteria:** Each instance has unique installationID; Resource tracking uses annotation+label; Instances operate without conflicts

> "Multiple Argo CD instances can use annotation-based tracking by assigning each instance a unique `installationID`, which enables them to correctly differentiate resources with identical application names, prevent conflicts, avoid infinite sync loops"

**Source:** Lines 1072-1244 → Configuring annotation-based tracking in multiple Argo CD instances  
**Module Type:** PROCEDURE  
**Note:** Must label namespaces to associate with correct instance

---

## Workflow Coverage

### Coverage by Stage
- **DEFINE:** 1 main job (Instance setup foundation)
- **PROVISION:** 1 user story + 2 tasks (Installation workflow)
- **CONFIGURE:** 7 main jobs + 8 user stories (Extensive configuration options)
- **SECURE:** 1 main job + 3 user stories (Security and access control)
- **SCALE:** 1 main job + 3 user stories (HA and performance)
- **EXTEND:** 1 user story (Plugin support)
- **MONITOR:** 1 main job + 3 user stories + 3 tasks (Notifications and alerting)
- **REFERENCE:** 1 main job + 5 user stories (Configuration reference)

### Coverage Gaps
- **TROUBLESHOOT:** No dedicated troubleshooting content (consider adding common issues and resolutions)
- **UPGRADE/MIGRATE:** No upgrade or migration procedures
- **BACKUP/RESTORE:** No disaster recovery or backup procedures for Argo CD instances
- **OPTIMIZE:** Limited performance tuning guidance beyond replica scaling

### Personas Addressed
- **Platform Administrator:** Primary persona (all jobs)
- **Application Developer:** Secondary persona (monitoring, custom resources)

---

## Document Statistics

- **Total Records:** 33
- **Main Jobs:** 15
- **User Stories:** 15
- **Tasks:** 3
- **Source Assemblies:** 2
  - setting-up-argocd-instance.adoc
  - argo-cd-cr-component-properties.adoc
- **Module Types:**
  - PROCEDURE: 9
  - CONCEPT: 5
  - REFERENCE: 2
- **Lines of Documentation:** 1250

---

**Navigation Complexity:** MEDIUM  
**Rationale:** Documentation covers 10 distinct job categories with clear progression from setup → configuration → scaling → monitoring. Configuration options are extensive but well-organized by component. Multi-instance scenarios add complexity but are isolated to specific sections.
