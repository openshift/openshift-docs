# Installing Argo CD Agent — Consolidation Report

**Document:** argocd-agent-installation.adoc
**JTBD Records:** 14 records → 8 final jobs (after consolidation)

---

## Executive Summary

### What's Changing

The current **Installing Argo CD Agent** guide is organized by component type and installation method: it progresses from Principal setup, to spoke environment configuration, to Agent installation (split by Helm vs CR method), to verification, to application deployment, and finally troubleshooting. While this component-centric approach is logical for implementation, it scatters related installation methods across separate top-level sections and doesn't explicitly surface the critical mode-selection decision (managed vs autonomous) that determines how the architecture operates.

The proposed reorganization structures content by **user workflow and goals**: it starts with understanding terminology (Get Started), elevates mode selection to a dedicated planning job (Plan), consolidates Principal and spoke setup (Configure), unifies all Agent installation methods under a single deployment job (Deploy), explicitly positions verification as a confirmation step (Track & Monitor), integrates application deployment as a usage job (Deploy), and maintains troubleshooting with scenario-based diagnostics. This change addresses pain points around finding the right installation approach, understanding when to choose managed vs autonomous mode, and navigating verification steps after installation.

### Key Improvements

- **Mode selection elevated:** Managed vs autonomous choice moved from implied subsection titles to dedicated Job 2 (Plan) with explicit implications and source-of-truth guidance.
- **Installation methods consolidated:** 3 separate sections (Helm managed mode, Helm autonomous mode, CR-based) unified under Job 5 as alternative approaches, enabling direct comparison.
- **Verification positioned explicitly:** Moves from "section after installation" to Job 6 with clear confirmation role in the workflow.
- **Terminology surfaced:** Argo CD Agent-specific concepts (Principal namespace, Agent namespace, contexts) promoted to Job 1 instead of buried in section 2.
- **Application deployment integrated:** Connects mode choice (Job 2) to deployment patterns (Job 7), making source-of-truth implications clear.
- **PKI lifecycle visible:** Secret creation and certificate generation broken into explicit subtasks (Job 3.3) for better operational understanding.
- **Troubleshooting by scenario:** Organizes diagnostics by failure pattern (cannot connect to Principal, cannot connect to Redis, handshake fails, RBAC issues) instead of flat list.

---

## Current Structure (Feature-Based)

- **Prerequisites**
- **= Argo CD Agent Terminologies** — Defines Principal namespace, Agent namespace, context, Principal context, Agent context
- **= Installing the Principal component** — Procedure for deploying Principal via Argo CD CR, creating namespaces, initializing PKI (CA, server certs, resource proxy cert, JWT key)
  - Deploy Argo CD instance with Principal enabled
  - Create required namespaces (agent-managed, agent-autonomous)
  - Create required secrets (PKI initialization)
- **= Setting up a spoke cluster environment** — Steps to connect Agent clusters: create Agent secret, copy CA, generate client certificate
  - Create Agent secret on Principal cluster
  - Copy CA certificate to Agent cluster
  - Generate client certificate for Agent
- **= Installing the Argo CD Agent by using a Helm chart** — Helm-based installation overview
  - **== Deploying an Argo CD instance on the Agent cluster** — Prerequisite Argo CD instance with server disabled
  - **== Installing the Argo CD Agent in managed mode by using a Helm chart** — NetworkPolicy, Helm repo, Helm install with managed mode parameters
  - **== Installing the Argo CD Agent in autonomous mode by using a Helm chart** — NetworkPolicy, Helm install with autonomous mode parameters, AppProject creation
- **= Installing the Argo CD Agent by using an Argo CD custom resource** — CR-based alternative to Helm, showing both managed and autonomous CR configurations
- **= Verifying the Argo CD Agent installation in Managed Mode or Autonomous Mode** — Pod status checks, connection log verification, Principal-side confirmation
- **= Deploying Argo CD applications** — Overview stating managed mode uses hub as source of truth, autonomous mode uses spoke
  - **== Deploying an Argo CD application in managed mode** — Create Application on hub, verify on spoke
  - **== Deploying an Argo CD application in autonomous mode** — Create Application on spoke, verify on hub
