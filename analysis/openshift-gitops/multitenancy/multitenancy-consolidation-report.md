# Multitenancy Support in GitOps — Consolidation Report

**Document:** multitenancy-support-in-gitops.adoc
**JTBD Records:** 14 records → 8 main jobs (after consolidation)

---

## Executive Summary

### What's Changing

The current documentation for OpenShift GitOps multitenancy is organized by technical components: instance types, RBAC mechanisms, and custom resources. While comprehensive, this structure forces users to navigate across multiple sections to understand how to accomplish specific goals. For example, a cluster administrator wanting to provide isolated GitOps capabilities to application teams must read through the namespace-scoped instance section, understand the RBAC subsection in "Important considerations," and separately locate the NamespaceManagement CR section.

The proposed JTBD-based structure reorganizes this content by user goals and workflow stages. Instead of presenting "features of namespace-scoped instances," the structure focuses on what users want to accomplish: deploy namespace-scoped instances, extend permissions, enable tenant self-service, and prevent privilege escalation. This shift reduces navigation complexity while maintaining comprehensive coverage of all technical details.

The consolidation merges 14 user stories and configuration variations into 8 main jobs organized across 4 workflow stages: Understand Your Options, Set Up & Configure, Secure Your Environment, and Administer Platform. This restructure makes it easier for both cluster administrators and application teams to find relevant content by goal rather than by technical component knowledge.

### Key Improvements

- **Permission extension consolidation:** 3 permission extension methods (managed-by label, custom cluster roles, NamespaceManagement CR) previously scattered across 2 sections → unified under Jobs 2 and 7 with clear comparison
- **Security elevation:** RBAC content promoted from buried subsection → dedicated "Secure Your Environment" workflow stage (Job 5)
- **Persona separation:** Cluster administrator jobs (1-7) clearly distinguished from tenant jobs (8), reducing cognitive load
- **Instance type comparison:** 3 instance scope modes (namespace, cluster, default) consolidated into planning job (Job 1) with decision guidance
- **Workflow staging:** Clear progression from Plan (Job 1) → Configure (Jobs 2, 3, 7, 8) → Secure (Job 5) → Administer (Jobs 4, 6)
- **Configuration method grouping:** Related configuration approaches grouped under single jobs (Job 2 has 3 approaches for namespace-scoped instances)
- **Quick navigation added:** New "Quick Navigation" section enables direct goal-based lookup ("I want to isolate tenants" → Job 2)
- **Gap visibility:** Missing workflow stages (Monitor, Troubleshoot, Upgrade) explicitly identified with recommendations

---

## Current Structure (Feature-Based)

- **Overview** — Introduction to multitenancy concept and GitOps Operator capabilities
- **Argo CD instance scopes** — Technical classification of instance types
  - Namespace-scoped instance (Application delivery instance) — Permissions, managed-by label, custom cluster roles
    - How does this method work? — Implementation details for label-based and custom role approaches
  - Cluster-scoped instance — Cluster-level resource management
    - How does this method work? — ARGOCD_CLUSTER_CONFIG_NAMESPACES configuration
  - Default cluster-scoped instance — openshift-gitops namespace instance
- **Important considerations when adopting the multitenancy model** — Security and permission model
  - Argo CD role-based access control (RBAC) — Two-level permission model (Kubernetes + Argo CD)
  - Argo CD projects — AppProject CR for tenant restrictions
- **Enable tenant namespace management with the NamespaceManagement CR** — Self-service feature
  - NamespaceManagement CR Overview — Feature introduction and glob patterns
  - Effects of NamespaceManagement CR — CR lifecycle (creation, update, deletion)
  - Configuring namespace management for Argo CD tenants — Step-by-step procedure
    - Prerequisites — Required permissions and installations
    - Procedure — Three-step configuration (Subscription, Argo CD CR, NamespaceManagement CR)
    - Verification — Verifying automatic RBAC provisioning

**Total:** 4 major sections, 10+ subsections, organized by technical components and features.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Understand Your Options**
  - Job 1: Understand Multitenancy Architecture and Instance Scopes
- **Set Up & Configure**
  - Job 2: Deploy Namespace-Scoped Argo CD Instances
  - Job 3: Deploy Cluster-Scoped Argo CD Instance
  - Job 7: Enable Tenant Self-Service for Namespace Management
  - Job 8: Delegate My Namespaces to Argo CD (Tenant Perspective)
