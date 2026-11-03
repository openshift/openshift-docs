# Access Control and User Management - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-04-09
**JTBD Records:** 12
**Main Jobs:** 3 (rolled up from 12 records)
**Coverage:** Standard schema (no research extensions)

---

## Current Structure (Feature-Based)

```
Access Control and User Management

= Configuring Argo CD RBAC
  == Configuring user level access

= Configuring SSO for Argo CD using Dex
  == Configuration to enable the Dex OpenShift OAuth Connector
  === Mapping users to specific roles

= Configuring SSO for Argo CD using external OIDC providers
  == Understanding OIDC integration approaches for Argo CD
  == Prerequisites
  == Configuring direct OIDC integration for Argo CD
  == Verifying OIDC login for Argo CD

= Managing local users in Argo CD
  == About local user management in Argo CD
  == Local user configuration in Argo CD
  == Example local user configuration in Argo CD
  == Token storage and access
  == Token lifecycle management
  == User lifecycle management
  == Integration with legacy configuration
  == Creating local users in Argo CD
```

**Organization:** By authentication method/technology (RBAC, Dex SSO, OIDC SSO, local users)

**User Journey:** Linear progression through authentication approaches

**Navigation:** 4 top-level assemblies, 16 subsections

---

## Proposed JTBD-Based Structure

## Secure Access to Argo CD

### Job 1: Configure Role-Based Access Control
**When:** Managing access to Argo CD  
**Personas:** Cluster administrator

**Context:** Default instance grants no access except kube:admin; custom instances provide read-only by default.

**Implementation Path:**

- **User-Level RBAC Configuration**
  - Persona: Cluster administrator needing specific permissions
  - → Lines 142-185: Configuring user level access
  - Source: Configuring Argo CD RBAC assembly
  - Edit RBAC policy in Argo CD CR
  - Assign roles to users
  - Configure scopes

**Prerequisites:**
- OpenShift GitOps Operator installed
- cluster-admin access

**Related Jobs:**
- Job 2: Configure single sign-on
- Job 3: Manage local users

---

### Job 2: Configure Single Sign-On
**When:** Managing multiple users  
**Personas:** Cluster administrator

**Context:** Argo CD creates an admin user after operator installation. For multiple users, configure SSO using Dex or external OIDC providers.

**Implementation Paths:**

**Option A: Dex-Based SSO with OpenShift OAuth**
- Persona: Cluster administrator leveraging OpenShift users/groups
- → Lines 329-365: Configuration to enable the Dex OpenShift OAuth Connector
- → Lines 373-400: Mapping users to specific roles
- Source: Configuring SSO for Argo CD using Dex assembly
- Uses Dex as intermediary identity broker
- Connects to OpenShift OAuth
- Map users to roles via groups

**Option B: Direct OIDC Integration**
- Persona: Cluster administrator integrating with enterprise identity providers
- → Lines 543-665: Configuring direct OIDC integration for Argo CD
- Source: Configuring SSO for Argo CD using external OIDC providers assembly
- Connects directly to OIDC-compliant provider
- Bypasses Dex intermediary
- Provider-agnostic approach

**Verification:**
- → Lines 673-688: Verifying OIDC login for Argo CD
- Test authentication flow
- Confirm role-based permissions

**Prerequisites:**
- OpenShift OAuth server configured (for Dex option)
- OIDC provider configured with client ID/secret (for OIDC option)

**Important:** Cannot use `spec.sso` and `spec.oidcConfig` simultaneously.

---

## Provide API Access for Automation

### Job 3: Manage Local User Accounts
**When:** Needing API tokens for automation or small teams without SSO  
**Personas:** Cluster administrator, Automation engineer

**Context:** Operator manages local users by creating accounts, generating JWT tokens, configuring lifetimes/renewal, and storing tokens in Kubernetes secrets.

**Implementation Paths:**

**Create Local Users for API Access**
- → Lines 1210-1255: Creating local users in Argo CD
- Source: Managing local users in Argo CD assembly
- Define users in localUsers configuration
- Configure token lifetimes and renewal
- Operator creates secrets automatically

