// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-policy-responsibility-matrix.adoc

:_mod-docs-content-type: CONCEPT
[id="rosa-policy-responsibilities_{context}"]
= Shared responsibilities for {product-title}


While Red Hat and Amazon Web Services (AWS) manage the {product-title} services, the customer shares certain responsibilities. The {product-title} services are accessed remotely, hosted on public cloud resources, created in customer-owned AWS accounts, and have underlying platform and data security that is owned by Red Hat.

[IMPORTANT]
====
If the `cluster-admin` role is added to a user, see the responsibilities and exclusion notes in the link:https://www.redhat.com/en/about/agreements[Red Hat Enterprise Agreement Appendix 4 (Online Subscription Services)].
====

[cols="2a,3a,3a,3a,3a,3a",options="header"]
|===

|Resource
|Incident and operations management
|Change management
|Access and identity authorization
|Security and regulation compliance
|Disaster recovery

|Customer data |Customer |Customer |Customer |Customer |Customer

|Customer applications |Customer |Customer |Customer |Customer |Customer

|Developer services |Customer |Customer |Customer |Customer |Customer

|Platform monitoring |Red Hat |Red Hat |Red Hat |Red Hat |Red Hat

|Logging |Red Hat |Red Hat and Customer |Red Hat and Customer |Red Hat and Customer |Red Hat

|Application networking |Red Hat and Customer |Red Hat and Customer |Red Hat and Customer |Red Hat |Red Hat

|Cluster networking |Red Hat |Red Hat and Customer |Red Hat and Customer |Red Hat |Red Hat

|Virtual networking management |Red Hat and Customer |Red Hat and Customer |Red Hat and Customer |Red Hat and Customer |Red Hat and Customer

|Virtual compute management (control plane, infrastructure and worker nodes) |Red Hat |Red Hat |Red Hat |Red Hat |Red Hat

|Cluster version |Red Hat |Red Hat and Customer |Red Hat |Red Hat |Red Hat

|Capacity management |Red Hat |Red Hat and Customer |Red Hat |Red Hat |Red Hat

|Virtual storage management |Red Hat |Red Hat |Red Hat |Red Hat |Red Hat

|AWS software (public AWS services) |AWS |AWS
|AWS |AWS |AWS

|Hardware/AWS global infrastructure |AWS |AWS |AWS |AWS |AWS

|===
