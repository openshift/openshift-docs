// Module included in the following assemblies:
//
// * openshift_images/triggering-updates-on-imagestream-changes.adoc


[id="images-triggering-updates-imagestream-changes-kubernetes-about_{context}"]
= Triggering Kubernetes resources

Kubernetes resources do not have fields for triggering, unlike deployment and build configurations, which include as part of their API definition a set of fields for controlling triggers. Instead, you can use annotations in {product-title} to request triggering.

The annotation is defined as follows:

[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  annotations:
    image.openshift.io/triggers:
      [
       {
         "from": {
           "kind": "ImageStreamTag", <1>
           "name": "example:latest", <2>
           "namespace": "myapp" <3>
         },
         "fieldPath": "spec.template.spec.containers[?(@.name==\"web\")].image", <4>
         "paused": false <5>
       },
      # ...
      ]
# ...
----
<1> Required: `kind` is the resource to trigger from must be `ImageStreamTag`.
<2> Required: `name` must be the name of an image stream tag.
<3> Optional: `namespace` defaults to the namespace of the object.
<4> Required: `fieldPath` is the JSON path to change. This field is limited and accepts only a JSON path expression that precisely matches a container by ID or index. For pods, the JSON path is `spec.containers[?(@.name='web')].image`.
<5> Optional: `paused` is whether or not the trigger is paused, and the default value is `false`. Set `paused` to `true` to temporarily disable this trigger.

When one of the core Kubernetes resources contains both a pod template and this annotation, {product-title} attempts to update the object by using the image currently associated with the image stream tag that is referenced by trigger. The update is performed against the `fieldPath` specified.

Examples of core Kubernetes resources that can contain both a pod template and annotation include:

* `CronJobs`
* `Deployments`
* `StatefulSets`
* `DaemonSets`
* `Jobs`
* `ReplicationControllers`
* `Pods`
