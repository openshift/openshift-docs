# Argo CD Agent Architecture
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** This guide helps platform teams understand, evaluate, and configure the Argo CD Agent architecture for managing multi-cluster GitOps deployments in a hub-and-spoke model.

**Personas:** Platform architect, Platform engineer, Security engineer

**Main Jobs:** 5 core jobs across 4 workflow stages (Architecture, Plan, Configure, Secure)

---

## Quick Navigation

**I want to:**
- Understand what Argo CD Agent is and how it works → Job 1 (Architecture)
- Compare Agent vs traditional Argo CD → Job 2 (Plan)
- Choose between Managed and Autonomous modes → Job 3 (Configure)
- Secure communication between clusters → Job 4 (Secure)
- Set up namespace isolation for multi-cluster apps → Job 5 (Configure)

---

# Table of Contents

## Understand Architecture

### Job 1: Understand the Argo CD Agent Architecture and Its Capabilities
*When managing multiple OpenShift clusters with GitOps*

**Personas:** Platform architect

#### 1.1 Overview: Hub-and-Spoke Model for Multi-Cluster GitOps

→ Lines 3-12: Introduction to the Argo CD Agent architecture

**Key concepts:**
- Hub-and-spoke architecture with pull-based change management
- Single pane of glass for monitoring across multiple clusters
- Extends Argo CD without replacing it
- Designed for advanced users already familiar with Argo CD

**Why this matters:** Determines if Agent architecture fits your multi-cluster deployment needs before committing to implementation.

#### 1.2 Architecture Components and Terminology

→ Lines 14-26: Architecture and Terminology

**Core terms:**
- **Control plane cluster (hub):** Single cluster providing centralized monitoring; in Managed mode, also source of truth for Application definitions
- **Workload cluster (spoke):** Cluster running application workloads; hosts lightweight Argo CD instance plus agent for local reconciliation
- Pull-based synchronization between control plane and workload clusters

**Agent extension:** Does not replace Argo CD functionality; extends multi-cluster management with pull-based sync and centralized observability.

#### 1.3 Synchronization Mechanism

→ Lines 71-86: Synchronization mechanism between the control plane and workload clusters

**Resource synchronization:**
- Synchronizes Application, AppProject, and Secret objects between control plane and workload clusters
- In Managed mode: changes on control plane propagate to workload clusters
- Status changes on workload clusters report back to control plane

**Unified observability:**
- Control plane web console displays real-time state of applications across all clusters
- Independent synchronization by Agent container, outside Argo CD internal reconciliation loop

---

## Choose Your Approach

### Job 2: Compare Traditional Argo CD with Argo CD Agent
*When choosing between traditional Argo CD and Argo CD Agent*

**Personas:** Platform architect

**Why:** Wrong architecture choice can impact security posture, scalability limits, and operational complexity at scale.

→ Lines 28-69: Comparing Argo CD Agent with traditional Argo CD architecture

#### 2.1 Architecture Comparison Matrix

| Capability | Traditional Push-Based Argo CD | Argo CD Agent Pull-Based |
|------------|--------------------------------|--------------------------|
| **Single pane of glass** | No (each instance shows only its apps) | Yes (all apps across all instances) |
| **Network connectivity** | Hub must connect to cluster APIs; firewalled clusters cannot be managed | Enables firewalled clusters via pull-based sync |
| **Scalability** | Single instance manages multiple clusters; potential CPU/memory bottlenecks | Distributed management; each cluster has dedicated Argo CD instance |
| **Security** | Hub stores credentials for all clusters; workload APIs exposed | No workload credentials or API access needed |
| **Local reconciliation** | Cross-cluster modifications; network latency, egress costs, instability | Each cluster deploys to itself; avoids network issues |
| **Single point of failure** | Hub outage prevents sync to all spokes | Each cluster operates independently |
| **Complexity** | Easier initially, more complex at scale | More complex setup, scales consistently |
| **Maturity** | Fully mature and supported | Emerging; not all features supported |

#### 2.2 Decision Guide

**Choose Traditional Argo CD if:**
- Small number of clusters (<10)
- All clusters are network-accessible from control plane
- Mature feature set is required (ApplicationSets, advanced RBAC, multi-tenancy)
- Simplicity is priority over scalability

**Choose Argo CD Agent if:**
- Large number of clusters (10+) with scalability concerns
- Firewalled or network-isolated clusters need management
- Security requirements prohibit centralized cluster credentials
- Independent cluster operation is required (reduce single point of failure)
- Pull-based GitOps model aligns with operational philosophy

---

## Set Up & Configure

### Job 3: Choose Between Managed and Autonomous Modes
*When configuring Argo CD Agent*

**Personas:** Platform architect, Platform engineer

**Timing:** BEFORE installing Argo CD Agent - mode determines where Application specifications are defined

