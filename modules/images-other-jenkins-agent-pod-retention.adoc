// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins-agent.adoc

:_mod-docs-content-type: REFERENCE
[id="images-other-jenkins-agent-pod-retention_{context}"]
= Jenkins agent pod retention

Jenkins agent pods, are deleted by default after the build completes or is stopped. This behavior can be changed by the Kubernetes plugin pod retention setting. Pod retention can be set for all Jenkins builds, with overrides for each pod template. The following behaviors are supported:

* `Always` keeps the build pod regardless of build result.
* `Default` uses the plugin value, which is the pod template only.
* `Never` always deletes the pod.
* `On Failure` keeps the pod if it fails during the build.

You can override pod retention in the pipeline Jenkinsfile:

[source,groovy]
----
podTemplate(label: "mypod",
  cloud: "openshift",
  inheritFrom: "maven",
  podRetention: onFailure(), <1>
  containers: [
    ...
  ]) {
  node("mypod") {
    ...
  }
}
----
<1> Allowed values for `podRetention` are `never()`, `onFailure()`, `always()`, and `default()`.

[WARNING]
====
Pods that are kept might continue to run and count against resource quotas.
====
