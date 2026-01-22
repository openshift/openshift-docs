// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-view_{context}"]
= View the default Ingress Controller

The Ingress Operator is a core feature of {product-title} and is enabled out of the
box.

Every new {product-title} installation has an `ingresscontroller` named default. It
can be supplemented with additional Ingress Controllers. If the default
`ingresscontroller` is deleted, the Ingress Operator will automatically recreate it
within a minute.

.Procedure

* View the default Ingress Controller:
+
[source,terminal]
----
$ oc describe --namespace=openshift-ingress-operator ingresscontroller/default
----