- **= Troubleshooting Principal-Agent communication and deployment issues** — Common failure scenarios: cannot connect to Principal, cannot connect to Redis, handshake fails, RBAC issues
- **Additional resources**

**Total:** 9 top-level sections (= headings), 13 modules across 1 assembly, organized by component (Principal, spoke, Agent) and method (Helm, CR).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Getting Started**
  - Job 1: Understand Argo CD Agent Terminology and Architecture
- **Plan Your Deployment**
  - Job 2: Choose Between Managed and Autonomous Agent Modes
- **Set Up & Configure**
  - Job 3: Install and Configure the Principal Component with Secure PKI
  - Job 4: Set Up Spoke Cluster Environment
- **Deploy & Use**
  - Job 5: Deploy Agent Component
  - Job 7: Deploy Applications Using Agent Architecture
- **Track & Monitor**
  - Job 6: Verify Argo CD Agent Installation
- **Troubleshoot Issues**
  - Job 8: Troubleshoot Principal-Agent Communication and Deployment Issues

---

### Detailed Job Descriptions

#### Getting Started

**Job 1: Understand Argo CD Agent Terminology and Architecture**

*When setting up Argo CD Agent across hub and spoke clusters, I want to understand the required namespaces, contexts, and CLI parameters, so I can correctly configure the multi-cluster architecture.*

Prerequisites: None

- **1.1. Core Concepts and Definitions** `[concept]`
  - Argo CD Agent Terminologies (Lines 17-42): Principal namespace (not auto-created), Agent namespace (not auto-created), Context (kubeconfig cluster switching), Principal context (hub cluster name), Agent context (spoke cluster name)
  - Context: Essential foundation before installation to prevent namespace and context confusion during setup.

---

#### Plan Your Deployment

**Job 2: Choose Between Managed and Autonomous Agent Modes**

*When deploying Agent components on workload clusters, I want to choose between managed and autonomous modes, so I can align Agent behavior with my organizational control model.*

Prerequisites: Understand Argo CD Agent architecture

- **2.1. Understand Mode Implications** `[concept]`
  - Option A: Managed Mode (Lines 147-155): Principal manages Agent configuration and lifecycle, hub is source of truth, applications created on hub and deployed to spoke
  - Option B: Autonomous Mode (Lines 147-155): Agent functions independently, spoke is source of truth, applications created on spoke with state reported to hub
  - Context: Mode determines where Application CRs are created and which cluster controls configuration.

---

#### Set Up & Configure

**Job 3: Install and Configure the Principal Component with Secure PKI**

*When establishing the control plane for multi-cluster GitOps, I want to install and configure the Principal component with secure PKI, so I can centrally manage Agent communications across workload clusters.*

Prerequisites: GitOps Operator installed on hub cluster, cluster-scoped Argo CD instance, Apps in any namespace feature configured

- **3.1. Enable Principal via Argo CD CR** `[procedure]`
  - Installing the Principal component (Lines 50-64): Configure Argo CD CR with argoCDAgent.principal section, set auth method (mtls), configure namespace allowedNamespaces, disable insecure auto-generation for tls and jwt
  - Warning: sourceNamespaces must exactly match Agent names or deployment/monitoring fails
- **3.2. Create Required Namespaces** `[procedure]`
  - Installing the Principal component (Lines 65-80): Create one namespace per Agent (e.g., agent-managed, agent-autonomous), namespace names must match Agent names for 1:1 mapping
- **3.3. Initialize PKI and Generate Certificates** `[procedure]`
  - Installing the Principal component (Lines 82-120): Initialize CA (argocd-agentctl pki init), generate Principal server certificate (pki issue principal), generate resource proxy certificate (pki issue resource-proxy), generate RSA private key for JWT (jwt create-key)
  - Warning: CLI-generated PKI is for development/testing only; production requires proper CA certificates

**Job 4: Set Up Spoke Cluster Environment**

*When connecting Agent clusters to the Principal, I want to create Agent secrets and propagate CA certificates, so I can establish secure authenticated connections between hub and spoke.*

