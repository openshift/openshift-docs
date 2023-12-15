// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc

:_mod-docs-content-type: PROCEDURE

[id="olmv1-installing-an-operator_{context}"]
= Installing an Operator

You can install an Operator from a catalog by creating an Operator custom resource (CR) and applying it to the cluster.

.Prerequisite

* You have added a catalog to your cluster.
* You have inspected the details of an Operator to find what version you want to install.

.Procedure

. Create an Operator CR, similar to the following example:
+
.Example `test-operator.yaml` CR
[source,yaml]
----
apiVersion: operators.operatorframework.io/v1alpha1
kind: Operator
metadata:
  name: quay-example
spec:
  packageName: quay-operator
  version: 3.8.12
----

. Apply the Operator CR to the cluster by running the following command:
+
[source,terminal]
----
$ oc apply -f test-operator.yaml
----
+
.Example output
[source,text]
----
operator.operators.operatorframework.io/quay-example created
----

.Verification

. View the Operator's CR in the YAML format by running the following command:
+
[source,terminal]
----
$ oc get operator.operators.operatorframework.io/quay-example -o yaml
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
      {"apiVersion":"operators.operatorframework.io/v1alpha1","kind":"Operator","metadata":{"annotations":{},"name":"quay-example"},"spec":{"packageName":"quay-operator","version":"3.8.12"}}
  creationTimestamp: "2023-10-19T18:39:37Z"
  generation: 1
  name: quay-example
  resourceVersion: "45663"
  uid: 2558623b-8689-421c-8ed5-7b14234af166
spec:
  packageName: quay-operator
  version: 3.8.12
status:
  conditions:
  - lastTransitionTime: "2023-10-19T18:39:37Z"
    message: resolved to "registry.redhat.io/quay/quay-operator-bundle@sha256:bf26c7679ea1f7b47d2b362642a9234cddb9e366a89708a4ffcbaf4475788dc7"
    observedGeneration: 1
    reason: Success
    status: "True"
    type: Resolved
  - lastTransitionTime: "2023-10-19T18:39:46Z"
    message: installed from "registry.redhat.io/quay/quay-operator-bundle@sha256:bf26c7679ea1f7b47d2b362642a9234cddb9e366a89708a4ffcbaf4475788dc7"
    observedGeneration: 1
    reason: Success
    status: "True"
    type: Installed
  installedBundleResource: registry.redhat.io/quay/quay-operator-bundle@sha256:bf26c7679ea1f7b47d2b362642a9234cddb9e366a89708a4ffcbaf4475788dc7
  resolvedBundleResource: registry.redhat.io/quay/quay-operator-bundle@sha256:bf26c7679ea1f7b47d2b362642a9234cddb9e366a89708a4ffcbaf4475788dc7
----

. Get information about your Operator's controller manager pod by running the following command:
+
[source,terminal]
----
$ oc get pod -n quay-operator-system
----
+
.Example output
[source,text]
----
NAME                                     READY   STATUS    RESTARTS   AGE
quay-operator.v3.8.12-6677b5c98f-2kdtb   1/1     Running   0          2m28s
----
