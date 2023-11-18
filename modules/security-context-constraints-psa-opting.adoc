// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc

:_mod-docs-content-type: PROCEDURE
[id="security-context-constraints-psa-opting_{context}"]
= Controlling pod security admission synchronization

You can enable or disable automatic pod security admission synchronization for most namespaces.

[IMPORTANT]
====
You cannot enable pod security admission synchronization on 
ifndef::openshift-dedicated,openshift-rosa[]
some
endif::openshift-dedicated,openshift-rosa[]
system-created namespaces. For more information, see _Pod security admission synchronization namespace exclusions_.
====

.Procedure

* For each namespace that you want to configure, set a value for the `security.openshift.io/scc.podSecurityLabelSync` label:
** To disable pod security admission label synchronization in a namespace, set the value of the `security.openshift.io/scc.podSecurityLabelSync` label to `false`.
+
Run the following command:
+
[source,terminal]
----
$ oc label namespace <namespace> security.openshift.io/scc.podSecurityLabelSync=false
----

** To enable pod security admission label synchronization in a namespace, set the value of the `security.openshift.io/scc.podSecurityLabelSync` label to `true`.
+
Run the following command:
+
[source,terminal]
----
$ oc label namespace <namespace> security.openshift.io/scc.podSecurityLabelSync=true
----
