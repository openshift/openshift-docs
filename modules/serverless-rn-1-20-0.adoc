// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-rn-1-20-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.20.0

{ServerlessProductName} 1.20.0 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on {product-title} are included in this topic.

[id="new-features-1-20-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 0.26.
* {ServerlessProductName} now uses Knative Eventing 0.26.
* {ServerlessProductName} now uses Kourier 0.26.
* {ServerlessProductName} now uses Knative (`kn`) CLI 0.26.
* {ServerlessProductName} now uses Knative Kafka 0.26.
* The `kn func` CLI plugin now uses `func` 0.20.

* The Kafka broker is now available as a Technology Preview.
+
[IMPORTANT]
====
The Kafka broker, which is currently in Technology Preview, is not supported on FIPS.
====

* The `kn event` plugin is now available as a Technology Preview.

* The `--min-scale` and `--max-scale` flags for the `kn service create` command have been deprecated. Use the `--scale-min` and `--scale-max` flags instead.

[id="known-issues-1-20-0_{context}"]
== Known issues

* {ServerlessProductName} deploys Knative services with a default address that uses HTTPS. When sending an event to a resource inside the cluster, the sender does not have the cluster certificate authority (CA) configured. This causes event delivery to fail, unless the cluster uses globally accepted certificates.
+
For example, an event delivery to a publicly accessible address works:
+
[source,terminal]
----
$ kn event send --to-url https://ce-api.foo.example.com/
----
+
On the other hand, this delivery fails if the service uses a public address with an HTTPS certificate issued by a custom CA:
+
[source,terminal]
----
$ kn event send --to Service:serving.knative.dev/v1:event-display
----
+
Sending an event to other addressable objects, such as brokers or channels, is not affected by this issue and works as expected.

* The Kafka broker currently does not work on a cluster with Federal Information Processing Standards (FIPS) mode enabled.

* If you create a Springboot function project directory with the `kn func create` command, subsequent running of the `kn func build` command fails with this error message:
+
[source,terminal]
----
[analyzer] no stack metadata found at path ''
[analyzer] ERROR: failed to : set API for buildpack 'paketo-buildpacks/ca-certificates@3.0.2': buildpack API version '0.7' is incompatible with the lifecycle
----
+
As a workaround, you can change the `builder` property to `gcr.io/paketo-buildpacks/builder:base` in the function configuration file `func.yaml`.

* Deploying a function using the `gcr.io` registry fails with this error message:
+
[source,terminal]
----
Error: failed to get credentials: failed to verify credentials: status code: 404
----
+
As a workaround, use a different registry than `gcr.io`, such as `quay.io` or `docker.io`.

* TypeScript functions created with the `http` template fail to deploy on the cluster.
+
As a workaround, in the `func.yaml` file, replace the following section:
+
[source,terminal]
----
buildEnvs: []
----
+
with this:
+
[source,terminal]
----
buildEnvs:
- name: BP_NODE_RUN_SCRIPTS
  value: build
----

* In `func` version 0.20, some runtimes might be unable to build a function by using podman. You might see an error message similar to the following:
+
[source,terminal]
----
ERROR: failed to image: error during connect: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.40/info": EOF
----
+
** The following workaround exists for this issue:

.. Update the podman service by adding `--time=0` to the service `ExecStart` definition:
+
.Example service configuration
[source,terminal]
----
ExecStart=/usr/bin/podman $LOGGING system service --time=0
----
.. Restart the podman service by running the following commands:
+
[source,terminal]
----
$ systemctl --user daemon-reload
----
+
[source,terminal]
----
$ systemctl restart --user podman.socket
----

** Alternatively, you can expose the podman API by using TCP:
+
[source,terminal]
----
$ podman system service --time=0 tcp:127.0.0.1:5534 &
export DOCKER_HOST=tcp://127.0.0.1:5534
----
