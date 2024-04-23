:_mod-docs-content-type: ASSEMBLY
[id="serverless-functions-reference-guide"]
= Functions development reference guide
include::_attributes/common-attributes.adoc[]
:context: serverless-functions-reference-guide

toc::[]

{FunctionsProductName} provides templates that can be used to create basic functions. A template initiates the function project boilerplate and prepares it for use with the `kn func` tool. Each function template is tailored for a specific runtime and follows its conventions. With a template, you can initiate your function project automatically.

Templates for the following runtimes are available:

// add xref links to docs once added
* xref:../../serverless/functions/serverless-developing-nodejs-functions.adoc#serverless-developing-nodejs-functions[Node.js]
* xref:../../serverless/functions/serverless-developing-quarkus-functions.adoc#serverless-developing-quarkus-functions[Quarkus]
* xref:../../serverless/functions/serverless-developing-typescript-functions.adoc#serverless-developing-typescript-functions[TypeScript]
//* SpringBoot - TBC

include::modules/serverless-nodejs-context-object-reference.adoc[leveloffset=+1]
include::modules/serverless-typescript-context-object-reference.adoc[leveloffset=+1]
