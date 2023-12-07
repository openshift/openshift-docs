// Module included in the following assemblies:
//
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * openshift_images/configuring-samples-operator.adoc

[id="installation-images-samples-disconnected-mirroring-assist_{context}"]
= Cluster Samples Operator assistance for mirroring

During installation, {product-title} creates a config map named `imagestreamtag-to-image` in the `openshift-cluster-samples-operator` namespace. The `imagestreamtag-to-image` config map contains an entry, the populating image, for each image stream tag.

The format of the key for each entry in the data field in the config map is `<image_stream_name>_<image_stream_tag_name>`.

ifndef::openshift-rosa;openshift-dedicated[]
During a disconnected installation of {product-title}, the status of the Cluster Samples Operator is set to `Removed`. If you choose to change it to `Managed`, it installs samples.
[NOTE]
====
The use of samples in a network-restricted or discontinued environment may require access to services external to your network. Some example services include: Github, Maven Central, npm, RubyGems, PyPi and others. There might be additional steps to take that allow the cluster samples operators's objects to reach the services they require.
====
endif::openshift-rosa;openshift-dedicated[]

You can use this config map as a reference for which images need to be mirrored for your image streams to import.

* While the Cluster Samples Operator is set to `Removed`, you can create your mirrored registry, or determine which existing mirrored registry you want to use.
* Mirror the samples you want to the mirrored registry using the new config map as your guide.
* Add any of the image streams you did not mirror to the `skippedImagestreams` list of the Cluster Samples Operator configuration object.
* Set `samplesRegistry` of the Cluster Samples Operator configuration object to the mirrored registry.
* Then set the Cluster Samples Operator to `Managed` to install the image streams you have mirrored.
