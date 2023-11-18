// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * openshift_images/samples-operator-alt-registry.adoc

ifeval::["{context}" == "post-install-cluster-tasks"]
:restrictednetwork:
endif::[]

ifeval::["{context}" == "samples-operator-alt-registry"]
:samplesoperatoraltreg:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="installation-restricted-network-samples_{context}"]
= Using Cluster Samples Operator image streams with alternate or mirrored registries

Most image streams in the `openshift` namespace managed by the Cluster Samples Operator
point to images located in the Red Hat registry at link:https://registry.redhat.io[registry.redhat.io].
ifdef::restrictednetwork[]
Mirroring
will not apply to these image streams.
endif::[]

[NOTE]
====
The `cli`, `installer`, `must-gather`, and `tests` image streams, while
part of the install payload, are not managed by the Cluster Samples Operator. These are
not addressed in this procedure.
====

[IMPORTANT]
====
The Cluster Samples Operator must be set to `Managed` in a disconnected environment. To install the image streams, you have a mirrored registry.
====

.Prerequisites
ifndef::openshift-rosa,openshift-dedicated[]
* Access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* Access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* Create a pull secret for your mirror registry.

.Procedure

. Access the images of a specific image stream to mirror, for example:
+
[source,terminal]
----
$ oc get is <imagestream> -n openshift -o json | jq .spec.tags[].from.name | grep registry.redhat.io
----
+
. Mirror images from link:https://registry.redhat.io[registry.redhat.io] associated with any image streams you need
ifdef::restrictednetwork[]
in the restricted network environment into one of the defined mirrors, for example:
endif::[]
ifdef::configsamplesoperator[]
into your defined preferred registry, for example:
endif::[]
+
[source,terminal]
----
$ oc image mirror registry.redhat.io/rhscl/ruby-25-rhel7:latest ${MIRROR_ADDR}/rhscl/ruby-25-rhel7:latest
----

. Create the cluster's image configuration object:
+
[source,terminal]
----
$ oc create configmap registry-config --from-file=${MIRROR_ADDR_HOSTNAME}..5000=$path/ca.crt -n openshift-config
----

. Add the required trusted CAs for the mirror in the cluster's image
configuration object:
+
[source,terminal]
----
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-config"}}}' --type=merge
----

. Update the `samplesRegistry` field in the Cluster Samples Operator configuration object
to contain the `hostname` portion of the mirror location defined in the mirror
configuration:
+
[source,terminal]
----
$ oc edit configs.samples.operator.openshift.io -n openshift-cluster-samples-operator
----
+
[NOTE]
====
This is required because the image stream import process does not use the mirror or search mechanism at this time.
====
+
. Add any image streams that are not mirrored into the `skippedImagestreams` field
of the Cluster Samples Operator configuration object. Or if you do not want to support
any of the sample image streams, set the Cluster Samples Operator to `Removed` in the
Cluster Samples Operator configuration object.
+
[NOTE]
====
The Cluster Samples Operator issues alerts if image stream imports are failing but the Cluster Samples Operator is either periodically retrying or does not appear to be retrying them.
====
+
Many of the templates in the `openshift` namespace
reference the image streams. So using `Removed` to purge both the image streams
and templates will eliminate the possibility of attempts to use them if they
are not functional because of any missing image streams.

ifeval::["{context}" == "post-install-cluster-tasks"]
:!restrictednetwork:
endif::[]

ifeval::["{context}" == "samples-operator-alt-registry"]
:!samplesoperatoraltreg:
endif::[]
