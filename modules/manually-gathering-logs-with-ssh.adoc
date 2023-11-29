// Module included in the following assemblies:
//
// *installing/installing-troubleshooting.adoc

:_mod-docs-content-type: PROCEDURE
[id="installation-manually-gathering-logs-with-SSH_{context}"]
= Manually gathering logs with SSH access to your host(s)

Manually gather logs in situations where `must-gather` or automated collection
methods do not work.

[IMPORTANT]
====
By default, SSH access to the {product-title} nodes is disabled on the {rh-openstack-first} based installations.
====

.Prerequisites

* You must have SSH access to your host(s).

.Procedure

. Collect the `bootkube.service` service logs from the bootstrap host using the
`journalctl` command by running:
+
[source,terminal]
----
$ journalctl -b -f -u bootkube.service
----

. Collect the bootstrap host's container logs using the podman logs. This is shown
as a loop to get all of the container logs from the host:
+
[source,terminal]
----
$ for pod in $(sudo podman ps -a -q); do sudo podman logs $pod; done
----

. Alternatively, collect the host's container logs using the `tail` command by
running:
+
[source,terminal]
----
# tail -f /var/lib/containers/storage/overlay-containers/*/userdata/ctr.log
----

. Collect the `kubelet.service` and `crio.service` service logs from the master
and worker hosts using the `journalctl` command by running:
+
[source,terminal]
----
$ journalctl -b -f -u kubelet.service -u crio.service
----

. Collect the master and worker host container logs using the `tail` command by
running:
+
[source,terminal]
----
$ sudo tail -f /var/log/containers/*
----
