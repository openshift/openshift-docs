:_mod-docs-content-type: ASSEMBLY
[id="working-with-quotas"]
= Working with quotas
include::_attributes/common-attributes.adoc[]
:context: working-with-quotas

toc::[]

A _resource quota_, defined by a ResourceQuota object, provides constraints that
limit aggregate resource consumption per project. It can limit the quantity of
objects that can be created in a project by type, as well as the total amount of
compute resources and storage that may be consumed by resources in that project.

An _object quota count_ places a defined quota on all standard namespaced resource
types. When using a resource quota, an object is charged against the quota if it
exists in server storage. These types of quotas are useful to protect against
exhaustion of storage resources.

This guide describes how resource quotas work and how developers can work with
and view them.

include::modules/quotas-viewing-quotas.adoc[leveloffset=+1]
include::modules/quotas-resources-managed.adoc[leveloffset=+1]
include::modules/quotas-scopes.adoc[leveloffset=+1]
include::modules/quotas-enforcement.adoc[leveloffset=+1]
include::modules/quotas-requests-vs-limits.adoc[leveloffset=+1]
