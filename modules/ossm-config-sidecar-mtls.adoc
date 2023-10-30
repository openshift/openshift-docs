// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-config.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-security-mtls-sidecars-incoming-services_{context}"]
= Configuring sidecars for incoming connections for specific services

You can also configure mTLS for individual services by creating a policy.

.Procedure

. Create a YAML file using the following example.
+
.PeerAuthentication Policy example policy.yaml
[source,yaml]
----
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: <namespace>
spec:
  mtls:
    mode: STRICT
----
+
.. Replace `<namespace>` with the namespace where the service is located.

. Run the following command to create the resource in the namespace where the service is located. It must match the `namespace` field in the Policy resource you just created.
+
[source,terminal]
----
$ oc create -n <namespace> -f <policy.yaml>
----

[NOTE]
====
If you are not using automatic mTLS and you are setting `PeerAuthentication` to STRICT, you must create a `DestinationRule` resource for your service.
====