**Retrieve and Use API Tokens**
- → Lines 1060-1109: Token storage and access
- Extract tokens from Kubernetes secrets
- Decode base64-encoded values
- Use with Argo CD CLI or API

**Manage Token Lifecycle**
- → Lines 1117-1141: Token lifecycle management
- Configure automatic renewal
- Manually rotate tokens by deleting secrets
- Disable API keys to revoke access

**Manage User Lifecycle**
- → Lines 1149-1173: User lifecycle management
- Disable users temporarily (preserves config)
- Remove users permanently (cleanup all resources)

**Prerequisites:**
- Argo CD instance deployed

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Authentication methods and technologies (RBAC, Dex, OIDC, local users)  
**Navigation:** 4 assemblies, 16 subsections  
**User Journey:** Linear reading through authentication approaches  
**Entry Points:** Must know which authentication method to use

### Proposed Structure (JTBD-Based)

**Organized By:** Security goals (control access, centralize authentication, provide API access)  
**Navigation:** 3 main jobs with implementation paths  
**User Journey:** Goal-directed, choose authentication approach based on need  
**Entry Points:** Start with goal, discover implementation options

---

## Hierarchy Levels

### Level 1: Main Jobs (3 total)

Stable, outcome-focused goals that don't change even as technology evolves:
- Job 1: Configure RBAC
- Job 2: Configure SSO
- Job 3: Manage local users

**Characteristics:**
- Tool-agnostic (goal remains even if tools change)
- Organized by security stage (Secure, Confirm, Execute, Operate)
- 10-15 jobs typical for complete guide (this guide focuses on access control only)

### Level 2: User Stories (9 total)

Persona-specific or technology-specific implementation paths:
- User-level RBAC configuration
- Dex-based SSO vs Direct OIDC integration
- Create users, retrieve tokens, manage lifecycle

**Characteristics:**
- Implementation-specific (UI vs CLI, Dex vs OIDC)
- Persona-specific approaches
- Multiple ways to accomplish the main job

### Level 3: Procedures (References)

Step-by-step instructions with line numbers:
- Lines 142-185: Configuring user level access
- Lines 329-365: Enable Dex OpenShift OAuth
- Lines 1210-1255: Creating local users

**Characteristics:**
- Specific procedures from source documentation
- Line number references for traceability
- Supporting details for user stories

---

## Example: Content Consolidation

### Example 1: SSO Configuration

**Current (Fragmented):**
- Assembly: Configuring SSO for Argo CD using Dex
  - Section: Configuration to enable the Dex OpenShift OAuth Connector
  - Section: Mapping users to specific roles
- Assembly: Configuring SSO for Argo CD using external OIDC providers
  - Section: Understanding OIDC integration approaches
  - Section: Configuring direct OIDC integration
  - Section: Verifying OIDC login

**Proposed (Consolidated):**
```
Job 2: Configure Single Sign-On
  Option A: Dex-Based SSO with OpenShift OAuth
    - Enable Dex connector (Lines 329-365)
    - Map users to roles (Lines 373-400)
  
  Option B: Direct OIDC Integration
    - Understanding approaches (Lines 543-560)
    - Configure OIDC integration (Lines 580-665)
    - Verify login (Lines 673-688)
```

**Benefit:**
- One place to learn about SSO configuration
- Clear comparison of Dex vs OIDC approaches
- Guided decision-making with Option A/B structure

### Example 2: Local User Management

**Current (Fragmented):**
- About local user management in Argo CD (concept)
- Local user configuration in Argo CD (reference)
- Example local user configuration in Argo CD (examples)
- Token storage and access (concept + procedure)
- Token lifecycle management (concept)
- User lifecycle management (concept)
- Integration with legacy configuration (reference)
- Creating local users in Argo CD (procedure)

**Proposed (Consolidated):**
```
Job 3: Manage Local User Accounts
  - Create Local Users for API Access (Lines 1210-1255)
  - Retrieve and Use API Tokens (Lines 1060-1109)
  - Manage Token Lifecycle (Lines 1117-1141)
  - Manage User Lifecycle (Lines 1149-1173)
```

