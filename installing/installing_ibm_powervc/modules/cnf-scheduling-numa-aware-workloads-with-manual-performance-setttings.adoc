// Module included in the following assemblies:
//
// *scalability_and_performance/cnf-numa-aware-scheduling.adoc

:_mod-docs-content-type: PROCEDURE
[id="cnf-scheduling-numa-aware-workloads-with-manual-performance-setttings_{context}"]
= Scheduling workloads with the NUMA-aware scheduler with manual performance settings

You can schedule workloads with the NUMA-aware scheduler using `Deployment` CRs that specify the minimum required resources to process the workload.

The following example deployment uses NUMA-aware scheduling for a sample workload.

.Prerequisites

* Install the OpenShift CLI (`oc`).

* Log in as a user with `cluster-admin` privileges.

* Install the NUMA Resources Operator and deploy the NUMA-aware secondary scheduler.

.Procedure

. Get the name of the NUMA-aware scheduler that is deployed in the cluster by running the following command:
+
[source,terminal]
----
$ oc get numaresourcesschedulers.nodetopology.openshift.io numaresourcesscheduler -o json | jq '.status.schedulerName'
----
+
.Example output
[source,terminal]
----
topo-aware-scheduler
----

. Create a `Deployment` CR that uses scheduler named `topo-aware-scheduler`, for example:

.. Save the following YAML in the `nro-deployment.yaml` file:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: numa-deployment-1
  namespace: openshift-numaresources
spec:
  replicas: 1
  selector:
    matchLabels:
      app: test
  template:
    metadata:
      labels:
        app: test
    spec:
      schedulerName: topo-aware-scheduler <1>
      containers:
      - name: ctnr
        image: quay.io/openshifttest/hello-openshift:openshift
        imagePullPolicy: IfNotPresent
        resources:
          limits:
            memory: "100Mi"
            cpu: "10"
          requests:
            memory: "100Mi"
            cpu: "10"
      - name: ctnr2
        image: registry.access.redhat.com/rhel:latest
        imagePullPolicy: IfNotPresent
        command: ["/bin/sh", "-c"]
        args: [ "while true; do sleep 1h; done;" ]
        resources:
          limits:
            memory: "100Mi"
            cpu: "8"
          requests:
            memory: "100Mi"
            cpu: "8"
----
<1> `schedulerName` must match the name of the NUMA-aware scheduler that is deployed in your cluster, for example `topo-aware-scheduler`.

.. Create the `Deployment` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nro-deployment.yaml
----

.Verification

. Verify that the deployment was successful:
+
[source,terminal]
----
$ oc get pods -n openshift-numaresources
----
+
.Example output
[source,terminal]
----
NAME                                                READY   STATUS    RESTARTS   AGE
numa-deployment-1-56954b7b46-pfgw8                  2/2     Running   0          129m
numaresources-controller-manager-7575848485-bns4s   1/1     Running   0          15h
numaresourcesoperator-worker-dvj4n                  2/2     Running   0          18h
numaresourcesoperator-worker-lcg4t                  2/2     Running   0          16h
secondary-scheduler-56994cf6cf-7qf4q                1/1     Running   0          18h
----

. Verify that the `topo-aware-scheduler` is scheduling the deployed pod by running the following command:
+
[source,terminal]
----
$ oc describe pod numa-deployment-1-56954b7b46-pfgw8 -n openshift-numaresources
----
+
.Example output
[source,terminal]
----
Events:
  Type    Reason          Age   From                  Message
  ----    ------          ----  ----                  -------
  Normal  Scheduled       130m  topo-aware-scheduler  Successfully assigned openshift-numaresources/numa-deployment-1-56954b7b46-pfgw8 to compute-0.example.com
----
+
[NOTE]
====
Deployments that request more resources than is available for scheduling will fail with a `MinimumReplicasUnavailable` error. The deployment succeeds when the required resources become available. Pods remain in the `Pending` state until the required resources are available.
====

. Verify that the expected allocated resources are listed for the node.

.. Identify the node that is running the deployment pod by running the following command, replacing <namespace> with the namespace you specified in the `Deployment` CR:
+
[source,terminal]
----
$ oc get pods -n <namespace> -o wide
----
+
.Example output
[source,terminal]
----
NAME                                 READY   STATUS    RESTARTS   AGE   IP            NODE     NOMINATED NODE   READINESS GATES
numa-deployment-1-65684f8fcc-bw4bw   0/2     Running   0          82m   10.128.2.50   worker-0   <none>  <none>
----
+
.. Run the following command, replacing <node_name> with the name of that node that is running the deployment pod:
+
[source,terminal]
----
$ oc describe noderesourcetopologies.topology.node.k8s.io <node_name>
----
+
.Example output
[source,terminal]
----
...

Zones:
  Costs:
    Name:   node-0
    Value:  10
    Name:   node-1
    Value:  21
  Name:     node-0
  Resources:
    Allocatable:  39
    Available:    21 <1>
    Capacity:     40
    Name:         cpu
    Allocatable:  6442450944
    Available:    6442450944
    Capacity:     6442450944
    Name:         hugepages-1Gi
    Allocatable:  134217728
    Available:    134217728
    Capacity:     134217728
    Name:         hugepages-2Mi
    Allocatable:  262415904768
    Available:    262206189568
    Capacity:     270146007040
    Name:         memory
  Type:           Node
----
<1> The `Available` capacity is reduced because of the resources that have been allocated to the guaranteed pod.
+
Resources consumed by guaranteed pods are subtracted from the available node resources listed under `noderesourcetopologies.topology.node.k8s.io`.

. Resource allocations for pods with a `Best-effort` or `Burstable` quality of service (`qosClass`) are not reflected in the NUMA node resources under `noderesourcetopologies.topology.node.k8s.io`. If a pod's consumed resources are not reflected in the node resource calculation, verify that the pod has `qosClass` of `Guaranteed` and the CPU request is an integer value, not a decimal value. You can verify the that the pod has a  `qosClass` of `Guaranteed` by running the following command:
+
[source,terminal]
----
$ oc get pod <pod_name> -n <pod_namespace> -o jsonpath="{ .status.qosClass }"
----
+
.Example output
[source,terminal]
----
Guaranteed
----
