:_mod-docs-content-type: ASSEMBLY
[id="serverless-functions-on-cluster-builds"]
= On-cluster function building and deploying
:context: serverless-functions-on-cluster-builds
include::_attributes/common-attributes.adoc[]

toc::[]

Instead of building a function locally, you can build a function directly on the cluster. When using this workflow on a local development machine, you only need to work with the function source code. This is useful, for example, when you cannot install on-cluster function building tools, such as docker or podman.

include::modules/serverless-functions-creating-on-cluster-builds.adoc[leveloffset=+1]
include::modules/serverless-functions-specifying-function-revision.adoc[leveloffset=+1]
