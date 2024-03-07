:_mod-docs-content-type: ASSEMBLY
[id="ldap-syncing"]
= Syncing LDAP groups
include::_attributes/common-attributes.adoc[]
:context: ldap-syncing-groups

toc::[]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
As an administrator,
endif::[]
ifdef::openshift-dedicated,openshift-rosa[]
As an administrator with the `dedicated-admin` role,
endif::openshift-dedicated,openshift-rosa[]
you can use groups to manage users, change
their permissions, and enhance collaboration. Your organization may have already
created user groups and stored them in an LDAP server. {product-title} can sync
those LDAP records with internal {product-title} records, enabling you to manage
your groups in one place. {product-title} currently supports group sync with
LDAP servers using three common schemas for defining group membership: RFC 2307,
Active Directory, and augmented Active Directory.

ifndef::openshift-dedicated,openshift-rosa[]
For more information on configuring LDAP, see
xref:../authentication/identity_providers/configuring-ldap-identity-provider.adoc#configuring-ldap-identity-provider[Configuring an LDAP identity provider].
endif::openshift-dedicated,openshift-rosa[]

ifdef::openshift-dedicated,openshift-rosa[]
For more information on configuring LDAP, see
xref:../authentication/sd-configuring-identity-providers.adoc#config-ldap-idp_sd-configuring-identity-providers[Configuring an LDAP identity provider].
endif::openshift-dedicated,openshift-rosa[]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
[NOTE]
====
You must have `cluster-admin` privileges to sync groups.
====
endif::[]
ifdef::openshift-dedicated,openshift-rosa[]
[NOTE]
====
You must have `dedicated-admin` privileges to sync groups.
====
endif::openshift-dedicated,openshift-rosa[]

include::modules/ldap-syncing-about.adoc[leveloffset=+1]
include::modules/ldap-syncing-config-rfc2307.adoc[leveloffset=+2]
include::modules/ldap-syncing-config-activedir.adoc[leveloffset=+2]
include::modules/ldap-syncing-config-augmented-activedir.adoc[leveloffset=+2]
include::modules/ldap-syncing-running.adoc[leveloffset=+1]
include::modules/ldap-syncing-running-all-ldap.adoc[leveloffset=+2]
include::modules/ldap-syncing-running-openshift.adoc[leveloffset=+2]
include::modules/ldap-syncing-running-subset.adoc[leveloffset=+2]
include::modules/ldap-syncing-pruning.adoc[leveloffset=+1]

// OSD and ROSA dedicated-admins cannot create the cluster roles and cluster role bindings required for this procedure.
ifndef::openshift-dedicated,openshift-rosa[]
// Automatically syncing LDAP groups
include::modules/ldap-auto-syncing.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../authentication/identity_providers/configuring-ldap-identity-provider.adoc#configuring-ldap-identity-provider[Configuring an LDAP identity provider]
* xref:../nodes/jobs/nodes-nodes-jobs.adoc#nodes-nodes-jobs-creating-cron_nodes-nodes-jobs[Creating cron jobs]
endif::openshift-dedicated,openshift-rosa[]

include::modules/ldap-syncing-examples.adoc[leveloffset=+1]
include::modules/ldap-syncing-rfc2307.adoc[leveloffset=+2]
include::modules/ldap-syncing-rfc2307-user-defined.adoc[leveloffset=+2]
include::modules/ldap-syncing-rfc2307-user-defined-error.adoc[leveloffset=+2]
include::modules/ldap-syncing-activedir.adoc[leveloffset=+2]
include::modules/ldap-syncing-augmented-activedir.adoc[leveloffset=+2]
include::modules/ldap-syncing-nesting.adoc[leveloffset=+2]
include::modules/ldap-syncing-spec.adoc[leveloffset=+1]
