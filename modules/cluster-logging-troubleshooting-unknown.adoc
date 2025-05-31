// Module included in the following assemblies:
//
// * logging/cluster-logging-troublehsooting.adoc

[id="cluster-logging-troubleshooting-unknown_{context}"]
= Troubleshooting a Kubernetes unknown error while connecting to Elasticsearch

If you are attempting to use a F-5 load balancer in front of Kibana with
`X-Forwarded-For` enabled, this can cause an issue in which the Elasticsearch
`Searchguard` plugin is unable to correctly accept connections from Kibana.

.Example Kibana Error Message
----
Kibana: Unknown error while connecting to Elasticsearch

Error: Unknown error while connecting to Elasticsearch
Error: UnknownHostException[No trusted proxies]
----

.Procedure

To configure Searchguard to ignore the extra header:

. Scale down all Fluentd pods.

. Scale down Elasticsearch after the Fluentd pods have terminated.

. Add `searchguard.http.xforwardedfor.header: DUMMY` to the Elasticsearch
configuration section.
+
[source,terminal]
----
$ oc edit configmap/elasticsearch <1>
----
<1> This approach requires that Elasticsearch configurations are within a config map.
+

. Scale Elasticsearch back up.

. Scale up all Fluentd pods.
