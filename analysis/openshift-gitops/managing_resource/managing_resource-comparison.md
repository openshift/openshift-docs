# Structure Comparison: Current vs JTBD-Based
# Managing Resource Use

**Document**: managing_resource  
**Analysis Date**: 2026-04-09  
**Source**: 2 assemblies, 260 lines

---

## Header & Metadata

| Attribute | Current Structure | Proposed JTBD Structure |
|-----------|------------------|-------------------------|
| Organization | Component-based (Argo CD CR vs GitOpsService CR) | Job-based workflow (what to accomplish) |
| Primary axis | Resource type (ArgoCD workloads vs plugin components) | User goal + workflow stage |
| Chapters | 2 (Argo CD, Plugin) | 2 (Argo CD Resource Management, Plugin Resource Management) |
| Hierarchy depth | 2 levels (Assembly > Section) | 3 levels (Job > User Story > Task) |
| Navigation | By component type | By workflow stage (planning, setup, operations) |

---

## Current Structure (Component-Based)

### Assembly 1: Configuring resource quota or requests
- **Abstract**: Create, update, and delete resource requests/limits for Argo CD workloads
- **Section**: Configuring workloads with resource requests and limits
  - Type: REFERENCE
  - Content: YAML example with resources for all 6 components (server, applicationSet, repo, dex, redis, controller)
- **Section**: Patching Argo CD instance to update the resource requirements
  - Type: PROCEDURE
  - Content: Commands to update Application Controller CPU and memory via `oc patch`
- **Section**: Removing resource requests
  - Type: PROCEDURE
  - Content: Commands to remove Application Controller CPU and memory via `oc patch`

### Assembly 2: Configure resource requests and limits for GitOps plugin components
- **Abstract**: Configure CPU/memory for console plugin and backend components via GitOpsService CR
- **Section**: Enabling the GitOpsService custom resource
  - Type: PROCEDURE
  - Prerequisites: Admin login, GitOps Operator installed
  - Content: Retrieve GitOpsService CR, edit to add backend and plugin resources, verify
- **Section**: Behavior of resource configuration
  - Type: CONCEPT
  - Content: How GitOpsService controller applies values, default resource table

**Total**: 2 assemblies, 5 sections, 2 hierarchy levels

---

## Proposed JTBD-Based Structure

### Chapter 1: Resource Management for Argo CD Workloads
**Job 1: Manage Argo CD resource allocation**
- **User Story 1.1**: Configure resource requests and limits for initial deployment
  - Stage: SETUP
  - Tasks: Define Application Controller specs, Define ApplicationSet Controller specs, Define Server component specs
  - Module Type: REFERENCE
- **User Story 1.2**: Update resource requirements post-installation
  - Stage: OPERATIONS
  - Tasks: Patch Application Controller CPU request, Patch Application Controller memory request
  - Module Type: PROCEDURE
- **User Story 1.3**: Remove resource constraints
  - Stage: OPERATIONS
  - Tasks: Remove Application Controller CPU constraint, Remove Application Controller memory constraint
  - Module Type: PROCEDURE

### Chapter 2: Resource Management for GitOps Console Plugin
**Job 2: Configure GitOps plugin resource allocation**
- **User Story 2.1**: Configure plugin component resource limits
  - Stage: SETUP
  - Tasks: Locate GitOpsService custom resource, Edit GitOpsService CR with resource specifications, Verify resource configuration applied
  - Module Type: PROCEDURE
- **User Story 2.2**: Understand resource configuration behavior
  - Stage: PLANNING
  - Tasks: Review default resource values
  - Module Type: CONCEPT

**Total**: 2 chapters, 2 main jobs, 5 user stories, 10 tasks, 3 hierarchy levels

---

## Key Differences

