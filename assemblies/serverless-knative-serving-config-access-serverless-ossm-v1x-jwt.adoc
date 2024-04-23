:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-ossm-v1x-jwt"]
= Using JSON Web Token authentication with {SMProductShortName} 1.x
:context: serverless-ossm-v1x-jwt

You can use JSON Web Token (JWT) authentication with Knative services by using {SMProductShortName} 1.x and {ServerlessProductName}. To do this, you must create a policy in the application namespace that is a member of the `ServiceMeshMemberRoll` object. You must also enable sidecar injection for the service.


include::modules/serverless-ossm-v1x-jwt.adoc[leveloffset=+1]
