// Module included in the following assemblies
//
// * /serverless/serverless-release-notes.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-rn-1-28-0_{context}"]
= Release notes for Red Hat {ServerlessProductName} 1.28

{ServerlessProductName} 1.28 is now available. New features, changes, and known issues that pertain to {ServerlessProductName} on {product-title} are included in this topic.

[id="new-features-1-28-0_{context}"]
== New features

* {ServerlessProductName} now uses Knative Serving 1.7.
* {ServerlessProductName} now uses Knative Eventing 1.7.
* {ServerlessProductName} now uses Kourier 1.7.
* {ServerlessProductName} now uses Knative (`kn`) CLI 1.7.
* {ServerlessProductName} now uses Knative broker implementation for Apache Kafka 1.7.
* The `kn func` CLI plug-in now uses `func` 1.9.1 version.

* Node.js and TypeScript runtimes for {ServerlessProductName} Functions are now Generally Available (GA).

* Python runtime for {ServerlessProductName} Functions is now available as a Technology Preview.

* Multi-container support for Knative Serving is now available as a Technology Preview. This feature allows you to use a single Knative service to deploy a multi-container pod.

* In {ServerlessProductName} 1.29 or later, the following components of Knative Eventing will be scaled down from two pods to one:
+
--
* `imc-controller`
* `imc-dispatcher`
* `mt-broker-controller`
* `mt-broker-filter`
* `mt-broker-ingress`
--

* The `serverless.openshift.io/enable-secret-informer-filtering` annotation for the Serving CR is now deprecated. The annotation is valid only for Istio, and not for Kourier.
+
With {ServerlessProductName} 1.28, the {ServerlessOperatorName} allows injecting the environment variable `ENABLE_SECRET_INFORMER_FILTERING_BY_CERT_UID` for both `net-istio` and `net-kourier`.
+
If you enable secret filtering, all of your secrets need to be labeled with  `networking.internal.knative.dev/certificate-uid: "<id>"`. Otherwise, Knative Serving does not detect them, which leads to failures. You must label both new and existing secrets.
+
In one of the following {ServerlessProductName} releases, secret filtering will become enabled by default. To prevent failures, label your secrets in advance.

[id="known-issues-1-28-0_{context}"]
== Known issues

* Currently, runtimes for Python are not supported for {ServerlessProductName} Functions on {ibm-power-name}, {ibm-z-name} Systems, and {ibm-linuxone-name}.
+
Node.js, TypeScript, and Quarkus functions are supported on these architectures.

* On the Windows platform, Python functions cannot be locally built, run, or deployed using the Source-to-Image builder due to the `app.sh` file permissions.
+
To work around this problem, use the Windows Subsystem for Linux.
