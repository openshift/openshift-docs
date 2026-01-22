// Module included in the following assemblies:
//
// * scalability_and_performance/optimization/optimizing-cpu-usage.adoc

:_mod-docs-content-type: PROCEDURE
[id="supporting-encapsulation_{context}"]
= Inspecting encapsulated namespaces

You can inspect Kubernetes-specific mount points in the cluster host operating system for debugging or auditing purposes by using the `kubensenter` script that is available in {op-system-first}.

SSH shell sessions to the cluster host are in the default namespace.
To inspect Kubernetes-specific mount points in an SSH shell prompt, you need to run the `kubensenter` script as root.
The `kubensenter` script is aware of the state of the mount encapsulation, and is safe to run even if encapsulation is not enabled.

[NOTE]
====
`oc debug` remote shell sessions start inside the Kubernetes namespace by default.
You do not need to run `kubensenter` to inspect mount points when you use `oc debug`.
====

If the encapsulation feature is not enabled, the `kubensenter findmnt` and `findmnt` commands return the same output, regardless of whether they are run in an `oc debug` session or in an SSH shell prompt.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in as a user with `cluster-admin` privileges.

* You have configured SSH access to the cluster host.

.Procedure

. Open a remote SSH shell to the cluster host. For example:
+
[source,terminal]
----
$ ssh core@<node_name>
----

. Run commands using the provided `kubensenter` script as the root user.
To run a single command inside the Kubernetes namespace, provide the command and any arguments to the `kubensenter` script.
For example, to run the `findmnt` command inside the Kubernetes namespace, run the following command:
+
[source,terminal]
----
[core@control-plane-1 ~]$ sudo kubensenter findmnt
----
+
.Example output
[source,terminal]
----
kubensenter: Autodetect: kubens.service namespace found at /run/kubens/mnt
TARGET                                SOURCE                 FSTYPE     OPTIONS
/                                     /dev/sda4[/ostree/deploy/rhcos/deploy/32074f0e8e5ec453e56f5a8a7bc9347eaa4172349ceab9c22b709d9d71a3f4b0.0]
|                                                            xfs        rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,prjquota
                                      shm                    tmpfs
...
----

. To start a new interactive shell inside the Kubernetes namespace, run the `kubensenter` script without any arguments:
+
[source,terminal]
----
[core@control-plane-1 ~]$ sudo kubensenter
----
+
.Example output
[source,terminal]
----
kubensenter: Autodetect: kubens.service namespace found at /run/kubens/mnt
----
