// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deploy-mod-v2x.adoc


[id="ossm-deploy-multi-mesh_{context}"]
= Multimesh or federated deployment model

_Federation_ is a deployment model that lets you share services and workloads between separate meshes managed in distinct administrative domains.

The Istio multi-cluster model requires a high level of trust between meshes and remote access to all Kubernetes API servers on which the individual meshes reside. {SMProductName} federation takes an opinionated approach to a multi-cluster implementation of Service Mesh that assumes _minimal_ trust between meshes.

A _federated mesh_ is a group of meshes behaving as a single mesh. The services in each mesh can be unique services, for example a mesh adding services by importing them from another mesh, can provide additional workloads for the same services across the meshes, providing high availability, or a combination of both. All meshes that are joined into a federated mesh remain managed individually, and you must explicitly configure which services are exported to and imported from other meshes in the federation. Support functions such as certificate generation, metrics and trace collection remain local in their respective meshes.