| Aspect | Current (Component-Based) | JTBD (Job-Based) | Impact |
|--------|------------------------|------------------|--------|
| **Organization** | By custom resource type (ArgoCD CR vs GitOpsService CR) | By user goal (Manage Argo CD allocation vs Configure plugin allocation) | Users find content by what they want to accomplish, not by which CR to edit |
| **Workflow Integration** | Separate assemblies with no lifecycle connection | Organized by workflow stage (planning, setup, operations) | Clearer understanding of when to perform each task |
| **Task Granularity** | Sections mix concepts with procedures | Tasks clearly separated by specific actions | Users can identify precise steps for their immediate need |
| **Prerequisites** | Listed once at assembly level | Embedded in job dependencies | Clearer understanding of job requirements |
| **Default Values** | Concept section at end of second assembly | Planning stage user story before setup | Users learn defaults before configuring custom values |
| **Component Coverage** | Example shows all 6 components, but patch examples only Application Controller | Tasks explicitly cover controller types users actually configure | No ambiguity about which components can be modified |
| **Success Criteria** | Implicit (assumed if command succeeds) | Explicit per user story | Clear definition of done for each job |
| **Pain Points** | Not documented | Captured per job (e.g., "JSON patch syntax complexity") | Users aware of common challenges and can prepare |

---

## Hierarchy Levels

### Current Structure
```
Assembly (Level 1)
└── Section (Level 2)
```

**Example**:
```
Configuring resource quota or requests (Assembly)
├── Configuring workloads with resource requests and limits (Section - REFERENCE)
├── Patching Argo CD instance to update the resource requirements (Section - PROCEDURE)
└── Removing resource requests (Section - PROCEDURE)
```

### JTBD Structure
```
Chapter (Workflow Phase)
└── Main Job (Level 1)
    └── User Story (Level 2)
        └── Tasks (Level 3)
```

**Example**:
```
Resource Management for Argo CD Workloads (Chapter)
└── Job 1: Manage Argo CD resource allocation (Main Job - OPERATIONS)
    ├── User Story 1.1: Configure for initial deployment (SETUP)
    │   ├── Task: Define Application Controller specs
    │   ├── Task: Define ApplicationSet Controller specs
    │   └── Task: Define Server component specs
    ├── User Story 1.2: Update post-installation (OPERATIONS)
    │   ├── Task: Patch CPU request
    │   └── Task: Patch memory request
    └── User Story 1.3: Remove constraints (OPERATIONS)
        ├── Task: Remove CPU constraint
        └── Task: Remove memory constraint
```

---

## Example Consolidation

### Example 1: Resource Configuration Workflow

**Current Structure (scattered across sections)**:
1. **Reference Section**: See YAML example with all resources defined
2. **Procedure Section**: Patch to update resources
3. **Procedure Section**: Patch to remove resources
4. **Concept Section** (in different assembly): Learn about defaults

**JTBD Structure (consolidated lifecycle)**:
1. **Planning Stage**: Understand default values and controller behavior → decide if custom configuration needed
2. **Setup Stage**: Configure resources during initial deployment → all components in one user story
3. **Operations Stage**: Update resources when requirements change → CPU and memory tasks under one user story
4. **Operations Stage**: Remove constraints when no longer needed → removal tasks under dedicated user story

**Navigation Improvement**: 4 separate navigations reduced to 1 job with 4 user stories organized by stage

---

### Example 2: GitOps Plugin Resource Management

**Current Structure**:
1. **Assembly Title**: "Configure resource requests and limits for GitOps plugin components"
2. **Procedure Section**: "Enabling the GitOpsService custom resource"
3. **Concept Section**: "Behavior of resource configuration"

User path: Read concept first (to understand defaults) → then go back to procedure

**JTBD Structure**:
1. **Job 2.2** (Planning): Understand resource configuration behavior → includes reviewing defaults
2. **Job 2.1** (Setup): Configure plugin component resource limits → procedure with clear steps

User path: Planning stage → Setup stage (logical progression)

**Navigation Improvement**: Concepts placed before procedures in workflow order, not document order

---

## Navigation Improvement Metrics

