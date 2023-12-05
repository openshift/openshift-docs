// Module included in the following assemblies:
//
// * cicd/jenkins/important-changes-to-openshift-jenkins-images.adoc
:_mod-docs-content-type: CONCEPT

[id="relocation-of-openshift-jenkins-images_{context}"]
= Relocation of OpenShift Jenkins images

{product-title} 4.11 makes significant changes to the location and availability of specific OpenShift Jenkins images. Additionally, you can configure when and how to update these images.

.What stays the same with the OpenShift Jenkins images?

* The Cluster Samples Operator manages the `ImageStream` and `Template` objects for operating the OpenShift Jenkins images.
* By default, the Jenkins `DeploymentConfig` object from the Jenkins pod template triggers a redeployment when the Jenkins image changes. By default, this image is referenced by the `jenkins:2` image stream tag of Jenkins image stream in the `openshift` namespace in the `ImageStream` YAML file in the Samples Operator payload.
* If you upgrade from {product-title} 4.10 and earlier to 4.11, the deprecated `maven` and `nodejs` pod templates are still in the default image configuration.
* If you upgrade from {product-title} 4.10 and earlier to 4.11, the `jenkins-agent-maven` and `jenkins-agent-nodejs` image streams still exist in your cluster. To maintain these image streams, see the following section, "What happens with the `jenkins-agent-maven` and `jenkins-agent-nodejs` image streams in the `openshift` namespace?"

.What changes in the support matrix of the OpenShift Jenkins image?

Each new image in the `ocp-tools-4` repository in the `registry.redhat.io` registry supports multiple versions of {product-title}. When Red Hat updates one of these new images, it is simultaneously available for all versions. This availability is ideal when Red Hat updates an image in response to a security advisory. Initially, this change applies to {product-title} 4.11 and later. It is planned that this change will eventually apply to {product-title} 4.9 and later.

Previously, each Jenkins image supported only one version of {product-title} and Red Hat might update those images sequentially over time.

.What additions are there with the OpenShift Jenkins and Jenkins Agent Base ImageStream and ImageStreamTag objects?

By moving from an in-payload image stream to an image stream that references non-payload images, {product-title} can define additional image stream tags. Red Hat has created a series of new image stream tags to go along with the existing `"value": "jenkins:2"` and `"value": "image-registry.openshift-image-registry.svc:5000/openshift/jenkins-agent-base-rhel8:latest"` image stream tags present in {product-title} 4.10 and earlier. These new image stream tags address some requests to improve how the Jenkins-related image streams are maintained.

About the new image stream tags:

`ocp-upgrade-redeploy`:: To update your Jenkins image when you upgrade {product-title}, use this image stream tag in your Jenkins deployment configuration. This image stream tag corresponds to the existing `2` image stream tag of the `jenkins` image stream and the `latest` image stream tag of the `jenkins-agent-base-rhel8` image stream. It employs an image tag specific to only one SHA or image digest. When the `ocp-tools-4` image changes, such as for Jenkins security advisories, Red Hat Engineering updates the Cluster Samples Operator payload.

`user-maintained-upgrade-redeploy`:: To manually redeploy Jenkins after you upgrade {product-title}, use this image stream tag in your Jenkins deployment configuration. This image stream tag uses the least specific image version indicator available. When you redeploy Jenkins, run the following command: `$ oc import-image jenkins:user-maintained-upgrade-redeploy -n openshift`. When you issue this command, the {product-title} `ImageStream` controller accesses the `registry.redhat.io` image registry and stores any updated images in the {product-registry}'s slot for that Jenkins `ImageStreamTag` object. Otherwise, if you do not run this command, your Jenkins deployment configuration does not trigger a redeployment.

`scheduled-upgrade-redeploy`:: To automatically redeploy the latest version of the Jenkins image when it is released, use this image stream tag in your Jenkins deployment configuration. This image stream tag uses the periodic importing of image stream tags feature of the {product-title} image stream controller, which checks for changes in the backing image. If the image changes, for example, due to a recent Jenkins security advisory, {product-title} triggers a redeployment of your Jenkins deployment configuration. See "Configuring periodic importing of image stream tags" in the following "Additional resources."


.What happens with the `jenkins-agent-maven` and `jenkins-agent-nodejs` image streams in the `openshift` namespace?

The OpenShift Jenkins Maven and NodeJS Agent images for {product-title} were deprecated in 4.10, and are removed from the {product-title} install payload in 4.11. They do not have alternatives defined in the `ocp-tools-4` repository. However, you can work around this by using the sidecar pattern described in the "Jenkins agent" topic mentioned in the following "Additional resources" section.

However, the Cluster Samples Operator does not delete the `jenkins-agent-maven` and `jenkins-agent-nodejs` image streams created by prior releases, which point to the tags of the respective {product-title} payload images on `registry.redhat.io`. Therefore, you can pull updates to these images by running the following commands:

[source,terminal]
----
$ oc import-image jenkins-agent-nodejs -n openshift
----

[source,terminal]
----
$ oc import-image jenkins-agent-maven -n openshift
----
