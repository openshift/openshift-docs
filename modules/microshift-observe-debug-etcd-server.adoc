// Module included in the following assemblies:
//
//* microshift_support/microshift-etcd.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-observe-debug-etcd-server_{context}"]
= Observe and debug the {microshift-short} etcd server

You can gather `journalctl` logs to observe and debug the etcd server logs.

.Prerequisites

* The {microshift-short} service is running.

.Procedure

* To get the logs for etcd, run the following command:
+
[source,terminal]
----
$ sudo journalctl -u microshift-etcd.scope
----
+
[NOTE]
====
{microshift-short} logs can be accessed separately from etcd logs using the `journalctl -u microshift` command.
====