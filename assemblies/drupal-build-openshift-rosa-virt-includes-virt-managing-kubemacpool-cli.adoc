// Module included in the following assemblies:
//
// * virt/vm_networking/virt-using-mac-address-pool-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-managing-kubemacpool-cli_{context}"]
= Managing KubeMacPool by using the command line

You can disable and re-enable KubeMacPool by using the command line.

KubeMacPool is enabled by default.

.Procedure

* To disable KubeMacPool in two namespaces, run the following command:
+
[source,terminal]
----
$ oc label namespace <namespace1> <namespace2> mutatevirtualmachines.kubemacpool.io=ignore
----

* To re-enable KubeMacPool in two namespaces, run the following command:
+
[source,terminal]
----
$ oc label namespace <namespace1> <namespace2> mutatevirtualmachines.kubemacpool.io-
----
