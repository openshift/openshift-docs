// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-config.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-security-enabling-strict-mtls_{context}"]
= Enabling strict mTLS across the service mesh

If your workloads do not communicate with outside services, you can quickly enable mTLS across your mesh without communication interruptions. You can enable it by setting `spec.security.dataPlane.mtls` to `true` in the `ServiceMeshControlPlane` resource. The Operator creates the required resources.

[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
spec:
  version: v{MaistraVersion}
  security:
    dataPlane:
      mtls: true
----

You can also enable mTLS by using the {product-title} web console.

.Procedure

. Log in to the web console.

. Click the *Project* menu and select the project where you installed the {SMProductShortName} control plane, for example *istio-system*.

. Click *Operators* -> *Installed Operators*.

. Click *Service Mesh Control Plane* under *Provided APIs*.

. Click the name of your `ServiceMeshControlPlane` resource, for example, `basic`.

. On the *Details* page, click the toggle in the *Security* section for *Data Plane Security*.
