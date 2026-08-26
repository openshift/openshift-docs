:_mod-docs-content-type: ASSEMBLY
[id="verifying-application-deployment"]
= Verifying your serverless application deployment
include::_attributes/common-attributes.adoc[]
:context: verifying-application-deployment


To verify that your serverless application has been deployed successfully, you must get the application URL created by Knative, and then send a request to that URL and observe the output. {ServerlessProductName} supports the use of both HTTP and HTTPS URLs, however the output from `oc get ksvc` always prints URLs using the `http://` format.

include::modules/verifying-serverless-app-deployment.adoc[leveloffset=+1]
