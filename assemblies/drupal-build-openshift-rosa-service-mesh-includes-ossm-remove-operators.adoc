// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc
// * service_mesh/v2x/installing-ossm.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-operatorhub-remove-operators_{context}"]
= Removing the installed Operators

You must remove the Operators to successfully remove {SMProductName}. After you remove the {SMProductName} Operator, you must remove the Kiali Operator, the {JaegerName} Operator, and the OpenShift Elasticsearch Operator.

[id="ossm-remove-operator-servicemesh_{context}"]
== Removing the Operators

Follow this procedure to remove the Operators that make up {SMProductName}. Repeat the steps for each of the following Operators.

* {SMProductName}
* Kiali
* {JaegerName}
* OpenShift Elasticsearch

.Procedure

. Log in to the {product-title} web console.

. From the *Operators* → *Installed Operators* page, scroll or type a keyword into the *Filter by name* to find each Operator. Then, click the Operator name.

. On the *Operator Details* page, select *Uninstall Operator* from the *Actions* menu. Follow the prompts to uninstall each Operator.
