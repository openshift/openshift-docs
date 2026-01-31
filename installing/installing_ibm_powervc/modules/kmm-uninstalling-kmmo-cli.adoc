// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: PROCEDURE
[id="kmm-uninstalling-kmmo-cli_{context}"]
= Uninstalling a CLI installation

Use this command if the KMM Operator was installed using the OpenShift CLI.

.Procedure

* Run the following command to uninstall the KMM Operator:
+
[source,terminal]
----
$ oc delete -k https://github.com/rh-ecosystem-edge/kernel-module-management/config/default
----
+
[NOTE]
====
Using this command deletes the ``Module`` CRD and all ``Module`` instances in the cluster.
====
