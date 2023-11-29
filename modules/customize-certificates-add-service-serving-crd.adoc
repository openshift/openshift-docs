// Module included in the following assemblies:
//
// * security/certificates/service-serving-certificate.adoc

:_mod-docs-content-type: PROCEDURE
[id="add-service-certificate-crd_{context}"]
= Add the service CA bundle to a custom resource definition

You can annotate a `CustomResourceDefinition` (CRD) object with `service.beta.openshift.io/inject-cabundle=true` to have its `spec.conversion.webhook.clientConfig.caBundle` field populated with the service CA bundle. This allows the Kubernetes API server to validate the service CA certificate used to secure the targeted endpoint.

[NOTE]
====
The service CA bundle will only be injected into the CRD if the CRD is configured to use a webhook for conversion. It is only useful to inject the service CA bundle if a CRD's webhook is secured with a service CA certificate.
====

.Procedure

. Annotate the CRD with `service.beta.openshift.io/inject-cabundle=true`:
+
[source,terminal]
----
$ oc annotate crd <crd_name> \//<1>
     service.beta.openshift.io/inject-cabundle=true
----
<1> Replace `<crd_name>` with the name of the CRD to annotate.
+
For example, use the following command to annotate the CRD `test1`:
+
[source,terminal]
----
$ oc annotate crd test1 service.beta.openshift.io/inject-cabundle=true
----

. View the CRD to ensure that the service CA bundle has been injected:
+
[source,terminal]
----
$ oc get crd <crd_name> -o yaml
----
+
The CA bundle is displayed in the `spec.conversion.webhook.clientConfig.caBundle` field in the YAML output:
+
[source,terminal]
----
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    service.beta.openshift.io/inject-cabundle: "true"
...
spec:
  conversion:
    strategy: Webhook
    webhook:
      clientConfig:
        caBundle: <CA_BUNDLE>
...
----
