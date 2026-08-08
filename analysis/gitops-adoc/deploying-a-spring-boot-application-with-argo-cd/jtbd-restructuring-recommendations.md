# JTBD-Based Restructuring Recommendations
## Deploying a Spring Boot Application with Argo CD

### Current Structure (Feature-Based)

```
Deploying a Spring Boot application with Argo CD
├── Creating an application by using the Argo CD dashboard
├── Creating an application by using the oc tool
└── Verifying Argo CD self-healing behavior
```

**Issues with Current Structure:**
- Focuses on tools/features (dashboard vs. oc) rather than user goals
- Self-healing verification feels disconnected from main workflow
- Namespace labeling buried in procedures (critical step hidden)
- No clear guidance on when to use dashboard vs. CLI

---

### Proposed Structure (JTBD-Based)

```
Deploying Applications with Argo CD
├── Overview: GitOps deployment workflow
│
├── DEPLOY YOUR APPLICATION
│   ├── Before you begin: Configure namespace permissions ⚠️ CRITICAL
│   ├── Option 1: Deploy using the Argo CD dashboard (recommended for first-time users)
│   └── Option 2: Deploy using the oc CLI (recommended for automation)
│
├── UPDATE YOUR APPLICATION
│   └── Making changes through Git commits
│
├── MONITOR YOUR APPLICATION
│   ├── Check sync status in the dashboard
│   └── View application events and history
│
└── VERIFY & TROUBLESHOOT
    ├── Test self-healing behavior
    └── Troubleshoot sync failures
```

---

## Key Improvements

### 1. Job-Oriented Section Headers
**Before**: "Creating an application by using the Argo CD dashboard"
**After**: "Deploy your application" with subsections for tools

**Benefit**: Users think "I need to deploy" not "I need to use the dashboard"

### 2. Elevate Critical Prerequisites
**Before**: Namespace labeling embedded in step 9 of procedures
**After**: Dedicated "Before you begin" section with warning

**Benefit**: Prevents common deployment failures from missing labels

### 3. Tool Selection Guidance
**Before**: Two separate procedures with no guidance
**After**: Clear options with recommendations:
- Dashboard: First-time users, visual learners, one-off deployments
- CLI: Automation, scripts, CI/CD pipelines, batch operations

**Benefit**: Users pick the right tool for their context

### 4. Workflow Progression
**Before**: Procedures presented as alternatives
**After**: Clear progression: Deploy → Update → Monitor → Verify

**Benefit**: Matches natural user workflow and learning path

### 5. Troubleshooting Integration
**Before**: Self-healing verification as separate task
**After**: Part of "Verify & Troubleshoot" section

**Benefit**: Users find verification and troubleshooting in one place

---

## Detailed Section Breakdowns

### Section 1: Overview
**Purpose**: Set context and explain GitOps concepts
**Content**:
- What is GitOps deployment with Argo CD?
- How Argo CD maintains sync between Git and cluster
- Prerequisites checklist (GitOps installed, logged into Argo CD)

**Job Addressed**: Understanding how Argo CD works (implicit concept job)

---

### Section 2: Before You Begin - Configure Namespace Permissions
**Purpose**: Prevent deployment failures from missing labels
**Content**:
- Why namespace labeling is required
- How to apply the label (web console and CLI options)
- How to verify the label is applied
- What happens if you skip this step

**Job Addressed**: 
- Job #4 (CRITICAL): Ensure namespace can be managed by Argo CD

**Current Location**: Embedded in procedures
**Recommended Location**: Standalone prerequisite section with warning box

---

### Section 3: Deploy Your Application

#### Option 1: Using the Argo CD Dashboard
**When to use**: First-time deployments, learning Argo CD, one-off applications
**Content**: Current dashboard procedure
**Job Addressed**: Job #2 (HIGH): Create and configure Argo CD application visually

#### Option 2: Using the oc CLI
**When to use**: Automated deployments, CI/CD integration, managing multiple applications
**Content**: Current oc tool procedure
**Job Addressed**: Job #3 (HIGH): Create Argo CD application from command line

**Unified Job**: Job #1 (HIGH): Deploy Spring Boot application to OpenShift

