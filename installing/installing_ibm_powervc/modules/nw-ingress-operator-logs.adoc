// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-operator-logs_{context}"]
= View Ingress Controller logs

You can view your Ingress Controller logs.

.Procedure

* View your Ingress Controller logs:
+
[source,terminal]
----
$ oc logs --namespace=openshift-ingress-operator deployments/ingress-operator -c <container_name>
----
