// Module included in the following assemblies
//
// * serverless/admin_guide/serverless-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="knative-serving-controller-custom-certs-secrets_{context}"]
= Configuring tag-to-digest resolution by using a secret

If the `controller-custom-certs` spec uses the `Secret` type, the secret is mounted as a secret volume. Knative components consume the secret directly, assuming that the secret has the required certificates.

.Prerequisites

ifdef::openshift-enterprise[]
* You have cluster administrator permissions on {product-title}.
endif::[]

ifdef::openshift-dedicated,openshift-rosa[]
* You have cluster or dedicated administrator permissions on {product-title}.
endif::[]

* You have installed the {ServerlessOperatorName} and Knative Serving on your cluster.

.Procedure

. Create a secret:
+
.Example command
[source,yaml]
----
$ oc -n knative-serving create secret generic custom-secret --from-file=<secret_name>.crt=<path_to_certificate>
----

. Configure the `controller-custom-certs` spec in the `KnativeServing` custom resource (CR) to use the `Secret` type:
+
.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
  namespace: knative-serving
spec:
  controller-custom-certs:
    name: custom-secret
    type: Secret
----
