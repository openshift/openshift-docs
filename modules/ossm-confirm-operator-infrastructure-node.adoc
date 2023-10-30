// Module included in the following assemblies:
//
// * service_mesh/v2x/installing-ossm.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-confirm-operator-infrastructure-node_{context}"]
= Verifying the {SMProductShortName} Operator is running on infrastructure node

.Procedure

* Verify that the node associated with the Operator pod is an infrastructure node:
+
[source,terminal]
----
$ oc -n openshift-operators get po -l name=istio-operator -owide
----
