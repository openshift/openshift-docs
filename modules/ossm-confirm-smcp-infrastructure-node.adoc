// Module included in the following assemblies:
//
// * service_mesh/v2x/installing-ossm.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-confirm-smcp-infrastructure-node_{context}"]
= Verifying the {SMProductShortName} control plane is running on infrastructure nodes

.Procedure

* Confirm that the nodes associated with Istiod, Ingress Gateway, and Egress Gateway pods are infrastructure nodes:
+
[source,terminal]
----
$ oc -n istio-system get pods -owide
----
