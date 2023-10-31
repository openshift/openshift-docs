:_mod-docs-content-type: ASSEMBLY
[id="setting-quotas-across-multiple-projects"]
= Resource quotas across multiple projects
include::_attributes/common-attributes.adoc[]
:context: setting-quotas-across-multiple-projects

toc::[]

A multi-project quota, defined by a `ClusterResourceQuota` object, allows quotas to be shared across multiple projects. Resources used in each selected project are aggregated and that aggregate is used to limit resources across all the selected projects.

This guide describes how cluster administrators can set and manage resource quotas across multiple projects.

include::snippets/default-projects.adoc[]

include::modules/quotas-selecting-projects.adoc[leveloffset=+1]
include::modules/quotas-viewing-clusterresourcequotas.adoc[leveloffset=+1]
include::modules/quotas-selection-granularity.adoc[leveloffset=+1]
