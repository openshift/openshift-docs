// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift

[id="creating-a-new-client-in-keycloak_{context}"]
= Creating a new client in Keycloak

.Procedure

. Log in to your Keycloak server, select the realm you want to use, navigate to the *Clients* page, and then click *Create* in the upper-right section of the screen.

. Specify the following values:
Client ID:: `argocd`
Client Protocol:: `openid-connect` 
Route URL:: <your-argo-cd-route-url>
Access Type:: `confidential`
Valid Redirect URIs:: <your-argo-cd-route-url>/auth/callback
Base URL:: `/applications`

. Click *Save* to see the *Credentials* tab added to the *Client* page.

. Copy the secret from the *Credentials* tab for further configuration.
