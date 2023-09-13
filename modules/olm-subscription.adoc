// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc

ifdef::openshift-origin[]
:global_ns: olm
endif::[]
ifndef::openshift-origin[]
:global_ns: openshift-marketplace
endif::[]

[id="olm-subscription_{context}"]
= Subscription

A _subscription_, defined by a `Subscription` object, represents an intention to install an Operator. It is the custom resource that relates an Operator to a catalog source.

Subscriptions describe which channel of an Operator package to subscribe to, and whether to perform updates automatically or manually. If set to automatic, the subscription ensures Operator Lifecycle Manager (OLM) manages and upgrades the Operator to ensure that the latest version is always running in the cluster.

.Example `Subscription` object
[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: example-operator
  namespace: example-namespace
spec:
  channel: stable
  name: example-operator
  source: example-catalog
  sourceNamespace: {global_ns}
----

This `Subscription` object defines the name and namespace of the Operator, as well as the catalog from which the Operator data can be found. The channel, such as `alpha`, `beta`, or `stable`, helps determine which Operator stream should be installed from the catalog source.

The names of channels in a subscription can differ between Operators, but the naming scheme should follow a common convention within a given Operator. For example, channel names might follow a minor release update stream for the application provided by the Operator (`1.2`, `1.3`) or a release frequency (`stable`, `fast`).

In addition to being easily visible from the {product-title} web console, it is possible to identify when there is a newer version of an Operator available by inspecting the status of the related subscription. The value associated with the `currentCSV` field is the newest version that is known to OLM, and `installedCSV` is the version that is installed on the cluster.

ifdef::openshift-origin[]
:!global_ns:
endif::[]
ifndef::openshift-origin[]
:!global_ns:
endif::[]
