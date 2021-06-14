// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc
// * Unused. Can be removed by 4.9 if still unused. Request full peer review for the module if it’s used.

[id="images-using-images-s2i-perl_{context}"]
= Perl overview

{product-title} provides source-to-image (S2I) enabled Perl images for building and running Perl applications. The Perl S2I builder image assembles your application source with any required dependencies to create a new image containing your Perl application. This resulting image can be run either by {product-title} or by a container runtime.

[id="images-using-images-s2i-perl-accessing-logs_{context}"]
== Accessing logs
Access logs are streamed to standard output and as such they can be viewed using the `oc logs` command. Error logs are stored in the `/tmp/error_log` file, which can be viewed using the `oc rsh` command to access the container.
