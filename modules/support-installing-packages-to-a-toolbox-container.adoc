// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-packages-to-a-toolbox-container_{context}"]
= Installing packages to a `toolbox` container

ifndef::openshift-origin[]
By default, running the `toolbox` command starts a container with the `registry.redhat.io/rhel8/support-tools:latest` image. This image contains the most frequently used support tools. If you need to collect node-specific data that requires a support tool that is not part of the image, you can install additional packages.
endif::openshift-origin[]

ifdef::openshift-origin[]
By default, running the `toolbox` command starts a container with the `quay.io/fedora/fedora:36` image. This image contains the most frequently used support tools. If you need to collect node-specific data that requires a support tool that is not part of the image, you can install additional packages.
endif::openshift-origin[]

.Prerequisites

* You have accessed a node with the `oc debug node/<node_name>` command.

.Procedure

. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----

. Start the toolbox container:
+
[source,terminal]
----
# toolbox
----

. Install the additional package, such as `wget`:
+
[source,terminal]
----
# dnf install -y <package_name>
----
