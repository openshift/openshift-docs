// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

:_mod-docs-content-type: CONCEPT
[id="jt-comparison-of-jenkins-openshift-pipelines-execution-models_{context}"]
= Comparison of Jenkins and {pipelines-shortname} execution models

Jenkins and {pipelines-shortname} offer similar functions but are different in architecture and execution.

.Comparison of execution models in Jenkins and {pipelines-shortname}
[cols="1,1",options="header"]
|===
|Jenkins|{pipelines-shortname}
|Jenkins has a controller node. Jenkins runs pipelines and steps centrally, or orchestrates jobs running in other nodes.|{pipelines-shortname} is serverless and distributed, and there is no central dependency for execution.
|Containers are launched by the Jenkins controller node through the pipeline.|{pipelines-shortname} adopts a 'container-first' approach, where every step runs as a container in a pod (equivalent to nodes in Jenkins).
|Extensibility is achieved by using plugins.|Extensibility is achieved by using tasks in Tekton Hub or by creating custom tasks and scripts.
|===
