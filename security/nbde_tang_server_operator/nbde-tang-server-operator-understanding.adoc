:_mod-docs-content-type: ASSEMBLY
[id="understanding-nbde-tang-server-operator"]
= Understanding the NBDE Tang Server Operator
include::_attributes/common-attributes.adoc[]
:context: understanding-nbde-tang-server-operator

toc::[]

You can use the NBDE Tang Server Operator to automate the deployment of a Tang server in an {product-title} cluster that requires Network Bound Disk Encryption (NBDE) internally, leveraging the tools that {product-title} provides to achieve this automation.

The NBDE Tang Server Operator simplifies the installation process and uses native features provided by the {product-title} environment, such as multi-replica deployment, scaling, traffic load balancing, and so on. The Operator also provides automation of certain operations that are error-prone when you perform them manually, for example:

* server deployment and configuration
* key rotation
* hidden keys deletion

The NBDE Tang Server Operator is implemented using the Operator SDK and allows the deployment of one or more Tang servers in OpenShift through custom resource definitions (CRDs).


[id="understanding-nbde-tang-server-operator_additional-resources"]
[role="_additional-resources"]
== Additional resources
* link:https://cloud.redhat.com/blog/tang-operator-providing-nbde-in-openshift[Tang-Operator: Providing NBDE in OpenShift] Red Hat Hybrid Cloud blog article
* link:https://github.com/latchset/tang-operator[tang-operator] Github project
* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening[Configuring automated unlocking of encrypted volumes using policy-based decryption] chapter in the RHEL 9 Security hardening document

