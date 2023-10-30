:_mod-docs-content-type: ASSEMBLY
//Jenkins-Tekton-Migration
[id="migrating-from-jenkins-to-openshift-pipelines_{context}"]
= Migrating from Jenkins to {pipelines-shortname} or Tekton
include::_attributes/common-attributes.adoc[]
:context: migrating-from-jenkins-to-openshift-pipelines

toc::[]

You can migrate your CI/CD workflows from Jenkins to link:https://docs.openshift.com/pipelines/latest/about/understanding-openshift-pipelines.html[{pipelines-title}], a cloud-native CI/CD experience based on the Tekton project.

include::modules/jt-comparison-of-jenkins-and-openshift-pipelines-concepts.adoc[leveloffset=+1]

include::modules/jt-migrating-a-sample-pipeline-from-jenkins-to-openshift-pipelines.adoc[leveloffset=+1]

include::modules/jt-migrating-from-jenkins-plugins-to-openshift-pipelines-hub-tasks.adoc[leveloffset=+1]

include::modules/jt-extending-openshift-pipelines-capabilities-using-custom-tasks-and-scripts.adoc[leveloffset=+1]

include::modules/jt-comparison-of-jenkins-openshift-pipelines-execution-models.adoc[leveloffset=+1]

include::modules/jt-examples-of-common-use-cases.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources
* link:https://docs.openshift.com/pipelines/latest/about/understanding-openshift-pipelines.html[Understanding {pipelines-shortname}]
* xref:../../authentication/using-rbac.adoc#using-rbac[Role-based Access Control]
