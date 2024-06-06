// Module included in the following assemblies:
//
// * virt/storage/virt-managing-data-volume-annotations.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-dv-annotations_{context}"]
= Example: Data volume annotations

This example shows how you can configure data volume (DV) annotations to control which network the importer pod uses. The `v1.multus-cni.io/default-network: bridge-network` annotation causes the pod to use the multus network named `bridge-network` as its default network.
If you want the importer pod to use both the default network from the cluster and the secondary multus network, use the `k8s.v1.cni.cncf.io/networks: <network_name>` annotation.

.Multus network annotation example
[source,yaml]
----
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: datavolume-example
  annotations:
    v1.multus-cni.io/default-network: bridge-network <1>
# ...
----
<1> Multus network annotation
