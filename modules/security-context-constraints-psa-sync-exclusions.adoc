// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc
// * operators/operator_sdk/osdk-complying-with-psa.adoc

:_mod-docs-content-type: CONCEPT
[id="security-context-constraints-psa-sync-exclusions_{context}"]
= Pod security admission synchronization namespace exclusions

ifndef::openshift-dedicated,openshift-rosa[]
Pod security admission synchronization is permanently disabled on most system-created namespaces. Synchronization is also initially disabled on user-created `openshift-*` prefixed namespaces, but you can enable synchronization on them later.
endif::openshift-dedicated,openshift-rosa[]

ifdef::openshift-dedicated,openshift-rosa[]
Pod security admission synchronization is permanently disabled on system-created namespaces and `openshift-*` prefixed namespaces.
endif::openshift-dedicated,openshift-rosa[]

ifndef::openshift-dedicated,openshift-rosa[]
[IMPORTANT]
====
If a pod security admission label (`pod-security.kubernetes.io/<mode>`) is manually modified from the automatically labeled value on a label-synchronized namespace, synchronization is disabled for that label.

If necessary, you can enable synchronization again by using one of the following methods:

* By removing the modified pod security admission label from the namespace
* By setting the `security.openshift.io/scc.podSecurityLabelSync` label to `true`
+
If you force synchronization by adding this label, then any modified pod security admission labels will be overwritten.
====

[discrete]
== Permanently disabled namespaces
endif::openshift-dedicated,openshift-rosa[]

Namespaces that are defined as part of the cluster payload have pod security admission synchronization disabled permanently. The following namespaces are permanently disabled:

* `default`
* `kube-node-lease`
* `kube-system`
* `kube-public`
* `openshift`
* All system-created namespaces that are prefixed with `openshift-`
ifndef::openshift-dedicated,openshift-rosa[]
, except for `openshift-operators`
endif::openshift-dedicated,openshift-rosa[]

ifndef::openshift-dedicated,openshift-rosa[]
[discrete]
== Initially disabled namespaces

By default, all namespaces that have an `openshift-` prefix have pod security admission synchronization disabled initially. You can enable synchronization for user-created [x-]`openshift-*` namespaces and for the `openshift-operators` namespace.

[NOTE]
====
You cannot enable synchronization for any system-created [x-]`openshift-*` namespaces, except for `openshift-operators`.
====

If an Operator is installed in a user-created `openshift-*` namespace, synchronization is enabled automatically after a cluster service version (CSV) is created in the namespace. The synchronized label is derived from the permissions of the service accounts in the namespace.
endif::openshift-dedicated,openshift-rosa[]
