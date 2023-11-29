// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-security.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-cert-cleanup_{context}"]
== Removing the certificates

To remove the certificates you added, follow these steps.

. Remove the secret `cacerts`. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.
+
[source,terminal]
----
$ oc delete secret cacerts -n istio-system
----
+
. Redeploy {SMProductShortName} with a self-signed root certificate in the `ServiceMeshControlPlane` resource.
+
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
spec:
  security:
    dataPlane:
      mtls: true
----
