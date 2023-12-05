// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc


:_mod-docs-content-type: PROCEDURE

[id="running-insights-operator-gather-web-console_{context}"]
= Running an Insights Operator gather operation using the web console
You can run an Insights Operator gather operation using the {product-title} web console.

.Prerequisites

* You are logged in to the {product-title} web console as a user with the `cluster-admin` role.

.Procedure

. Navigate to *Administration* -> *CustomResourceDefinitions*.
. On the *CustomResourceDefinitions* page, use the *Search by name* field to find the *DataGather* resource definition and click it.
. On the *CustomResourceDefinition details* page, click the *Instances* tab.
. Click *Create DataGather*.
. To create a new `DataGather` operation, edit the configuration file:
+
[source,yaml]
----
apiVersion: insights.openshift.io/v1alpha1
kind: DataGather
metadata:
  name: <your_data_gather> <1>
spec:
 gatherers: <2>
   - name: workloads
     state: Disabled
----
+
--
<1> Replace the `<your_data_gather>` with a unique name for your gather operation.
<2> Enter individual gather operations to disable under the `gatherers` parameter. This example disables the `workloads` data gather operation and will run the remainder of the default operations. To run the complete list of default gather operations, leave the `spec` parameter empty. You can find the complete list of gather operations in the Insights Operator documentation.
--
+
. Click *Save*.

.Verification

. Navigate to *Workloads* -> *Pods*.
. On the Pods page, select the *Project* pulldown menu, and then turn on Show default projects.
. Select the `openshift-insights` project from the *Project* pulldown menu.
. Check that your new gather operation is prefixed with your chosen name under the list of pods in the `openshift-insights` project. Upon completion, the Insights Operator automatically uploads the data to Red Hat for processing.
