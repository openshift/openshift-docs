:_mod-docs-content-type: ASSEMBLY
[id="customizing-configurations-in-the-tektonconfig-cr"]
= Customizing configurations in the TektonConfig custom resource
include::_attributes/common-attributes.adoc[]
:context: customizing-configurations-in-the-tektonconfig-cr

toc::[]

In {pipelines-title}, you can customize the following configurations by using the `TektonConfig` custom resource (CR):

* Configuring the {pipelines-title} control plane
* Changing the default service account
* Disabling the service monitor
* Configuring pipeline resolvers
* Disabling cluster tasks and pipeline templates
* Disabling the integration of {tekton-hub}
* Disabling the automatic creation of RBAC resources
* Pruning of task runs and pipeline runs

[id="prerequisites_customizing-configurations-in-the-tektonconfig-cr"]
== Prerequisites

* You have installed the {pipelines-title} Operator.

include::modules/op-configuring-pipelines-control-plane.adoc[leveloffset=+1]

include::modules/op-modifiable-fields-with-default-values.adoc[leveloffset=+2]

include::modules/op-optional-configuration-fields.adoc[leveloffset=+2]

include::modules/op-changing-default-service-account.adoc[leveloffset=+1]

include::modules/op-disabling-the-service-monitor.adoc[leveloffset=+1]

include::modules/op-configuring-pipeline-resolvers.adoc[leveloffset=+1]

include::modules/op-disabling-cluster-tasks-and-pipeline-templates.adoc[leveloffset=+1]

include::modules/op-disabling-the-integretion-of-tekton-hub.adoc[leveloffset=+1]

include::modules/op-disabling-automatic-creation-of-rbac-resources.adoc[leveloffset=+1]

include::modules/op-automatic-pruning-taskrun-pipelinerun.adoc[leveloffset=+1]

include::modules/op-default-pruner-configuration.adoc[leveloffset=+2]

include::modules/op-annotations-for-automatic-pruning-taskruns-pipelineruns.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_customizing-configurations-in-the-tektonconfig-cr"]
== Additional resources

* xref:../../cicd/pipelines/authenticating-pipelines-using-git-secret.adoc#op-configuring-ssh-authentication-for-git_authenticating-pipelines-using-git-secret[Configuring SSH authentication for Git]
* xref:../../cicd/pipelines/managing-nonversioned-and-versioned-cluster-tasks.adoc#managing-nonversioned-and-versioned-cluster-tasks[Managing non-versioned and versioned cluster tasks]
* xref:../../applications/pruning-objects.adoc#pruning-objects[Pruning objects to reclaim resources]
* xref:../../cicd/pipelines/working-with-pipelines-web-console.adoc#op-creating-pipeline-templates-admin-console_working-with-pipelines-web-console[Creating pipeline templates in the Administrator perspective]
