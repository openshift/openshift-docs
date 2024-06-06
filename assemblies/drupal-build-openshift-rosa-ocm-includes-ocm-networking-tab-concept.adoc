// Module included in the following assemblies:
//
// ocm/ocm-overview.adoc
:_mod-docs-content-type: CONCEPT
[id="ocm-networking-tab_{context}"]
= Networking tab

The **Networking** tab provides a control plane API endpoint as well as the default application router. Both the control plane API endpoint and the default application router can be made private by selecting the respective box below each of them.

ifdef::openshift-rosa[]
[IMPORTANT]
====
For Security Token Service (STS) installations, these options cannot be changed. STS installations also do not allow you to change privacy nor allow you to add an additional router.
====
endif::openshift-rosa[]

ifndef::openshift-rosa[]
[IMPORTANT]
====
{cluster-manager-first} does not support the networking tab for a Google Cloud Platform (GCP), non-CCS cluster running in a Red Hat GCP project.
====
endif::openshift-rosa[]
