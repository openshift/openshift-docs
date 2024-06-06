// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-getting-started-configure-an-idp_{context}"]
= Configuring an identity provider

ifeval::["{context}" == "rosa-getting-started"]
:getting-started:
endif::[]
ifeval::["{context}" == "rosa-quickstart"]
:quickstart:
endif::[]

You can configure different identity provider types for your {product-title} (ROSA) cluster. Supported types include GitHub, GitHub Enterprise, GitLab, Google, LDAP, OpenID Connect and htpasswd identity providers.

[IMPORTANT]
====
The htpasswd identity provider option is included only to enable the creation of a single, static administration user. htpasswd is not supported as a general-use identity provider for {product-title}.
====

The following procedure configures a GitHub identity provider as an example.

ifdef::getting-started[]
.Prerequisites

* You have an AWS account.
* You installed and configured the latest {product-title} (ROSA) CLI, `rosa`, on your workstation.
* You logged in to your Red Hat account using the ROSA CLI (`rosa`).
* You created a ROSA cluster.
* You have a GitHub user account.
endif::[]

.Procedure

. Go to link:https://github.com[github.com] and log in to your GitHub account.

. If you do not have an existing GitHub organization to use for identity provisioning for your ROSA cluster, create one. Follow the steps in the link:https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch[GitHub documentation].

. Configure a GitHub identity provider for your cluster that is restricted to the members of your GitHub organization.
.. Configure an identity provider using the interactive mode:
+
[source,terminal]
----
$ rosa create idp --cluster=<cluster_name> --interactive <1>
----
<1> Replace `<cluster_name>` with the name of your cluster.
+
.Example output
[source,terminal]
----
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Type of identity provider: github
? Identity provider name: github-1
? Restrict to members of: organizations
? GitHub organizations: <github_org_name> <1>
? To use GitHub as an identity provider, you must first register the application:
  - Open the following URL:
    https://github.com/organizations/<github_org_name>/settings/applications/new?oauth_application%5Bcallback_url%5D=https%3A%2F%2Foauth-openshift.apps.<cluster_name>/<random_string>.p1.openshiftapps.com%2Foauth2callback%2Fgithub-1&oauth_application%5Bname%5D=<cluster_name>&oauth_application%5Burl%5D=https%3A%2F%2Fconsole-openshift-console.apps.<cluster_name>/<random_string>.p1.openshiftapps.com
  - Click on 'Register application'
...
----
<1> Replace `<github_org_name>` with the name of your GitHub organization.
.. Follow the URL in the output and select *Register application* to register a new OAuth application in your GitHub organization. By registering the application, you enable the OAuth server that is built into ROSA to authenticate members of your GitHub organization into your cluster.
+
[NOTE]
====
The fields in the *Register a new OAuth application* GitHub form are automatically filled with the required values through the URL defined by the ROSA CLI.
====
.. Use the information from your GitHub OAuth application page to populate the remaining `rosa create idp` interactive prompts.
+
.Continued example output
[source,terminal]
----
...
? Client ID: <github_client_id> <1>
? Client Secret: [? for help] <github_client_secret> <2>
? GitHub Enterprise Hostname (optional):
? Mapping method: claim <3>
I: Configuring IDP for cluster '<cluster_name>'
I: Identity Provider 'github-1' has been created.
   It will take up to 1 minute for this configuration to be enabled.
   To add cluster administrators, see 'rosa grant user --help'.
   To login into the console, open https://console-openshift-console.apps.<cluster_name>.<random_string>.p1.openshiftapps.com and click on github-1.
----
<1> Replace `<github_client_id>` with the client ID for your GitHub OAuth application.
<2> Replace `<github_client_secret>` with a client secret for your GitHub OAuth application.
<3> Specify `claim` as the mapping method.
+
[NOTE]
====
It might take approximately two minutes for the identity provider configuration to become active. If you have configured a `cluster-admin` user, you can watch the OAuth pods redeploy with the updated configuration by running `oc get pods -n openshift-authentication --watch`.
====
.. Enter the following command to verify that the identity provider has been configured correctly:
+
[source,terminal]
----
$ rosa list idps --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
NAME        TYPE      AUTH URL
github-1    GitHub    https://oauth-openshift.apps.<cluster_name>.<random_string>.p1.openshiftapps.com/oauth2callback/github-1
----

ifeval::["{context}" == "rosa-getting-started"]
:getting-started:
endif::[]
ifeval::["{context}" == "rosa-quickstart"]
:quickstart:
endif::[]
