:_mod-docs-content-type: ASSEMBLY
:context: nodes-cma-autoscaling-custom-audit-log
[id="nodes-cma-autoscaling-custom-audit-log"]
= Gathering audit logs
include::_attributes/common-attributes.adoc[]

toc::[]

// Text borrowed from gathering-cluster-data.adoc. Make into snippet?

You can gather audit logs, which are a security-relevant chronological set of records documenting the sequence of activities that have affected the system by individual users, administrators, or other components of the system.

For example, audit logs can help you understand where an autoscaling request is coming from. This is key information when backends are getting overloaded by autoscaling requests made by user applications and you need to determine which is the troublesome application.

include::modules/nodes-cma-autoscaling-custom-audit.adoc[leveloffset=+1]
