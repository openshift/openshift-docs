// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-traffic-manage.adoc
// * service_mesh/v2x/ossm-traffic-manage.adoc
:_mod-docs-content-type: PROCEDURE
[id="ossm-routing-sidecar_{context}"]
= Configuring sidecars for traffic management

By default, {SMProductName} configures every Envoy proxy to accept traffic on all the ports of its associated workload, and to reach every workload in the mesh when forwarding traffic. You can use a sidecar configuration to do the following:

* Fine-tune the set of ports and protocols that an Envoy proxy accepts.
* Limit the set of services that the Envoy proxy can reach.

[NOTE]
====
To optimize performance of your service mesh, consider limiting Envoy proxy configurations.
====

In the Bookinfo sample application, configure a Sidecar so all services can reach other services running in the same namespace and control plane. This Sidecar configuration is required for using {SMProductName} policy and telemetry features.

.Procedure

. Create a YAML file using the following example to specify that you want a sidecar configuration to apply to all workloads in a particular namespace. Otherwise, choose specific workloads using a `workloadSelector`.
+
.Example sidecar.yaml
[source,yaml]
----
apiVersion: networking.istio.io/v1alpha3
kind: Sidecar
metadata:
  name: default
  namespace: bookinfo
spec:
  egress:
  - hosts:
    - "./*"
    - "istio-system/*"
----

. Run the following command to apply `sidecar.yaml`, where `sidecar.yaml` is the path to the file.
+
[source,terminal]
----
$ oc apply -f sidecar.yaml
----

. Run the following command to verify that the sidecar was created successfully.
+
[source,terminal]
----
$ oc get sidecar
----
