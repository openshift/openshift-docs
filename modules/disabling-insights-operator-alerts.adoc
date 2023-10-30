// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc


:_mod-docs-content-type: CONCEPT
[id="disabling-insights-operator-alerts_{context}"]
= Disabling Insights Operator alerts

ifndef::openshift-rosa,openshift-dedicated[]
To prevent the Insights Operator from sending alerts to the cluster Prometheus instance, you edit the `support` secret. If the `support` secret doesn't exist, you must create it when you first add custom configurations. Note that configurations within the `support` secret take precedence over the default settings defined in the `pod.yaml` file.
endif::openshift-rosa,openshift-dedicated[]
ifndef::openshift-rosa,openshift-dedicated[]
To prevent the Insights Operator from sending alerts to the cluster Prometheus instance, you edit the `support` secret. Note that this `secret` is created by default. The configurations stored in the support secret take precedence over any default settings specified in the `pod.yaml` file.
endif::openshift-rosa,openshift-dedicated[]

.Prerequisites

* Remote health reporting is enabled, which is the default.
ifndef::openshift-rosa,openshift-dedicated[]
* You are logged in to the {product-title} web console as `cluster-admin`.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You are logged in to the {product-title} web console as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]

.Procedure

. Navigate to *Workloads* -> *Secrets*.
. On the *Secrets* page, select *All Projects* from the *Project* list, and then set *Show default projects* to on.
. Select the *openshift-config* project from the *Projects* list.
. Search for the *support* secret by using the *Search by name* field.
+
* If the secret exists:
. Click the *Options* menu {kebab}, and then click *Edit Secret*.
. Click *Add Key/Value*.
.. In the *Key* field, enter `disableInsightsAlerts`.
.. In the *Value* field, enter `True`.
+
* If the secret does not exist:
.. Click *Create* -> *Key/value secret*.
... In the *Secret name* field, enter `support`.
... In the *Key* field, enter `disableInsightsAlerts`.
... In the *Value* field, enter `True`.
.. Click *Create*.

After you save the changes, Insights Operator no longer sends alerts to the cluster Prometheus instance.
