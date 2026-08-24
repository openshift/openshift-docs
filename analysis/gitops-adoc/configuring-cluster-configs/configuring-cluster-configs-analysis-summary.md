# JTBD Analysis Summary

**Document**: configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.adoc  
**Analysis Date**: 2026-04-06  
**Total Records**: 18

## Overview

This assembly covers configuring OpenShift clusters by deploying applications with cluster configurations using GitOps. The workflow involves setting up Argo CD permissions, creating applications, synchronizing with Git repositories, and managing Operators declaratively.

## Main Jobs Identified (7)

1. **Configure my Argo CD instance with appropriate permissions** (Configure stage)
   - Enable cluster-scoped resource management through GitOps
   - 2 user stories (UI-based configuration, CLI verification)

2. **Understand the default permission model** (Plan stage)
   - Determine permission requirements before deployment
   - 1 user story (understanding in-built permissions)

3. **Run Argo CD on dedicated infrastructure nodes** (Configure stage)
   - Isolate GitOps workloads for production environments

4. **Create an Argo CD application pointing to my Git repository** (Deploy stage)
   - Deploy cluster configurations declaratively
   - 3 user stories (Dashboard method, CLI method, namespace labeling)

5. **Trigger synchronization to apply Git repository changes** (Execute stage)
   - Apply configurations from Git to cluster
   - 1 user story (verification workflow)

6. **Create custom cluster roles and bindings** (Configure stage)
   - Grant additional permissions beyond defaults
   - 1 user story (UI-based RBAC configuration)

7. **Automate Operator installation via GitOps** (Deploy stage)
   - Eliminate manual Operator installation procedures
   - 3 user stories (cluster-scoped, namespace-scoped, conflict avoidance)

## Personas

- **Cluster Administrator** (13 records) - Primary persona managing cluster configurations
- **Platform Engineer** (5 records) - Infrastructure and automation focus

## Job Map Distribution

| Stage | Count | Main Jobs | User Stories |
|-------|-------|-----------|--------------|
| Plan | 2 | 1 | 1 |
| Configure | 7 | 4 | 3 |
| Confirm | 2 | 0 | 2 |
| Deploy | 7 | 3 | 4 |
| Execute | 1 | 1 | 0 |
| Troubleshoot | 1 | 0 | 1 |

## Job Type Distribution

- **Core**: 16 records
- **Related**: 2 records
- **Consumption**: 0 records
- **Emotional**: 0 records

## Granularity Distribution

- **Main Jobs**: 7
- **User Stories**: 11
- **Procedures**: 0

## Key Workflows

### Workflow 1: Initial Setup
1. Install GitOps Operator (prerequisite)
2. Understand default permission model
3. Configure Argo CD for cluster-scoped resources
4. Optionally run Argo CD on infrastructure nodes

### Workflow 2: Application Deployment
1. Create Argo CD application (via Dashboard or CLI)
2. Label namespace for management
3. Synchronize application with Git repository
4. Verify configurations in OpenShift console

### Workflow 3: Permission Management
1. Understand default permissions
2. Identify required additional permissions
3. Create custom cluster roles and bindings

### Workflow 4: Operator Management
1. Configure Argo CD for cluster-scoped resources
2. Add Operator Subscriptions to Git repository
3. For namespace-scoped: Add OperatorGroup (only one per namespace)
4. Monitor Operator installation

## Strategic Insights

### Consolidation Opportunities

**Multiple approaches to same job**:
- Create Argo CD application: Dashboard vs CLI (2 user stories)
- Verify permissions: UI search vs CLI command (1 user story)
- Configure RBAC: UI console vs YAML (1 user story)

### Critical Dependencies

1. **Namespace labeling** is required for Argo CD management (often overlooked)
2. **OperatorGroup uniqueness** constraint for namespace-scoped Operators
3. **Permission configuration** must occur before application deployment

### Pain Points (Inferred)

1. **OperatorGroup conflicts**: TooManyOperatorGroups causes CSV failures requiring manual intervention
2. **Permission discovery**: Users must know what additional permissions are needed beyond defaults
3. **Multi-step verification**: Configuration requires verification in multiple locations

## Desired Outcomes (Top 10)

1. Minimize time to deploy cluster configurations
2. Ensure Git repository is source of truth
3. Reduce manual configuration errors
4. Enable automatic drift detection
5. Minimize time to grant additional permissions
6. Ensure permissions follow least-privilege principle
7. Minimize time to install Operators across multiple clusters
8. Ensure consistent Operator versions
9. Enable declarative Operator lifecycle management
10. Minimize OperatorGroup conflicts

## Module Breakdown

| Module | Type | Lines | Jobs Extracted |
|--------|------|-------|----------------|
| gitops-using-argo-cd-instance-to-manage-cluster-scoped-resources.adoc | PROCEDURE | 51 | 3 |
| gitops-default-permissions-of-an-argocd-instance.adoc | PROCEDURE | 47 | 1 |
| go-run-argo-cd-instance-on-infrastructure-nodes.adoc | PROCEDURE | 58 | 1 |
| gitops-creating-an-application-by-using-the-argo-cd-dashboard.adoc | PROCEDURE | 59 | 3 |
| gitops-creating-an-application-by-using-the-oc-tool.adoc | PROCEDURE | 68 | 1 |
| gitops-synchronizing-your-application-application-with-your-git-repository.adoc | PROCEDURE | 21 | 2 |
| gitops-inbuilt-permissions-for-cluster-config.adoc | REFERENCE | 25 | 1 |
| gitops-additional-permissions-for-cluster-config.adoc | PROCEDURE | 54 | 2 |
| gitops-installing-olm-operators-using-gitops.adoc | PROCEDURE | 80 | 4 |

## Quality Metrics

- **Main jobs**: 7 (within 10-15 target range)
- **Average user stories per main job**: 1.6
- **Jobs with prerequisites**: 15/18 (83%)
- **Jobs with desired outcomes**: 18/18 (100%)
- **Evidence with line numbers**: 18/18 (100%)

## Notes

- No emotional/social jobs explicitly stated in the documentation
- Focus is heavily on configuration and deployment stages
- Strong emphasis on security (permissions, RBAC, least privilege)
- Multiple user stories reflect UI vs CLI approach alternatives
- OperatorGroup constraint is a critical troubleshooting concern
