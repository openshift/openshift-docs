// Module included in the following assemblies:
//
// * logging/log_visualizer/logging-kibana.adoc

:_mod-docs-content-type: PROCEDURE
[id="cluster-logging-visualizer-indices_{context}"]
= Defining Kibana index patterns

An index pattern defines the Elasticsearch indices that you want to visualize. To explore and visualize data in Kibana, you must create an index pattern.

.Prerequisites

* A user must have the `cluster-admin` role, the `cluster-reader` role, or both roles to view the *infra* and *audit* indices in Kibana. The default `kubeadmin` user has proper permissions to view these indices.
+
If you can view the pods and logs in the `default`, `kube-` and `openshift-` projects, you should be able to access these indices. You can use the following command to check if the current user has appropriate permissions:
+
[source,terminal]
----
$ oc auth can-i get pods --subresource log -n <project>
----
+
.Example output
[source,terminal]
----
yes
----
+
[NOTE]
====
The audit logs are not stored in the internal {product-title} Elasticsearch instance by default. To view the audit logs in Kibana, you must use the Log Forwarding API to configure a pipeline that uses the `default` output for audit logs.
====

* Elasticsearch documents must be indexed before you can create index patterns. This is done automatically, but it might take a few minutes in a new or updated cluster.

.Procedure

To define index patterns and create visualizations in Kibana:

. In the {product-title} console, click the Application Launcher {launch} and select *Logging*.

. Create your Kibana index patterns by clicking *Management* -> *Index Patterns* -> *Create index pattern*:

** Each user must manually create index patterns when logging into Kibana the first time to see logs for their projects. Users must create an index pattern named `app` and use the `@timestamp` time field to view their container logs.

** Each admin user must create index patterns when logged into Kibana the first time for the `app`, `infra`, and `audit` indices using the `@timestamp` time field.

. Create Kibana Visualizations from the new index patterns.
