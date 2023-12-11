:_mod-docs-content-type: ASSEMBLY
[id="serverless-functions-about"]
= About {FunctionsProductName}
:context: serverless-functions-about
include::_attributes/common-attributes.adoc[]

toc::[]

{FunctionsProductName} enables developers to create and deploy stateless, event-driven functions as a Knative service on {product-title}. The `kn func` CLI is provided as a plugin for the Knative `kn` CLI. You can use the `kn func` CLI to create, build, and deploy the container image as a Knative service on the cluster.

[id="serverless-functions-about-runtimes"]
== Included runtimes

{FunctionsProductName} provides templates that can be used to create basic functions for the following runtimes:

// add xref links to docs once added
* xref:../../serverless/functions/serverless-developing-quarkus-functions.adoc#serverless-developing-quarkus-functions[Quarkus]
* xref:../../serverless/functions/serverless-developing-nodejs-functions.adoc#serverless-developing-nodejs-functions[Node.js]
* xref:../../serverless/functions/serverless-developing-typescript-functions.adoc#serverless-developing-typescript-functions[TypeScript]

[id="next-steps_serverless-functions-about"]
== Next steps

* xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-functions-getting-started[Getting started with functions].
