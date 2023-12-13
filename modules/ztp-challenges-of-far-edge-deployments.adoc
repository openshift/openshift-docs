// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-clusters-at-scale.adoc

:_mod-docs-content-type: CONCEPT
[id="ztp-challenges-of-far-edge-deployments_{context}"]
= Overcoming the challenges of the network far edge

Today, service providers want to deploy their infrastructure at the edge of the network. This presents significant challenges:

* How do you handle deployments of many edge sites in parallel?
* What happens when you need to deploy sites in disconnected environments?
* How do you manage the lifecycle of large fleets of clusters?

{ztp-first} and _GitOps_ meets these challenges by allowing you to provision remote edge sites at scale with declarative site definitions and configurations for bare-metal equipment. Template or overlay configurations install {product-title} features that are required for CNF workloads. The full lifecycle of installation and upgrades is handled through the {ztp} pipeline.

{ztp} uses GitOps for infrastructure deployments. With GitOps, you use declarative YAML files and other defined patterns stored in Git repositories. {rh-rhacm-first} uses your Git repositories to drive the deployment of your infrastructure.

GitOps provides traceability, role-based access control (RBAC), and a single source of truth for the desired state of each site. Scalability issues are addressed by Git methodologies and event driven operations through webhooks.

You start the {ztp} workflow by creating declarative site definition and configuration custom resources (CRs) that the {ztp} pipeline delivers to the edge nodes.

The following diagram shows how {ztp} works within the far edge framework.

image::217_OpenShift_Zero_Touch_Provisioning_updates_1022_1.png[{ztp} at the network far edge]
