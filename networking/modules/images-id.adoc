// Module included in the following assemblies:
// * openshift_images/images-understand.aodc

[id="images-id_{context}"]
= Image IDs

An image ID is a SHA (Secure Hash Algorithm) code that can be used to pull an image. A SHA image ID cannot change. A specific SHA identifier always references the exact same container image content.  For example:

[source,text]
----
docker.io/openshift/jenkins-2-centos7@sha256:ab312bda324
----