**Benefit:**
- Organized by task sequence (create → retrieve → manage)
- Combines concepts, examples, and procedures
- Clear workflow progression

---

## Navigation Improvement

### Current Navigation

**To configure SSO with OpenShift:**
1. Read "Access Control and User Management" overview
2. Skip "Configuring Argo CD RBAC" (not relevant)
3. Find "Configuring SSO for Argo CD using Dex"
4. Read "Configuration to enable the Dex OpenShift OAuth Connector"
5. Read "Mapping users to specific roles"
6. (Maybe) Check "Configuring SSO for Argo CD using external OIDC providers" to understand alternatives

**Steps:** 6 navigation steps, 2 assemblies

### Proposed Navigation

**To configure SSO with OpenShift:**
1. Navigate to "Secure Access to Argo CD"
2. Find "Job 2: Configure Single Sign-On"
3. Choose "Option A: Dex-Based SSO with OpenShift OAuth"
4. Follow implementation steps

**Steps:** 4 navigation steps, 1 job with clear option selection

### Metrics

**Current:**
- 4 top-level assemblies
- 16 subsections
- Average navigation depth: 3-4 levels
- Requires understanding authentication technologies upfront

**Proposed:**
- 3 main jobs
- 9 user stories/paths
- Average navigation depth: 2-3 levels
- Guides technology selection based on goal

**Improvement:**
- 25% reduction in top-level navigation items (4 → 3)
- 44% reduction in subsections (16 → 9 user stories)
- Clearer decision points with Option A/B structure
- Context-driven guidance instead of technology-first organization

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Get Started | ❌ Missing | ❌ Missing | Gap remains |
| Plan | ⚠️ Prerequisites only | ⚠️ Prerequisites only | Gap remains |
| Secure | ✅ All 4 assemblies | ✅ Jobs 1, 2, 3 | Reorganized |
| Confirm | ⚠️ OIDC verify only | ✅ Job 2 (verify SSO) | Improved |
| Execute | ⚠️ Embedded in local users | ✅ Job 3 (retrieve tokens) | Elevated |
| Operate | ⚠️ Embedded in local users | ✅ Job 3 (lifecycle) | Elevated |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Reference | ⚠️ Embedded in concepts | ⚠️ Embedded in user stories | Gap remains |

**Gap Recommendations:**

1. **Get Started (Missing):**
   - Add overview of authentication options
   - Include decision tree: RBAC vs SSO vs local users
   - Provide getting started checklist

2. **Plan (Minimal):**
   - Add capacity planning for OIDC provider
   - Include architecture diagrams for Dex vs direct OIDC
   - Document security considerations and trade-offs

3. **Troubleshoot (Missing):**
   - Add common RBAC configuration errors
   - Include SSO authentication troubleshooting
   - Document local user token issues and resolution

4. **Reference (Embedded):**
   - Extract RBAC policy syntax reference
   - Create OIDC scopes and claims reference
   - Document local user configuration field reference

---

## UX Research Alignment

**Note:** No research-specific fields populated (loop, genai_phase, strategic_priority, pain_points, teams_involved). This analysis uses generic persona detection from documentation content.

**If research data were available, we would include:**
- Strategic priority indicators on high-value jobs
- Pain point patterns detected in documentation
- Team collaboration indicators
- Inner/outer loop categorization

---

## Document Statistics

**Current Structure:**
- Assemblies: 4
- Subsections: 16
- Total sections: 20

**Proposed Structure:**
- Main Jobs: 3
- User Stories: 9
- Total sections: 12

**Source Coverage:**
- Lines analyzed: 1,263
- JTBD records extracted: 12
- Main jobs rolled up: 3
- Consolidation ratio: 4:1 (12 records → 3 main jobs)

**Navigation Efficiency:**
- Current top-level items: 4
- Proposed top-level items: 3
- Reduction: 25%

**Workflow Coverage:**
- Stages covered: 4 (Secure, Confirm, Execute, Operate)
- Stages with gaps: 4 (Get Started, Plan, Troubleshoot, Reference)
- Coverage: 50%
