////
This module included in the following assemblies:
* service_mesh/v2x/ossm-federation.adoc
////

[id="ossm-federation-planning_{context}"]
= Planning your mesh federation

Before you start configuring your mesh federation, you should take some time to plan your implementation.

* How many meshes do you plan to join in a federation? You probably want to start with a limited number of meshes, perhaps two or three.
* What naming convention do you plan to use for each mesh? Having a pre-defined naming convention will help with configuration and troubleshooting. The examples in this documentation use different colors for each mesh. You should decide on a naming convention that will help you determine who owns and manages each mesh, as well as the following federation resources:
** Cluster names
** Cluster network names
** Mesh names and namespaces
** Federation ingress gateways
** Federation egress gateways
** Security trust domains
+
[NOTE]
====
Each mesh in the federation must have its own unique trust domain.
====
+
* Which services from each mesh do you plan to export to the federated mesh? Each service can be exported individually, or you can specify labels or use wildcards.
** Do you want to use aliases for the service namespaces?
** Do you want to use aliases for the exported services?
* Which exported services does each mesh plan to import? Each mesh only imports the services that it needs.
** Do you want to use aliases for the imported services?
