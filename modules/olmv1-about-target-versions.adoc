// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc
// * operators/olm_v1/arch/olmv1-operator-controller.adoc

:_mod-docs-content-type: CONCEPT

[id="olmv1-about-operator-updates_{context}"]
= About target versions in {olmv1}

In {olmv1-first}, cluster administrators set the target version of an Operator declaratively in the Operator's custom resource (CR).

If you specify a channel in the Operator's CR, {olmv1} installs the latest release from the specified channel. When updates are published to the specified channel, {olmv1} automatically updates to the latest release from the channel.

.Example CR with a specified channel
[source,yaml]
----
apiVersion: operators.operatorframework.io/v1alpha1
kind: Operator
metadata:
  name: quay-example
spec:
  packageName: quay-operator
  channel: stable-3.8 <1>
----
<1> Installs the latest release published to the specified channel. Updates to the channel are automatically installed.

If you specify the Operator's target version in the CR, {olmv1} installs the specified version. When the target version is specified in the Operator's CR, {olmv1} does not change the target version when updates are published to the catalog.

If you want to update the version of the Operator that is installed on the cluster, you must manually update the Operator's CR. Specifying a Operator's target version pins the Operator's version to the specified release.

.Example CR with the target version specified
[source,yaml]
----
apiVersion: operators.operatorframework.io/v1alpha1
kind: Operator
metadata:
  name: quay-example
spec:
  packageName: quay-operator
  version: 3.8.12 <1>
----
<1> Specifies the target version. If you want to update the version of the Operator that is installed on the cluster, you must manually update this field the Operator's CR to the desired target version.

If you want to change the installed version of an Operator, edit the Operator's CR to the desired target version.

[WARNING]
====
In previous versions of OLM, Operator authors could define upgrade edges to prevent you from updating to unsupported versions. In its current state of development, {olmv1} does not enforce upgrade edge definitions. You can specify any version of an Operator, and {olmv1} attempts to apply the update.
====

You can inspect an Operator's catalog contents, including available versions and channels, by running the following command:

.Command syntax
[source,terminal]
----
$ oc get package <catalog_name>-<package_name> -o yaml
----

After you create or update a CR, create or configure the Operator by running the following command:

.Command syntax
[source,terminal]
----
$ oc apply -f <extension_name>.yaml
----

.Troubleshooting

* If you specify a target version or channel that does not exist, you can run the following command to check the status of your Operator:
+
[source,terminal]
----
$ oc get operator.operators.operatorframework.io <operator_name> -o yaml
----
+
.Example output
[source,text]
----
apiVersion: operators.operatorframework.io/v1alpha1
kind: Operator
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"operators.operatorframework.io/v1alpha1","kind":"Operator","metadata":{"annotations":{},"name":"quay-example"},"spec":{"packageName":"quay-operator","version":"999.99.9"}}
  creationTimestamp: "2023-10-19T18:39:37Z"
  generation: 3
  name: quay-example
  resourceVersion: "51505"
  uid: 2558623b-8689-421c-8ed5-7b14234af166
spec:
  packageName: quay-operator
  version: 999.99.9
status:
  conditions:
  - lastTransitionTime: "2023-10-19T18:50:34Z"
    message: package 'quay-operator' at version '999.99.9' not found
    observedGeneration: 3
    reason: ResolutionFailed
    status: "False"
    type: Resolved
  - lastTransitionTime: "2023-10-19T18:50:34Z"
    message: installation has not been attempted as resolution failed
    observedGeneration: 3
    reason: InstallationStatusUnknown
    status: Unknown
    type: Installed
----