---

### Section 4: Update Your Application
**Purpose**: Teach GitOps workflow for making changes
**Content**:
- How to modify application in Git repository
- How Argo CD detects changes
- Automatic vs. manual sync policies
- Verifying updates are deployed

**Job Addressed**: Job #6 (HIGH): Modify deployed application via Git commits

**Current Location**: Example in self-healing procedure
**Recommended Location**: Standalone section on update workflow

---

### Section 5: Monitor Your Application
**Purpose**: Verify deployment status and health
**Content**:
- Checking sync status in dashboard
- Understanding sync states (Synced, OutOfSync, Unknown)
- Viewing deployed resources
- Interpreting application health

**Job Addressed**: Job #7 (MEDIUM): Verify Argo CD application sync status

**Current Location**: Mentioned briefly in self-healing
**Recommended Location**: Standalone monitoring section

---

### Section 6: Verify & Troubleshoot

#### Test Self-Healing Behavior
**Purpose**: Build confidence in Argo CD automation
**Content**: Current self-healing verification procedure
**Job Addressed**: Job #5 (MEDIUM): Understand self-healing mechanism

#### Troubleshoot Sync Failures
**Purpose**: Debug deployment issues
**Content**:
- Viewing application events
- Common sync failure causes
- How to interpret event timeline
- Where to find detailed error messages

**Job Addressed**: Job #8 (HIGH): Troubleshoot sync issues using events

**Current Location**: Events mentioned in self-healing
**Recommended Location**: Expanded troubleshooting section

---

## Content Gaps to Address

### 1. Sync Policy Decision
**Missing Job**: "When I need to choose between automatic and manual sync, I want to understand the trade-offs..."

**Recommended Addition**:
- Table comparing automatic vs. manual sync
- Use cases for each approach
- How to change sync policy later

### 2. Repository Structure
**Missing Job**: "When I need to prepare my Git repository for Argo CD, I want to understand what structure is required..."

**Recommended Addition**:
- Example repository structure
- What Argo CD looks for in the specified path
- How to organize multi-environment configs

### 3. Error Scenarios
**Missing Job**: "When my Argo CD deployment fails, I want to know what went wrong and how to fix it..."

**Recommended Addition**:
- Common error messages and solutions
- Namespace permission errors
- Git repository access issues
- Invalid manifest errors

### 4. Multi-Environment Deployments
**Missing Job**: "When I need to deploy to multiple environments (dev/staging/prod), I want to use the same Git repository..."

**Recommended Addition**:
- Using different branches or paths
- Kustomize overlays (if supported)
- Environment-specific configurations

---

## Migration Path

### Phase 1: Quick Wins (No structural changes)
1. Add warning box about namespace labeling to both procedures
2. Add "When to use" guidance to dashboard and CLI procedures
3. Expand events/troubleshooting content in self-healing section

### Phase 2: Reorganization (Moderate changes)
1. Create "Before you begin" section for namespace labeling
2. Group dashboard and CLI as options under "Deploy"
3. Extract Git update workflow from self-healing to standalone section
4. Create dedicated monitoring section

### Phase 3: Full JTBD Structure (Significant changes)
1. Implement full proposed structure
2. Add missing content for gaps
3. Update cross-references in other assemblies
4. Update navigation/TOC

---

## Success Metrics

### Quantitative
- **Time to first successful deployment**: Should decrease
- **Namespace labeling errors**: Should decrease
- **Sync troubleshooting support tickets**: Should decrease
- **Page views per session**: May increase (more sections) but bounce rate should decrease

### Qualitative
- Users can quickly find the right deployment method for their needs
- Critical steps (namespace labeling) are not overlooked
- Update workflow through Git is clear and discoverable
- Troubleshooting path is obvious when issues occur

---

## Next Steps

1. **Validate with users**: Interview 3-5 users to confirm jobs and priorities
2. **Prototype restructure**: Create mockup of proposed structure
3. **Test navigation**: Verify users can find content for each job
4. **Plan migration**: Determine which phase to implement first
5. **Update related assemblies**: Ensure shared modules work with new structure
