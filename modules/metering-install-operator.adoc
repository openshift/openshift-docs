// Module included in the following assemblies:
//
// * metering/metering-installing-metering.adoc

[id="metering-install-operator_{context}"]
= Installing the Metering Operator

You can install metering by deploying the Metering Operator. The Metering Operator creates and manages the components of the metering stack.

[NOTE]
====
You cannot create a project starting with `openshift-` using the web console or by using the `oc new-project` command in the CLI.
====

[NOTE]
====
If the Metering Operator is installed using a namespace other than `openshift-metering`, the metering reports are only viewable using the CLI. It is strongly suggested throughout the installation steps to use the `openshift-metering` namespace.
====

[id="metering-install-web-console_{context}"]
== Installing metering using the web console
You can use the {product-title} web console to install the Metering Operator.

.Procedure

.  Create a namespace object YAML file for the Metering Operator with the `oc create -f <file-name>.yaml` command. You must use the CLI to create the namespace. For example, `metering-namespace.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-metering <1>
  annotations:
    openshift.io/node-selector: "" <2>
  labels:
    openshift.io/cluster-monitoring: "true"
----
<1> It is strongly recommended to deploy metering in the `openshift-metering` namespace.
<2> Include this annotation before configuring specific node selectors for the operand pods.

.  In the {product-title} web console, click *Operators* -> *OperatorHub*. Filter for `metering` to find the Metering Operator.

.  Click the *Metering* card, review the package description, and then click *Install*.
.  Select an *Update Channel*, *Installation Mode*, and *Approval Strategy*.
.  Click *Install*.

.  Verify that the Metering Operator is installed by switching to the *Operators* -> *Installed Operators* page. The Metering Operator has a *Status* of *Succeeded* when the installation is complete.
+
[NOTE]
====
It might take several minutes for the Metering Operator to appear.
====

. Click *Metering* on the *Installed Operators* page for Operator *Details*. From the *Details* page you can create different resources related to metering.

To complete the metering installation, create a `MeteringConfig` resource to configure metering and install the components of the metering stack.

[id="metering-install-cli_{context}"]
== Installing metering using the CLI

You can use the {product-title} CLI to install the Metering Operator.

.Procedure

. Create a `Namespace` object YAML file for the Metering Operator. You must use the CLI to create the namespace. For example, `metering-namespace.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-metering <1>
  annotations:
    openshift.io/node-selector: "" <2>
  labels:
    openshift.io/cluster-monitoring: "true"
----
<1> It is strongly recommended to deploy metering in the `openshift-metering` namespace.
<2> Include this annotation before configuring specific node selectors for the operand pods.

.  Create the `Namespace` object:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
For example:
+
[source,terminal]
----
$ oc create -f openshift-metering.yaml
----

.  Create the `OperatorGroup` object YAML file. For example, `metering-og`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-metering <1>
  namespace: openshift-metering <2>
spec:
  targetNamespaces:
  - openshift-metering
----
<1> The name is arbitrary.
<2> Specify the `openshift-metering` namespace.

.  Create a `Subscription` object YAML file to subscribe a namespace to the Metering Operator. This object targets the most recently released version in the `redhat-operators` catalog source. For example, `metering-sub.yaml`:
+
[source,yaml, subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: metering-ocp <1>
  namespace: openshift-metering <2>
spec:
  channel: "{product-version}" <3>
  source: "redhat-operators" <4>
  sourceNamespace: "openshift-marketplace"
  name: "metering-ocp"
  installPlanApproval: "Automatic" <5>
----
<1> The name is arbitrary.
<2> You must specify the `openshift-metering` namespace.
<3> Specify {product-version} as the channel.
<4> Specify the `redhat-operators` catalog source, which contains the `metering-ocp` package manifests. If your {product-title} is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator LifeCycle Manager (OLM).
<5> Specify "Automatic" install plan approval.
