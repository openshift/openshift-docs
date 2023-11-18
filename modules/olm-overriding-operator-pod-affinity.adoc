// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-node-affinity.adoc
// * nodes/scheduling/nodes-scheduler-pod-affinity.adoc
// * operators/admin/olm-adding-operators-to-cluster.adoc

ifeval::["{context}" == "nodes-scheduler-pod-affinity"]
:pod:
endif::[]
ifeval::["{context}" == "nodes-scheduler-node-affinity"]
:node:
endif::[]
ifeval::["{context}" == "olm-adding-operators-to-a-cluster"]
:olm:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="olm-overriding-operator-pod-affinity_{context}"]

ifdef::olm[]
= Controlling where an Operator is installed
endif::olm[]

ifdef::pod[]
= Using pod affinity and anti-affinity to control where an Operator is installed
endif::pod[]

ifdef::node[]
= Using node affinity to control where an Operator is installed
endif::node[]

By default, when you install an Operator, {product-title} installs the Operator pod to one of your worker nodes randomly. However, there might be situations where you want that pod scheduled on a specific node or set of nodes.

The following examples describe situations where you might want to schedule an Operator pod to a specific node or set of nodes:

ifndef::openshift-dedicated,openshift-rosa[]
* If an Operator requires a particular platform, such as `amd64` or `arm64`
* If an Operator requires a particular operating system, such as Linux or Windows
endif::openshift-dedicated,openshift-rosa[]
* If you want Operators that work together scheduled on the same host or on hosts located on the same rack
* If you want Operators dispersed throughout the infrastructure to avoid downtime due to network or hardware issues

ifdef::olm[]
You can control where an Operator pod is installed by adding node affinity, pod affinity, or pod anti-affinity constraints to the Operator's `Subscription` object. Node affinity is a set of rules used by the scheduler to determine where a pod can be placed. Pod affinity enables you to ensure that related pods are scheduled to the same node. Pod anti-affinity allows you to prevent a pod from being scheduled on a node.
endif::olm[]

ifdef::pod[]
You can control where an Operator pod is installed by adding a pod affinity or anti-affinity to the Operator's `Subscription` object.
endif::pod[]

ifdef::node[]
You can control where an Operator pod is installed by adding a node affinity constraints to the Operator's `Subscription` object.
endif::node[]

ifdef::olm[]
The following examples show how to use node affinity or pod anti-affinity to install an instance of the Custom Metrics Autoscaler Operator to a specific node in the cluster:
endif::olm[]
ifdef::node[]
The following examples show how to use node affinity to install an instance of the Custom Metrics Autoscaler Operator to a specific node in the cluster:
endif::node[]

ifndef::pod[]
.Node affinity example that places the Operator pod on a specific node
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity: <1>
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
              - ip-10-0-163-94.us-west-2.compute.internal
#...
----
<1> A node affinity that requires the Operator's pod to be scheduled on a node named `ip-10-0-163-94.us-west-2.compute.internal`.

.Node affinity example that places the Operator pod on a node with a specific platform
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      nodeAffinity: <1>
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/arch
              operator: In
              values:
              - arm64
            - key: kubernetes.io/os
              operator: In
              values:
              - linux
#...
----
<1> A node affinity that requires the Operator's pod to be scheduled on a node with the `kubernetes.io/arch=arm64` and `kubernetes.io/os=linux` labels.
endif::pod[]

ifdef::pod[]
The following example shows how to use pod anti-affinity to prevent the installation the Custom Metrics Autoscaler Operator from any node that has pods with a specific label:
endif::pod[]

ifndef::node[]
.Pod affinity example that places the Operator pod on one or more specific nodes
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAffinity: <1>
        requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values:
              - test
          topologyKey: kubernetes.io/hostname
#...
----
<1> A pod affinity that places the Operator's pod on a node that has pods with the `app=test` label.

.Pod anti-affinity example that prevents the Operator pod from one or more specific nodes
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAntiAffinity: <1>
        requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
            - key: cpu
              operator: In
              values:
              - high
          topologyKey: kubernetes.io/hostname
#...
----
<1> A pod anti-affinity that prevents the Operator's pod from being scheduled on a node that has pods with the `cpu=high` label.
endif::node[]

.Procedure

To control the placement of an Operator pod, complete the following steps:

. Install the Operator as usual.

. If needed, ensure that your nodes are labeled to properly respond to the affinity.

. Edit the Operator `Subscription` object to add an affinity:
+
ifndef::pod[]
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity: <1>
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
              - ip-10-0-185-229.ec2.internal
#...
----
ifdef::olm[]
<1> Add a `nodeAffinity`, `podAffinity`, or `podAntiAffinity`. See the Additional resources section that follows for information about creating the affinity.
endif::[]
ifdef::node[]
<1> Add a `nodeAffinity`.
endif::[]
endif::pod[]
ifdef::pod[]
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-custom-metrics-autoscaler-operator
  namespace: openshift-keda
spec:
  name: my-package
  source: my-operators
  sourceNamespace: operator-registries
  config:
    affinity:
      podAntiAffinity: <1>
        requiredDuringSchedulingIgnoredDuringExecution:
          podAffinityTerm:
            labelSelector:
              matchExpressions:
              - key: kubernetes.io/hostname
                operator: In
                values:
                - ip-10-0-185-229.ec2.internal
            topologyKey: topology.kubernetes.io/zone
#...
----
<1> Add a `podAffinity` or `podAntiAffinity`.
endif::pod[]

.Verification

* To ensure that the pod is deployed on the specific node, run the following command:
+
[source,yaml]
----
$ oc get pods -o wide
----
+
.Example output
+
[source,terminal]
----
NAME                                                  READY   STATUS    RESTARTS   AGE   IP            NODE                           NOMINATED NODE   READINESS GATES
custom-metrics-autoscaler-operator-5dcc45d656-bhshg   1/1     Running   0          50s   10.131.0.20   ip-10-0-185-229.ec2.internal   <none>           <none>
----

ifeval::["{context}" == "nodes-scheduler-pod-affinity"]
:!pod:
endif::[]
ifeval::["{context}" == "nodes-scheduler-node-affinity"]
:!node:
endif::[]
ifeval::["{context}" == "olm-adding-operators-to-a-cluster"]
:!olm:
endif::[]
