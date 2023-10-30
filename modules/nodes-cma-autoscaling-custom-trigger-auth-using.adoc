// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-trigger-auth.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cma-autoscaling-custom-trigger-auth-using_{context}"]
= Using trigger authentications

You use trigger authentications and cluster trigger authentications by using a custom resource to create the authentication,  then add a reference to a scaled object or scaled job.

.Prerequisites

* The Custom Metrics Autoscaler Operator must be installed.

* If you are using a secret, the `Secret` object must exist, for example:
+
.Example secret
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
data:
  user-name: <base64_USER_NAME>
  password: <base64_USER_PASSWORD>
----

.Procedure

. Create the `TriggerAuthentication` or  `ClusterTriggerAuthentication` object.

.. Create a YAML file that defines the object:
+
.Example trigger authentication with a secret
[source,yaml]
----
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: prom-triggerauthentication
  namespace: my-namespace
spec:
  secretTargetRef:
  - parameter: user-name
    name: my-secret
    key: USER_NAME
  - parameter: password
    name: my-secret
    key: USER_PASSWORD
----

.. Create the `TriggerAuthentication` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. Create or edit a `ScaledObject` YAML file that uses the trigger authentication:

.. Create a YAML file that defines the object by running the following command:
+
.Example scaled object with a trigger authentication
[source,yaml,options="nowrap"]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: scaledobject
  namespace: my-namespace
spec:
  scaleTargetRef:
    name: example-deployment
  maxReplicaCount: 100
  minReplicaCount: 0
  pollingInterval: 30
  triggers:
  - type: prometheus
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest # replace <NAMESPACE>
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: "basic"
    authenticationRef:
      name: prom-triggerauthentication <1>
      kind: TriggerAuthentication <2>
----
<1> Specify the name of your trigger authentication object.
<2> Specify `TriggerAuthentication`. `TriggerAuthentication` is the default.
+
.Example scaled object with a cluster trigger authentication
[source,yaml,options="nowrap"]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: scaledobject
  namespace: my-namespace
spec:
  scaleTargetRef:
    name: example-deployment
  maxReplicaCount: 100
  minReplicaCount: 0
  pollingInterval: 30
  triggers:
  - type: prometheus
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest # replace <NAMESPACE>
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: "basic"
    authenticationRef:
      name: prom-cluster-triggerauthentication <1>
      kind: ClusterTriggerAuthentication <2>
----
<1> Specify the name of your trigger authentication object.
<2> Specify `ClusterTriggerAuthentication`.

.. Create the scaled object by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>
----