**Why:** Mode choice impacts security model, operational workflows, and which deployment patterns are supported.

→ Lines 88-100: Argo CD Agent modes overview

#### 3.1 Mode Overview

**Two operational modes:**
- **Managed mode:** Control plane defines application specifications
- **Autonomous mode:** Each workload cluster defines its own application specifications

**Mixed mode supported:** Different clusters can operate under different modes in same configuration.

**Status visibility:** Regardless of mode, control plane displays up-to-date application status across all clusters.

#### 3.2 Managed Mode: Centralized Application Management

→ Lines 102-124: Argo CD Agent Managed mode

**Goal:** Centralize application definitions while improving security over traditional Argo CD.

**Sync direction:**
- `.spec`: Control plane → Workload cluster
- `.status`: Workload cluster → Control plane

**Advantages:**
- Familiar, centralized Argo CD experience
- Create and manage apps via control plane console, CLI, or API
- Eliminates need for centralized cluster credentials (improvement over traditional Argo CD)
- Improves security by removing credential centralization

**Limitations:**
- Limited app-of-apps pattern support
- Control plane compromise risks workload clusters (changes sync downstream)
- Single point of failure: control plane down = no sync to workload clusters

**Best for:**
- Teams preferring centralized application management
- Organizations with strong control plane security
- Workflows where control plane defines deployment targets

#### 3.3 Autonomous Mode: GitOps-First with Distributed Definitions

→ Lines 126-146: Argo CD Agent Autonomous mode

**Goal:** Maintain application definitions in Git while gaining centralized observability without control plane as single point of failure.

**Sync direction:**
- `.spec`: Workload cluster → Control plane
- `.status`: Workload cluster → Control plane

**Advantages:**
- Git as single source of truth for Application definitions (true GitOps)
- No single point of failure in control plane
- Supports complex deployment patterns (app-of-apps)
- Centralized visibility without centralized control

**Limitations:**
- Cannot modify applications from control plane interface
- Requires external management of Application definitions in Git repositories

**Best for:**
- Teams committed to GitOps principles (Git as single source of truth)
- Organizations requiring maximum resilience (no single point of failure)
- Complex deployment patterns (app-of-apps)
- Distributed teams managing their own clusters

---

## Secure Your Environment

### Job 4: Implement mTLS Certificate-Based Authentication
*When securing multi-cluster Argo CD deployments*

**Personas:** Security engineer

**Requires:** Certificate generation and management capabilities (user responsibility)

→ Lines 148-164: Security and Authentication

#### 4.1 Certificate Architecture

**mTLS benefits over password-based authentication:**
- Certificate expiration and rotation support
- Subject verification to prevent Man-in-the-Middle (MITM) attacks
- More secure than traditional passwords

**Certificate structure:**
- Root CA certificate signs both principal and agent certificates
- Public root CA certificate must be available on control plane and workload clusters for validation
- Principal Agent certificate (control plane) signed by root CA
- Each agent has own root CA-signed certificate

#### 4.2 Authentication Flow

**Certificate-based trust establishment:**
1. Root CA certificate distributed to all clusters
2. Control plane (principal) presents CA-signed certificate to agents
3. Agents present CA-signed certificates to principal
4. Mutual verification using root CA public certificate
5. Secure, verifiable communication with rotation and expiration policies

**User responsibility:** You must generate and manage mTLS certificates (not automated).

**Outcome:** Reduced risk of credential exposure; secure communication between control plane and workload clusters.

---

## Set Up & Configure (Continued)

### Job 5: Configure Namespace Isolation for Multi-Cluster Applications
*When managing applications from multiple workload clusters on the control plane*

**Personas:** Platform engineer

**Requires:** Argo CD Agent configured; mode selected (Managed or Autonomous)

→ Lines 166-231: Application Management Across Namespaces

#### 5.1 Namespace Isolation Architecture

**Applications in any namespace feature:**
- Control plane uses this feature to separate Application resources from individual workload clusters
- Each workload cluster assigned dedicated namespace on control plane
- Namespaces act as "source namespaces" for control plane Argo CD instance
- Maintains strict isolation between workload clusters

**Example namespace organization (3 workload clusters w1, w2, w3):**

**Control plane cluster:**
- `argocd` namespace: Argo CD and Argo CD Agent instances
- `argocd-w1` namespace: Applications for workload cluster w1
- `argocd-w2` namespace: Applications for workload cluster w2
- `argocd-w3` namespace: Applications for workload cluster w3

**Each workload cluster:**
- `argocd` namespace: Local Argo CD and Agent instances + Applications

**Synchronization:** Applications in control plane `argocd-w1` namespace sync to `argocd` namespace on workload cluster w1.

#### 5.2 Configure sourceNamespaces in Argo CD CR

