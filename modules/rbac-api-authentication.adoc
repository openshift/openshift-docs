[id="rbac-api-authentication_{context}"]
= API authentication
Requests to the {product-title} API are authenticated using the following
methods:

OAuth access tokens::
* Obtained from the {product-title} OAuth server using the
`_<namespace_route>_/oauth/authorize` and `_<namespace_route>_/oauth/token`
endpoints.
* Sent as an `Authorization: Bearer...` header.
* Sent as a websocket subprotocol header in the form
`base64url.bearer.authorization.k8s.io.<base64url-encoded-token>` for websocket
requests.

X.509 client certificates::
* Requires an HTTPS connection to the API server.
* Verified by the API server against a trusted certificate authority bundle.
* The API server creates and distributes certificates to controllers to authenticate themselves.

Any request with an invalid access token or an invalid certificate is rejected
by the authentication layer with a `401` error.

If no access token or certificate is presented, the authentication layer assigns
the `system:anonymous` virtual user and the `system:unauthenticated` virtual
group to the request. This allows the authorization layer to determine which
requests, if any, an anonymous user is allowed to make.
