// Module included in the following assemblies:
//
// * virt/install/uninstalling-virt.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-deleting-virt-cli_{context}"]
= Uninstalling {VirtProductName} by using the CLI

You can uninstall {VirtProductName} by using the OpenShift CLI (`oc`).

.Prerequisites

* You have access to an {product-title} cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).
* You have deleted all virtual machines and virtual machine instances. You cannot uninstall {VirtProductName} while its workloads remain on the cluster.

.Procedure

. Delete the `HyperConverged` custom resource:
+
[source,terminal,subs="attributes+"]
----
$ oc delete HyperConverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Delete the {VirtProductName} Operator subscription:
+
[source,terminal,subs="attributes+"]
----
$ oc delete subscription kubevirt-hyperconverged -n {CNVNamespace}
----

. Delete the {VirtProductName} `ClusterServiceVersion` resource:
+
[source,terminal,subs="attributes+"]
----
$ oc delete csv -n openshift-cnv -l operators.coreos.com/kubevirt-hyperconverged.{CNVNamespace}
----

. Delete the {VirtProductName} namespace:
+
[source,terminal]
----
$ oc delete namespace openshift-cnv
----

. List the {VirtProductName} custom resource definitions (CRDs) by running the `oc delete crd` command with the `dry-run` option:
+
[source,terminal,subs="attributes+"]
----
$ oc delete crd --dry-run=client -l operators.coreos.com/kubevirt-hyperconverged.{CNVNamespace}
----
+
.Example output
----
customresourcedefinition.apiextensions.k8s.io "cdis.cdi.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "hostpathprovisioners.hostpathprovisioner.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "hyperconvergeds.hco.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "kubevirts.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "networkaddonsconfigs.networkaddonsoperator.network.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "ssps.ssp.kubevirt.io" deleted (dry run)
customresourcedefinition.apiextensions.k8s.io "tektontasks.tektontasks.kubevirt.io" deleted (dry run)
----

. Delete the CRDs by running the `oc delete crd` command without the `dry-run` option:
+
[source,terminal,subs="attributes+"]
----
$ oc delete crd -l operators.coreos.com/kubevirt-hyperconverged.{CNVNamespace}
----
