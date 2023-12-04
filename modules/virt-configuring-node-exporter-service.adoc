// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-custom-metrics-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-node-exporter-service_{context}"]
= Configuring the node exporter service

The node-exporter agent is deployed on every virtual machine in the cluster from which you want to collect metrics. Configure the node-exporter agent as a service to expose internal metrics and processes that are associated with virtual machines.

.Prerequisites

* Install the {product-title} CLI `oc`.
* Log in to the cluster as a user with `cluster-admin` privileges.
* Create the `cluster-monitoring-config` `ConfigMap` object in the `openshift-monitoring` project.
* Configure the `user-workload-monitoring-config` `ConfigMap` object in the `openshift-user-workload-monitoring` project by setting `enableUserWorkload` to `true`.

.Procedure

. Create the `Service` YAML file. In the following example, the file is called `node-exporter-service.yaml`.
+
[source,yaml]
----
kind: Service
apiVersion: v1
metadata:
  name: node-exporter-service <1>
  namespace: dynamation <2>
  labels:
    servicetype: metrics <3>
spec:
  ports:
    - name: exmet <4>
      protocol: TCP
      port: 9100 <5>
      targetPort: 9100 <6>
  type: ClusterIP
  selector:
    monitor: metrics <7>
----
<1> The node-exporter service that exposes the metrics from the virtual machines.
<2> The namespace where the service is created.
<3> The label for the service. The `ServiceMonitor` uses this label to match this service.
<4> The name given to the port that exposes metrics on port 9100 for the `ClusterIP` service.
<5> The target port used by `node-exporter-service` to listen for requests.
<6> The TCP port number of the virtual machine that is configured with the `monitor` label.
<7> The label used to match the virtual machine's pods. In this example, any virtual machine's pod with the label `monitor` and a value of `metrics` will be matched.

. Create the node-exporter service:
+
[source,terminal]
----
$ oc create -f node-exporter-service.yaml
----
