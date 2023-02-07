// Module included in the following assemblies:
//
// * authentication/understanding-authentication.adoc
// * authentication/configuring-internal-oauth.adoc


[id="oauth-server-overview_{context}"]
= {product-title} OAuth server

The {product-title} master includes a built-in OAuth server. Users obtain OAuth
access tokens to authenticate themselves to the API.

When a person requests a new OAuth token, the OAuth server uses the configured
identity provider
to determine the identity of the person making the request.

It then determines what user that identity maps to, creates an access token for
that user, and returns the token for use.
