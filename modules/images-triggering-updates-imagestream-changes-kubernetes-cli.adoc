// Module included in the following assemblies:
//
// * openshift_images/triggering-updates-on-imagestream-changes.adoc


:_mod-docs-content-type: PROCEDURE
[id="images-triggering-updates-imagestream-changes-kubernetes-cli_{context}"]
= Setting the image trigger on Kubernetes resources

When adding an image trigger to deployments, you can use the `oc set triggers` command. For example, the sample command in this procedure adds an image change trigger to the deployment named `example` so that when the `example:latest` image stream tag is updated, the `web` container inside the deployment updates with the new image value. This command sets the correct `image.openshift.io/triggers` annotation on the deployment resource.

.Procedure

* Trigger Kubernetes resources by entering the `oc set triggers` command:
+
[source,terminal]
----
$ oc set triggers deploy/example --from-image=example:latest -c web
----
+
.Example deployment with trigger annotation
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    image.openshift.io/triggers: '[{"from":{"kind":"ImageStreamTag","name":"example:latest"},"fieldPath":"spec.template.spec.containers[?(@.name==\"container\")].image"}]'
# ...
----
+
Unless the deployment is paused, this pod template update automatically causes a deployment to occur with the new image value.
