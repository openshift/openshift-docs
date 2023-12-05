:_mod-docs-content-type: ASSEMBLY
[id="quotas-setting-per-project"]
= Resource quotas per project
include::_attributes/common-attributes.adoc[]
:context: quotas-setting-per-project

toc::[]

A _resource quota_, defined by a `ResourceQuota` object, provides constraints that limit aggregate resource consumption per project. It can limit the quantity of objects that can be created in a project by type, as well as the total amount of compute resources and storage that might be consumed by resources in that project.

This guide describes how resource quotas work, how cluster administrators can set and manage resource quotas on a per project basis, and how developers and cluster administrators can view them.

include::modules/quotas-resources-managed.adoc[leveloffset=+1]
include::modules/quotas-scopes.adoc[leveloffset=+1]
include::modules/quotas-enforcement.adoc[leveloffset=+1]
include::modules/quotas-requests-vs-limits.adoc[leveloffset=+1]
include::modules/quotas-sample-resource-quotas-def.adoc[leveloffset=+1]
include::modules/quotas-creating-a-quota.adoc[leveloffset=+1]
include::modules/quotas-creating-object-count-quotas.adoc[leveloffset=+2]
include::modules/setting-resource-quota-for-extended-resources.adoc[leveloffset=+2]
include::modules/quotas-viewing-quotas.adoc[leveloffset=+1]
include::modules/quotas-requiring-explicit-quota.adoc[leveloffset=+1]
