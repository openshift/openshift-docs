// Module included in the following assemblies:
//
// * logging/viewing/cluster-logging-visualizer.adoc

:_mod-docs-content-type: PROCEDURE
[id="cluster-logging-visualizer-kibana_{context}"]
= Viewing cluster logs in Kibana

You view cluster logs in the Kibana web console. The methods for viewing and visualizing your data in Kibana that are beyond the scope of this documentation. For more information, refer to the link:https://www.elastic.co/guide/en/kibana/6.8/tutorial-sample-discover.html[Kibana documentation].

.Prerequisites

* The Red Hat OpenShift Logging and Elasticsearch Operators must be installed.

* Kibana index patterns must exist.

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

.Procedure

To view logs in Kibana:

. In the {product-title} console, click the Application Launcher {launch} and select *Logging*.

. Log in using the same credentials you use to log in to the {product-title} console.
+
The Kibana interface launches.

. In Kibana, click *Discover*.

. Select the index pattern you created from the drop-down menu in the top-left corner: *app*, *audit*, or *infra*.
+
The log data displays as  time-stamped documents.

. Expand one of the time-stamped documents.

. Click the *JSON* tab to display the log entry for that document.
+
.Sample infrastructure log entry in Kibana
[%collapsible]
====
[source,terminal]
----
{
  "_index": "infra-000001",
  "_type": "_doc",
  "_id": "YmJmYTBlNDkZTRmLTliMGQtMjE3NmFiOGUyOWM3",
  "_version": 1,
  "_score": null,
  "_source": {
    "docker": {
      "container_id": "f85fa55bbef7bb783f041066be1e7c267a6b88c4603dfce213e32c1"
    },
    "kubernetes": {
      "container_name": "registry-server",
      "namespace_name": "openshift-marketplace",
      "pod_name": "redhat-marketplace-n64gc",
      "container_image": "registry.redhat.io/redhat/redhat-marketplace-index:v4.7",
      "container_image_id": "registry.redhat.io/redhat/redhat-marketplace-index@sha256:65fc0c45aabb95809e376feb065771ecda9e5e59cc8b3024c4545c168f",
      "pod_id": "8f594ea2-c866-4b5c-a1c8-a50756704b2a",
      "host": "ip-10-0-182-28.us-east-2.compute.internal",
      "master_url": "https://kubernetes.default.svc",
      "namespace_id": "3abab127-7669-4eb3-b9ef-44c04ad68d38",
      "namespace_labels": {
        "openshift_io/cluster-monitoring": "true"
      },
      "flat_labels": [
        "catalogsource_operators_coreos_com/update=redhat-marketplace"
      ]
    },
    "message": "time=\"2020-09-23T20:47:03Z\" level=info msg=\"serving registry\" database=/database/index.db port=50051",
    "level": "unknown",
    "hostname": "ip-10-0-182-28.internal",
    "pipeline_metadata": {
      "collector": {
        "ipaddr4": "10.0.182.28",
        "inputname": "fluent-plugin-systemd",
        "name": "fluentd",
        "received_at": "2020-09-23T20:47:15.007583+00:00",
        "version": "1.7.4 1.6.0"
      }
    },
    "@timestamp": "2020-09-23T20:47:03.422465+00:00",
    "viaq_msg_id": "YmJmYTBlNDktMDMGQtMjE3NmFiOGUyOWM3",
    "openshift": {
      "labels": {
        "logging": "infra"
      }
    }
  },
  "fields": {
    "@timestamp": [
      "2020-09-23T20:47:03.422Z"
    ],
    "pipeline_metadata.collector.received_at": [
      "2020-09-23T20:47:15.007Z"
    ]
  },
  "sort": [
    1600894023422
  ]
}
----
====
