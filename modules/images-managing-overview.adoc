// Module included in the following assemblies:
//
// * openshift-images/managing-images.adoc

:_mod-docs-content-type: CONCEPT
[id="images-managing-overview_{context}"]
= Images overview

An image stream comprises any number of container images identified by tags. It presents a single virtual view of related images, similar to a container image repository.

By watching an image stream, builds and deployments can receive notifications when new images are added or modified and react by performing a build or deployment, respectively.
