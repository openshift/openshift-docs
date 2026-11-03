# JTBD-Oriented Table of Contents
# Installing GitOps

**Document**: installing_gitops  
**Generated**: 2026-04-09  
**Total Jobs**: 5 main jobs, 12 user stories

---

## Quick Navigation

### By Workflow Stage
- **DEFINE** (Planning): Job 1
- **EXECUTE** (Installation & Access): Jobs 2, 3, 4, 5
- **VERIFY** (Validation): Job 3.3

### By Persona
- **Cluster Administrator**: Jobs 1, 2, 3, 4
- **DevOps Engineer**: Job 5

### By Criticality
- **High**: Jobs 1, 2, 3, 4
- **Medium**: Jobs 5

---

## Planning & Preparation

### 1. Plan GitOps installation capacity requirements
**Persona**: Cluster Administrator  
**Context**: Before installing OpenShift GitOps on an OpenShift cluster  
**Outcome**: Ensure adequate cluster resources are allocated to prevent installation failures and pod scheduling issues

**Approach**:
- Review default resource allocations for all workload components
- Calculate total resource footprint across 7 GitOps components
- Configure Redis memory limits for large-scale deployments
- Adjust resource quotas to accommodate operator requirements

**User Stories**:

#### 1.1 Understand default resource allocations for all workload components
-> Lines 11-30: Sizing requirements for GitOps - Resource requirements table

**Tasks**:
- Review CPU and memory requests/limits for 7 workload components
- Compare workload requirements against available cluster resources
- Identify which components consume most resources (application-controller: 2 CPU limit, repo-server: 1 CPU limit)
- Learn how to view and modify resource settings via ArgoCD CR

**Success Criteria**:
- Can compare workload requirements against available cluster resources
- Understand which components consume most resources
- Know how to use `oc edit argocd` command to modify resource settings

**Pain Points**:
- Need to manually sum resources across all components
- Resource requirements table doesn't indicate total footprint

---

#### 1.2 Increase Redis memory limits for large-scale deployments
-> Lines 32-78: Sizing requirements for Argo CD redis

**Tasks**:
- Check current Redis memory configuration using `oc get argocd -n openshift-gitops openshift-gitops -o json | jq '.spec.redis.resources'`
- Identify when default 256Mi limit is insufficient (large resource counts)
- Use `oc patch` command to increase memory limits (e.g., 8Gi limit, 256Mi request)
- Monitor memory metrics during application scale-up

**Success Criteria**:
- Successfully patch ArgoCD CR to increase Redis memory
- Verify new limits applied to redis pod
- Monitor memory metrics during application scale-up

**Pain Points**:
- Default 256Mi memory limit insufficient for large resource counts
- Need to monitor metrics and adjust reactively during scale-up
- Must use JSON patch syntax which is error-prone

**Alternatives**:
- Accept default limits and restart pods when memory issues occur
- Pre-configure higher limits in initial ArgoCD CR before installation

---

## Installing the Operator

### 2. Install GitOps Operator via web console
**Persona**: Cluster Administrator  
**Context**: Need to enable GitOps capabilities on an OpenShift cluster using the web console UI  
**Outcome**: GitOps Operator successfully installed with default Argo CD instance available in openshift-gitops namespace

**Approach**:
- Navigate to OperatorHub in web console
- Select appropriate update channel and version
- Configure installation namespace and cluster monitoring
- Verify operator and default Argo CD instance

**User Stories**:

#### 2.1 Select the appropriate update channel and version
-> Lines 97-102: Installing OpenShift GitOps - Channel information

**Tasks**:
- Understand difference between 'latest' channel and version-specific channels (e.g., gitops-1.19)
- Select channel matching organization's version requirements
- Choose between automatic upgrades ('latest') or controlled versions

**Success Criteria**:
- Understand difference between 'latest' channel and version-specific channels
- Selected channel matches organization's version requirements
- Installation proceeds without channel/version conflicts

**Pain Points**:
- 'Latest' channel may auto-upgrade to new major versions unexpectedly
- Unclear which channel to use for production vs non-production clusters

---

#### 2.2 Enable cluster monitoring for the operator namespace
-> Lines 127-143: Installing GitOps Operator in web console - Cluster monitoring

**Tasks**:
- Select "Enable Operator recommended cluster monitoring" checkbox during installation
- Alternatively, apply `openshift.io/cluster-monitoring=true` label to namespace
- Verify monitoring enabled for operator performance tracking

**Success Criteria**:
- Cluster monitoring checkbox selected during installation
- Can verify namespace has openshift.io/cluster-monitoring=true label
- Operator metrics available in cluster monitoring

**Pain Points**:
- Monitoring not enabled by default
- Can forget to enable during installation and have to apply label afterward

---

### 3. Install GitOps Operator via CLI
**Persona**: Cluster Administrator  
**Context**: Need to install GitOps Operator using command-line tools for automation or when web console unavailable  
**Outcome**: GitOps Operator installed via CLI with namespace, OperatorGroup, and Subscription configured correctly

