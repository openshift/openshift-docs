# Access Control and User Management
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Configure secure access to Argo CD through role-based access control, single sign-on, and local user management

**Personas:** Cluster administrator, Automation engineer

**Main Jobs:** 3 core jobs across Secure, Confirm, Execute, and Operate stages

---

## Quick Navigation

**I want to:**
- Control who can access Argo CD → Job 1 (Secure)
- Use enterprise identity providers → Job 2 (Secure)
- Provide API tokens for automation → Job 3 (Secure)
- Verify SSO is working correctly → Job 2 (Confirm)
- Manage token lifecycle → Job 3 (Operate)

---

# Table of Contents

## Secure Access to Argo CD

### Job 1: Configure Role-Based Access Control
*When managing access to Argo CD*

**Personas:** Cluster administrator

**Context:** By default, the default Argo CD instance grants no access except to `kube:admin`. Custom instances provide read-only access by default. RBAC policies control which users can perform which operations.

#### User-Level RBAC Configuration

**For: Cluster administrator needing to grant specific permissions**

**Approach:** Edit RBAC policy in Argo CD CR

1. Access the Argo CD custom resource
   - Lines 151-156: Edit argocd CR command
2. Configure RBAC policy for specific users
   - Lines 169-179: Add policy configuration with name and role
3. Apply scopes configuration
   - Lines 177-179: Set scopes to '[groups]'

**Note:** Red Hat SSO cannot read GitOps user group information, requiring user-level RBAC configuration.

**Prerequisites:**
- OpenShift GitOps Operator installed
- cluster-admin access

**Related Jobs:**
- Job 2: Configure single sign-on
- Job 3: Manage local users

**Desired Outcomes:**
- Complete RBAC configuration in under 5 minutes
- Avoid granting excessive permissions
- Ensure user access aligns with organizational roles

---

### Job 2: Configure Single Sign-On
*When managing multiple users*

**Personas:** Cluster administrator

**Context:** After the GitOps Operator is installed, Argo CD creates an admin user. For multiple users, administrators can configure SSO using Dex (with OpenShift OAuth) or external OIDC providers directly.

#### SSO Integration Approaches

Argo CD supports two primary authentication approaches:

**Option A: Dex-Based SSO (`spec.sso`)**
- Uses Dex as intermediary identity broker
- Connects to OpenShift OAuth or external providers
- Presents unified authentication interface

**Option B: Direct OIDC Integration (`spec.oidcConfig`)**
- Connects directly to OIDC-compliant provider
- Bypasses Dex intermediary
- Provider-agnostic approach

**Important:** Cannot use `spec.sso` and `spec.oidcConfig` simultaneously.

#### Approach A: Enable Dex with OpenShift OAuth

**For: Cluster administrator leveraging OpenShift users and groups**

1. Configure Dex provider in Argo CD CR
   - Lines 340-357: Set spec.sso.provider to dex and enable openShiftOAuth
2. Map users to Argo CD roles through OpenShift groups
   - Lines 382-399: Create cluster-admins group, add users, apply cluster-admin ClusterRole

**Prerequisites:**
- OpenShift OAuth server configured

**Desired Outcomes:**
- Complete SSO configuration in under 10 minutes
- Users authenticate with existing OpenShift credentials
- Avoid maintaining duplicate user databases

**Note:** Users with direct ClusterRoleBinding cannot be mapped to roles directly. Create groups and add users as a workaround.

#### Approach B: Configure External OIDC Integration

**For: Cluster administrator integrating with enterprise identity providers**

1. Obtain OIDC provider information
   - Lines 568-571: Issuer URL, Client ID, Client secret
2. Edit Argo CD CR with OIDC configuration
   - Lines 587-643: Add spec.oidcConfig with provider details, scopes, and claims
3. Restart Argo CD server to apply configuration
   - Lines 645-664: Rollout restart and verify deployment

**Prerequisites:**
- OIDC-compliant identity provider configured
- Client ID and secret from provider

**Desired Outcomes:**
- Successfully integrate with enterprise identity providers
- Minimize authentication latency by avoiding intermediaries
- Ensure proper scope and claim mapping

#### Verify SSO Authentication

**For: Cluster administrator validating SSO configuration**

1. Access Argo CD web UI via route URL
   - Lines 681-687: Verify login option appears with configured provider name
2. Test authentication with identity provider credentials
3. Confirm role-based permissions are applied correctly

**Prerequisites:**
- SSO configured (Dex or OIDC)

**Desired Outcomes:**
- Confirm authentication flow works end-to-end
- Verify role-based permissions are applied correctly
- Identify and resolve authentication issues quickly

---

## Provide API Access for Automation

### Job 3: Manage Local User Accounts
*When needing API tokens for automation or small teams without SSO*

**Personas:** Cluster administrator, Automation engineer

**Context:** The Argo CD Operator manages local users by creating accounts, generating JWT API tokens, configuring token lifetimes and automatic renewal, storing tokens in Kubernetes secrets, and cleaning up users when removed.

#### Create Local Users for API Access

**For: Cluster administrator providing API access for service accounts or automation**

1. Edit Argo CD CR and add localUsers configuration
   - Lines 1225-1250: Define users with name, enabled, apiKey, login, tokenLifetime, and autoRenewToken fields
2. Save configuration
   - Lines 1252-1254: Operator reconciles and creates secrets/tokens automatically

**Configuration Options:**

**Basic local user:** Non-expiring token, API-only access
```yaml
- name: developer
```

**Expiring token user:** 30-day lifetime with automatic renewal
```yaml
- name: ci-system
  tokenLifetime: "720h"
  autoRenewToken: true
```

**Long-lived token user:** 1-year lifetime without renewal
```yaml
- name: monitoring
  tokenLifetime: "8760h"
  autoRenewToken: false
```

