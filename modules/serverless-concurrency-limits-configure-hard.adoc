// Module included in the following assemblies:
//
// * serverless/knative-serving/autoscaling/serverless-autoscaling-developer.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-concurrency-limits-configure-hard_{context}"]
= Configuring a hard concurrency limit

A hard concurrency limit is a strictly enforced upper bound requests limit. If concurrency reaches the hard limit, surplus requests are buffered and must wait until there is enough free capacity to execute the requests. You can specify a hard concurrency limit for your Knative service by modifying the `containerConcurrency` spec, or by using the `kn service` command with the correct flags.

.Procedure

* Optional: Set the `containerConcurrency` spec for your Knative service in the spec of the `Service` custom resource:
+
.Example service spec
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example-service
  namespace: default
spec:
  template:
    spec:
      containerConcurrency: 50
----
+
The default value is `0`, which means that there is no limit on the number of simultaneous requests that are permitted to flow into one replica of the service at a time.
+
A value greater than `0` specifies the exact number of requests that are permitted to flow into one replica of the service at a time. This example would enable a hard concurrency limit of 50 requests.

* Optional: Use the `kn service` command to specify the `--concurrency-limit` flag:
+
[source,terminal]
----
$ kn service create <service_name> --image <image_uri> --concurrency-limit <integer>
----
+
.Example command to create a service with a concurrency limit of 50 requests
[source,terminal]
----
$ kn service create example-service --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest --concurrency-limit 50
----
