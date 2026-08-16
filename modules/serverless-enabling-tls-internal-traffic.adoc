// Module included in the following assemblies:
//
// * /serverless/security/serverless-config-tls.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-enabling-tls-internal-traffic_{context}"]
= Enabling TLS authentication for internal traffic

{ServerlessProductName} supports TLS edge termination by default, so that HTTPS traffic from end users is encrypted. However, internal traffic behind the OpenShift route is forwarded to applications by using plain data. By enabling TLS for internal traffic, the traffic sent between components is encrypted, which makes this traffic more secure.

[NOTE]
====
If you want to enable internal TLS with a {SMProductName} integration, you must enable {SMProductShortName} with mTLS instead of the internal encryption explained in the following procedure.
====

:FeatureName: Internal TLS encryption support
include::snippets/technology-preview.adoc[]

.Prerequisites

* You have installed the {ServerlessOperatorName} and Knative Serving.
* You have installed the OpenShift (`oc`) CLI.

.Procedure

. Create a Knative service that includes the `internal-encryption: "true"` field in the spec:
+
[source,yaml]
----
...
spec:
  config:
    network:
      internal-encryption: "true"
...
----

. Restart the activator pods in the `knative-serving` namespace to load the certificates:
+
[source,terminal]
----
$ oc delete pod -n knative-serving --selector app=activator
----
