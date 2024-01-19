// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-controller-status_{context}"]
= View Ingress Controller status

Your can view the status of a particular Ingress Controller.

.Procedure

* View the status of an Ingress Controller:
+
[source,terminal]
----
$ oc describe --namespace=openshift-ingress-operator ingresscontroller/<name>
----