**Approach**:
- Create operator namespace and enable monitoring
- Create and apply OperatorGroup manifest
- Create and apply Subscription manifest
- Verify pods running in both namespaces

**User Stories**:

#### 3.1 Create and configure Subscription for GitOps Operator
-> Lines 225-248: Installing GitOps Operator using CLI - Subscription YAML

**Tasks**:
- Create openshift-gitops-sub.yaml with correct channel and source configuration
- Understand role of metadata.name, metadata.namespace, spec.channel, spec.source fields
- Apply Subscription to cluster using `oc apply`

**Success Criteria**:
- Understand role of metadata.name, metadata.namespace, spec.channel, spec.source fields
- Can modify channel to install specific version
- Subscription applies successfully without errors

**Pain Points**:
- Field descriptions have typos in documentation
- Unclear what happens if wrong channel or source specified
- Must know to use 'redhat-operators' source and 'openshift-marketplace' namespace

---

#### 3.2 Enable cluster monitoring for operator namespace via CLI
-> Lines 182-196: Installing GitOps Operator using CLI - Enable monitoring

**Tasks**:
- Apply `openshift.io/cluster-monitoring=true` label to openshift-gitops-operator namespace
- Use `oc label namespace` command

**Success Criteria**:
- Label applied successfully to namespace
- Can verify monitoring metrics available for operator

**Pain Points**:
- Must remember to apply label separately after namespace creation
- Monitoring not enabled by default

---

#### 3.3 Verify all expected pods are running after installation
-> Lines 263-296: Installing GitOps Operator using CLI - Verification

**Tasks**:
- Run `oc get pods -n openshift-gitops` to verify 8 pods running
- Run `oc get pods -n openshift-gitops-operator` to verify 2 pods running
- Check all pod statuses show Running with appropriate READY counts

**Success Criteria**:
- 8 pods running in openshift-gitops namespace
- 2 pods running in openshift-gitops-operator namespace
- All pod statuses show Running with appropriate READY counts

**Pain Points**:
- Must check two separate namespaces
- Pod names include generated suffixes which change between installations
- Need to understand which pods should be in which namespace

---

## Accessing Argo CD

### 4. Access Argo CD UI after installation
**Persona**: Cluster Administrator  
**Context**: After installing GitOps Operator, need to log into Argo CD UI to begin managing applications  
**Outcome**: Successfully logged into Argo CD UI using either OpenShift credentials or admin password

**Approach**:
- Navigate to Argo CD via console application menu
- Choose authentication method (OpenShift SSO or admin password)
- Retrieve admin password from secret if needed
- Log into Argo CD dashboard

**User Stories**:

#### 4.1 Retrieve admin password from cluster secret
-> Lines 318-323: Logging in to Argo CD - Obtain password

**Tasks**:
- Navigate to Workloads > Secrets in correct namespace
- Find and open `<argo_CD_instance_name>-cluster` secret
- Copy admin.password value from Details tab
- Log in with username 'admin' and copied password

**Success Criteria**:
- Navigate to Workloads > Secrets in correct namespace
- Find and open instance secret
- Copy admin.password field
- Successfully log in with username 'admin' and copied password

**Pain Points**:
- Multi-step navigation required to find password
- Password is random and cannot be predicted
- Secret name includes instance name which may vary

**Alternatives**:
- Use OpenShift credentials if member of cluster-admins group
- Retrieve password via `oc get secret` command from CLI

---

#### 4.2 Use OpenShift credentials via SSO
-> Lines 312-317: Logging in to Argo CD - OpenShift SSO

**Tasks**:
- Ensure user is member of cluster-admins group
- Select "LOG IN VIA OPENSHIFT" option at Argo CD login page
- Authenticate with OpenShift credentials

**Success Criteria**:
- Member of cluster-admins group in OpenShift
- Successfully redirected to OpenShift auth page
- Authenticated and returned to Argo CD UI

**Pain Points**:
- Must be member of cluster-admins group (not just have cluster-admin role binding)
- Need to run `oc adm groups` command to add users to cluster-admins group

**Alternatives**:
- Use admin password from secret instead
- Configure alternative RBAC groups in Argo CD

---

## Installing CLI Tools

### 5. Install GitOps CLI tool on workstation
**Persona**: DevOps Engineer  
**Context**: Need command-line access to configure and manage GitOps and Argo CD resources  
**Outcome**: GitOps argocd CLI installed and functional on local workstation

**Approach**:
- Choose installation method based on OS (Linux tar.gz/RPM, Windows zip, macOS tar.gz)
- Download binary for correct architecture
- Install binary in PATH location
- Verify installation with version command

**User Stories**:

#### 5.1 Install GitOps CLI on Linux using tar.gz
-> Lines 351-417: Installing GitOps CLI on Linux