**User with login capability:** Can use web UI and API tokens
```yaml
- name: developer
  login: true
  tokenLifetime: "24h"
  autoRenewToken: true
```

**Prerequisites:**
- Argo CD instance deployed

**Desired Outcomes:**
- Complete local user creation in under 5 minutes
- Ensure tokens are generated and stored securely
- Enable automation without SSO complexity

#### Retrieve and Use API Tokens

**For: Cluster administrator or automation engineer accessing Argo CD APIs**

1. Retrieve token from Kubernetes secret
   - Lines 1097-1099: Extract apiToken from {username}-local-user secret
2. Decode base64-encoded token
3. Use token with Argo CD CLI or API
   - Lines 1106-1108: Example argocd CLI command with auth-token

**Token Storage:**
- Secret name: `{username}-local-user`
- Fields: apiToken, user, expAt, tokenLifetime, autoRenew (all base64-encoded)
- Lines 1069-1085: Example secret structure

**Prerequisites:**
- Local user with API key created

**Desired Outcomes:**
- Retrieve tokens quickly from Kubernetes secrets
- Ensure tokens are base64-decoded correctly
- Successfully authenticate automation scripts and service accounts

#### Manage Token Lifecycle

**For: Cluster administrator balancing security with operational continuity**

**Automatic Renewal:**
- Configure autoRenewToken: true for uninterrupted automation
- Lines 1123-1125: Operator renews tokens before expiration

**Manual Token Rotation:**
- Delete user secret to trigger immediate rotation
- Lines 1129-1136: Delete secret, Operator generates new token

**Disable API Keys:**
- Set apiKey: false to revoke token access
- Lines 1138-1140: Cleanup secrets and stop renewal timers

**Prerequisites:**
- Local users created

**Desired Outcomes:**
- Ensure automation continues without token expiration interruptions
- Minimize manual token rotation overhead
- Maintain security through time-limited tokens

#### Manage User Lifecycle

**For: Cluster administrator responding to changing access needs**

**Disable Users:**
- Set enabled: false to temporarily revoke access
- Lines 1157-1163: User account remains, tokens preserved, authentication blocked

**Remove Users:**
- Delete entry from localUsers list
- Lines 1166-1172: Secret deleted, token removed, renewal timers canceled, account removed

**Prerequisites:**
- Local users created

**Desired Outcomes:**
- Revoke access immediately when needed
- Preserve configuration for temporary disablement
- Clean up all resources when users are permanently removed

---

## Appendices

### A. SSO Integration Comparison Matrix

| Approach | Intermediary | Use Case | Complexity | Configuration |
|----------|--------------|----------|------------|---------------|
| Dex with OpenShift OAuth | Dex broker | Leverage existing OpenShift users/groups | Low | `spec.sso.provider: dex` |
| Direct OIDC | None | Enterprise identity providers (Keycloak, Okta, etc.) | Medium | `spec.oidcConfig` |

### B. Local User Configuration Decision Guide

| Requirement | Configuration | Example |
|-------------|---------------|---------|
| Non-expiring API token | Default (tokenLifetime: 0h) | Service accounts |
| Renewable token for CI/CD | tokenLifetime + autoRenewToken: true | CI systems |
| Long-lived manual rotation | tokenLifetime + autoRenewToken: false | Monitoring systems |
| Web UI + API access | login: true + apiKey: true | Developers |
| Temporary access revocation | enabled: false | Suspended accounts |

### C. Workflow Coverage Analysis

| Stage | Jobs | Coverage |
|-------|------|----------|
| Get Started | - | Gap: No getting started content |
| Secure | 3 jobs | ✅ Complete (RBAC, SSO, local users) |
| Confirm | 1 job | ✅ Verify SSO login |
| Execute | 1 job | ✅ Retrieve/use tokens |
| Operate | 2 jobs | ✅ Token/user lifecycle |
| Reference | - | Gap: No reference material |

**Identified Gaps:**
- No onboarding/getting started guidance
- No reference material for RBAC policy syntax
- No troubleshooting section for authentication issues

---

## Navigation Guide

### By User Journey

**Cluster administrator setting up RBAC-only access:**
1. Job 1: Configure RBAC policies for user-level permissions
2. (Optional) Job 2: Add SSO for multiple users later

**Cluster administrator integrating with OpenShift:**
1. Job 2: Enable Dex with OpenShift OAuth
2. Job 2: Map users to roles via groups
3. Job 2: Verify SSO login
4. Job 1: Configure RBAC for fine-grained permissions

**Cluster administrator integrating with external OIDC provider:**
1. Job 2: Configure direct OIDC integration
2. Job 2: Verify OIDC login
3. Job 1: Configure RBAC for role mapping

**Automation engineer setting up CI/CD access:**
1. Job 3: Create local user with renewable token
2. Job 3: Retrieve token from Kubernetes secret
3. Job 3: Configure automation to use token

**Cluster administrator managing user lifecycle:**
1. Job 3: Create local users as needed
2. Job 3: Monitor and rotate tokens
3. Job 3: Disable or remove users when access changes

---

## Document Statistics

**Workflow Coverage:**
- Secure: 3 jobs (RBAC, SSO, local users)
- Confirm: 1 job (Verify SSO)
- Execute: 1 job (Retrieve/use tokens)
- Operate: 2 jobs (Token lifecycle, user lifecycle)
- **Gaps:** Get Started, Reference, Troubleshooting

**Main Jobs:** 3
**User Stories/Paths:** 9
**Source Sections:** 4 assemblies
**Authentication Variations:** 3 (RBAC, Dex SSO, OIDC SSO, local users)

**Platform/Integration Coverage:**
- OpenShift OAuth via Dex
- External OIDC providers (provider-agnostic)
- Local user management with operator automation
