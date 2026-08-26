// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc
// * networking/routes/route-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-route-admission-policy_{context}"]
= Configuring the route admission policy

Administrators and application developers can run applications in multiple namespaces with the same domain name. This is for organizations where multiple teams develop microservices that are exposed on the same hostname.

[WARNING]
====
Allowing claims across namespaces should only be enabled for clusters with trust between namespaces, otherwise a malicious user could take over a hostname. For this reason, the default admission policy disallows hostname claims across namespaces.
====

.Prerequisites

* Cluster administrator privileges.

.Procedure

* Edit the `.spec.routeAdmission` field of the `ingresscontroller` resource variable using the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default --patch '{"spec":{"routeAdmission":{"namespaceOwnership":"InterNamespaceAllowed"}}}' --type=merge
----
+
.Sample Ingress Controller configuration
[source,yaml]
----
spec:
  routeAdmission:
    namespaceOwnership: InterNamespaceAllowed
...
----
+
[TIP]
====
You can alternatively apply the following YAML to configure the route admission policy:
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  routeAdmission:
    namespaceOwnership: InterNamespaceAllowed
----
====
