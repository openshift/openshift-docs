// Module included in the following assemblies:
// * openshift_images/image-streams-managing.adoc

[id="images-using-imagestream-change-triggers_{context}"]
= Image stream change triggers

Image stream triggers allow your builds and deployments to be automatically
invoked when a new version of an upstream image is available.

//from FAQ

For example, builds and deployments can be automatically started when an image
stream tag is modified. This is achieved by monitoring that particular image
stream tag and notifying the build or deployment when a change is detected.
