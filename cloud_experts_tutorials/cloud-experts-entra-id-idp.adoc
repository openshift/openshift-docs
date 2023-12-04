:_mod-docs-content-type: ASSEMBLY
[id="cloud-experts-entra-id-idp"]
= Tutorial: Configuring Microsoft Entra ID (formerly Azure Active Directory) as an identity provider
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: cloud-experts-entra-id-idp

toc::[]

//Mobb content metadata
//Brought into ROSA product docs 2023-09-18
// ---
// date: '2022-09-19'
// title: Configure ROSA to use Entra ID Group Claims
// authors:
//   - Michael McNeill
//   - Paul Czarkowski
// ---

This tutorial demonstrates how to configure Microsoft Entra ID (formerly Azure Active Directory) as the cluster identity provider in {product-title} (ROSA). This tutorial walks through the creation of an Microsoft Entra ID (Entra ID) application and configure Red Hat OpenShift Service on AWS (ROSA) to authenticate using Azure AD.

This tutorial walks through the following steps:

. Register a new application in Entra ID for authentication.
. Configure the application registration in Entra ID to include optional and group claims in tokens.
. Configure the OpenShift cluster to use Entra ID as the identity provider.
. Grant additional permissions to individual groups.

[id="cloud-experts-entra-id-idp-prerequisites"]
== Prerequisites

Create a set of security groups and assign users by following link:https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/how-to-manage-groups[the Microsoft documentation].

[id="cloud-experts-entra-id-idp-register-application"]
== Register a new application in Entra ID for authentication

. Capture the OAuth callback URL
+
First, construct the cluster's OAuth callback URL and make note of it. To do so, run the following command, making sure to replace the variable specified:
+
The "AAD" directory at the end of the OAuth callback URL should match the OAuth identity provider name you'll setup later.
+
[source,terminal]
----
$ domain=$(rosa describe cluster -c <cluster_name> | grep "DNS" | grep -oE '\S+.openshiftapps.com')
$ echo "OAuth callback URL: https://oauth-openshift.apps.$domain/oauth2callback/AAD"
----

. Register a new application in Entra ID
+
You need to create the Entra ID application itself. To do so, log in to the Azure portal, and navigate to link:https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade[App registrations blade], and click on "New registration" to create a new application.
+
image:azure-portal_app-registrations-blade.png[Azure Portal - App registrations blade]
+
Provide a name for the application, for example `openshift-auth`. Select "Web" from the Redirect URI dropdown and fill in the Redirect URI using the value of the OAuth callback URL you retrieved in the previous step. Once you fill in the necessary information, click "Register" to create the application.
+
image:azure-portal_register-an-application-page.png[Azure Portal - Register an application page]
+
Then, click on the "Certificates & secrets" sub-blade and select "New client secret". Fill in the details request and make note of the generated client secret value, as you'll use it in a later step. You won't be able to retrieve it again.
+
image:azure-portal_certificates-secrets-page.png[Azure Portal - Certificates & secrets page]
image:azure-portal_add-a-client-secret-page.png[Azure Portal - Add a Client Secret page]
image:azure-portal_copy-client-secret-page.png[Azure Portal - Copy Client Secret page]
+
Then, click on the "Overview" sub-blade and make note of the "Application (client) ID" and "Directory (tenant) ID". You'll need those values in a later step as well.

[id="rosa-mobb-entra-id-configure-optional-claims"]
== Configure optional claims

To provide OpenShift with enough information about the user to create their account, we will configure Entra ID to provide two optional claims, specifically "email" and "preferred_username". For more information on optional claims in Entra ID, see link:https://learn.microsoft.com/en-us/azure/active-directory/develop/optional-claims[the Microsoft documentation].

Click on the "Token configuration" sub-blade and select the "Add optional claim" button.

image:azure-portal_optional-claims-page.png[Azure Portal - Add Optional Claims Page]

Select ID then check the "email" and "preferred_username" claims and click the "Add" button to configure them for your Entra ID application.

image:azure-portal_add-optional-claims-page.png[Azure Portal - Add Optional Claims - Token Type]
image:azure-portal_add-optional-email-claims-page.png[Azure Portal - Add Optional Claims - email]
image:azure-portal_add-optional-preferred_username-claims-page.png[Azure Portal - Add Optional Claims - preferred_username]

When prompted, follow the prompt to enable the necessary Microsoft Graph permissions.

image:azure-portal_add-optional-claims-graph-permissions-prompt.png[Azure Portal - Add Optional Claims - Graph Permissions Prompt]

[id="rosa-mobb-entra-id-configure-group-claims"]
== Configure group claims (optional)

