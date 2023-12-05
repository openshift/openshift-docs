// Module included in the following assemblies:
//
// * nodes/nodes-containers-events.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-containers-events-about_{context}"]
= Understanding events

Events allow {product-title} to record
information about real-world events in a resource-agnostic manner. They also
allow developers and administrators to consume information about system
components in a unified way.

ifdef::openshift-online[]
[id="event-failure-notifications_{context}"]
== Failure Notifications

For each of your projects, you can choose to receive email notifications
about various failures, including dead or failed deployments, dead builds, and
dead or failed persistent volume claims (PVCs).

See Notifications.
endif::[]
