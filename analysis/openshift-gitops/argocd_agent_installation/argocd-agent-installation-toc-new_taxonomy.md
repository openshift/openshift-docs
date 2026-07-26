# Installing Argo CD Agent
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform administrators to install and configure Argo CD Agent architecture for multi-cluster GitOps management across hub and spoke clusters.

**Personas:** Platform administrator

**Main Jobs:** 7 core jobs across 6 workflow stages

---

## Quick Navigation

**I want to:**
- Understand Agent terminology and architecture → Job 1 (Get Started)
- Set up the control plane → Job 2 (Configure)  
- Connect spoke clusters → Job 3 (Configure)
- Choose deployment mode → Job 4 (Plan)
- Verify Agent installation → Job 5 (Confirm)
- Deploy applications via Agents → Job 6 (Deploy)
- Fix connectivity problems → Job 7 (Troubleshoot)

---

# Table of Contents

## Getting Started

### Job 1: Understand Argo CD Agent Terminology and Architecture
*When setting up Argo CD Agent across hub and spoke clusters*

**Personas:** Platform administrator

#### 1.1 Core Concepts and Definitions `[concept]`
**Goal:** Understand the namespaces, contexts, and CLI parameters required for multi-cluster setup.

- **Task:** Learn Principal and Agent namespace requirements
  → Lines 17-42: Argo CD Agent Terminologies
  Source: Argo CD Agent Terminologies section
  - Principal namespace: where Principal component is installed (not auto-created)
  - Agent namespace: where Agent component is installed (not auto-created)
  - Context: named kubeconfig configuration for cluster switching
  - Principal context: hub (control plane) cluster context name
  - Agent context: spoke (workload) cluster context name

**Context:** Essential foundation before installation. Prevents namespace and context confusion during setup.

---

## Plan Your Deployment

### Job 2: Choose Between Managed and Autonomous Agent Modes
*When deploying Agent components on workload clusters*

**Personas:** Platform administrator
**Timing:** BEFORE Job 5 (Install Agent) - mode choice affects configuration and application deployment patterns

#### 2.1 Understand Mode Implications `[concept]`
**Goal:** Determine the correct deployment mode for organizational control model.

- **Option A: Managed Mode** (hub controls application lifecycle)
  → Lines 147-155: Installing the Argo CD Agent by using a Helm chart - Overview
  Source: Installing the Argo CD Agent by using a Helm chart section
  - Principal manages Agent configuration and lifecycle
  - Hub cluster is source of truth
  - Applications created on hub, deployed to spoke
  
- **Option B: Autonomous Mode** (spoke controls application lifecycle)
  → Lines 147-155: Installing the Argo CD Agent by using a Helm chart - Overview
  Source: Installing the Argo CD Agent by using a Helm chart section
  - Agent functions independently of Principal
  - Spoke cluster is source of truth
  - Applications created on spoke, state reported to hub

**Context:** Mode determines where Application CRs are created and which cluster controls configuration.

---

## Set Up & Configure

### Job 3: Install and Configure the Principal Component with Secure PKI
*When establishing the control plane for multi-cluster GitOps*

**Personas:** Platform administrator
**Requires:** GitOps Operator installed on hub cluster, cluster-scoped Argo CD instance, Apps in any namespace feature configured

#### 3.1 Enable Principal via Argo CD CR `[procedure]`
**Goal:** Deploy Principal component with proper auth and TLS configuration.

- **Task:** Configure Argo CD CR with argoCDAgent.principal section
  → Lines 50-64: Installing the Principal component - Argo CD CR configuration
  Source: Installing the Principal component section
  - Enable Principal with `argoCDAgent.principal.enabled: true`
  - Set auth method: `"mtls:CN=([^,]+)"`
  - Configure namespace allowedNamespaces
  - Disable insecure auto-generation for tls and jwt

**Warning:** sourceNamespaces must exactly match Agent names or deployment/monitoring fails.

#### 3.2 Create Required Namespaces `[procedure]`
**Goal:** Establish namespace-to-agent mapping.

- **Task:** Create one namespace per Agent
  → Lines 65-80: Installing the Principal component - Create namespaces
  Source: Installing the Principal component section
  - Example: `agent-managed`, `agent-autonomous`
  - Namespace names must match Agent names (1:1 mapping)

#### 3.3 Initialize PKI and Generate Certificates `[procedure]`
**Goal:** Secure all Principal-Agent communications with proper PKI.

