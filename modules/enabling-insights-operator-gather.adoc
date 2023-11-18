// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc


:_mod-docs-content-type: PROCEDURE
[id="enabling-insights-operator-gather_{context}"]
= Enabling the Insights Operator gather operations

You can enable the Insights Operator gather operations, if the gather operations have been disabled.

:FeatureName: The `InsightsDataGather` custom resource
include::snippets/technology-preview.adoc[]

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You are logged in to the {product-title} web console as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You are logged in to the {product-title} web console as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]

.Procedure

. Navigate to *Administration* -> *CustomResourceDefinitions*.
. On the *CustomResourceDefinitions* page, use the *Search by name* field to find the *InsightsDataGather* resource definition and click it.
. On the *CustomResourceDefinition details* page, click the *Instances* tab.
. Click *cluster*, and then click the *YAML* tab.
. Enable the gather operations by performing one of the following edits:

** To enable all disabled gather operations, remove the `gatherConfig` stanza:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1alpha1
kind: InsightsDataGather
metadata:
....

spec:
  gatherConfig: <1>
    disabledGatherers: all
----
+
--
<1> Remove the `gatherConfig` stanza to enable all gather operations.
--

** To enable individual gather operations, remove their values under the `disabledGatherers` key:
+
[source,yaml]
----
spec:
  gatherConfig:
    disabledGatherers:
      - clusterconfig/container_images <1>
      - clusterconfig/host_subnets
      - workloads/workload_info
----
+
--
<1> Remove one or more gather operations.
--
+
. Click *Save*.
+
After you save the changes, the Insights Operator gather configurations are updated and the affected gather operations start.

[NOTE]
====
Disabling gather operations degrades Insights Advisor's ability to offer effective recommendations for your cluster.
====
