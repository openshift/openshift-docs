:_mod-docs-content-type: ASSEMBLY
[id="serverless-functions-accessing-secrets-configmaps"]
= Accessing secrets and config maps from functions
include::_attributes/common-attributes.adoc[]
:context: serverless-functions-secrets

toc::[]

After your functions have been deployed to the cluster, they can access data stored in secrets and config maps. This data can be mounted as volumes, or assigned to environment variables. You can configure this access interactively by using the Knative CLI, or by manually by editing the function configuration YAML file.

[IMPORTANT]
====
To access secrets and config maps, the function must be deployed on the cluster. This functionality is not available to a function running locally.

If a secret or config map value cannot be accessed, the deployment fails with an error message specifying the inaccessible values.
====

include::modules/serverless-functions-secrets-configmaps-interactively.adoc[leveloffset=+1]
include::modules/serverless-functions-secrets-configmaps-interactively-specialized.adoc[leveloffset=+1]

[id="serverless-functions-secrets-configmaps-manually_{context}"]
== Adding function access to secrets and config maps manually

You can manually add configuration for accessing secrets and config maps to your function. This might be preferable to using the `kn func config` interactive utility and commands, for example when you have an existing configuration snippet.

include::modules/serverless-functions-mounting-secret-as-volume.adoc[leveloffset=+2]
include::modules/serverless-functions-mounting-configmap-as-volume.adoc[leveloffset=+2]
include::modules/serverless-functions-key-value-in-secret-to-env-variable.adoc[leveloffset=+2]
include::modules/serverless-functions-key-value-in-configmap-to-env-variable.adoc[leveloffset=+2]
include::modules/serverless-functions-all-values-in-secret-to-env-variables.adoc[leveloffset=+2]
include::modules/serverless-functions-all-values-in-configmap-to-env-variables.adoc[leveloffset=+2]
