:_mod-docs-content-type: ASSEMBLY
[id="serverless-ossm-v2x-jwt"]
= Using JSON Web Token authentication with {SMProductShortName} 2.x
include::_attributes/common-attributes.adoc[]
:context: serverless-ossm-v2x-jwt

You can use JSON Web Token (JWT) authentication with Knative services by using {SMProductShortName} 2.x and {ServerlessProductName}. To do this, you must create authentication requests and policies in the application namespace that is a member of the `ServiceMeshMemberRoll` object. You must also enable sidecar injection for the service.

include::modules/serverless-ossm-v2x-jwt.adoc[leveloffset=+1]