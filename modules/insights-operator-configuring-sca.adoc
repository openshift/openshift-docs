// Module included in the following assemblies:
//
// * support/remote_health_monitoring/insights-operator-simple-access.adoc


:_mod-docs-content-type: PROCEDURE
[id="insights-operator-configuring-sca_{context}"]
= Configuring simple content access import interval

You can configure how often the Insights Operator imports the simple content access entitlements by using the `support` secret in the `openshift-config` namespace. The entitlement import normally occurs every eight hours, but you can shorten this interval if you update your simple content access configuration in Red Hat Subscription Management.

This procedure describes how to update the import interval to one hour.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You are logged in to the {product-title} web console as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You are logged in to the {product-title} web console as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]

.Procedure

. Navigate to *Workloads* -> *Secrets*.
. Select the *openshift-config* project.
. Search for the *support* secret by using the *Search by name* field. If it does not exist, click *Create* -> *Key/value secret* to create it.
+
--
* If the secret exists:
. Click the *Options* menu {kebab}, and then click *Edit Secret*.
. Click *Add Key/Value*.
.. In the *Key* field, enter `scaInterval`.
.. In the *Value* field, enter `1h`.
+
* If the secret does not exist:
.. Click *Create* -> *Key/value secret*.
... In the *Secret name* field, enter `support`.
... In the *Key* field, enter `scaInterval`.
... In the *Value* field, enter `1h`.
.. Click *Create*.
--
+
[NOTE]
====
The interval `1h` can also be entered as `60m` for 60 minutes.
====
