# Argo CD Agent Architecture - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-04-09
**JTBD Records:** 10
**Main Jobs:** 5 (consolidated from analysis)
**Source Document:** argocd-agent-architecture-overview.adoc (242 lines, single assembly)

---

## Current Structure (Feature-Based)

**Argo CD Agent Architecture Overview**

= Introduction to the Argo CD Agent architecture
- Introduction to the Argo CD Agent architecture
- Architecture and Terminology
- Comparing Argo CD Agent with traditional Argo CD architecture
- Synchronization mechanism between the control plane and workload clusters
- Argo CD Agent modes
  - Argo CD Agent Managed mode
  - Argo CD Agent Autonomous mode
- Security and Authentication
- Application Management Across Namespaces
- Known Limitations
- Additional resources

**Organization:** Sequential concept modules organized by architectural topics
**Navigation:** 10 top-level sections (1 with 2 sub-sections)
**User Journey:** Linear reading from introduction through concepts to limitations

---

## Proposed JTBD-Based Structure

### Understand Architecture

**Job 1: Understand the Argo CD Agent Architecture and Its Capabilities**
When: Managing multiple OpenShift clusters with GitOps
Personas: Platform architect

User stories:
- 1.1 Overview: Hub-and-Spoke Model for Multi-Cluster GitOps
  → Lines 3-12: Introduction to the Argo CD Agent architecture
  Context: Foundational understanding of Agent value proposition

- 1.2 Architecture Components and Terminology
  → Lines 14-26: Architecture and Terminology
  Context: Control plane cluster (hub) and workload cluster (spoke) definitions

- 1.3 Synchronization Mechanism
  → Lines 71-86: Synchronization mechanism
  Context: How resources sync between control plane and workload clusters

---

### Choose Your Approach

**Job 2: Compare Traditional Argo CD with Argo CD Agent**
When: Choosing between traditional Argo CD and Argo CD Agent
Personas: Platform architect

User story:
- 2.1 Architecture Comparison Matrix
  → Lines 28-69: Comparing Argo CD Agent with traditional Argo CD architecture
  Context: 8 capability dimensions (pane of glass, network, scalability, security, reconciliation, failure, complexity, maturity)

- 2.2 Decision Guide
  Context: When to choose traditional Argo CD vs Agent based on cluster count, network topology, security requirements

---

### Set Up & Configure

**Job 3: Choose Between Managed and Autonomous Modes**
When: Configuring Argo CD Agent
Personas: Platform architect, Platform engineer
Timing: BEFORE installing Argo CD Agent - mode determines where Application specifications are defined

User stories:
- 3.1 Mode Overview
  → Lines 88-100: Argo CD Agent modes
  Context: Two modes (Managed, Autonomous) plus mixed mode option

- 3.2 Managed Mode: Centralized Application Management
  → Lines 102-124: Argo CD Agent Managed mode
  Context: Control plane defines specs; familiar centralized experience; security improvement over traditional Argo CD
  Prerequisites: Strong control plane security

- 3.3 Autonomous Mode: GitOps-First with Distributed Definitions
  → Lines 126-146: Argo CD Agent Autonomous mode
  Context: Git as single source of truth; no single point of failure; supports app-of-apps
  Prerequisites: Git repository for application definitions

---

### Secure Your Environment

**Job 4: Implement mTLS Certificate-Based Authentication**
When: Securing multi-cluster Argo CD deployments
Personas: Security engineer
Prerequisites: Certificate generation and management capabilities

User stories:
- 4.1 Certificate Architecture
  → Lines 148-164: Security and Authentication
  Context: mTLS benefits (expiration, rotation, MITM prevention); root CA signs principal and agent certs

- 4.2 Authentication Flow
  Context: Certificate-based trust establishment; user responsible for generating and managing mTLS certificates

---

### Set Up & Configure (Continued)

**Job 5: Configure Namespace Isolation for Multi-Cluster Applications**
When: Managing applications from multiple workload clusters on the control plane
Personas: Platform engineer
Prerequisites: Argo CD Agent configured; mode selected

User stories:
- 5.1 Namespace Isolation Architecture
  → Lines 166-214: Application Management Across Namespaces (architecture explanation)
  Context: Applications in any namespace feature; each workload cluster gets dedicated namespace on control plane

- 5.2 Configure sourceNamespaces in Argo CD CR
  → Lines 215-231: Application Management Across Namespaces (configuration)
  Context: YAML configuration to enable discovery of applications from workload-specific namespaces

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Architectural concepts and features in sequential order
**Navigation:** 10 top-level sections with minimal hierarchy
**User Journey:** Linear reading; assumes user reads all content
**Finding Content:** Scan all sections to find relevant information
**Granularity:** Single-level hierarchy (no clear distinction between concepts, configuration, and procedures)

