// Module included in the following assemblies:
// * openshift_images/tagging-images

[id="images-tagging-conventions_{context}"]
= Image tag conventions

Images evolve over time and their tags reflect this. Generally, an image tag always points to the latest image built.

If there is too much information embedded in a tag name, like `v2.0.1-may-2019`, the tag points to just one revision of an image and is never updated. Using default image pruning options, such an image is never removed.
ifdef::openshift-origin,openshift-enterprise,openshift-webscale[]
In very large clusters, the schema of creating new tags for every revised image could eventually fill up the etcd datastore with excess tag metadata for images that are long outdated.
endif::[]

If the tag is named `v2.0`, image revisions are more likely. This results in longer tag history and, therefore, the image pruner is more likely to remove old and unused images.

Although tag naming convention is up to you, here are a few examples in the format `<image_name>:<image_tag>`:

.Image tag naming conventions
[width="50%",options="header"]
|===
|Description |Example

|Revision
|`myimage:v2.0.1`

|Architecture
|`myimage:v2.0-x86_64`

|Base image
|`myimage:v1.2-centos7`

|Latest (potentially unstable)
|`myimage:latest`

|Latest stable
|`myimage:stable`
|===

If you require dates in tag names, periodically inspect old and unsupported images and `istags` and remove them. Otherwise, you can experience increasing resource usage caused by retaining old images.
