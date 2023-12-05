// Module included in the following assemblies:
//
// * networking/ingress-controller-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-autoscaling-ingress-controller_{context}"]
= Autoscaling an Ingress Controller

Automatically scale an Ingress Controller to dynamically meet routing performance or availability requirements such as the requirement to increase throughput. The following procedure provides an example for scaling up the default `IngressController`.

.Prerequisites
. You have the OpenShift CLI (`oc`) installed.
. You have access to an {product-title} cluster as a user with the `cluster-admin` role.
. You have the Custom Metrics Autoscaler Operator installed.
. You are in the `openshift-ingress-operator` project namespace.

.Procedure

. Create a service account to authenticate with Thanos by running the following command:
+
[source,terminal]
----
$ oc create serviceaccount thanos && oc describe serviceaccount thanos
----
+
.Example output
[source,terminal]
----
Name:                thanos
Namespace:           openshift-ingress-operator
Labels:              <none>
Annotations:         <none>
Image pull secrets:  thanos-dockercfg-b4l9s
Mountable secrets:   thanos-dockercfg-b4l9s
Tokens:              thanos-token-c422q
Events:              <none>
----

. Define a `TriggerAuthentication` object within the `openshift-ingress-operator` namespace using the service account's token.

.. Define the variable `secret` that contains the secret by running the following command:
+
[source,terminal]
----
$ secret=$(oc get secret | grep thanos-token | head -n 1 | awk '{ print $1 }')
----

.. Create the `TriggerAuthentication` object and pass the value of the `secret` variable to the `TOKEN` parameter:
+
[source,terminal]
----
$ oc process TOKEN="$secret" -f - <<EOF | oc apply -f -
apiVersion: template.openshift.io/v1
kind: Template
parameters:
- name: TOKEN
objects:
- apiVersion: keda.sh/v1alpha1
  kind: TriggerAuthentication
  metadata:
    name: keda-trigger-auth-prometheus
  spec:
    secretTargetRef:
    - parameter: bearerToken
      name: \${TOKEN}
      key: token
    - parameter: ca
      name: \${TOKEN}
      key: ca.crt
EOF
----

. Create and apply a role for reading metrics from Thanos:

.. Create a new role, `thanos-metrics-reader.yaml`, that reads metrics from pods and nodes:
+
.thanos-metrics-reader.yaml
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: thanos-metrics-reader
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - nodes
  verbs:
  - get
- apiGroups:
  - metrics.k8s.io
  resources:
  - pods
  - nodes
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - namespaces
  verbs:
  - get
----

.. Apply the new role by running the following command:
+
[source,terminal]
----
$ oc apply -f thanos-metrics-reader.yaml
----

. Add the new role to the service account by entering the following commands:
+
[source,terminal]
----
$ oc adm policy add-role-to-user thanos-metrics-reader -z thanos --role-namespace=openshift-ingress-operator
----
+
[source,terminal]
----
$ oc adm policy -n openshift-ingress-operator add-cluster-role-to-user cluster-monitoring-view -z thanos
----
+
[NOTE]
====
The argument `add-cluster-role-to-user` is only required if you use cross-namespace queries. The following step uses a query from the `kube-metrics` namespace which requires this argument.
====

. Create a new `ScaledObject` YAML file, `ingress-autoscaler.yaml`, that targets the default Ingress Controller deployment:
+
.Example `ScaledObject` definition
[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: ingress-scaler
spec:
  scaleTargetRef: <1>
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    name: default
    envSourceContainerName: ingress-operator
  minReplicaCount: 1
  maxReplicaCount: 20 <2>
  cooldownPeriod: 1
  pollingInterval: 1
  triggers:
  - type: prometheus
    metricType: AverageValue
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9091 <3>
      namespace: openshift-ingress-operator <4>
      metricName: 'kube-node-role'
      threshold: '1'
      query: 'sum(kube_node_role{role="worker",service="kube-state-metrics"})' <5>
      authModes: "bearer"
    authenticationRef:
      name: keda-trigger-auth-prometheus
----
<1> The custom resource that you are targeting. In this case, the Ingress Controller.
<2> Optional: The maximum number of replicas. If you omit this field, the default maximum is set to 100 replicas.
<3> The Thanos service endpoint in the `openshift-monitoring` namespace.
<4> The Ingress Operator namespace.
<5> This expression evaluates to however many worker nodes are present in the deployed cluster.
+
[IMPORTANT]
====
If you are using cross-namespace queries, you must target port 9091 and not port 9092 in the `serverAddress` field. You also must have elevated privileges to read metrics from this port.
====

. Apply the custom resource definition by running the following command:
+
[source,terminal]
----
$ oc apply -f ingress-autoscaler.yaml
----

.Verification
* Verify that the default Ingress Controller is scaled out to match the value returned by the `kube-state-metrics` query by running the following commands:

** Use the `grep` command to search the Ingress Controller YAML file for replicas:
+
[source,terminal]
----
$ oc get ingresscontroller/default -o yaml | grep replicas:
----
+
.Example output
[source,terminal]
----
replicas: 3
----

** Get the pods in the `openshift-ingress` project:
+
[source,terminal]
----
$ oc get pods -n openshift-ingress
----
+
.Example output
[source,terminal]
----
NAME                             READY   STATUS    RESTARTS   AGE
router-default-7b5df44ff-l9pmm   2/2     Running   0          17h
router-default-7b5df44ff-s5sl5   2/2     Running   0          3d22h
router-default-7b5df44ff-wwsth   2/2     Running   0          66s
----
