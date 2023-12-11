:_mod-docs-content-type: ASSEMBLY
[id="serverless-developing-nodejs-functions"]
= Developing Node.js functions
:context: serverless-developing-nodejs-functions
include::_attributes/common-attributes.adoc[]

toc::[]

After you have xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-create-func-kn_serverless-functions-getting-started[created a Node.js function project], you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-nodejs-functions"]
== Prerequisites

* Before you can develop functions, you must complete the steps in xref:../../serverless/functions/serverless-functions-setup.adoc#serverless-functions-setup[Setting up {FunctionsProductName}].

include::modules/serverless-nodejs-template.adoc[leveloffset=+1]

[id="serverless-developing-nodejs-functions-about-invoking"]
== About invoking Node.js functions

When using the Knative (`kn`) CLI to create a function project, you can generate a project that responds to CloudEvents, or one that responds to simple HTTP requests. CloudEvents in Knative are transported over HTTP as a POST request, so both function types listen for and respond to incoming HTTP events.

Node.js functions can be invoked with a simple HTTP request. When an incoming request is received, functions are invoked with a `context` object as the first parameter.

include::modules/serverless-nodejs-functions-context-objects.adoc[leveloffset=+2]
include::modules/serverless-nodejs-function-return-values.adoc[leveloffset=+1]
include::modules/serverless-testing-nodejs-functions.adoc[leveloffset=+1]

[id="next-steps_serverless-developing-nodejs-functions"]
== Next steps

* See the xref:../../serverless/functions/serverless-functions-reference-guide.adoc#serverless-nodejs-context-object-reference_serverless-functions-reference-guide[Node.js context object reference] documentation.
* xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-build-func-kn_serverless-functions-getting-started[Build] and xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-deploy-func-kn_serverless-functions-getting-started[deploy] a function.
