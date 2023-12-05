:_mod-docs-content-type: ASSEMBLY
[id="using-tekton-hub-with-openshift-pipelines"]
= Using Tekton Hub with {pipelines-shortname}
include::_attributes/common-attributes.adoc[]
:context: using-tekton-hub-with-openshift-pipelines

toc::[]

:FeatureName: Tekton Hub
include::snippets/technology-preview.adoc[]

[role="_abstract"]
{tekton-hub} helps you discover, search, and share reusable tasks and pipelines for your CI/CD workflows. A public instance of {tekton-hub} is available at link:https://hub.tekton.dev/[hub.tekton.dev]. Cluster administrators can also install and deploy a custom instance of {tekton-hub} by modifying the configurations in the `TektonHub` custom resource (CR).

include::modules/op-installing-and-deploying-tekton-hub-on-an-openshift-cluster.adoc[leveloffset=+1]

include::modules/op-installing-tekton-hub-without-login-and-rating.adoc[leveloffset=+2]

include::modules/op-installing-tekton-hub-with-login-and-rating.adoc[leveloffset=+2]

include::modules/op-using-a-custom-database-in-tekton-hub.adoc[leveloffset=+1]

include::modules/op-installing-crunchy-postgres-database-and-tekton-hub.adoc[leveloffset=+2]

include::modules/op-migrating-tekton-hub-data-to-an-existing-crunchy-postgres-database.adoc[leveloffset=+2]

include::modules/op-updating-tekton-hub-with-custom-categories-and-catalogs.adoc[leveloffset=+1]

include::modules/op-modifying-catalog-refresh-interval-tekton-hub.adoc[leveloffset=+1]

include::modules/op-adding-new-users-in-tekton-hub-configuration.adoc[leveloffset=+1]

include::modules/op-disabling-tekton-hub-authorization-after-upgrade.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources-tekton-hub"]
== Additional resources

* GitHub repository of link:https://github.com/tektoncd/hub[Tekton Hub]

* xref:../../cicd/pipelines/installing-pipelines.adoc#installing-pipelines[Installing {pipelines-shortname}]

* xref:../../cicd/pipelines/op-release-notes.adoc#op-release-notes[{pipelines-title} release notes]