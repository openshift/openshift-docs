[id="deploying-local-provisioner_{context}"]
= Deploying the local provisioner

This paragraph is the procedure module introduction: a short description of the procedure.

.Prerequisites

* Before starting the provisioner, mount all local devices and create a ConfigMap with storage classes and their directories.

.Procedure

. Install the local provisioner from the `*local-storage-provisioner-template.yaml*` file.
. Create a service account that allows running Pods as a root user, using hostPath volumes, and using any SELinux context to monitor, manage, and clean local volumes, for example:
+
----
$ oc create serviceaccount local-storage-admin
$ oc adm policy add-scc-to-user privileged -z local-storage-admin
----
+
To allow the provisioner Pod to delete content on local volumes created by any Pod, root privileges and any SELinux context are required. hostPath is required to access the `*/mnt/local-storage*` path on the host.
