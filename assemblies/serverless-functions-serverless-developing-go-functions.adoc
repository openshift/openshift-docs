:_mod-docs-content-type: ASSEMBLY
[id="serverless-developing-go-functions"]
= Developing Go functions
:context: serverless-developing-go-functions
include::_attributes/common-attributes.adoc[]

toc::[]

:FeatureName: {FunctionsProductName} with Go
include::snippets/technology-preview.adoc[leveloffset=+2]

After you have xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-create-func-kn_serverless-functions-getting-started[created a Go function project], you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-go-functions"]
== Prerequisites

* Before you can develop functions, you must complete the steps in xref:../../serverless/functions/serverless-functions-setup.adoc#serverless-functions-setup[Setting up {FunctionsProductName}].

include::modules/serverless-go-template.adoc[leveloffset=+1]

[id="serverless-developing-go-functions-about-invoking"]
== About invoking Go functions

When using the Knative (`kn`) CLI to create a function project, you can generate a project that responds to CloudEvents, or one that responds to simple HTTP requests. Go functions are invoked by using different methods, depending on whether they are triggered by an HTTP request or a CloudEvent.

include::modules/serverless-invoking-go-functions-http.adoc[leveloffset=+2]
include::modules/serverless-invoking-go-functions-cloudevent.adoc[leveloffset=+2]

include::modules/serverless-go-function-return-values.adoc[leveloffset=+1]
include::modules/serverless-testing-go-functions.adoc[leveloffset=+1]

[id="next-steps_serverless-developing-go-functions"]
== Next steps

* xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-build-func-kn_serverless-functions-getting-started[Build] and xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-deploy-func-kn_serverless-functions-getting-started[deploy] a function.