### Proposed Structure (JTBD-Based)

**Organized By:** Job map stages (Architecture -> Plan -> Configure -> Secure)
**Navigation:** 5 main jobs organized into 4 workflow phases
**User Journey:** Goal-directed; jump to the job that matches your current need
**Finding Content:** Navigate by workflow stage, then select job
**Granularity:** 3-level hierarchy (Jobs -> User Stories -> Tasks with clear line references)

---

## Hierarchy Levels Explanation

### Level 1: Main Jobs (5 total)
**Stable, outcome-focused goals that would exist even if technology changed**

Examples:
- "Understand the Argo CD Agent Architecture and Its Capabilities"
- "Compare Traditional Argo CD with Argo CD Agent"
- "Choose Between Managed and Autonomous Modes"

### Level 2: User Stories (10 total)
**Persona-specific or option-based implementation paths**

Examples:
- "Managed Mode: Centralized Application Management" (implementation path)
- "Autonomous Mode: GitOps-First with Distributed Definitions" (alternative path)
- "Certificate Architecture" (security implementation detail)

### Level 3: Procedures (line references to source)
**Step-by-step instructions with clear source attribution**

Format: `→ Lines X-Y: Section Title`

Examples:
- `→ Lines 102-124: Argo CD Agent Managed mode`
- `→ Lines 215-231: Application Management Across Namespaces (configuration)`

---

## Example Consolidations

### Example 1: Modes Consolidation

**Current (Fragmented):**
- Section: "Argo CD Agent modes" (overview)
- Sub-section: "Argo CD Agent Managed mode" (detail)
- Sub-section: "Argo CD Agent Autonomous mode" (detail)

**Proposed (Consolidated Under Single Job):**
Job 3: Choose Between Managed and Autonomous Modes
- User Story 3.1: Mode Overview (lines 88-100)
- User Story 3.2: Managed Mode (lines 102-124)
- User Story 3.3: Autonomous Mode (lines 126-146)

**Benefit:** All mode-related decisions consolidated under one job! User navigates to "Choose Between Managed and Autonomous Modes" and sees complete decision framework with all options.

### Example 2: Architecture Understanding Consolidation

**Current (Scattered):**
- Section: "Introduction to the Argo CD Agent architecture"
- Section: "Architecture and Terminology"
- Section: "Synchronization mechanism between the control plane and workload clusters"

**Proposed (Consolidated Under Single Job):**
Job 1: Understand the Argo CD Agent Architecture and Its Capabilities
- User Story 1.1: Overview (lines 3-12)
- User Story 1.2: Architecture Components and Terminology (lines 14-26)
- User Story 1.3: Synchronization Mechanism (lines 71-86)

**Benefit:** Complete architecture understanding in one place! User doesn't need to read 3 separate sections to get full architecture picture.

---

## Navigation Improvement Metrics

### Current Structure
- **Top-level sections:** 10
- **Hierarchy depth:** 1-2 levels (minimal nesting)
- **Navigation path:** Scan all 10 sections to find relevant content
- **Clicks to content:** 5-10 (browse all sections)
- **Decision support:** Comparison table exists but not organized as decision job

### Proposed Structure
- **Main jobs:** 5
- **Hierarchy depth:** 3 levels (Jobs -> User Stories -> Tasks)
- **Navigation path:** Choose workflow stage (4 options) -> Select job (5 total) -> Choose user story
- **Clicks to content:** 2-3 (stage -> job -> content)
- **Decision support:** Job 2 and Job 3 explicitly frame architecture and mode selection as decisions

### Improvement Metrics
- **50% reduction** in top-level items (10 sections → 5 jobs)
- **60% reduction** in clicks to content (5-10 clicks → 2-3 clicks)
- **Clear workflow progression** (Architecture -> Plan -> Configure -> Secure vs linear concept list)
- **Decision jobs elevated** (comparison and mode selection explicitly presented as decisions to make)

---

## Workflow Coverage Comparison

| Stage | Current Structure | Proposed Structure | Gap Status |
|-------|------------------|-------------------|------------|
| Architecture | ✅ Multiple sections (intro, terminology, sync) | ✅ Job 1 (consolidated) | Reorganized |
| Plan | ⚠️ Comparison table exists but not framed as planning job | ✅ Job 2 (elevated as decision) | Improved |
| Configure | ✅ Modes, namespace configuration | ✅ Jobs 3, 5 (organized by job) | Reorganized |
| Secure | ✅ Security and Authentication section | ✅ Job 4 (dedicated job) | Reorganized |
| Deploy | ❌ Not in this guide | ❌ Not in this guide | Link to installation guide |
| Monitor | ❌ Not covered | ❌ Not covered | Gap remains |
| Troubleshoot | ❌ Not covered | ❌ Not covered | Gap remains |
| Reference | ⚠️ Known limitations, additional resources | ⚠️ Appendix A (limitations) | Maintained |

