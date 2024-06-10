// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-config.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-security-mtls-sidecars-outgoing_{context}"]
== Configuring sidecars for outgoing connections

Create a destination rule to configure {SMProductShortName} to use mTLS when sending requests to other services in the mesh.

.Procedure

. Create a YAML file using the following example.
+
.DestinationRule example destination-rule.yaml
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: default
  namespace: <namespace>
spec:
  host: "*.<namespace>.svc.cluster.local"
  trafficPolicy:
   tls:
    mode: ISTIO_MUTUAL
----
+
.. Replace `<namespace>` with the namespace where the service is located.

. Run the following command to create the resource in the namespace where the service is located. It must match the `namespace` field in the `DestinationRule` resource you just created.
+
[source,terminal]
----
$ oc create -n <namespace> -f <destination-rule.yaml>
----