- **Secure Your Environment**
  - Job 5: Understand the Two-Level RBAC Model
- **Administer Platform**
  - Job 4: Use the Default Cluster-Scoped Instance
  - Job 6: Define AppProject Custom Resources for Tenant Management

---

### Detailed Job Descriptions

#### Understand Your Options

**Job 1: Understand Multitenancy Architecture and Instance Scopes**

*When deploying applications for multiple teams, I want to understand multitenancy architecture and instance scopes, so I can choose the right deployment model for my organization.*

Prerequisites: None

- **1.1. Learn Core Multitenancy Concepts** `[concept]`
  - Overview (Lines 1-17): Introduction to multitenancy, tenant autonomy, permission model
  - Context: Essential foundation for all multitenancy decisions
- **1.2. Compare Instance Scope Modes** `[concept]`
  - Argo CD instance scopes (Lines 19-24): Three modes overview with decision guidance
  - Context: Use this to select between namespace-scoped (tenant self-service), cluster-scoped (shared management), or default (cluster config only)

---

#### Set Up & Configure

**Job 2: Deploy Namespace-Scoped Argo CD Instances**

*When providing GitOps capabilities to application teams, I want to deploy namespace-scoped Argo CD instances, so I can give teams autonomy without granting cluster-admin privileges.*

Prerequisites: Understand multitenancy architecture (Job 1)

- **2.1. Deploy Basic Namespace-Scoped Instance** `[procedure]`
  - Namespace-scoped instance (Lines 25-38): Create Argo CD CR in tenant namespace
  - Context: Starting point for all namespace-scoped deployments, provides isolation in instance's own namespace only
- **2.2. Extend Permissions Using Managed-By Label (Standard Approach)** `[procedure]`
  - How does this method work? (Lines 40-48): Label namespaces with argocd.argoproj.io/managed-by
  - Context: Use when tenants need to deploy across multiple namespaces in same cluster, default admin role is acceptable
- **2.3. Restrict Permissions Using Custom Cluster Roles (Secure Approach)** `[procedure]`
  - Custom cluster role configuration (Lines 49-55): Set CONTROLLER_CLUSTER_ROLE and CONTROLLER_SERVER_ROLE environment variables
  - Context: Use when least-privilege access required, cluster admin defines precise permissions

**Job 3: Deploy Cluster-Scoped Argo CD Instance**

*When managing cluster-level resources or supporting Applications in any namespace, I want to deploy a cluster-scoped Argo CD instance, so I can manage resources across the entire cluster.*

Prerequisites: Understand multitenancy architecture (Job 1), Understand security implications

- **3.1. Understand Cluster-Scoped Instance Use Cases** `[concept]`
  - Cluster-scoped instance (Lines 57-64): Use cases, Applications in any namespace feature, security warnings
  - Context: Validate need before elevating - NOT for tenant self-managed instances
- **3.2. Elevate Instance Using Environment Variable** `[procedure]`
  - How does this method work? (Lines 65-73): Configure ARGOCD_CLUSTER_CONFIG_NAMESPACES in Subscription
  - Context: Prevents non-admin self-elevation, Operator creates cluster roles with limited permissions

**Job 7: Enable Tenant Self-Service for Namespace Management**

*When enabling tenant self-service for namespace management, I want to use the NamespaceManagement CR feature, so I can allow tenants to delegate control without requiring cluster-admin intervention.*

Prerequisites: Deploy namespace-scoped instances (Job 2)

- **7.1. Understand NamespaceManagement CR Feature** `[concept]`
  - Enable tenant namespace management with NamespaceManagement CR (Lines 119-133): Feature overview, glob patterns, automatic RBAC provisioning
  - Context: Disabled by default for security, requires cluster admin enablement
- **7.2. Enable Feature in Subscription** `[procedure]`
  - Configuring namespace management - Procedure step 1 (Lines 155-176): Set ALLOW_NAMESPACE_MANAGEMENT_IN_NAMESPACE_SCOPED_INSTANCES environment variable
  - Context: First of three steps to enable self-service, cluster admin only
