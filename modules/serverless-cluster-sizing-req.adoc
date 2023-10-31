// Module included in the following assemblies:
//
// * /serverless/install/preparing-serverless-install.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-cluster-sizing-req_{context}"]
= Defining cluster size requirements

To install and use {ServerlessProductName}, the {product-title} cluster must be sized correctly.

[NOTE]
====
The following requirements relate only to the pool of worker machines of the {product-title} cluster. Control plane nodes are not used for general scheduling and are omitted from the requirements.
====

The minimum requirement to use {ServerlessProductName} is a cluster with 10 CPUs and 40GB memory.
By default, each pod requests ~400m of CPU, so the minimum requirements are based on this value.

The total size requirements to run {ServerlessProductName} are dependent on the components that are installed and the applications that are deployed, and might vary depending on your deployment.
