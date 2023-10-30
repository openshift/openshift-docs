:_mod-docs-content-type: ASSEMBLY
[id="serverless-developing-typescript-functions"]
= Developing TypeScript functions
:context: serverless-developing-typescript-functions
include::_attributes/common-attributes.adoc[]

toc::[]

After you have xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-create-func-kn_serverless-functions-getting-started[created a TypeScript function project], you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-typescript-functions"]
== Prerequisites

* Before you can develop functions, you must complete the steps in xref:../../serverless/functions/serverless-functions-setup.adoc#serverless-functions-setup[Setting up {FunctionsProductName}].

include::modules/serverless-typescript-template.adoc[leveloffset=+1]

[id="serverless-developing-typescript-functions-about-invoking"]
== About invoking TypeScript functions

When using the Knative (`kn`) CLI to create a function project, you can generate a project that responds to CloudEvents or one that responds to simple HTTP requests. CloudEvents in Knative are transported over HTTP as a POST request, so both function types listen for and respond to incoming HTTP events.

TypeScript functions can be invoked with a simple HTTP request. When an incoming request is received, functions are invoked with a `context` object as the first parameter.

include::modules/serverless-typescript-functions-context-objects.adoc[leveloffset=+2]
include::modules/serverless-typescript-function-return-values.adoc[leveloffset=+1]
include::modules/serverless-testing-typescript-functions.adoc[leveloffset=+1]

[id="next-steps_serverless-developing-typescript-functions"]
== Next steps

* See the xref:../../serverless/functions/serverless-functions-reference-guide.adoc#serverless-typescript-context-object-reference_serverless-functions-reference-guide[TypeScript context object reference] documentation.
* xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-build-func-kn_serverless-functions-getting-started[Build] and xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-deploy-func-kn_serverless-functions-getting-started[deploy] a function.
* See link:https://getpino.io/#/docs/api[the Pino API documentation] for more information about logging with functions.
