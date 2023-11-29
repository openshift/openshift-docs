// Module included in the following assemblies:
//
// * microshift_running_apps/microshift-authentication.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-viewing-security-context_{context}"]
= Viewing security context constraints in a namespace

You can view the security context constraints (SCC) permissions in a given namespace.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

.Procedure

* To view the security context constraints in your namespace, run the following command:
+
[source,terminal]
----
oc get --show-labels namespace <namespace>
----
