// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deploy-mod-v2x.adoc

[id="ossm-deploy-single-mesh_{context}"]
= Single mesh deployment model

The simplest Istio deployment model is a single mesh.

Service names within a mesh must be unique because Kubernetes only allows one service to be named `myservice` in the `mynamespace` namespace. However, workload instances can share a common identity since service account names can be shared across workloads in the same namespace
