// Module included in the following assemblies:
//
// * applications/idling-applications.adoc

:_mod-docs-content-type: PROCEDURE
[id="idle-idling-applications_{context}"]
= Idling applications

Idling an application involves finding the scalable resources (deployment
configurations, replication controllers, and others) associated with a service.
Idling an application finds the service and marks it as idled, scaling down the
resources to zero replicas.

You can use the `oc idle` command to idle a single service, or use the
`--resource-names-file` option to idle multiple services.

[id="idle-idling-applications-single_{context}"]
== Idling a single service

.Procedure

. To idle a single service, run:
+
[source,terminal]
----
$ oc idle <service>
----

[id="idle-idling-applications-multiple_{context}"]
== Idling multiple services

Idling multiple services is helpful if an application spans across a set of
services within a project, or when idling multiple services in conjunction with
a script to idle multiple applications in bulk within the same project.

.Procedure

. Create a file containing a list of the services, each on their own line.

. Idle the services using the `--resource-names-file` option:
+
[source,terminal]
----
$ oc idle --resource-names-file <filename>
----

[NOTE]
====
The `idle` command is limited to a single project. For idling applications across
a cluster, run the `idle` command for each project individually.
====
