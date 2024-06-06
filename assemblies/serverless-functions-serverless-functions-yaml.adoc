:_mod-docs-content-type: ASSEMBLY
[id="serverless-functions-project-configuration"]
= Function project configuration in func.yaml
include::_attributes/common-attributes.adoc[]
:context: serverless-functions-yaml

toc::[]

The `func.yaml` file contains the configuration for your function project. Values specified in `func.yaml` are used when you execute a `kn func` command. For example, when you run the `kn func build` command, the value in the `build` field is used. In some cases, you can override these values with command line flags or environment variables.

include::modules/serverless-functions-func-yaml-fields.adoc[leveloffset=+1]
include::modules/serverless-functions-func-yaml-environment-variables.adoc[leveloffset=+1]

[id="additional-resources_serverless-functions-project-configuration"]
[role="_additional-resources"]
== Additional resources
* xref:../../serverless/functions/serverless-functions-getting-started.adoc#serverless-functions-getting-started[Getting started with functions]
* xref:../../serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc#serverless-functions-accessing-secrets-configmaps[Accessing secrets and config maps from Serverless functions]
* link:https://knative.dev/docs/serving/autoscaling/[Knative documentation on Autoscaling]
* link:https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/[Kubernetes documentation on managing resources for containers]
* link:https://knative.dev/docs/serving/autoscaling/concurrency/[Knative documentation on configuring concurrency]