- **Task:** Initialize CA certificate
  → Lines 82-120: Installing the Principal component - Create required secrets
  Source: Installing the Principal component section
  - Run `argocd-agentctl pki init` to create self-signed CA
  - Creates `argocd-agent-ca` secret

- **Task:** Generate Principal server certificate
  → Lines 82-120: Installing the Principal component - Create required secrets
  Source: Installing the Principal component section
  - Run `argocd-agentctl pki issue principal` with DNS name
  - Creates `argocd-agent-principal-tls` secret

- **Task:** Generate resource proxy certificate
  → Lines 82-120: Installing the Principal component - Create required secrets
  Source: Installing the Principal component section
  - Run `argocd-agentctl pki issue resource-proxy`
  - Creates `argocd-agent-resource-proxy-tls` secret

- **Task:** Generate RSA private key for JWT
  → Lines 82-120: Installing the Principal component - Create required secrets
  Source: Installing the Principal component section
  - Run `argocd-agentctl jwt create-key`
  - Creates `argocd-agent-jwt` secret

**Warning:** CLI-generated PKI is for development/testing only. Production requires proper CA certificates.

---

### Job 4: Set Up Spoke Cluster Environment
*When connecting Agent clusters to the Principal*

**Personas:** Platform administrator
**Requires:** Principal setup complete, argocd-agentctl CLI installed, helm CLI installed (>v3.8.0), access to both clusters

#### 4.1 Create Agent Secrets and Propagate CA `[procedure]`
**Goal:** Establish secure authenticated connections between hub and spoke.

- **Task:** Create Agent secret on Principal cluster
  → Lines 122-145: Setting up a spoke cluster environment
  Source: Setting up a spoke cluster environment section
  - Run `argocd-agentctl agent create` with agent name and resource proxy URL
  - Generates client certificate signed by Principal CA
  - Creates Argo CD cluster secret

- **Task:** Copy CA certificate to Agent cluster
  → Lines 122-145: Setting up a spoke cluster environment
  Source: Setting up a spoke cluster environment section
  - Run `argocd-agentctl pki propagate` 
  - Creates `argocd-agent-ca` secret on Agent cluster

- **Task:** Generate Agent client certificate
  → Lines 122-145: Setting up a spoke cluster environment
  Source: Setting up a spoke cluster environment section
  - Run `argocd-agentctl pki issue agent`
  - Creates `argocd-agent-client-tls` secret on Agent cluster

---

## Deploy & Use

### Job 5: Deploy Agent Component
*When installing the Agent on workload clusters*

**Personas:** Platform administrator
**Requires:** Principal running, spoke cluster environment configured, mode choice made (Job 2)

#### 5.1 Deploy Minimal Argo CD Instance on Agent Cluster `[procedure]`
**Goal:** Provide application controller needed for Agent operations.

- **Task:** Create Argo CD CR with server disabled
  → Lines 157-170: Deploying an Argo CD instance on the Agent cluster
  Source: Installing the Argo CD Agent by using a Helm chart section
  - Set `spec.server.enabled: false` to minimize resource overhead
  - Argo CD instance runs alongside Agent component

#### 5.2 Install Agent in Managed Mode (Helm) `[procedure]`
**Goal:** Enable Principal-controlled application deployment.

- **Task:** Create custom NetworkPolicy for Agent-Redis communication
  → Lines 172-186: Installing the Argo CD Agent in managed mode
  Source: Installing the Argo CD Agent by using a Helm chart section
  - Default GitOps Operator NetworkPolicy blocks Agent-Redis
  - Policy allows ingress on port 6379 from argocd-agent-agent pods

- **Task:** Install managed Agent via Helm
  → Lines 172-186: Installing the Argo CD Agent in managed mode
  Source: Installing the Argo CD Agent by using a Helm chart section
  - Add openshift-helm-charts repo
  - Install with `agentMode="managed"` and Redis configuration

#### 5.3 Install Agent in Autonomous Mode (Helm) `[procedure]`
**Goal:** Enable spoke-controlled application deployment with hub visibility.

- **Task:** Create custom NetworkPolicy for Agent-Redis communication
  → Lines 188-202: Installing the Argo CD Agent in autonomous mode
  Source: Installing the Argo CD Agent by using a Helm chart section
  - Same NetworkPolicy requirement as managed mode