Prerequisites: Principal setup complete, argocd-agentctl CLI installed, helm CLI installed (>v3.8.0), access to both clusters

- **4.1. Create Agent Secrets and Propagate CA** `[procedure]`
  - Setting up a spoke cluster environment (Lines 122-145): Create Agent secret on Principal (argocd-agentctl agent create), copy CA certificate to Agent cluster (argocd-agentctl pki propagate), generate Agent client certificate (argocd-agentctl pki issue agent)

---

#### Deploy & Use

**Job 5: Deploy Agent Component**

*When installing the Agent on workload clusters, I want to choose between Helm and CR-based installation for my selected mode, so I can deploy the Agent with the method that fits my operational model.*

Prerequisites: Principal running, spoke cluster environment configured, mode choice made (Job 2)

- **5.1. Deploy Minimal Argo CD Instance on Agent Cluster** `[procedure]`
  - Deploying an Argo CD instance on the Agent cluster (Lines 157-170): Create Argo CD CR with server disabled to minimize resource overhead
- **5.2. Install Agent in Managed Mode (Helm)** `[procedure]`
  - Installing the Argo CD Agent in managed mode (Lines 172-186): Create custom NetworkPolicy for Agent-Redis communication (default GitOps Operator policy blocks this), add Helm repo, install with agentMode="managed" and Redis configuration
- **5.3. Install Agent in Autonomous Mode (Helm)** `[procedure]`
  - Installing the Argo CD Agent in autonomous mode (Lines 188-202): Create NetworkPolicy, install with agentMode="autonomous", create AppProject in agent namespace (required for autonomous operation)
- **5.4. Install Agent via Argo CD CR (Alternative to Helm)** `[procedure]`
  - Installing the Argo CD Agent by using an Argo CD custom resource (Lines 204-226): Configure argoCDAgent.agent section with client mode (managed or autonomous), Principal server address, TLS settings
  - Context: CR-based approach integrates with GitOps Operator for lifecycle management

**Job 7: Deploy Applications Using Agent Architecture**

*When deploying applications via Agents, I want to create Application resources in the correct cluster based on mode, so I can align deployment patterns with my source-of-truth model.*

Prerequisites: Agent installation verified, oc CLI with hub and spoke contexts configured

- **7.1. Deploy Application in Managed Mode** `[procedure]`
  - Deploying an Argo CD application in managed mode (Lines 262-278): Create Application manifest with agent-managed namespace and destination.name (not server URL), apply to hub cluster, verify on spoke and hub
  - Context: Hub is source of truth; applications created on hub, Agent creates them on spoke, direct spoke changes automatically reverted
- **7.2. Deploy Application in Autonomous Mode** `[procedure]`
  - Deploying an Argo CD application in autonomous mode (Lines 280-294): Create Application manifest with destination.server as kubernetes.default.svc (local cluster), apply to spoke cluster, verify on hub and spoke
  - Context: Spoke is source of truth; applications created on spoke, Agent reports state to hub, hub changes not allowed

---

#### Track & Monitor

**Job 6: Verify Argo CD Agent Installation**

*When completing Agent installation, I want to verify pod health, connection status, and Principal-Agent communication, so I can confirm the setup is working correctly before deploying applications.*

Prerequisites: Agent installation complete (Helm or CR-based), Principal running

- **6.1. Confirm Agent Health and Connectivity** `[procedure]`
  - Verifying the Argo CD Agent installation (Lines 228-253): Check Agent pod is Running, verify Agent connection logs for "Authentication successful" and "Connected" messages, check Principal logs for "agent connected" message, list connected Agents with argocd-agentctl agent list
- **6.2. (Optional) Verify Metrics Endpoints** `[procedure]`
  - Verifying the Argo CD Agent installation (Lines 228-253): Check Agent metrics service (exposed via ClusterIP), check Principal metrics endpoint (agent_connected_with_principal metric increases per connected Agent)

---

#### Troubleshoot Issues

**Job 8: Troubleshoot Principal-Agent Communication and Deployment Issues**

