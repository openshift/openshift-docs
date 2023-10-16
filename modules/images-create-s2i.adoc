// Module included in the following assemblies:
//
// * builds/build-strategies.adoc
// * openshift_images/create-images.adoc

[id="images-create-s2i_{context}"]
= Creating images from source code with source-to-image

Source-to-image (S2I) is a framework that makes it easy to write images that take application source code as an input and produce a new image that runs the assembled application as output.

The main advantage of using S2I for building reproducible container images is the ease of use for developers. As a builder image author, you must understand two basic concepts in order for your images to provide the best S2I performance, the build process and S2I scripts.
