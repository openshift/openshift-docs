// Module included in the following assemblies:
//
// * virt/getting_started/virt-using-the-cli-tools.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-deploying-libguestfs-with-virtctl_{context}"]
= Deploying libguestfs by using virtctl

You can use the `virtctl guestfs` command to deploy an interactive container with `libguestfs-tools` and a persistent volume claim (PVC) attached to it.

.Procedure

* To deploy a container with `libguestfs-tools`, mount the PVC, and attach a shell to it, run the following command:
+
[source,terminal]
----
$ virtctl guestfs -n <namespace> <pvc_name> <1>
----
<1> The PVC name is a required argument. If you do not include it, an error message appears.