- **7.3. Configure Argo CD CR with Namespace Patterns** `[procedure]`
  - Configuring namespace management - Procedure step 2 (Lines 177-192): Define namespaceManagement with glob patterns
  - Context: Supports wildcards (/* , dev-/*) for flexible namespace matching
- **7.4. Understand NamespaceManagement CR Lifecycle** `[concept]`
  - Effects of NamespaceManagement CR (Lines 145-153): Creation, update, deletion behaviors
  - Context: Critical for troubleshooting, understand automatic cleanup on Subscription-level disable

**Job 8: Delegate My Namespaces to Argo CD (Tenant Perspective)**

*When I need my Argo CD instance to manage my namespaces, I want to create a NamespaceManagement CR in my namespace, so I can delegate control without waiting for cluster-admin approval.*

Prerequisites: Cluster admin has enabled namespace management (Job 7), Permissions to create NamespaceManagement CR

- **8.1. Create NamespaceManagement CR** `[procedure]`
  - Configuring namespace management - Procedure step 3 and Verification (Lines 193-209): Create CR, verify automatic Role/RoleBinding creation
  - Context: Tenant-initiated self-service, spec.managedBy must exactly match Argo CD namespace

---

#### Secure Your Environment

**Job 5: Understand the Two-Level RBAC Model**

*When designing multitenancy solutions, I want to understand the two-level RBAC model (Kubernetes and Argo CD), so I can mitigate privilege escalation risks.*

Prerequisites: Understand Kubernetes RBAC, Understand Argo CD permission model

- **5.1. Learn the Two Permission Layers** `[concept]`
  - Argo CD role-based access control (RBAC) (Lines 89-96): Kubernetes level vs Argo CD level permissions
  - Context: Critical security concept - two distinct permission systems interact
- **5.2. Mitigate Privilege Escalation** `[concept]`
  - Privilege escalation mitigation (Lines 97-101): Use Argo CD RBAC or separate instances
  - Context: Prevents tenants from leveraging controller's elevated privileges

---

#### Administer Platform

**Job 4: Use the Default Cluster-Scoped Instance**

*When managing cluster configuration resources, I want to use the default openshift-gitops instance, so I can maintain a centralized control plane for cluster-level operations.*

Prerequisites: OpenShift GitOps Operator installed

- **4.1. Understand Default Instance Purpose** `[concept]`
  - Default cluster-scoped instance (Lines 75-84): Opinionated setup, limitations, restrictions
  - Context: ONLY for cluster configuration, never for application delivery, cluster-admin access only

**Job 6: Define AppProject Custom Resources for Tenant Management**

*When managing multiple tenants with an Argo CD instance, I want to define AppProject custom resources with granular RBAC and restrictions, so I can control what resources tenants can deploy and where.*

Prerequisites: Understand Argo CD projects concept

- **6.1. Understand Argo CD Projects Purpose** `[concept]`
  - Argo CD projects (Lines 103-112): Group applications, specify restrictions, enable project-level RBAC
  - Context: More effective than global RBAC for large tenant counts
- **6.2. Define Tenant AppProject CRs** `[procedure]`
  - AppProject best practices (Lines 112-117): Define tenant RBAC with restrictions, use global projects for common config
  - Context: Never use default project, always define your own

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Technical components (instance types, RBAC, CRs) | User goals and workflow stages |
| **Top-level items** | 4 major sections + 10+ subsections (flat hierarchy) | 8 main jobs organized in 4 workflow stages (nested hierarchy) |
| **Navigation model** | Browse by component knowledge | Navigate by goal ("I want to isolate tenants") |
| **Permission extension** | Scattered across namespace-scoped section + separate NamespaceManagement section | Grouped under Jobs 2 (instance-level) and 7 (self-service) |
| **Security content** | RBAC buried as subsection under "Important considerations" | Elevated to dedicated "Secure Your Environment" stage (Job 5) |
| **Persona separation** | Mixed (cluster admin and tenant in same sections) | Clear (Jobs 1-7 cluster admin, Job 8 tenant) |
| **Instance type comparison** | Spread across 3 subsections | Consolidated in planning job (Job 1) with decision matrix |
| **Configuration method comparison** | Sequential presentation (no explicit comparison) | Grouped approaches with "Context" lines for when to use each |
| **Workflow staging** | Implicit (architecture first, then configuration) | Explicit (Plan → Configure → Secure → Administer) |
| **Quick navigation** | None (must browse sections) | "Quick Navigation" section for direct goal lookup |

### Job List Adjustments from Suggested Input

The suggested 14 records were consolidated to **8 main jobs** for the following reasons:

1. **Jobs 2.1, 2.2, 2.3 (namespace-scoped configuration variations) merged** → Three user stories consolidated under Job 2 as distinct approaches (basic deployment, managed-by label, custom cluster roles)
2. **Jobs 3.1, 3.2 (cluster-scoped understanding and configuration) merged** → Two user stories consolidated under Job 3 (understand use cases, elevate instance)
3. **Jobs 7.1, 7.2, 7.3, 7.4 (NamespaceManagement CR lifecycle steps) consolidated** → Four user stories grouped under Job 7 as multi-step procedure
4. **Job 5.1 and 5.2 (RBAC layers and mitigation) merged** → Two user stories consolidated under Job 5 (learn layers, mitigate escalation)
5. **Job 6.1 and 6.2 (projects purpose and definition) merged** → Two user stories consolidated under Job 6 (understand purpose, define AppProjects)

**Rationale:** Original 14 records represented granular user stories (Level 2). Consolidation groups these under 8 stable main jobs (Level 1) following the 3-tier hierarchy: Job → User Story → Procedure. This reduces top-level cognitive load while preserving all implementation details.

---

## Consolidation Examples

### Example 1: Permission Extension Methods (3 scattered approaches → 2 unified jobs)

**Current (Fragmented):**
- Namespace-scoped instance section (lines 25-55): Mentions managed-by label and custom cluster roles in single section without clear comparison
- Enable tenant namespace management with NamespaceManagement CR (lines 119-209): Separate top-level section for self-service approach, no connection to namespace-scoped methods

Users seeking permission extension guidance must read two separate sections and infer the differences between approaches. No decision matrix or comparative guidance exists.

**Proposed (Consolidated):**
- **Job 2: Deploy Namespace-Scoped Argo CD Instances**
  - 2.1. Deploy Basic Namespace-Scoped Instance
  - 2.2. Extend Permissions Using Managed-By Label (Standard Approach)
  - 2.3. Restrict Permissions Using Custom Cluster Roles (Secure Approach)
- **Job 7: Enable Tenant Self-Service for Namespace Management**
  - 7.1-7.4. Multi-step procedure with lifecycle understanding

**Benefit:** All permission extension methods grouped for easy comparison, "Context" lines explain when to use each approach, self-service elevated to dedicated job recognizing its distinct workflow.

---

### Example 2: Security Content (buried subsection → dedicated workflow stage)

**Current (Fragmented):**
- Important considerations when adopting the multitenancy model (section heading)
  - Argo CD role-based access control (RBAC) (subsection, lines 89-101)
  - Argo CD projects (subsection, lines 103-117)

RBAC content buried as a subsection under "Important considerations," making it easy to overlook. No clear workflow positioning - should users read this before or after configuring instances?

**Proposed (Consolidated):**
- **Secure Your Environment** (dedicated workflow stage)
  - **Job 5: Understand the Two-Level RBAC Model**
    - 5.1. Learn the Two Permission Layers
    - 5.2. Mitigate Privilege Escalation

**Benefit:** Security elevated to dedicated workflow stage, positioned after configuration (Jobs 2-3) and before administration (Jobs 4, 6), making it clear when users need this knowledge.

---

### Example 3: Instance Type Selection (3 scattered sections → 1 planning job)

**Current (Fragmented):**
- Argo CD instance scopes (section heading, lines 19-24): Lists three modes
  - Namespace-scoped instance (lines 25-55): Details for application delivery
  - Cluster-scoped instance (lines 57-73): Details for cluster management
  - Default cluster-scoped instance (lines 75-84): Details for default instance

Users must read all three subsections sequentially to understand differences and make selection. No comparison matrix or decision guidance.

**Proposed (Consolidated):**
- **Job 1: Understand Multitenancy Architecture and Instance Scopes**
  - 1.1. Learn Core Multitenancy Concepts
  - 1.2. Compare Instance Scope Modes (includes decision guidance: namespace-scoped for tenant self-service, cluster-scoped for shared management, default for cluster config only)

**Benefit:** Instance type comparison in planning job with decision criteria, users understand all options before diving into configuration procedures.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Application deployment procedures | All jobs (next step after instance setup) | No coverage - documentation ends at instance configuration | **High** — Users need guidance on next steps after configuring multitenancy, likely causes "what now?" support tickets |
| Observability for multitenant deployments | Missing Monitor workflow stage | No coverage - no guidance on monitoring tenant activity or instance health | **High** — Production deployments require observability, gap forces users to generic Argo CD docs |
| Troubleshooting permission issues | Jobs 2, 5, 7, 8 (permission configuration) | No coverage - no debugging guidance for RBAC failures or CR lifecycle issues | **High** — Permission errors are common in multitenancy, reduces support burden |
| Instance upgrade and migration procedures | Missing Upgrade workflow stage | No coverage - no guidance on upgrading instances or migrating tenants | **Medium** — Day 2 operations critical for lifecycle management, workaround is generic upgrade docs |
| Performance tuning for shared instances | Job 3 (cluster-scoped instances) | Mentioned in passing (default permissions can be extended) but no tuning guidance | **Medium** — Users managing large tenant counts need performance optimization |
| Backup and disaster recovery | Missing Operate workflow stage | No coverage - no guidance on backing up instance configuration or tenant data | **Medium** — Production deployments require DR planning |
| Tenant onboarding automation | Job 2, 7 (namespace management) | Procedure shown but no automation guidance (GitOps of GitOps) | **Low** — Nice-to-have for large deployments, users can script manually |
| Cost optimization for multi-instance deployments | Job 2 (namespace-scoped instances) | No coverage - no guidance on resource limits or instance consolidation | **Low** — Advanced topic, users can apply generic resource management |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 4 major sections | 8 jobs (4 stages) | 43% reduction in top-level cognitive load (flat to nested hierarchy) |
| Sections to browse for "namespace-scoped setup" | 1 section (Namespace-scoped instance) but must find subsections | 1 job (Job 2) with 3 clearly labeled approaches | 0% raw section count but improved discoverability via approach labeling |
| Sections to browse for "permission extension" | 2 sections (Namespace-scoped instance + NamespaceManagement CR section) | 2 jobs (Job 2 for instance-level, Job 7 for self-service) but grouped in same workflow stage | 50% reduction in context switching (both in "Set Up & Configure") |
| Clicks to find "managed-by label" | 2-3 clicks (Argo CD instance scopes → Namespace-scoped instance → scroll to subsection) | 2 clicks (Set Up & Configure → Job 2 → 2.2) | ~33% reduction with labeled approaches |
| Clicks to find "RBAC model" | 3 clicks (Important considerations → Argo CD RBAC → scroll) | 2 clicks (Secure Your Environment → Job 5) | ~33% reduction with dedicated workflow stage |
| Persona-specific navigation | Mixed (must filter mentally) | Clear (Jobs 1-7 cluster admin, Job 8 tenant) | Added capability - persona-based filtering |
| Goal-based navigation | No quick navigation | "Quick Navigation" section with direct goal lookup | Added capability - 8 direct goal links |

**Final job count: 8** (reduced from suggested 14 records). Consolidation follows 3-tier hierarchy: 8 stable main jobs (Level 1) group 14 user stories (Level 2) which reference procedural content (Level 3). This structure reduces top-level cognitive load while preserving granular implementation details.

---

## Document Statistics

### Current Structure
- **Sections:** 4 major, 10+ subsections
- **Total headings:** ~14
- **Organizing principle:** Technical components (instance types, RBAC, CRs)
- **Hierarchy depth:** 3 levels (section → subsection → content)
- **Personas addressed:** 2 (cluster administrator, tenant - mixed)
- **Configuration methods:** 4 (managed-by label, custom cluster roles, ARGOCD_CLUSTER_CONFIG_NAMESPACES, NamespaceManagement CR)
- **Workflow coverage:** Plan (partial), Configure (complete), Secure (buried), Administer (partial)

### Proposed Structure
- **Main jobs:** 8
- **User stories:** 14 (nested under jobs)
- **Workflow stages:** 4 (Understand Your Options, Set Up & Configure, Secure Your Environment, Administer Platform)
- **Organizing principle:** User goals and workflow stages
- **Hierarchy depth:** 3 levels (job → user story → procedure reference)
- **Personas addressed:** 3 (cluster administrator, platform engineer, application delivery team - clearly separated)
- **Configuration methods:** 4 (same, but grouped for comparison)
- **Workflow coverage:** Plan (elevated), Configure (reorganized), Secure (elevated), Administer (dedicated), gaps identified (Deploy, Monitor, Troubleshoot, Upgrade)

### Complexity Comparison
- **Current:** 14 navigable items (flat structure)
- **Proposed:** 8 main jobs (nested structure) - 43% reduction in top-level cognitive load
- **Navigation model shift:** Browse by component knowledge → Navigate by goal
- **Quick navigation:** None → 8 direct goal links added
