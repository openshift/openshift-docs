////
This module included in the following assemblies:
* service_mesh/v2x/ossm-federation.adoc
////

[id="ossm-federation-remove-mesh_{context}"]
= Removing a mesh from the federated mesh

If you need to remove a mesh from the federation, you can do so.

. Edit the removed mesh's `ServiceMeshControlPlane` resource to remove all federation ingress gateways for peer meshes.

. For each mesh peer that the removed mesh has been federated with:

.. Remove the `ServiceMeshPeer` resource that links the two meshes.

.. Edit the peer mesh's `ServiceMeshControlPlane` resource to remove the egress gateway that serves the removed mesh.
