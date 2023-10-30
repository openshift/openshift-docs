// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc


:_mod-docs-content-type: PROCEDURE
[id="running-insights-operator-gather-openshift-cli_{context}"]
= Running an Insights Operator gather operation using the OpenShift CLI
You can run an Insights Operator gather operation using the {product-title} command line interface.

.Prerequisites

* You are logged in to {product-title} as a user with the `cluster-admin` role.

.Procedure
* Enter the following command to run the gather operation:
+
[source,terminal]
----
$ oc apply -f <your_datagather_definition>.yaml
----
+
Replace `<your_datagather_definition>.yaml` with a configuration file using the following parameters:
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

.Verification

* Check that your new gather operation is prefixed with your chosen name under the list of pods in the `openshift-insights` project. Upon completion, the Insights Operator automatically uploads the data to Red Hat for processing.

