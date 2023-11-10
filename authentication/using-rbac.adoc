:_mod-docs-content-type: ASSEMBLY
[id="using-rbac"]
= Using RBAC to define and apply permissions
include::_attributes/common-attributes.adoc[]
:context: using-rbac

toc::[]

include::modules/rbac-overview.adoc[leveloffset=+1]

include::modules/rbac-projects-namespaces.adoc[leveloffset=+1]

include::modules/rbac-default-projects.adoc[leveloffset=+1]

include::modules/rbac-viewing-cluster-roles.adoc[leveloffset=+1]

include::modules/rbac-viewing-local-roles.adoc[leveloffset=+1]

include::modules/rbac-adding-roles.adoc[leveloffset=+1]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin,openshift-dedicated,openshift-rosa[]
include::modules/rbac-creating-local-role.adoc[leveloffset=+1]

include::modules/rbac-creating-cluster-role.adoc[leveloffset=+1]
endif::[]

include::modules/rbac-local-role-binding-commands.adoc[leveloffset=+1]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin,openshift-dedicated,openshift-rosa[]
include::modules/rbac-cluster-role-binding-commands.adoc[leveloffset=+1]
endif::[]

ifndef::openshift-dedicated,openshift-rosa[]
include::modules/rbac-creating-cluster-admin.adoc[leveloffset=+1]
endif::openshift-dedicated,openshift-rosa[]

ifdef::openshift-rosa[]
include::modules/rosa-create-cluster-admins.adoc[leveloffset=+1]
include::modules/rosa-create-dedicated-cluster-admins.adoc[leveloffset=+1]
endif::openshift-rosa[]

ifdef::openshift-dedicated[]
include::modules/osd-grant-admin-privileges.adoc[leveloffset=+1]
endif::openshift-dedicated[]
