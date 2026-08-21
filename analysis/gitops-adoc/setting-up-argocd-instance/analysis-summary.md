# JTBD Analysis Summary: Setting up an Argo CD instance

## Document Information

- **Assembly**: `cicd/gitops/setting-up-argocd-instance.adoc`
- **Type**: ASSEMBLY
- **Analysis Date**: 2026-04-06
- **Total JTBD Records**: 5
- **Total Modules**: 4 (all PROCEDURE type)

## Module Breakdown

| Module | Type | Section Title |
|--------|------|---------------|
| `modules/gitops-argo-cd-installation.adoc` | PROCEDURE | Installing Argo CD |
| `modules/gitops-enable-replicas-for-argo-cd-server.adoc` | PROCEDURE | Enabling replicas for Argo CD server and repo server |
| `modules/gitops-deploy-resources-different-namespaces.adoc` | PROCEDURE | Deploying resources to a different namespace |
| `modules/gitops-customize-argo-cd-consolelink.adoc` | PROCEDURE | Customizing the Argo CD console link |

## JTBD Records Summary

### Primary Persona
- **Platform administrator** (5 jobs)

### Workflow Stages Distribution
- **Setup and Configuration**: 2 jobs
- **Configuration**: 2 jobs
- **Optimization**: 1 job

### Task Types
- Installation: 1
- Access: 1
- Scaling: 1
- Authorization: 1
- Customization: 1

### Priority Distribution
- **High**: 3 jobs
- **Medium**: 2 jobs

### Complexity Distribution
- **Low**: 2 jobs
- **Medium**: 3 jobs

## Key Jobs

1. **gitops-001**: Install and deploy a new Argo CD instance to manage cluster configurations or deploy applications
   - Priority: High | Complexity: Medium
   - Stage: Setup and Configuration

2. **gitops-004**: Configure Argo CD to manage resources in namespaces other than where it's installed
   - Priority: High | Complexity: Low
   - Stage: Configuration

3. **gitops-003**: Scale Argo CD server and repo server replicas to distribute workloads
   - Priority: Medium | Complexity: Medium
   - Stage: Optimization

4. **gitops-005**: Customize which Argo CD instance appears in the OpenShift console link
   - Priority: Medium | Complexity: Medium
   - Stage: Configuration

5. **gitops-002**: Access the Argo CD web UI after installation
   - Priority: High | Complexity: Low
   - Stage: Setup and Configuration

## Output Files

1. **JTBD Records (JSONL)**: `setting-up-argocd-instance-jtbd.jsonl`
2. **JTBD Records (CSV)**: `setting-up-argocd-instance-jtbd.csv`
3. **Include Graph**: `setting-up-argocd-instance-include-graph.json`
4. **Reduced AsciiDoc**: `setting-up-argocd-instance-reduced.adoc`

## Analysis Notes

This assembly focuses on **post-installation configuration** of Argo CD instances. It assumes the OpenShift GitOps Operator is already installed and provides procedures for:

1. Creating additional Argo CD instances beyond the default `openshift-gitops` instance
2. Scaling instances for better performance
3. Extending permissions to manage resources across namespaces
4. Resolving multi-tenant UI access issues

All procedures are straightforward with clear step-by-step instructions, making them suitable for platform administrators with basic OpenShift knowledge.

## Recommendations

- These jobs represent a clear workflow: **Install → Access → Configure → Scale → Customize**
- Consider grouping related tasks (cross-namespace management + scaling + customization) under a "Managing Argo CD instances" chapter
- The distinction between the default instance and custom instances could be made clearer in the introduction