- **Task:** Install autonomous Agent via Helm
  → Lines 188-202: Installing the Argo CD Agent in autonomous mode
  Source: Installing the Argo CD Agent by using a Helm chart section
  - Install with `agentMode="autonomous"` and Redis configuration

- **Task:** Create AppProject in agent namespace
  → Lines 188-202: Installing the Argo CD Agent in autonomous mode
  Source: Installing the Argo CD Agent by using a Helm chart section
  - Required for autonomous mode operation
  - Typically uses wildcard permissions

#### 5.4 Install Agent via Argo CD CR (Alternative to Helm) `[procedure]`
**Goal:** Leverage GitOps Operator lifecycle management for Agent components.

- **Task:** Configure Agent via Argo CD CR
  → Lines 204-226: Installing the Argo CD Agent by using an Argo CD custom resource
  Source: Installing the Argo CD Agent by using an Argo CD custom resource section
  - Set `argoCDAgent.agent.enabled: true`
  - Configure client mode (managed or autonomous)
  - Set Principal server address and TLS settings

**Context:** Alternative to Helm-based installation. CR-based approach integrates with GitOps Operator for lifecycle management.

---

## Track & Monitor

### Job 6: Verify Argo CD Agent Installation
*When completing Agent installation*

**Personas:** Platform administrator
**Requires:** Agent installation complete (Helm or CR-based), Principal running

#### 6.1 Confirm Agent Health and Connectivity `[procedure]`
**Goal:** Ensure setup is working correctly before deploying applications.

- **Task:** Verify Agent pod status
  → Lines 228-253: Verifying the Argo CD Agent installation
  Source: Verifying the Argo CD Agent installation section
  - Check pod is Running with `oc get pod`

- **Task:** Verify Agent connection to Principal
  → Lines 228-253: Verifying the Argo CD Agent installation
  Source: Verifying the Argo CD Agent installation section
  - Check logs for "Authentication successful" and "Connected" messages
  - Verify event stream messages

- **Task:** Verify Principal-side connection
  → Lines 228-253: Verifying the Argo CD Agent installation
  Source: Verifying the Argo CD Agent installation section
  - Check Principal logs for "agent connected" message
  - Check connection status update for Agent
  - List connected Agents with `argocd-agentctl agent list`

#### 6.2 (Optional) Verify Metrics Endpoints `[procedure]`
**Goal:** Enable operational monitoring.

- **Task:** Check Agent metrics service
  → Lines 228-253: Verifying the Argo CD Agent installation
  Source: Verifying the Argo CD Agent installation section
  - Metrics exposed via ClusterIP service
  - Can create route for external access

- **Task:** Check Principal metrics endpoint
  → Lines 228-253: Verifying the Argo CD Agent installation
  Source: Verifying the Argo CD Agent installation section
  - `agent_connected_with_principal` metric increases per connected Agent

---

### Job 7: Deploy Applications Using Agent Architecture
*When deploying applications via Agents*

**Personas:** Platform administrator
**Requires:** Agent installation verified, oc CLI with hub and spoke contexts configured

#### 7.1 Deploy Application in Managed Mode `[procedure]`
**Goal:** Centrally control application deployment to spoke clusters.

- **Task:** Create Application manifest for hub cluster
  → Lines 262-278: Deploying an Argo CD application in managed mode
  Source: Deploying Argo CD applications section
  - Set `metadata.namespace` to agent-managed namespace
  - Set `destination.name` to agent name (not server URL)
  - Apply to hub cluster with `--context "<principal_context>"`

- **Validation:** Verify application on spoke and hub
  → Lines 262-278: Deploying an Argo CD application in managed mode
  Source: Deploying Argo CD applications section
  - Application created on spoke cluster
  - Sync status visible on hub cluster
  - Direct spoke changes automatically reverted

**Context:** Hub is source of truth. Applications created on hub, Agent creates them on spoke.

#### 7.2 Deploy Application in Autonomous Mode `[procedure]`
**Goal:** Enable spoke team autonomy with hub visibility.

- **Task:** Create Application manifest for spoke cluster
  → Lines 280-294: Deploying an Argo CD application in autonomous mode
  Source: Deploying Argo CD applications section
  - Set `destination.server` to `https://kubernetes.default.svc` (local cluster)
  - Apply to spoke cluster with `--context "<agent_context>"`

