# Installing GitOps - JTBD-Based Table of Contents

## Quick Navigation

**Jump to:**
- [Planning & Prerequisites](#1-plan-gitops-deployment-resources)
- [Web Console Installation](#2-install-gitops-operator-via-web-console)
- [CLI Installation](#3-install-gitops-operator-via-cli)
- [Access & Authentication](#4-access-argo-cd-instance)
- [CLI Tools](#cli-installation-workflows)

---

## Planning & Prerequisites

### 1. Plan GitOps deployment resources

**Goal:** Ensure adequate cluster resources before installing OpenShift GitOps

**When I want to** deploy GitOps in my cluster, **I need to** understand resource requirements, **so I can** avoid installation failures and ensure proper scheduling of Argo CD pods.

**Approach:**
- Review default resource requirements for all GitOps components
- Plan for scale by adjusting Redis memory limits based on workload size
- Validate namespace quotas won't block installation

**Key Tasks:**

#### 1.1 Understand resource requirements for default GitOps workloads
-> Lines 6-33: Sizing requirements for GitOps
- **Task 1.1.1:** Review default resource requests and limits
  - Source: Lines 13-25, Table of 7 GitOps components with CPU/memory specs
- **Task 1.1.2:** Check and modify ArgoCD custom resource specifications
  - Source: Lines 27-32, `oc edit argocd` command

#### 1.2 Size Redis resources for large-scale deployments
-> Lines 34-80: Sizing requirements for Argo CD redis
- **Task 1.2.1:** Check current Redis memory configuration
  - Source: Lines 40-66, `oc get argocd ... | jq '.spec.redis.resources'`
- **Task 1.2.2:** Adjust Redis memory limits for scale
  - Source: Lines 68-80, `oc patch argocd` to set 8Gi limit

---

## Installation Workflows

### 2. Install GitOps Operator via web console

**Goal:** Deploy the OpenShift GitOps Operator using the graphical web console

**When I want to** install GitOps using a GUI, **I need to** configure Operator settings through the web console, **so I can** visually track installation progress and verify deployment.

**Approach:**
- Navigate through OperatorHub to locate and select GitOps
- Configure installation namespace, version channel, and monitoring
- Verify successful deployment through Installed Operators view

**Key Tasks:**

#### 2.1 Navigate to OperatorHub and locate GitOps Operator
-> Lines 107-116: Installing OpenShift GitOps Operator in web console
- **Task 2.1.1:** Search for OpenShift GitOps in OperatorHub
  - Source: Lines 114-116, Search and click workflow

#### 2.2 Configure Operator installation settings
-> Lines 118-147: Install Operator page configuration
- **Task 2.2.1:** Select update channel and version
  - Source: Lines 120-129, Channel selection (latest vs. version-specific)
- **Task 2.2.2:** Choose installation namespace
  - Source: Lines 124-129, Default: `openshift-gitops-operator`
- **Task 2.2.3:** Enable cluster monitoring
  - Source: Lines 131-147, Cluster monitoring checkbox and label method

#### 2.3 Complete installation and verify deployment
-> Lines 149-155: Installation completion and verification
- **Task 2.3.1:** Click Install to deploy Operator
  - Source: Lines 149-151, Installs in all namespaces
- **Task 2.3.2:** Verify Operator status is Succeeded
  - Source: Lines 153-155, Check Installed Operators status

---

### 3. Install GitOps Operator via CLI

**Goal:** Deploy the OpenShift GitOps Operator using command-line tools for automation

**When I want to** install GitOps programmatically, **I need to** create OperatorGroup and Subscription resources via CLI, **so I can** automate deployments and integrate with infrastructure-as-code workflows.

**Approach:**
- Create operator namespace with monitoring enabled
- Apply OperatorGroup and Subscription manifests
- Verify pod deployments in both operator and runtime namespaces

**Key Tasks:**

#### 3.1 Create and configure Operator namespace
-> Lines 173-203: Namespace creation and configuration
- **Task 3.1.1:** Create openshift-gitops-operator namespace
  - Source: Lines 174-187, `oc create ns openshift-gitops-operator`
- **Task 3.1.2:** Enable cluster monitoring on namespace
  - Source: Lines 189-203, Label with `openshift.io/cluster-monitoring=true`

#### 3.2 Create and apply OperatorGroup
-> Lines 205-234: OperatorGroup resource creation
- **Task 3.2.1:** Create OperatorGroup YAML manifest
  - Source: Lines 206-219, OperatorGroup spec with upgradeStrategy
- **Task 3.2.2:** Apply OperatorGroup to cluster
  - Source: Lines 221-234, `oc apply -f gitops-operator-group.yaml`

#### 3.3 Subscribe namespace to GitOps Operator
-> Lines 235-277: Subscription resource creation
- **Task 3.3.1:** Create Subscription YAML manifest
  - Source: Lines 236-262, Subscription spec with channel, source, approval
- **Task 3.3.2:** Apply Subscription to cluster
  - Source: Lines 264-277, `oc apply -f openshift-gitops-sub.yaml`

#### 3.4 Verify GitOps pod deployment
-> Lines 279-316: Pod verification in both namespaces
- **Task 3.4.1:** Verify openshift-gitops pods are running
  - Source: Lines 279-300, `oc get pods -n openshift-gitops` (8 pods)
- **Task 3.4.2:** Verify operator controller is running
  - Source: Lines 302-316, `oc get pods -n openshift-gitops-operator` (controller-manager)

---

## Access & Authentication

### 4. Access Argo CD instance

**Goal:** Log in to the Argo CD UI using admin credentials or OpenShift SSO

**When I want to** access the Argo CD web interface, **I need to** retrieve admin credentials from Secrets, **so I can** manage applications and configurations through the UI.

**Approach:**
- Navigate to Argo CD UI via OpenShift console menu
- Retrieve admin password from Kubernetes Secret
- Choose between admin credentials or OpenShift SSO authentication

**Key Tasks:**

#### 4.1 Navigate to Argo CD UI
-> Lines 318-338: UI access and prerequisites
- **Task 4.1.1:** Verify GitOps Operator installation in console
  - Source: Line 331, Check Operators -> Installed Operators
- **Task 4.1.2:** Open Argo CD from console menu
  - Source: Line 332, Navigate to menu -> OpenShift GitOps -> Cluster Argo CD

#### 4.2 Authenticate with admin credentials
-> Lines 339-354: Admin credential retrieval and login
- **Task 4.2.1:** Retrieve admin password from Secret
  - Source: Lines 339-343, Navigate to Workloads -> Secrets, copy admin.password
- **Task 4.2.2:** Log in with admin username and password
  - Source: Line 344, Use `admin` as username

#### 4.3 Authenticate with OpenShift credentials
-> Lines 333-338: OpenShift SSO authentication
- **Task 4.3.1:** Add user to cluster-admins group
  - Source: Lines 335-338, `oc adm groups new cluster-admins <user>`
- **Task 4.3.2:** Select LOG IN VIA OPENSHIFT option
  - Source: Line 333, Use OpenShift OAuth

---

## CLI Installation Workflows

### 5. Install GitOps CLI on Linux

**Goal:** Install the argocd CLI tool on Linux systems

**When I want to** manage GitOps from the command line on Linux, **I need to** download and install the argocd binary, **so I can** execute GitOps commands without using the web UI.

**Approach:**
- Download architecture-specific tarball from Red Hat content gateway
- Extract and install binary to system PATH
- Verify installation with version check

**Key Tasks:**

#### 5.1 Download and extract CLI archive
-> Lines 381-410: Download and extraction process
- **Task 5.1.1:** Download architecture-specific tarball
  - Source: Lines 388-403, Support for x86_64, s390x, ppc64le, arm64
- **Task 5.1.2:** Extract tar.gz archive
  - Source: Lines 405-410, `tar xvzf <file>`

#### 5.2 Install CLI binary to PATH
-> Lines 412-424: Binary installation and permissions
- **Task 5.2.1:** Move binary to /usr/local/bin
  - Source: Lines 412-417, `sudo mv argocd /usr/local/bin/argocd`
- **Task 5.2.2:** Make binary executable
  - Source: Lines 419-424, `sudo chmod +x`

#### 5.3 Verify CLI installation
-> Lines 426-452: Version verification
- **Task 5.3.1:** Run argocd version command
  - Source: Lines 426-452, `argocd version --client` shows build info

---

### 6. Install GitOps CLI via RPM

**Goal:** Install the argocd CLI as a managed RPM package on RHEL systems

**When I want to** install argocd CLI with automatic updates, **I need to** enable GitOps repositories and install via yum/dnf, **so I can** benefit from system package management.

**Approach:**
- Register system with Red Hat Subscription Manager
- Enable architecture-specific GitOps repositories
- Install openshift-gitops-argocd-cli package

**Key Tasks:**

#### 6.1 Register system and enable GitOps repositories
-> Lines 466-554: Subscription and repository configuration
- **Task 6.1.1:** Register with subscription manager
  - Source: Lines 466-471, `subscription-manager register`
- **Task 6.1.2:** Refresh subscription data
  - Source: Lines 473-478, `subscription-manager refresh`
- **Task 6.1.3:** Find and attach GitOps subscription
  - Source: Lines 480-492, List and attach pool ID
- **Task 6.1.4:** Enable architecture-specific GitOps repository
  - Source: Lines 494-554, Enable repos for x86_64, s390x, ppc64le, aarch64

#### 6.2 Install and verify CLI package
-> Lines 556-589: Package installation and verification
- **Task 6.2.1:** Install openshift-gitops-argocd-cli RPM
  - Source: Lines 556-561, `yum install openshift-gitops-argocd-cli`
- **Task 6.2.2:** Verify CLI version and build
  - Source: Lines 563-589, `argocd version --client`

---

### 7. Install GitOps CLI on Windows

**Goal:** Install the argocd CLI tool on Windows systems

**When I want to** manage GitOps from Windows command line, **I need to** download and install the Windows binary, **so I can** execute GitOps commands on Windows workstations.

**Approach:**
- Download Windows x86_64 zip archive
- Extract and move binary to PATH directory
- Verify installation

**Key Tasks:**

#### 7.1 Download and extract CLI archive
-> Lines 591-619: Download and extraction for Windows
- **Task 7.1.1:** Download argocd-windows-amd64.zip
  - Source: Lines 598-610, Windows x86_64 only
- **Task 7.1.2:** Extract zip archive
  - Source: Line 612, Use ZIP program to extract

#### 7.2 Install CLI to PATH
-> Lines 614-619: Binary installation to PATH
- **Task 7.2.1:** Move argocd.exe to PATH directory
  - Source: Lines 614-619, `move argocd.exe <directory>`

#### 7.3 Verify CLI installation
-> Lines 621-647: Verification on Windows
- **Task 7.3.1:** Run argocd version command
  - Source: Lines 621-647, Platform shows windows/amd64

---

### 8. Install GitOps CLI on macOS

**Goal:** Install the argocd CLI tool on macOS systems

**When I want to** manage GitOps from macOS command line, **I need to** download and install the macOS binary, **so I can** execute GitOps commands on Mac workstations.

**Approach:**
- Download architecture-specific tarball (Intel or ARM)
- Extract and install binary to system PATH
- Verify installation

**Key Tasks:**

#### 8.1 Download and extract CLI archive
-> Lines 649-676: Download and extraction for macOS
- **Task 8.1.1:** Download architecture-specific tarball
  - Source: Lines 656-668, Intel (amd64) or ARM (arm64) options
- **Task 8.1.2:** Extract tar.gz archive
  - Source: Lines 670-676, `tar xvzf <file>`

#### 8.2 Install CLI binary to PATH
-> Lines 678-690: Binary installation and permissions
- **Task 8.2.1:** Move binary to /usr/local/bin
  - Source: Lines 678-683, `sudo mv argocd /usr/local/bin/argocd`
- **Task 8.2.2:** Make binary executable
  - Source: Lines 685-690, `sudo chmod +x`

#### 8.3 Verify CLI installation
-> Lines 692-718: Version verification on macOS
- **Task 8.3.1:** Run argocd version command
  - Source: Lines 692-718, Platform shows darwin/amd64

---

## Workflow Coverage

### Installation Path Decision Tree

```
Start: Do I need GitOps installed?
├─ Yes → Do I need to plan resources first?
│  ├─ Yes → [Job 1: Plan deployment resources]
│  └─ No → Continue
│
├─ Installation method?
│  ├─ Web Console → [Job 2: Install via web console]
│  ├─ CLI → [Job 3: Install via CLI]
│  └─ Both documented
│
└─ Post-install: Do I need to access Argo CD UI?
   └─ Yes → [Job 4: Access Argo CD instance]

Separate: Do I need CLI tools?
├─ Linux tarball → [Job 5: Install CLI on Linux]
├─ Linux RPM → [Job 6: Install via RPM]
├─ Windows → [Job 7: Install CLI on Windows]
└─ macOS → [Job 8: Install CLI on macOS]
```

### Coverage Gaps

| Gap Type | Description | Impact |
|----------|-------------|--------|
| **Troubleshooting** | No installation failure scenarios documented | Medium |
| **Multi-instance** | Creating additional Argo CD instances not covered | Medium |
| **Upgrades** | Channel switching and version upgrades not detailed | Medium |
| **Uninstallation** | Operator removal process not documented here | Low |

---

## Document Statistics

- **Total Jobs:** 8 main jobs
- **Total User Stories:** 26
- **Total Tasks:** 41
- **Total Records:** 75
- **Primary Personas:** 2 (cluster administrator, developer)
- **Workflow Stages:** 4 (DEFINE, EXECUTE, VERIFY, OPERATE)
- **Source Modules:** 9 unique modules
- **Module Types:** 3 (CONCEPT: 1, PROCEDURE: 7, SNIPPET: 1)

### Job Distribution by Stage

| Stage | Jobs | User Stories | Tasks |
|-------|------|--------------|-------|
| DEFINE | 1 | 2 | 4 |
| EXECUTE | 6 | 18 | 31 |
| VERIFY | 0 | 4 | 4 |
| OPERATE | 1 | 2 | 2 |

### Job Distribution by Persona

| Persona | Jobs | User Stories | Tasks |
|---------|------|--------------|-------|
| Cluster Administrator | 4 | 10 | 18 |
| Developer | 4 | 16 | 23 |

---

**Generated:** 2026-04-09  
**Source:** installing_gitops book, openshift-gitops distro  
**JTBD Records:** 75 total (8 main jobs, 26 user stories, 41 tasks)