In addition to individual user authentication, OpenShift provides group claim functionality. This functionality allows an OpenID Connect identity provider, like Entra ID, to offer a user’s group membership for use within OpenShift. To enable group claims, we will configure Entra ID to provide a groups claim.

Next, select the "Add groups claim" button.

image:azure-portal_optional-group-claims-page.png[Azure Portal - Add Groups Claim Page]

Select the "Security groups" option and click the "Add" button to configure group claims for your Entra ID application.

[NOTE]
====
In this example, we are providing all security groups a user is a member of via the group claim. In a real production environment, we highly recommend scoping the groups provided by the group claim to _only those groups which are applicable to OpenShift_.
====

image:azure-portal_edit-group-claims-page.png[Azure Portal - Edit Groups Claim Page]

[id="cloud-experts-entra-id-idp-configure-cluster"]
== Configure the OpenShift cluster to use Entra ID as the identity provider

Finally, we need to configure OpenShift to use Entra ID as its identity provider. While Red Hat OpenShift Service on AWS (ROSA) offers the ability to configure identity providers via the OpenShift Cluster Manager (OCM), we will use the configure the cluster's OAuth provider to use Entra ID as its identity provider via the `rosa` CLI. Before we can do so, we need to set some variables that we will use for our IDP configuration by running the following command:

[source,terminal]
----
$ CLUSTER_NAME=example-cluster <1>
$ IDP_NAME=AAD <2>
$ APP_ID=yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy <3>
$ CLIENT_SECRET=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx <4>
$ TENANT_ID=zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz <5>
----
--
<1> Replace this with the name of your ROSA cluster.
<2> Replace this with the name you used in the OAuth callback URL.
<3> Replace this with the Application (client) ID.
<4> Replace this with the Client Secret.
<5> Replace this with the Directory (tenant) ID.
--

Next, run the following command to configure the cluster's OAuth provider if you opted to enable group claims:

[source,terminal]
----
$ rosa create idp \
--cluster ${CLUSTER_NAME} \
--type openid \
--name ${IDP_NAME} \
--client-id ${APP_ID} \
--client-secret ${CLIENT_SECRET} \
--issuer-url https://login.microsoftonline.com/${TENANT_ID}/v2.0 \
--email-claims email \
--name-claims name \
--username-claims preferred_username \
--extra-scopes email,profile \
--groups-claims groups
----

Otherwise, run the following command to configure the cluster's OAuth provider if you opted to not enable group claims:

[source,terminal]
----
$ rosa create idp \
--cluster ${CLUSTER_NAME} \
--type openid \
--name ${IDP_NAME} \
--client-id ${APP_ID} \
--client-secret ${CLIENT_SECRET} \
--issuer-url https://login.microsoftonline.com/${TENANT_ID}/v2.0 \
--email-claims email \
--name-claims name \
--username-claims preferred_username \
--extra-scopes email,profile
----

[id="rosa-mobb-azure-oidc-grant-permissions"]
== Grant additional permissions to individual users

Once the cluster authentication Operator reconciles your changes (generally within a few minutes), you will be able to log in to the cluster using Entra ID.

Once you log in, you will notice that you have very limited permissions. This is because, by default, OpenShift only grants you the ability to create new projects (namespaces) in the cluster. Other projects (namespaces) are restricted from view.

OpenShift includes a significant number of preconfigured roles, including the `cluster-admin` role that grants full access and control over the cluster. To grant your user access to the `cluster-admin` role, run the following command:

[source,terminal]
----
$ rosa grant user cluster-admin \
    --user=<USERNAME> <1>
    --cluster=${CLUSTER_NAME}
----
--
<1> Provide your Entra ID username that you would like to have cluster admin permissions.
--

[id="cloud-experts-entra-id-idp-additional-permissions"]
== Grant additional permissions to individual groups

If you opted to enable group claims, the cluster OAuth provider will automatically create or update the membership of groups the user is a member of (using the group ID). The cluster OAuth provider **does not** automatically create RoleBindings and ClusterRoleBindings for the groups that are created, you are responsible for creating those via your own processes.

OpenShift includes a significant number of preconfigured roles, including the `cluster-admin` role that grants full access and control over the cluster. To grant an automatically generated group access to the `cluster-admin` role, you must create a ClusterRoleBinding to the group ID.

[source,terminal]
----
$ oc create clusterrolebinding cluster-admin-group \
--clusterrole=cluster-admin \
--group=<GROUP_ID> <1>
----
--
<1> Provide your Entra ID group ID that you would like to have cluster admin permissions.
--

Now, any user in the specified group will automatically be granted `cluster-admin` access.

For more information on how to use RBAC to define and apply permissions in OpenShift, see link:https://docs.openshift.com/container-platform/latest/authentication/using-rbac.html[the OpenShift documentation].
