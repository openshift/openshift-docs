// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

:_mod-docs-content-type: PROCEDURE
[id="starting-an-alternative-image-with-toolbox_{context}"]
= Starting an alternative image with `toolbox`

ifndef::openshift-origin[]
By default, running the `toolbox` command starts a container with the `registry.redhat.io/rhel8/support-tools:latest` image. You can start an alternative image by creating a `.toolboxrc` file and specifying the image to run.
endif::openshift-origin[]

ifdef::openshift-origin[]
By default, running the `toolbox` command starts a container with the `quay.io/fedora/fedora:36` image. You can start an alternative image by creating a `.toolboxrc` file and specifying the image to run.
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

. Create a `.toolboxrc` file in the home directory for the root user ID:
+
[source,terminal]
----
# vi ~/.toolboxrc
----
+
[source,text]
----
REGISTRY=quay.io                <1>
IMAGE=fedora/fedora:33-x86_64   <2>
TOOLBOX_NAME=toolbox-fedora-33  <3>
----
<1> Optional: Specify an alternative container registry.
<2> Specify an alternative image to start.
<3> Optional: Specify an alternative name for the toolbox container.

. Start a toolbox container with the alternative image:
+
[source,terminal]
----
# toolbox
----
+
[NOTE]
====
If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start...`. Remove the running toolbox container with `podman rm toolbox-` and spawn a new toolbox container, to avoid issues with `sosreport` plugins.
====