**Tasks**:
- Download correct tar.gz archive for architecture (x86_64, s390x, ppc64le, or arm64)
- Extract archive using `tar xvzf`
- Move binary to `/usr/local/bin/argocd`
- Set executable permissions with `chmod +x`
- Verify with `argocd version --client`

**Success Criteria**:
- Downloaded correct tar.gz for architecture
- Extracted archive successfully
- Moved binary to /usr/local/bin
- Set executable permissions
- argocd version --client shows expected output

**Pain Points**:
- Must choose correct architecture-specific archive
- Requires sudo to move to /usr/local/bin and set permissions
- Manual download and installation not managed by package manager

**Alternatives**:
- Use RPM method on RHEL for automatic updates
- Use pre-existing argocd binary if compatible version available

---

#### 5.2 Install GitOps CLI on RHEL using RPM
-> Lines 419-517: Installing GitOps CLI on Linux using RPM

**Tasks**:
- Register with Red Hat Subscription Manager
- Pull latest subscription data with `subscription-manager refresh`
- Attach OpenShift subscription pool
- Enable gitops repository for OS/architecture
- Install `openshift-gitops-argocd-cli` package with yum
- Verify installation

**Success Criteria**:
- Registered with Red Hat Subscription Manager
- Attached OCP subscription pool
- Enabled correct gitops repository
- Installed openshift-gitops-argocd-cli package
- argocd version --client shows expected output
- Future dnf upgrade commands will update argocd

**Pain Points**:
- Complex multi-step subscription-manager workflow required
- Must know correct repo name format with version and architecture variables
- Requires active OCP subscription on Red Hat account
- Need root/sudo privileges

**Alternatives**:
- Use tar.gz method to avoid subscription-manager setup
- Use container with CLI pre-installed

---

#### 5.3 Install GitOps CLI on macOS
-> Lines 572-636: Installing GitOps CLI on macOS

**Tasks**:
- Download correct tar.gz for architecture (Intel x86_64 or ARM arm64)
- Extract archive using `tar xvzf`
- Move binary to `/usr/local/bin/argocd`
- Set executable permissions with `chmod +x`
- Verify with `argocd version --client`

**Success Criteria**:
- Downloaded correct tar.gz for architecture
- Extracted archive successfully
- Moved binary to /usr/local/bin
- Set executable permissions
- argocd version --client shows expected output

**Pain Points**:
- Must choose correct architecture (Intel vs ARM)
- Requires sudo for /usr/local/bin installation
- macOS may show security warning for unsigned binary

---

#### 5.4 Install GitOps CLI on Windows
-> Lines 519-570: Installing GitOps CLI on Windows

**Tasks**:
- Download argocd-windows-amd64.zip
- Extract archive with ZIP program
- Move argocd.exe to directory in PATH
- Verify with `argocd version --client`

**Success Criteria**:
- Downloaded argocd-windows-amd64.zip
- Extracted archive with ZIP program
- Moved argocd.exe to directory in PATH
- argocd version --client shows expected output

**Pain Points**:
- Must manually update PATH environment variable or move to existing PATH directory
- No automatic updates (manual download needed for new versions)
- Only x86_64 architecture supported (no ARM64)

**Alternatives**:
- Use WSL and Linux binary instead
- Use container-based approach

---

## Workflow Coverage

### Coverage by Stage
| Stage | Jobs | Coverage |
|-------|------|----------|
| DEFINE | 1 | ✓ Capacity planning covered |
| EXECUTE | 4 (2, 3, 4, 5) | ✓ Full installation workflow |
| VERIFY | 1 (3.3) | ✓ Post-installation verification |

### Gaps & Recommendations
- **Post-Installation Configuration**: No jobs for configuring RBAC, SSO providers beyond default
- **Troubleshooting**: No jobs for resolving installation failures or resource conflicts
- **Upgrade Workflow**: No jobs for upgrading operator or CLI versions
- **Multi-Instance Management**: Limited coverage for creating additional Argo CD instances beyond default

---

## Document Statistics

| Metric | Count |
|--------|-------|
| Total JTBD Records | 17 |
| Main Jobs | 5 |
| User Stories | 12 |
| Unique Personas | 2 |
| Source Assemblies | 3 |
| Total Lines Analyzed | 636 |
| High Criticality Jobs | 4 |
| Medium Criticality Jobs | 1 |
| Procedures (Tasks) | 10 |
| Concepts (Understanding) | 1 |

---

## Related Documentation

**Referenced in this guide**:
- Configuring the GitOps CLI
- Logging in to the Argo CD server in the default mode
- Basic GitOps argocd commands
- Setting up a new Argo CD instance

**Cross-references**:
- xref:../argocd_instance/setting-up-argocd-instance.adoc
- xref:../gitops_cli_argocd/configuring-argocd-gitops-cli.adoc
- xref:../gitops_cli_argocd/logging-in-to-argocd-server-in-default-mode.adoc
- xref:../gitops_cli_argocd/argocd-gitops-cli-reference.adoc
