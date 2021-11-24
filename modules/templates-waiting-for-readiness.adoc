// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

[id="templates-waiting-for-readiness_{context}"]
= Waiting for template readiness

Template authors can indicate that certain objects within a template should be waited for before a template instantiation by the service catalog, {tsb-name}, or `TemplateInstance` API is considered complete.

To use this feature, mark one or more objects of kind `Build`, `BuildConfig`, `Deployment`, `DeploymentConfig`, `Job`, or `StatefulSet` in a template with the following annotation:

[source,text]
----
"template.alpha.openshift.io/wait-for-ready": "true"
----

Template instantiation is not complete until all objects marked with the annotation report ready. Similarly, if any of the annotated objects report failed, or if the template fails to become ready within a fixed timeout of one hour, the template instantiation fails.

For the purposes of instantiation, readiness and failure of each object kind are defined as follows:

[cols="1a,2a,2a", options="header"]
|===

| Kind
| Readiness
| Failure

| `Build`
| Object reports phase complete.
| Object reports phase canceled, error, or failed.

| `BuildConfig`
| Latest associated build object reports phase complete.
| Latest associated build object reports phase canceled, error, or failed.

| `Deployment`
| Object reports new replica set and deployment available. This honors readiness probes defined on the object.
| Object reports progressing condition as false.

|`DeploymentConfig`
| Object reports new replication controller and deployment available. This honors readiness probes defined on the object.
| Object reports progressing condition as false.

| `Job`
| Object reports completion.
| Object reports that one or more failures have occurred.

| `StatefulSet`
| Object reports all replicas ready. This honors readiness probes defined on
the object.
| Not applicable.
|===

The following is an example template extract, which uses the `wait-for-ready` annotation. Further examples can be found in the {product-title} quick start templates.

[source,yaml]
----
kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: my-template
objects:
- kind: BuildConfig
  apiVersion: build.openshift.io/v1
  metadata:
    name: ...
    annotations:
      # wait-for-ready used on BuildConfig ensures that template instantiation
      # will fail immediately if build fails
      template.alpha.openshift.io/wait-for-ready: "true"
  spec:
    ...
- kind: DeploymentConfig
  apiVersion: apps.openshift.io/v1
  metadata:
    name: ...
    annotations:
      template.alpha.openshift.io/wait-for-ready: "true"
  spec:
    ...
- kind: Service
  apiVersion: v1
  metadata:
    name: ...
  spec:
    ...
----

.Additional recommendations

* Set memory, CPU, and storage default sizes to make sure your application is given enough resources to run smoothly.

* Avoid referencing the `latest` tag from images if that tag is used across major versions. This can cause running applications to break when new images are pushed to that tag.

* A good template builds and deploys cleanly without requiring modifications after the template is deployed.
