:_mod-docs-content-type: ASSEMBLY
[id="serverless-developing-quarkus-functions"]
= Developing Quarkus functions
:context: serverless-developing-quarkus-functions
include::_attributes/common-attributes.adoc[]

toc::[]

After you have xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-create-func-kn_serverless-functions-getting-started[created a Quarkus function project], you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-quarkus-functions"]
== Prerequisites

* Before you can develop functions, you must complete the setup steps in xref:../../serverless/functions/serverless-functions-setup.adoc#serverless-functions-setup[Setting up {FunctionsProductName}].

// templates, invoking
include::modules/serverless-quarkus-template.adoc[leveloffset=+1]
include::modules/serverless-invoking-quarkus-functions.adoc[leveloffset=+1]
include::modules/serverless-quarkus-cloudevent-attributes.adoc[leveloffset=+1]
// return values
include::modules/serverless-quarkus-function-return-values.adoc[leveloffset=+1]
include::modules/serverless-functions-quarkus-return-value-types.adoc[leveloffset=+2]
// testing
include::modules/serverless-testing-quarkus-functions.adoc[leveloffset=+1]

[id="next-steps_serverless-developing-quarkus-functions"]
== Next steps

* xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-build-func-kn_serverless-functions-getting-started[Build] and xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-deploy-func-kn_serverless-functions-getting-started[deploy] a function.
