// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/config-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-config-identity-providers.adoc

:_mod-docs-content-type: PROCEDURE
[id="config-google-idp_{context}"]
= Configuring a Google identity provider


Configure a Google identity provider to allow users to authenticate with their Google credentials.

[WARNING]
====
Using Google as an identity provider allows any Google user to authenticate to your server.
You can limit authentication to members of a specific hosted domain with the
`hostedDomain` configuration attribute.
====

.Procedure

. From {cluster-manager-url}, navigate to the *Clusters* page and select the cluster that you need to configure identity providers for.

. Click the *Access control* tab.

. Click *Add identity provider*.
+
[NOTE]
====
You can also click the *Add Oauth configuration* link in the warning message displayed after cluster creation to configure your identity providers.
====

. Select *Google* from the drop-down menu.

. Enter a unique name for the identity provider. This name cannot be changed later.
** An *OAuth callback URL* is automatically generated in the provided field. You will provide this URL to Google.
+
----
https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----
+
For example:
+
----
https://oauth-openshift.apps.openshift-cluster.example.com/oauth2callback/google
----

. Configure a Google identity provider using link:https://developers.google.com/identity/protocols/OpenIDConnect[Google's OpenID Connect integration].

. Return to {product-title} and select a mapping method from the drop-down menu. *Claim* is recommended in most cases.

. Enter the *Client ID* of a registered Google project and the *Client secret* issued by Google.

. Enter a hosted domain to restrict users to a Google Apps domain.

. Click *Confirm*.

.Verification

* The configured identity provider is now visible on the *Access control* tab of the *Clusters* page.
