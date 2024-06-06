// Module included in the following assemblies:
//
// * virt/install/installing-virt.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-subscribing-cli_{context}"]
= Subscribing to the {VirtProductName} catalog by using the CLI

Before you install {VirtProductName}, you must subscribe to the {VirtProductName} catalog. Subscribing gives the `{CNVNamespace}` namespace access to the {VirtProductName} Operators.

To subscribe, configure `Namespace`, `OperatorGroup`, and `Subscription` objects by applying a single manifest to your cluster.

.Prerequisites
* Install {product-title} {product-version} on your cluster.
* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure
ifdef::openshift-enterprise[]
. Create a YAML file that contains the following manifest:
//Note that there are two versions of the following YAML file; the first one is for openshift-enterprise and the second is for openshift-origin (aka OKD).
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Namespace
metadata:
  name: {CNVNamespace}
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: kubevirt-hyperconverged-group
  namespace: {CNVNamespace}
spec:
  targetNamespaces:
    - {CNVNamespace}
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: hco-operatorhub
  namespace: {CNVNamespace}
spec:
  source: {CNVSubscriptionSpecSource}
  sourceNamespace: openshift-marketplace
  name: {CNVSubscriptionSpecName}
  startingCSV: kubevirt-hyperconverged-operator.v{HCOVersion}
  channel: "stable" <1>
----
<1> Using the `stable` channel ensures that you install the version of
{VirtProductName} that is compatible with your {product-title} version.
endif::openshift-enterprise[]

ifdef::openshift-origin[]
. Create a YAML file that contains the following manifest:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Namespace
metadata:
  name: {CNVNamespace}
---
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: kubevirt-hyperconverged-group
  namespace: {CNVNamespace}
spec: {}
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: hco-operatorhub
  namespace: {CNVNamespace}
spec:
  source: {CNVSubscriptionSpecSource}
  sourceNamespace: openshift-marketplace
  name: {CNVSubscriptionSpecName}
  startingCSV: kubevirt-hyperconverged-operator.v{HCOVersion}
  channel: "stable" <1>
----
<1> Using the `stable` channel ensures that you install the version of
{VirtProductName} that is compatible with your {product-title} version.
endif::openshift-origin[]

. Create the required `Namespace`, `OperatorGroup`, and `Subscription` objects
for {VirtProductName} by running the following command:
+
[source,terminal]
----
$ oc apply -f <file name>.yaml
----
