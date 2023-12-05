:_mod-docs-content-type: ASSEMBLY
[id="installing-ossm"]
= Installing the Operators
include::_attributes/common-attributes.adoc[]
:context: installing-ossm

toc::[]

To install {SMProductName}, first install the required Operators on {product-title} and then create a `ServiceMeshControlPlane` resource to deploy the control plane.

[NOTE]
====
This basic installation is configured based on the default OpenShift settings and is not designed for production use.  Use this default installation to verify your installation, and then configure your service mesh for your specific environment.
====

.Prerequisites
* Read the xref:../../service_mesh/v2x/preparing-ossm-installation.adoc#preparing-ossm-installation[Preparing to install {SMProductName}] process.
ifdef::openshift-rosa[]
* An account with the `cluster-admin` role.
endif::openshift-rosa[]
ifndef::openshift-rosa[]
* An account with the `cluster-admin` role. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.
endif::openshift-rosa[]

The following steps show how to install a basic instance of {SMProductName} on {product-title}.

include::modules/ossm-installation-activities.adoc[leveloffset=+1]

[WARNING]
====
Do not install Community versions of the Operators. Community Operators are not supported.
====

include::modules/ossm-install-ossm-operator.adoc[leveloffset=+1]

ifndef::openshift-rosa[]

include::modules/ossm-config-operator-infrastructure-node.adoc[leveloffset=+1]

include::modules/ossm-confirm-operator-infrastructure-node.adoc[leveloffset=+1]

endif::openshift-rosa[]

== Next steps

* The {SMProductName} Operator does not create the {SMProductShortName} custom resource definitions (CRDs) until you deploy a {SMProductShortName} control plane. You can use the `ServiceMeshControlPlane` resource to install and configure the {SMProductShortName} components. For more information, see xref:../../service_mesh/v2x/ossm-create-smcp.adoc#ossm-create-smcp[Creating the ServiceMeshControlPlane].
