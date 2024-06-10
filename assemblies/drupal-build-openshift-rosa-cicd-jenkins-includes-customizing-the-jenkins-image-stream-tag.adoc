// Module included in the following assemblies:
//
// * cicd/jenkins/important-changes-to-openshift-jenkins-images.adoc
:_mod-docs-content-type: PROCEDURE

[id="customizing-the-jenkins-image-stream-tag_{context}"]
= Customizing the Jenkins image stream tag

To override the default upgrade behavior and control how the Jenkins image is upgraded, you set the image stream tag value that your Jenkins deployment configurations use.

The default upgrade behavior is the behavior that existed when the Jenkins image was part of the install payload. The image stream tag names, `2` and `ocp-upgrade-redeploy`, in the `jenkins-rhel.json` image stream file use SHA-specific image references. Therefore, when those tags are updated with a new SHA, the {product-title} image change controller automatically redeploys the Jenkins deployment configuration from the associated templates, such as `jenkins-ephemeral.json` or `jenkins-persistent.json`.

For new deployments, to override that default value, you change the value of the  `JENKINS_IMAGE_STREAM_TAG` in the `jenkins-ephemeral.json` Jenkins template. For example, replace the `2` in `"value": "jenkins:2"` with one of the following image stream tags:

* `ocp-upgrade-redeploy`, the default value, updates your Jenkins image when you upgrade {product-title}.
* `user-maintained-upgrade-redeploy` requires you to manually redeploy Jenkins by running `$ oc import-image jenkins:user-maintained-upgrade-redeploy -n openshift` after upgrading {product-title}.
* `scheduled-upgrade-redeploy` periodically checks the given `<image>:<tag>` combination for changes and upgrades the image when it changes. The image change controller pulls the changed image and redeploys the Jenkins deployment configuration provisioned by the templates. For more information about this scheduled import policy, see the "Adding tags to image streams" in the following "Additional resources."

[NOTE]
====
To override the current upgrade value for existing deployments, change the values of the environment variables that correspond to those template parameters.
====

.Prerequisites

* You are running OpenShift Jenkins on {product-title} {product-version}.
* You know the namespace where OpenShift Jenkins is deployed.

.Procedure

* Set the image stream tag value, replacing `<namespace>` with namespace where OpenShift Jenkins is deployed and `<image_stream_tag>` with an image stream tag:
+
.Example
[source,terminal]
----
$ oc patch dc jenkins -p '{"spec":{"triggers":[{"type":"ImageChange","imageChangeParams":{"automatic":true,"containerNames":["jenkins"],"from":{"kind":"ImageStreamTag","namespace":"<namespace>","name":"jenkins:<image_stream_tag>"}}}]}}'
----
+
[TIP]
====
Alternatively, to edit the Jenkins deployment configuration YAML, enter `$ oc edit dc/jenkins -n <namespace>` and update the `value: 'jenkins:<image_stream_tag>'` line.
====
