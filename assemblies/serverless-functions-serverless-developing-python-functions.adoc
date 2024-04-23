:_mod-docs-content-type: ASSEMBLY
[id="serverless-developing-python-functions"]
= Developing Python functions
:context: serverless-developing-python-functions
include::_attributes/common-attributes.adoc[]

toc::[]

:FeatureName: {FunctionsProductName} with Python
include::snippets/technology-preview.adoc[leveloffset=+2]

After you have xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-create-func-kn_serverless-functions-getting-started[created a Python function project], you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-python-functions"]
== Prerequisites

* Before you can develop functions, you must complete the steps in xref:../../serverless/functions/serverless-functions-setup.adoc#serverless-functions-setup[Setting up {FunctionsProductName}].

include::modules/serverless-python-template.adoc[leveloffset=+1]
include::modules/serverless-invoking-python-functions.adoc[leveloffset=+1]
include::modules/serverless-python-function-return-values.adoc[leveloffset=+1]
include::modules/serverless-testing-python-functions.adoc[leveloffset=+1]

[id="next-steps_serverless-developing-python-functions"]
== Next steps

* xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-build-func-kn_serverless-functions-getting-started[Build] and xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-deploy-func-kn_serverless-functions-getting-started[deploy] a function.