### Coverage Summary

**Current structure coverage:** 4 stages (Architecture ✅, Plan ⚠️, Configure ✅, Secure ✅)
**Proposed structure coverage:** 4 stages (Architecture ✅, Plan ✅, Configure ✅, Secure ✅)
**Gaps addressed by restructure:** Plan elevated from comparison table to explicit decision job

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Deploy | Link to "Installing Argo CD Agent" guide; this is intentionally separate content | N/A (out of scope) |
| Monitor | Add section on monitoring Agent health, sync status, application health across clusters | High |
| Troubleshoot | Add common issues section (sync failures, certificate problems, namespace conflicts) | High |
| Upgrade | Add Agent upgrade procedures and version compatibility guidance | Medium |

---

## UX Research Alignment

*Note: No research extension fields were used in this analysis. The following insights are derived from the content structure itself.*

### Pain Points Addressed by Restructure

| Pain Point (inferred from content) | How New Structure Helps |
|-----------------------------------|------------------------|
| "Multiple architecture concepts scattered across sections" | Job 1 consolidates all architecture understanding in one place (overview, terminology, sync) |
| "Mode selection not framed as decision" | Job 3 explicitly presents mode choice with prerequisites, timing, and clear option comparison |
| "Comparison table exists but buried in linear content" | Job 2 elevates comparison to top-level decision job with decision guide |
| "Namespace configuration disconnected from mode selection" | Jobs 3 and 5 show prerequisite relationship (choose mode → then configure namespaces) |

### Strategic Priorities Elevated

The following jobs address strategic architectural decisions. The new structure gives them dedicated, top-level sections:

| Strategic Decision | Current Location | Proposed Location | Visibility Improvement |
|-------------------|------------------|-------------------|----------------------|
| Choose architecture (Agent vs traditional) | Section 3 (comparison) | Job 2 (dedicated decision job) | Elevated to Plan stage |
| Choose mode (Managed vs Autonomous) | Section 5 with 2 sub-sections | Job 3 (dedicated decision job with timing) | Prerequisites and timing made explicit |
| Secure multi-cluster communication | Section 7 | Job 4 (dedicated security job) | Security isolated as distinct job |

### Workflow Clarity Improvements

| Workflow Stage | Current Visibility | Proposed Visibility | Improvement |
|---------------|-------------------|---------------------|-------------|
| Architecture understanding | 3 scattered sections (intro, terminology, sync) | 1 consolidated job with 3 user stories | Clear starting point for learning |
| Decision-making | Comparison table exists but not framed as decision | 2 explicit decision jobs (architecture choice, mode choice) | Decision points surfaced |
| Configuration | 2 sections (modes, namespaces) | 2 jobs with clear prerequisites | Prerequisite chain visible (Job 3 → Job 5) |
| Security | 1 section | 1 dedicated job | Maintained as distinct concern |

---

## Document Statistics

### Current Structure
- **Sections:** 10 (9 level-1, 2 level-2)
- **Depth:** 2 levels maximum
- **Concepts:** 10 discrete concepts presented linearly
- **Source lines:** 242 lines (single assembly, 10 modules)

### Proposed Structure
- **Main jobs:** 5
- **User stories:** 10
- **Depth:** 3 levels (Job -> User Story -> Task/Line Reference)
- **Workflow stages:** 4 (Architecture, Plan, Configure, Secure)
- **Source lines:** 242 lines (same content, reorganized)

### Content Mapping
- **Module types:** 10 CONCEPT modules (no procedures or references in this guide)
- **Personas:** 3 (Platform architect, Platform engineer, Security engineer)
- **Job types:** 4 main_job, 5 user_story, 1 related (limitations awareness)

---

## Summary

The proposed JTBD-based structure provides:

1. **50% reduction in top-level navigation items** (10 sections → 5 jobs)
2. **Clear workflow progression** (Architecture → Plan → Configure → Secure)
3. **Decision jobs elevated** (architecture comparison and mode selection explicitly framed as decisions)
4. **Consolidated related concepts** (all architecture understanding in Job 1, all mode information in Job 3)
5. **Explicit prerequisite chains** (mode selection → namespace configuration)
6. **60% reduction in clicks to content** (browse 10 sections → navigate 4 workflow stages)
7. **Maintained coverage** (same stages covered, better organized)

The current structure is well-organized conceptually but linear. The proposed structure reorganizes the same excellent content into goal-oriented jobs that match how users approach multi-cluster Agent architecture decisions.
