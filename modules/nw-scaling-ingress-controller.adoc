// Module filename: nw-scaling-ingress-controller.adoc
// Module included in the following assemblies:
// * networking/ingress-controller-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-controller-configuration_{context}"]
= Scaling an Ingress Controller

Manually scale an Ingress Controller to meeting routing performance or
availability requirements such as the requirement to increase throughput. `oc`
commands are used to scale the `IngressController` resource. The following
procedure provides an example for scaling up the default `IngressController`.

[NOTE]
====
Scaling is not an immediate action, as it takes time to create the desired number of replicas.
====

.Procedure
. View the current number of available replicas for the default `IngressController`:
+
[source,terminal]
----
$ oc get -n openshift-ingress-operator ingresscontrollers/default -o jsonpath='{$.status.availableReplicas}'
----
+
.Example output
[source,terminal]
----
2
----

. Scale the default `IngressController` to the desired number of replicas using
the `oc patch` command. The following example scales the default `IngressController`
to 3 replicas:
+
[source,terminal]
----
$ oc patch -n openshift-ingress-operator ingresscontroller/default --patch '{"spec":{"replicas": 3}}' --type=merge
----
+
.Example output
[source,terminal]
----
ingresscontroller.operator.openshift.io/default patched
----

. Verify that the default `IngressController` scaled to the number of replicas
that you specified:
+
[source,terminal]
----
$ oc get -n openshift-ingress-operator ingresscontrollers/default -o jsonpath='{$.status.availableReplicas}'
----
+
.Example output
[source,terminal]
----
3
----
+
[TIP]
====
You can alternatively apply the following YAML to scale an Ingress Controller to three replicas:
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 3               <1>
----
====
<1> If you need a different amount of replicas, change the `replicas` value.
