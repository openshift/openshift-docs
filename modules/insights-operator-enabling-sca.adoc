// Module included in the following assemblies:
//
// * support/remote_health_monitoring/insights-operator-simple-access.adoc


:_mod-docs-content-type: PROCEDURE
[id="insights-operator-enabling-sca_{context}"]
= Enabling a previously disabled simple content access import

If the importing of simple content access entitlements is disabled, the Insights Operator does not import simple content access entitlements. You can change this behavior.

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
. Search for the *support* secret by using the *Search by name* field.
. Click the *Options* menu {kebab}, and then click *Edit Secret*.
. For the `scaPullDisabled` key, set the *Value* field to `false`.
+
The simple content access entitlement import is now disabled.