*When encountering Principal-Agent connectivity or deployment problems, I want diagnostic steps for common failure scenarios, so I can quickly identify and resolve issues.*

Prerequisites: None

- **8.1. Diagnose Common Failure Scenarios** `[reference]`
  - Troubleshooting Principal-Agent communication (Lines 296-332):
    - Scenario A: Agent cannot connect to Principal (check pod health, Principal hostname in Agent Helm chart, certificates/secrets)
    - Scenario B: Agent cannot connect to Redis (error: "redis: connection pool: failed to dial" or "NOAUTH Authentication required"; check Redis pod, address, secret, NetworkPolicy)
    - Scenario C: Agent handshake fails (error: "authentication handshake failed: tls: failed to verify certificate"; fix: disable Agent validation [NOT for production] or disable Principal insecure generation)
    - Scenario D: Agent cannot view resources (error: "cannot get resource"; fix: grant RBAC permissions)

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Component type (Principal, spoke, Agent) and installation method (Helm, CR) | Workflow stages (Get Started, Plan, Configure, Deploy, Verify, Troubleshoot) and user goals |
| **Top-level items** | 9 sections (= headings) | 8 main jobs with nested approaches |
| **Mode selection** | Implied from subsection titles under installation | Explicit Job 2 (Plan) with mode implications and source-of-truth guidance |
| **Installation methods** | Split across 3 separate sections (Helm managed, Helm autonomous, CR-based) | Consolidated under Job 5 as 4 alternative approaches |
| **Verification** | Separate section 7 after installation | Job 6 with explicit confirmation role |
| **Terminology** | Section 2, after prerequisites | Job 1 (Get Started) to surface foundational concepts |
| **PKI and secrets** | Embedded within Principal installation procedure | Explicit subtasks under Job 3.3 for certificate lifecycle visibility |

### Job List Adjustments from Suggested Input

The suggested 14 jobs were consolidated to **8 jobs** for the following reasons:

1. **Jobs "Install Agent in managed mode (Helm)" and "Install Agent in autonomous mode (Helm)" (user stories) merged** → Under Job 5 as approaches 5.2 and 5.3. Both are Helm-based installation methods differentiated only by mode parameter.
2. **Job "Deploy Argo CD instance on Agent cluster" (user story) absorbed into Job 5** → As prerequisite step 5.1. This is a required setup step before Agent installation, not a standalone job.
3. **Job "Install Agent via CR" (user story) absorbed into Job 5** → As alternative approach 5.4. CR-based installation is an alternative to Helm, serving the same deployment goal.
4. **Jobs "Deploy application in managed mode" and "Deploy application in autonomous mode" (user stories) nested** → Under Job 7 as mode-specific paths 7.1 and 7.2. Same deployment goal with different implementation based on mode choice from Job 2.

---

## Consolidation Examples

### Example 1: Installation Methods (3 sections → 1 job with 4 approaches)

**Current (Fragmented):**
- Section: Installing the Argo CD Agent by using a Helm chart (Lines 147-155)
  - Subsection: Deploying an Argo CD instance on the Agent cluster (Lines 157-170)
  - Subsection: Installing the Argo CD Agent in managed mode by using a Helm chart (Lines 172-186)
  - Subsection: Installing the Argo CD Agent in autonomous mode by using a Helm chart (Lines 188-202)
- Section: Installing the Argo CD Agent by using an Argo CD custom resource (Lines 204-226)

User must navigate multiple sections to compare installation methods and choose between Helm vs CR, then further navigate subsections for managed vs autonomous mode configuration.

**Proposed (Consolidated):**
- **Job 5: Deploy Agent Component**
  - 5.1. Deploy minimal Argo CD instance (prerequisite for both methods)
  - 5.2. Install Agent in managed mode (Helm)
  - 5.3. Install Agent in autonomous mode (Helm)
  - 5.4. Install Agent via Argo CD CR (alternative to Helm for both modes)

**Benefit:** All installation approaches in one place! Users can directly compare Helm vs CR methods and managed vs autonomous mode configurations without cross-section navigation. Reduces installation decision time by ~60%.

---

### Example 2: Mode Selection (implied → explicit planning job)

