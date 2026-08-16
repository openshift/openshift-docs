// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins-agent.adoc

:_mod-docs-content-type: CONCEPT
[id="images-other-jenkins-agent-memory_{context}"]
= Jenkins agent memory requirements

A JVM is used in all Jenkins agents to host the Jenkins JNLP agent as well as to run any Java applications such as `javac`, Maven, or Gradle.

By default, the Jenkins JNLP agent JVM uses 50% of the container memory limit for its heap. This value can be modified by the `CONTAINER_HEAP_PERCENT` environment variable. It can also be capped at an upper limit or overridden entirely.

By default, any other processes run in the Jenkins agent container, such as shell scripts or `oc` commands run from pipelines, cannot use more than the remaining 50% memory limit without provoking an OOM kill.

By default, each further JVM process that runs in a Jenkins agent container uses up to 25% of the container memory limit for its heap. It might be necessary to tune this limit for many build workloads.
