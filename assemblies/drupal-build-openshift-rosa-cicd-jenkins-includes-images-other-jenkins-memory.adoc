// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

:_mod-docs-content-type: CONCEPT
[id="images-other-jenkins-memory_{context}"]
= Jenkins memory requirements

When deployed by the provided Jenkins Ephemeral or Jenkins Persistent templates, the default memory limit is `1 Gi`.

By default, all other process that run in the Jenkins container cannot use more than a total of `512 MiB` of memory. If they require more memory, the container halts. It is therefore highly recommended that pipelines run external commands in an agent container wherever possible.

And if `Project` quotas allow for it, see recommendations from the Jenkins documentation on what a Jenkins master should have from a memory perspective. Those recommendations proscribe to allocate even more memory for the Jenkins master.

It is recommended to specify memory request and limit values on agent containers created by the Jenkins Kubernetes plugin. Admin users can set default values on a per-agent image basis through the Jenkins configuration. The memory request and limit parameters can also be overridden on a per-container basis.

You can increase the amount of memory available to Jenkins by overriding the `MEMORY_LIMIT` parameter when instantiating the Jenkins Ephemeral or Jenkins Persistent template.