- **Validation:** Verify application on hub and spoke
  → Lines 280-294: Deploying an Argo CD application in autonomous mode
  Source: Deploying Argo CD applications section
  - Application created on spoke cluster
  - State reported to hub cluster (agent-autonomous namespace)
  - Hub changes not allowed

**Context:** Spoke is source of truth. Applications created on spoke, Agent reports state to hub.

---

## Troubleshoot Issues

### Job 8: Troubleshoot Principal-Agent Communication and Deployment Issues
*When encountering connectivity or deployment problems*

**Personas:** Platform administrator

#### 8.1 Diagnose Common Failure Scenarios `[reference]`
**Goal:** Quickly identify and resolve issues.

- **Scenario A: Agent Cannot Connect to Principal**
  → Lines 296-332: Troubleshooting Principal-Agent communication
  Source: Troubleshooting section
  - Check: Principal and Agent pod health
  - Check: Principal hostname in Agent Helm chart (server parameter)
  - Check: Required certificates and secrets exist

- **Scenario B: Agent Cannot Connect to Redis**
  → Lines 296-332: Troubleshooting Principal-Agent communication
  Source: Troubleshooting section
  - Check: Redis pod health
  - Check: Redis address in Agent Helm chart (redisAddress parameter)
  - Check: Redis secret name and password key
  - Check: NetworkPolicy not blocking Agent-Redis communication
  - Error pattern: "redis: connection pool: failed to dial" or "NOAUTH Authentication required"

- **Scenario C: Agent Handshake with Principal Fails**
  → Lines 296-332: Troubleshooting Principal-Agent communication
  Source: Troubleshooting section
  - Issue: Principal auto-generates insecure certs but Agent validates them
  - Error pattern: "authentication handshake failed: tls: failed to verify certificate"
  - Fix: Either disable Agent validation (tlsClientInSecure=true, NOT for production) or disable Principal insecure generation

- **Scenario D: Agent Cannot View Workload Cluster Resources**
  → Lines 296-332: Troubleshooting Principal-Agent communication
  Source: Troubleshooting section
  - Issue: Agent lacks RBAC permissions outside its namespace
  - Error pattern: "User \"system:serviceaccount:argocd:argocd-agent-agent\" cannot get resource"
  - Fix: Grant appropriate namespace access to Agent service account

---

## Workflow Coverage

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ✅ | Job 1 | Terminology and architecture overview |
| Plan | ✅ | Job 2 | Mode selection (managed vs autonomous) |
| Configure | ✅ | Jobs 3, 4 | Principal setup, spoke environment setup |
| Deploy | ✅ | Jobs 5, 7 | Agent installation, application deployment |
| Confirm | ✅ | Job 6 | Verification procedures |
| Monitor | ⚠️ Limited | Job 6 (partial) | Basic metrics, no dashboard guidance |
| Troubleshoot | ✅ | Job 8 | Common failure scenarios |
| Upgrade | ❌ | - | No upgrade procedures |
| Reference | ⚠️ Limited | Job 8 (partial) | Troubleshooting reference only |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Monitor | No dashboard or metrics visualization guidance | Add section on monitoring Principal and Agent with OpenShift observability stack |
| Upgrade | No upgrade procedures | Add version upgrade procedures for Principal and Agent components |
| Reference | Limited reference material | Add Principal/Agent configuration parameter reference, CLI command reference |

---

## Navigation Guide

### By User Journey

**Initial Setup (Platform Administrator):**
1. Job 1: Understand terminology
2. Job 2: Choose deployment mode
3. Job 3: Install Principal component
4. Job 4: Set up spoke cluster environment
5. Job 5: Deploy Agent component
6. Job 6: Verify installation
7. Job 7: Deploy first application

**Ongoing Operations (Platform Administrator):**
1. Job 7: Deploy applications (managed or autonomous mode)
2. Job 6: Verify Agent health and metrics
3. Job 8: Troubleshoot issues as needed

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 1 job
- Plan: 1 job
- Configure: 2 jobs
- Deploy: 2 jobs
- Confirm: 1 job
- Troubleshoot: 1 job
- Monitor: Partial coverage (gaps identified)
- Upgrade: Gap identified
- Reference: Partial coverage (gaps identified)

**Main Jobs:** 8
**User Stories/Paths:** 14 total (7 user stories within main jobs, 7 main jobs)
**Source Sections:** 13 modules across 1 assembly
**Platform/Tool Variations:** 2 (Helm vs CR-based installation), 2 modes (managed vs autonomous)
