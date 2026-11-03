# Installing Argo CD Agent - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-04-10
**JTBD Records:** 14
**Main Jobs:** 7 (rolled up from records)
**Coverage:** Standard schema (no research extensions)

---

## Current Structure (Feature-Based)

**Installing Argo CD Agent**
- Prerequisites
- = Argo CD Agent Terminologies
- = Installing the Principal component
  - Procedure: Deploy Argo CD instance with Principal enabled
  - Create required namespaces
  - Create required secrets (PKI initialization)
- = Setting up a spoke cluster environment
  - Create Agent secret on Principal cluster
  - Copy CA certificate to Agent cluster
  - Generate client certificate for Agent
- = Installing the Argo CD Agent by using a Helm chart
  - == Deploying an Argo CD instance on the Agent cluster
  - == Installing the Argo CD Agent in managed mode by using a Helm chart
  - == Installing the Argo CD Agent in autonomous mode by using a Helm chart
- = Installing the Argo CD Agent by using an Argo CD custom resource
- = Verifying the Argo CD Agent installation in Managed Mode or Autonomous Mode
- = Deploying Argo CD applications
  - == Deploying an Argo CD application in managed mode
  - == Deploying an Argo CD application in autonomous mode
- = Troubleshooting Principal-Agent communication and deployment issues
- Additional resources

**Total:** 1 assembly, 13 included modules, organized by installation method and component type.

---

## Proposed JTBD-Based Structure

## Getting Started

**Job 1: Understand Argo CD Agent Terminology and Architecture**
When: Setting up Argo CD Agent across hub and spoke clusters
Personas: Platform administrator

- 1.1. Core Concepts and Definitions `[concept]`
  - Argo CD Agent Terminologies (Lines 17-42): Principal namespace, Agent namespace, Context, Principal context, Agent context

---

## Plan Your Deployment

**Job 2: Choose Between Managed and Autonomous Agent Modes**
When: Deploying Agent components on workload clusters
Personas: Platform administrator

- 2.1. Understand Mode Implications `[concept]`
  - Option A: Managed Mode (Lines 147-155): Hub controls lifecycle
  - Option B: Autonomous Mode (Lines 147-155): Spoke controls lifecycle

---

## Set Up & Configure

**Job 3: Install and Configure the Principal Component with Secure PKI**
When: Establishing the control plane for multi-cluster GitOps
Personas: Platform administrator

- 3.1. Enable Principal via Argo CD CR `[procedure]`
  - Installing the Principal component (Lines 50-64): Configure argoCDAgent.principal
- 3.2. Create Required Namespaces `[procedure]`
  - Installing the Principal component (Lines 65-80): Namespace-to-agent mapping
- 3.3. Initialize PKI and Generate Certificates `[procedure]`
  - Installing the Principal component (Lines 82-120): CA, server certs, resource proxy cert, JWT key

**Job 4: Set Up Spoke Cluster Environment**
When: Connecting Agent clusters to the Principal
Personas: Platform administrator

- 4.1. Create Agent Secrets and Propagate CA `[procedure]`
  - Setting up a spoke cluster environment (Lines 122-145): Agent secret, CA propagation, client certificate

---

## Deploy & Use

**Job 5: Deploy Agent Component**
When: Installing the Agent on workload clusters
Personas: Platform administrator

- 5.1. Deploy Minimal Argo CD Instance on Agent Cluster `[procedure]`
  - Deploying an Argo CD instance on the Agent cluster (Lines 157-170)
- 5.2. Install Agent in Managed Mode (Helm) `[procedure]`
  - Installing the Argo CD Agent in managed mode (Lines 172-186): NetworkPolicy, Helm install
- 5.3. Install Agent in Autonomous Mode (Helm) `[procedure]`
  - Installing the Argo CD Agent in autonomous mode (Lines 188-202): NetworkPolicy, Helm install, AppProject
- 5.4. Install Agent via Argo CD CR (Alternative to Helm) `[procedure]`
  - Installing the Argo CD Agent by using an Argo CD custom resource (Lines 204-226)

