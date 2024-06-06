// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc

:_mod-docs-content-type: CONCEPT
[id="images-s2i-build-process-overview_{context}"]
= Source-to-image build process overview

Source-to-image (S2I) produces ready-to-run images by injecting source code into a container that prepares that source code to be run. It performs the following steps:

. Runs the `FROM <builder image>` command
. Copies the source code to a defined location in the builder image
. Runs the assemble script in the builder image
. Sets the run script in the builder image as the default command

Buildah then creates the container image.
