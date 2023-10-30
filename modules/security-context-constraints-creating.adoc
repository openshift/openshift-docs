// Module included in the following assemblies:
//
// * authentication/managing-security-context-constraints.adoc

:_mod-docs-content-type: PROCEDURE
[id="security-context-constraints-creating_{context}"]
ifndef::openshift-dedicated[]
= Creating security context constraints
endif::[]
ifdef::openshift-dedicated[]
= Creating security context constraints for CCS clusters
endif::[]

You can create security context constraints (SCCs) by using the OpenShift CLI (`oc`).

[IMPORTANT]
====
Creating and modifying your own SCCs are advanced operations that might cause instability to your cluster. If you have questions about using your own SCCs, contact Red Hat Support. For information about contacting Red Hat support, see _Getting support_.
====

ifdef::openshift-dedicated[]
[NOTE]
====
In {product-title} deployments, you can create your own SCCs only for clusters that use the Customer Cloud Subscription (CCS) model. You cannot create SCCs for {product-title} clusters that use a Red Hat cloud account, because SCC resource creation requires `cluster-admin` privileges.
====
endif::openshift-dedicated[]

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in to the cluster as a user with the `cluster-admin` role.

.Procedure

. Define the SCC in a YAML file named `scc-admin.yaml`:
+
[source,yaml]
----
kind: SecurityContextConstraints
apiVersion: security.openshift.io/v1
metadata:
  name: scc-admin
allowPrivilegedContainer: true
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: RunAsAny
fsGroup:
  type: RunAsAny
supplementalGroups:
  type: RunAsAny
users:
- my-admin-user
groups:
- my-admin-group
----
+
Optionally, you can drop specific capabilities for an SCC by setting the `requiredDropCapabilities` field with the desired values. Any specified capabilities are dropped from the container. To drop all capabilities, specify `ALL`. For example, to create an SCC that drops the `KILL`, `MKNOD`, and `SYS_CHROOT` capabilities, add the following to the SCC object:
+
[source,yaml]
----
requiredDropCapabilities:
- KILL
- MKNOD
- SYS_CHROOT
----
+
[NOTE]
+
====
You cannot list a capability in both `allowedCapabilities` and `requiredDropCapabilities`.
====
+
CRI-O supports the same list of capability values that are found in the link:https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities[Docker documentation].

. Create the SCC by passing in the file:
+
[source,terminal]
----
$ oc create -f scc-admin.yaml
----
+
.Example output
[source,terminal]
----
securitycontextconstraints "scc-admin" created
----

.Verification

* Verify that the SCC was created:
+
[source,terminal]
----
$ oc get scc scc-admin
----
+
.Example output
[source,terminal]
----
NAME        PRIV      CAPS      SELINUX    RUNASUSER   FSGROUP    SUPGROUP   PRIORITY   READONLYROOTFS   VOLUMES
scc-admin   true      []        RunAsAny   RunAsAny    RunAsAny   RunAsAny   <none>     false            [awsElasticBlockStore azureDisk azureFile cephFS cinder configMap downwardAPI emptyDir fc flexVolume flocker gcePersistentDisk gitRepo glusterfs iscsi nfs persistentVolumeClaim photonPersistentDisk quobyte rbd secret vsphere]
----