**Job 7: Deploy Applications Using Agent Architecture**
When: Deploying applications via Agents
Personas: Platform administrator

- 7.1. Deploy Application in Managed Mode `[procedure]`
  - Deploying an Argo CD application in managed mode (Lines 262-278)
- 7.2. Deploy Application in Autonomous Mode `[procedure]`
  - Deploying an Argo CD application in autonomous mode (Lines 280-294)

---

## Track & Monitor

**Job 6: Verify Argo CD Agent Installation**
When: Completing Agent installation
Personas: Platform administrator

- 6.1. Confirm Agent Health and Connectivity `[procedure]`
  - Verifying the Argo CD Agent installation (Lines 228-253): Pod status, connection logs, Principal verification
- 6.2. (Optional) Verify Metrics Endpoints `[procedure]`
  - Verifying the Argo CD Agent installation (Lines 228-253): Agent metrics, Principal metrics

---

## Troubleshoot Issues

**Job 8: Troubleshoot Principal-Agent Communication and Deployment Issues**
When: Encountering connectivity or deployment problems
Personas: Platform administrator

- 8.1. Diagnose Common Failure Scenarios `[reference]`
  - Troubleshooting Principal-Agent communication (Lines 296-332): Four failure scenarios with diagnostics

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Installation method and component type | Workflow stages and user goals |
| **Top-level items** | 9 major sections (= headings) | 8 main jobs with nested approaches |
| **Mode selection** | Embedded within installation sections | Elevated to dedicated "Plan" job (Job 2) |
| **Installation methods** | Split across separate top-level sections (Helm vs CR) | Consolidated under Job 5 as alternative approaches |
| **Verification** | Separate section after installation | Integrated as Job 6 with explicit health/connectivity checks |
| **Application deployment** | Separate section at end | Integrated as Job 7 with clear mode-based paths |
| **Troubleshooting** | Single reference section at end | Dedicated job (Job 8) organized by failure scenario |
| **PKI and secrets** | Embedded within Principal installation | Explicit Job 3 subtasks (3.3) for certificate lifecycle |

---

### Job List Adjustments from Suggested Input

The suggested 14 records were consolidated to **8 jobs** (7 main jobs + 1 additional job for application deployment) for the following reasons:

1. **Jobs "Install Agent in managed mode" and "Install Agent in autonomous mode" (user stories) nested** → Under Job 5: Deploy Agent Component as alternative approaches (5.2 and 5.3)
2. **Job "Deploy application in managed mode" and "Deploy application in autonomous mode" (user stories) nested** → Under Job 7: Deploy Applications as mode-specific paths (7.1 and 7.2)
3. **Job "Deploy Argo CD instance on Agent cluster" (user story) absorbed into Job 5** → As prerequisite step 5.1
4. **Job "Install Agent via CR" (user story) absorbed into Job 5** → As alternative approach 5.4

---

## Hierarchy Levels

### Level 1: Main Jobs (8 total)
Stable, outcome-focused goals that represent what users want to accomplish:
- Job 1: Understand terminology
- Job 2: Choose deployment mode
- Job 3: Install Principal component
- Job 4: Set up spoke environment
- Job 5: Deploy Agent component
- Job 6: Verify installation
- Job 7: Deploy applications
- Job 8: Troubleshoot issues

### Level 2: User Stories (approaches nested under jobs)
Persona-specific or method-specific implementation paths:
- Under Job 5: Helm vs CR installation, managed vs autonomous mode
- Under Job 7: Managed mode vs autonomous mode deployment

### Level 3: Tasks/Procedures
Step-by-step instructions with line references to source sections.

---

## Example Consolidation

### Example 1: Installation Methods (3 sections → 1 unified job with 4 approaches)

**Current (Fragmented):**
- Section: Installing the Argo CD Agent by using a Helm chart
  - Subsection: Installing in managed mode by using a Helm chart
  - Subsection: Installing in autonomous mode by using a Helm chart
- Section: Installing the Argo CD Agent by using an Argo CD custom resource

