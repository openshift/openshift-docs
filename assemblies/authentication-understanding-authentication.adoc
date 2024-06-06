:_mod-docs-content-type: ASSEMBLY
[id="understanding-authentication"]
= Understanding authentication
include::_attributes/common-attributes.adoc[]
:context: understanding-authentication

toc::[]

For users to interact with {product-title}, they must first authenticate
to the cluster. The authentication layer identifies the user associated with requests to the
{product-title} API. The authorization layer then uses information about the
requesting user to determine if the request is allowed.

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
As an administrator, you can configure authentication for {product-title}.
endif::[]

include::modules/rbac-users.adoc[leveloffset=+1]

include::modules/rbac-groups.adoc[leveloffset=+1]

include::modules/rbac-api-authentication.adoc[leveloffset=+1]

include::modules/oauth-server-overview.adoc[leveloffset=+2]

include::modules/oauth-token-requests.adoc[leveloffset=+2]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
include::modules/authentication-api-impersonation.adoc[leveloffset=+3]

include::modules/authentication-prometheus-system-metrics.adoc[leveloffset=+3]
endif::[]
