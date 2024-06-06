[id="applications-create-using-cli-image_{context}"]
= Creating an application from an image

You can deploy an application from an existing image. Images can come from image streams in the {product-title} server, images in a specific registry, or images in the local Docker server.

The `new-app` command attempts to determine the type of image specified in the arguments passed to it. However, you can explicitly tell `new-app` whether the image is a container image using the `--docker-image` argument or an image stream using the `-i|--image-stream` argument.

[NOTE]
====
If you specify an image from your local Docker repository, you must ensure that the same image is available to the {product-title} cluster nodes.
====

== Docker Hub MySQL image

Create an application from the Docker Hub MySQL image, for example:

[source,terminal]
----
$ oc new-app mysql
----

== Image in a private registry

Create an application using an image in a private registry, specify the full container image specification:

[source,terminal]
----
$ oc new-app myregistry:5000/example/myimage
----

== Existing image stream and optional image stream tag

Create an application from an existing image stream and optional image stream tag:

[source,terminal]
----
$ oc new-app my-stream:v1
----
