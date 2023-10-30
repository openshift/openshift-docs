// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cma-autoscaling-custom-prometheus-config_{context}"]
= Configuring the custom metrics autoscaler to use {product-title} monitoring

You can use the installed {product-title} Prometheus monitoring as a source for the metrics used by the custom metrics autoscaler. However, there are some additional configurations you must perform.

[NOTE]
====
These steps are not required for an external Prometheus source.
====

You must perform the following tasks, as described in this section:

* Create a service account to get a token.
* Create a role.
* Add that role to the service account.
* Reference the token in the trigger authentication object used by Prometheus.

.Prerequisites

* {product-title} monitoring must be installed.

* Monitoring of user-defined workloads must be enabled in {product-title} monitoring, as described in the *Creating a user-defined workload monitoring config map* section.

* The Custom Metrics Autoscaler Operator must be installed.

.Procedure

. Change to the project with the object you want to scale:
+
[source,terminal]
----
$ oc project my-project
----

. Use the following command to create a service account, if your cluster does not have one:
+
[source,terminal]
----
$ oc create serviceaccount <service_account>
----
+
where:
+
<service_account>:: Specifies the name of the service account.

. Use the following command to locate the token assigned to the service account:
+
[source,terminal]
----
$ oc describe serviceaccount <service_account>
----
+
--
where:

<service_account>:: Specifies the name of the service account.
--
+
.Example output
[source,terminal]
----
Name:                thanos
Namespace:           my-project
Labels:              <none>
Annotations:         <none>
Image pull secrets:  thanos-dockercfg-nnwgj
Mountable secrets:   thanos-dockercfg-nnwgj
Tokens:              thanos-token-9g4n5 <1>
Events:              <none>

----
<1> Use this token in the trigger authentication.

. Create a trigger authentication with the service account token:

.. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-prometheus
spec:
  secretTargetRef: <1>
  - parameter: bearerToken <2>
    name: thanos-token-9g4n5 <3>
    key: token <4>
  - parameter: ca
    name: thanos-token-9g4n5
    key: ca.crt
----
<1> Specifies that this object uses a secret for authorization.
<2> Specifies the authentication parameter to supply by using the token.
<3> Specifies the name of the token to use.
<4> Specifies the key in the token to use with the specified parameter.

.. Create the CR object:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

. Create a role for reading Thanos metrics:
+
.. Create a YAML file with the following parameters:
+
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
----

.. Create the CR object:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

. Create a role binding for reading Thanos metrics:
+
.. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: thanos-metrics-reader <1>
  namespace: my-project <2>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: thanos-metrics-reader
subjects:
- kind: ServiceAccount
  name: thanos <3>
  namespace: my-project <4>
----
<1> Specifies the name of the role you created.
<2> Specifies the namespace of the object you want to scale.
<3> Specifies the name of the service account to bind to the role.
<4> Specifies the namespace of the object you want to scale.
.. Create the CR object:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

You can now deploy a scaled object or scaled job to enable autoscaling for your application, as described in "Understanding how to add custom metrics autoscalers". To use {product-title} monitoring as the source, in the trigger, or scaler, you must include the following parameters:

* `triggers.type` must be `prometheus`
* `triggers.metadata.serverAddress` must be `\https://thanos-querier.openshift-monitoring.svc.cluster.local:9092`
* `triggers.metadata.authModes` must be `bearer`
* `triggers.metadata.namespace` must be set to the namespace of the object to scale
* `triggers.authenticationRef` must point to the trigger authentication resource specified in the previous step