| Metric | Current | JTBD | Improvement |
|--------|---------|------|-------------|
| **Clicks to configure new Argo CD instance with resources** | 3 (find assembly → scroll to reference → interpret YAML) | 2 (Job 1 → User Story 1.1) | 33% reduction |
| **Clicks to update existing resources** | 4 (find assembly → skip reference → find patch section → identify component) | 2 (Job 1 → User Story 1.2) | 50% reduction |
| **Clicks to learn defaults before configuring plugin** | 5 (find assembly → scroll through procedure → reach concept section → read defaults → go back to procedure) | 3 (Job 2 → User Story 2.2 → User Story 2.1) | 40% reduction |
| **Average depth to actionable content** | 2.2 levels (assembly + section) | 2.5 levels (job + user story, sometimes + task) | +13% depth, but compensated by stage-based navigation |
| **Sections covering operational tasks** | 3 of 5 (60%) | 3 user stories + 8 tasks explicitly staged as OPERATIONS | Clearer lifecycle visibility |

---

## Workflow Coverage Comparison

### Current Coverage (by assembly sequence)
1. **Reference**: What resource specs look like
2. **Procedure**: How to patch after installation
3. **Procedure**: How to remove constraints
4. **Procedure**: How to configure plugin resources
5. **Concept**: Understand plugin controller behavior

**Gaps**:
- No coverage for monitoring actual resource consumption
- No troubleshooting for resource-related issues (OOMKilled, throttling)
- No guidance for right-sizing resources based on workload patterns
- Planning stage (understanding defaults) only appears in plugin section, not Argo CD section

### JTBD Coverage (by workflow stage)
| Stage | Coverage | Gap Indicators |
|-------|----------|----------------|
| PLANNING | ✓ Covered (Job 2.2 for plugin defaults) | ⚠ Argo CD defaults not explicitly documented |
| SETUP | ✓ Covered (Initial resource configuration for both Argo CD and plugin) | ✓ Complete |
| OPERATIONS | ✓ Covered (Update and remove resources) | ⚠ No monitoring or optimization guidance |
| MONITORING | ⚠ Missing | Missing entirely (should cover viewing actual usage vs limits) |
| TROUBLESHOOTING | ⚠ Missing | Missing entirely (should cover OOMKilled, throttling, right-sizing) |
| OPTIMIZATION | ⚠ Missing | Missing entirely (should cover capacity planning, workload-based tuning) |

**Recommendations**:
1. Add Job 1.0 (Planning): "Understand default Argo CD resource allocations" (mirror Job 2.2 for plugin)
2. Add Job 3 (Monitoring): "Monitor resource consumption for GitOps components"
3. Add Job 4 (Troubleshooting): "Diagnose and resolve resource-related issues"
4. Add reference material on recommended resource values by cluster size/workload

---

## Document Statistics

### Current Structure
- **Total Sections**: 5
- **Module Types**: 3 PROCEDURE, 1 REFERENCE, 1 CONCEPT
- **Lines of Code/Examples**: ~120 (YAML examples + command examples)
- **Prerequisites Mentioned**: 2 (admin login, operator installed)
- **Cross-references**: 0

### JTBD Structure
- **Main Jobs**: 2
- **User Stories**: 5
- **Tasks**: 10
- **Workflow Stages Covered**: 3 (Planning, Setup, Operations)
- **Workflow Stages Missing**: 3 (Monitoring, Troubleshooting, Optimization)
- **Personas**: 1 (Platform Administrator - 100% coverage)
- **Average User Stories per Job**: 2.5
- **Average Tasks per User Story**: 2.0
- **Pain Points Documented**: 5
- **Success Criteria Defined**: 5 (one per user story)

---

## Content Organization Patterns

### Current Pattern: Component-Driven
- Grouping: By custom resource type
- Sequence: Reference → Procedure → Procedure → Procedure → Concept
- User Journey: Read all sections to understand full lifecycle
- Best For: Users who know which CR they need to edit

### JTBD Pattern: Goal-Driven
- Grouping: By user goal and workflow stage
- Sequence: Planning → Setup → Operations (within each job)
- User Journey: Navigate to job matching goal → follow stage sequence
- Best For: Users who know what they want to accomplish

**Transformation Summary**:
- 2 component-based assemblies → 2 goal-based jobs
- 5 sections of mixed types → 5 user stories with explicit stages
- Implicit lifecycle → Explicit workflow stages (Planning, Setup, Operations)
- 0 documented pain points → 5 pain points captured
- 0 explicit success criteria → 5 success criteria defined
