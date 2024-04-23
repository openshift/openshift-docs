:_mod-docs-content-type: ASSEMBLY
[id=creating-a-java-application-with-a-database]
= Creating a Java application with a database
include::_attributes/common-attributes.adoc[]
:context: creating-a-java-application-with-a-database
toc::[]

This example describes how to deploy a Java application by using devfile and connect it to a database service.

.Prerequisites

* A running cluster.
* `{odo-title}` is installed.
* A Service Binding Operator is installed in your cluster. To learn how to install Operators, contact your cluster administrator or see xref:../../../operators/user/olm-installing-operators-in-namespace.adoc#olm-installing-operators-from-operatorhub_olm-installing-operators-in-namespace[Installing Operators from OperatorHub].
* A Dev4Devs PostgreSQL Operator Operator is installed in your cluster. To learn how to install Operators, contact your cluster administrator or see xref:../../../operators/user/olm-installing-operators-in-namespace.adoc#olm-installing-operators-from-operatorhub_olm-installing-operators-in-namespace[Installing Operators from OperatorHub].

include::modules/developer-cli-odo-creating-a-project.adoc[leveloffset=+1]

include::modules/developer-cli-odo-creating-a-java-microservice-jpa-application.adoc[leveloffset=+1]

include::modules/developer-cli-odo-creating-a-database-with-odo.adoc[leveloffset=+1]

include::modules/developer-cli-odo-connecting-a-java-application-to-mysql-database.adoc[leveloffset=+1]