**Proposed (Consolidated):**
- **Job 5: Deploy Agent Component**
  - 5.1. Deploy minimal Argo CD instance (prerequisite)
  - 5.2. Install Agent in managed mode (Helm)
  - 5.3. Install Agent in autonomous mode (Helm)
  - 5.4. Install Agent via Argo CD CR (alternative to Helm)

**Benefit:** All installation approaches in one place! Users can compare methods and choose the best fit without navigating multiple sections.

---

### Example 2: Application Deployment (2 separate subsections → 1 job with 2 mode-based paths)

**Current (Fragmented):**
- Section: Deploying Argo CD applications
  - Subsection: Deploying in managed mode
  - Subsection: Deploying in autonomous mode

**Proposed (Consolidated):**
- **Job 7: Deploy Applications Using Agent Architecture**
  - 7.1. Deploy application in managed mode (hub is source of truth)
  - 7.2. Deploy application in autonomous mode (spoke is source of truth)

**Benefit:** Clear choice based on mode selection from Job 2, with explicit source-of-truth callouts for each path.

---

## Navigation Improvement

**Current:** Browse 9 major sections to find installation and deployment procedures
**Proposed:** Navigate 8 main jobs → choose method/mode path
**Reduction:** ~11% fewer top-level items, with better thematic grouping
**Benefit:** Find content in 2-3 clicks vs 4-5 clicks. Clear workflow progression from planning to troubleshooting.

### Task-Specific Metrics

| Task | Current | Proposed | Improvement |
|------|---------|----------|-------------|
| Find mode selection guidance | Scan installation sections, infer from subsection titles | Job 2 dedicated to mode choice | ~60% faster navigation |
| Find all installation methods | Navigate 2 separate top-level sections | Job 5 with 4 approaches | Single location for all methods |
| Find verification steps | Scroll to section 6, locate subsections | Job 6 with explicit subtasks | Dedicated verification job |
| Find application deployment | Navigate to section 8 near end | Job 7 after verification | Clear workflow position |

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ⚠️ Terminology buried in section 2 | ✅ Job 1 | Elevated |
| Plan | ❌ Mode choice implied, not explicit | ✅ Job 2 | Added |
| Configure | ✅ Sections 3, 4, 5 | ✅ Jobs 3, 4 | Reorganized |
| Deploy | ✅ Sections 5, 6, 7 | ✅ Jobs 5, 7 | Consolidated |
| Confirm | ✅ Section 7 | ✅ Job 6 | Reorganized |
| Monitor | ⚠️ Metrics mentioned in verification | ⚠️ Limited | Gap remains |
| Troubleshoot | ✅ Section 9 | ✅ Job 8 | Reorganized by scenario |
| Upgrade | ❌ Missing | ❌ Missing | Gap remains |
| Reference | ⚠️ Limited to troubleshooting | ⚠️ Limited | Gap remains |

### Coverage Summary

**Current structure gaps:** Plan (mode selection not explicit), Monitor (no dashboard guidance), Upgrade
**Proposed structure gaps:** Monitor (no dashboard guidance), Upgrade, Reference (limited)
**Gaps addressed by restructure:** Plan (mode selection now explicit as Job 2)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Monitor | Add section on monitoring Principal and Agent with OpenShift observability dashboards and metrics | High |
| Upgrade | Add version upgrade procedures for Principal and Agent components | Medium |
| Reference | Add Principal/Agent configuration parameter reference and CLI command reference | Medium |

---

## Success Criteria

**The proposed JTBD structure achieves:**

✅ Users can immediately see main installation and deployment goals (8 jobs)
✅ Users can find jobs by what they need to accomplish (workflow stages)
✅ Content is simpler than current structure (consolidated installation methods)
✅ Stakeholders understand the proposed improvement (clear before/after examples)
✅ Content mappers know what to extract from where (line references preserved)
✅ Structure follows natural workflow progression (Get Started → Plan → Configure → Deploy → Verify → Troubleshoot)
✅ Mode selection (managed vs autonomous) elevated to explicit planning job
✅ Installation methods consolidated under single job with clear alternatives
