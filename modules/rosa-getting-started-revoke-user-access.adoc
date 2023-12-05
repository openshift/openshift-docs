// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-getting-started-revoke-user-access_{context}"]
= Revoking user access to a cluster

ifeval::["{context}" == "rosa-getting-started"]
:getting-started:
endif::[]
ifeval::["{context}" == "rosa-quickstart"]
:quickstart:
endif::[]

You can revoke cluster access for an identity provider user by removing them from your configured identity provider.

You can configure different types of identity providers for your ROSA cluster. The following example procedure revokes cluster access for a member of a GitHub organization that is configured for identity provision to the cluster.

ifdef::getting-started[]
.Prerequisites

* You have a ROSA cluster.
* You have a GitHub user account.
* You have configured a GitHub identity provider for your cluster and added an identity provider user.
endif::[]

.Procedure

. Navigate to link:https://github.com[github.com] and log in to your GitHub account.

. Remove the user from your GitHub organization. Follow the steps in link:https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization[Removing a member from your organization] in the GitHub documentation.

ifeval::["{context}" == "rosa-getting-started"]
:getting-started:
endif::[]
ifeval::["{context}" == "rosa-quickstart"]
:quickstart:
endif::[]