→ Lines 215-229: Configuration example

**Configuration:**
```yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: argo-cd
spec:
  sourceNamespaces:
    - argocd-w1
    - argocd-w2
    - argocd-w3
```

**Effect:** Control plane Argo CD instance discovers and reconciles Applications from all listed source namespaces.

**Note:** Namespace names are user-defined; no specific naming convention required by Argo CD Agent.

**Outcome:** Strict isolation between workload cluster applications; centralized monitoring without cross-cluster interference.

---

## Appendices

### A. Known Limitations and Unsupported Features

→ Lines 233-242: Known Limitations

**Active development status:** Feature under active development; limitations apply.

| Limitation | Impact | Workaround |
|------------|--------|------------|
| Limited/no namespace support on workload clusters | Cannot use Applications in any namespace on workload clusters | Use single namespace per workload cluster |
| Partial ApplicationSet support | ApplicationSet features may not work as expected | Verify specific use case before relying on ApplicationSets |
| Limited app-of-apps in Managed mode | App-of-apps pattern restricted in Managed mode | Use Autonomous mode for app-of-apps patterns |
| No pod logs/terminal from control plane | Cannot stream logs or access terminals via control plane | Access workload clusters directly for logs/terminal |
| No principal Agent high availability | Principal Agent is single point of failure | Plan for principal Agent downtime scenarios |
| RBAC/multi-tenancy under development | Advanced RBAC and multi-tenancy not fully supported | Use simpler RBAC models; avoid complex multi-tenancy |

**Planning recommendation:** Review limitations against your requirements before committing to Argo CD Agent architecture.

---

### B. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Architecture | ✅ | Job 1 | Complete architecture overview |
| Plan | ✅ | Job 2 | Architecture comparison and selection |
| Configure | ✅ | Jobs 3, 5 | Mode selection and namespace configuration |
| Secure | ✅ | Job 4 | mTLS certificate-based authentication |
| Deploy | ❌ | - | Installation covered in separate guide |
| Monitor | ❌ | - | No observability content in this guide |
| Troubleshoot | ❌ | - | No troubleshooting procedures |
| Upgrade | ❌ | - | No upgrade content |
| Reference | ⚠️ Limited | Jobs 1, 2 | Architectural reference only |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Deploy | No installation procedures | Link to "Installing Argo CD Agent" guide |
| Monitor | No observability | Add monitoring and health check procedures |
| Troubleshoot | No troubleshooting | Add common issues and resolution steps |
| Upgrade | No upgrade procedures | Add version upgrade and migration guidance |

---

### C. Navigation Guide

#### By User Journey

**Platform Architect evaluating Argo CD Agent:**
1. Job 1: Understand the Argo CD Agent Architecture → Get overview of capabilities
2. Job 2: Compare Traditional Argo CD with Argo CD Agent → Assess tradeoffs
3. Job 3: Choose Between Managed and Autonomous Modes → Determine operational model

**Platform Engineer implementing Argo CD Agent:**
1. Job 1: Understand the Argo CD Agent Architecture → Review synchronization mechanism
2. Job 3: Choose Between Managed and Autonomous Modes → Select and configure mode
3. Job 4: Implement mTLS Certificate-Based Authentication → Secure communication
4. Job 5: Configure Namespace Isolation → Set up multi-cluster isolation

**Security Engineer securing Argo CD Agent:**
1. Job 2: Compare Traditional Argo CD with Argo CD Agent → Review security advantages
2. Job 4: Implement mTLS Certificate-Based Authentication → Configure mTLS
3. Appendix A: Known Limitations → Review RBAC and multi-tenancy status

---

## Document Statistics

**Workflow Coverage:**
- Architecture: 1 job (complete)
- Plan: 1 job (complete)
- Configure: 2 jobs (mode selection, namespace isolation)
- Secure: 1 job (mTLS authentication)
- Deploy: Gap identified
- Monitor: Gap identified
- Troubleshoot: Gap identified
- Upgrade: Gap identified

**Main Jobs:** 5

**User Stories/Approaches:** 8
- Job 1: 3 sub-topics (Overview, Terminology, Sync)
- Job 2: 2 sub-topics (Matrix, Decision Guide)
- Job 3: 3 sub-topics (Overview, Managed, Autonomous)

**Source Sections:** 10 module files (all CONCEPT type)

**Personas:** 3 (Platform architect, Platform engineer, Security engineer)

**Key Capabilities Covered:**
- Hub-and-spoke architecture understanding
- Traditional vs Agent comparison
- Managed vs Autonomous mode selection
- mTLS security configuration
- Namespace isolation setup

**Missing Content (link to other guides):**
- Installation procedures (see "Installing Argo CD Agent" guide)
- Monitoring and observability
- Troubleshooting procedures
- Upgrade and migration