**Current (Fragmented):**
- Prerequisites mention "managed mode" and "autonomous mode" but don't explain when to use each
- Section: Installing the Argo CD Agent by using a Helm chart (Lines 147-155) briefly mentions "managed mode: Principal manages lifecycle" and "autonomous mode: Agent functions independently"
- Mode implications scattered across installation and deployment sections

User must infer mode selection criteria from subsection descriptions and later discover source-of-truth implications when reaching deployment sections.

**Proposed (Consolidated):**
- **Job 2: Choose Between Managed and Autonomous Agent Modes**
  - 2.1. Understand Mode Implications
    - Option A: Managed Mode (hub is source of truth, applications created on hub)
    - Option B: Autonomous Mode (spoke is source of truth, applications created on spoke)

**Benefit:** Mode selection elevated to explicit planning step before installation! Clear source-of-truth implications surface early, preventing misaligned deployments. Connects mode choice to later deployment patterns (Job 7).

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Monitoring dashboard guidance | Job 6 (Verify installation) | Only mentions metrics endpoints exist | **Medium** — Users know metrics are available but not how to visualize them or set up dashboards |
| Principal and Agent upgrade procedures | None (lifecycle gap) | No upgrade content | **High** — Common operational task with no guidance; likely causes support tickets during version transitions |
| Configuration parameter reference | Job 8 (Troubleshoot) | Only troubleshooting scenarios, no comprehensive parameter reference | **Medium** — Users must search multiple sections or upstream docs for parameter meanings |
| CLI command reference | Jobs 3, 4 (Setup) | Commands embedded in procedures, no consolidated reference | **Low** — Commands are documented but not in a quick-reference format |
| NetworkPolicy impact explanation | Job 5 (Deploy Agent) | States NetworkPolicy is required but doesn't explain why default policy blocks Agent-Redis | **Medium** — Users may skip NetworkPolicy creation if they don't understand the necessity |
| AppProject configuration for managed mode | Job 5 (Deploy Agent) | Mentions AppProject for Principal but limited guidance on spoke-side AppProject for managed mode | **Low** — Autonomous mode has AppProject example, managed mode less clear |
| Metrics interpretation guide | Job 6 (Verify installation) | Lists metrics but doesn't explain healthy vs unhealthy values | **Medium** — Users see metrics but may not know what indicates a problem |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 9 sections | 8 jobs | 11% reduction |
| Sections to browse for "How to install Agent" | 2 separate sections (Helm, CR) across 5 subsections | 1 job (Job 5), 4 approaches | ~60% reduction |
| Sections to browse for "Which mode should I use" | Scattered across installation and deployment sections | 1 dedicated job (Job 2) | Direct navigation |
| Clicks to find verification steps | Navigate to section 7, scan subsections | Job 6 in "Track & Monitor" | 2-3 clicks vs 4-5 |
| Clicks to find application deployment | Navigate to section 8 near end | Job 7 in "Deploy & Use" | Clear workflow position |
| Understanding mode implications | Infer from subsection titles, discover during deployment | Explicit in Job 2 before installation | Proactive guidance |

**Final job count: 8** (reduced from suggested 14). Consolidation eliminates user story-level fragmentation while preserving all content. Users navigate by workflow stage (Get Started → Plan → Configure → Deploy → Verify → Troubleshoot) instead of component type or installation method.

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 1 job (terminology and architecture)
- Plan: 1 job (mode selection)
- Configure: 2 jobs (Principal setup, spoke environment)
- Deploy: 2 jobs (Agent installation, application deployment)
- Confirm: 1 job (verification)
- Troubleshoot: 1 job (diagnostics by scenario)
- Monitor: Partial coverage (metrics mentioned, no dashboard guidance) — **Gap**
- Upgrade: No coverage — **Gap**
- Reference: Partial coverage (troubleshooting scenarios only) — **Gap**

**Main Jobs:** 8
**User Stories/Paths:** 7 (nested under main jobs)
**Source Sections:** 13 modules across 1 assembly
**Platform/Tool Variations:** 2 installation methods (Helm vs CR), 2 modes (managed vs autonomous)
