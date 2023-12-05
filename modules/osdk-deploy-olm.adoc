// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc
// * operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc
// * operators/operator_sdk/helm/osdk-helm-tutorial.adoc
// * operators/operator_sdk/osdk-working-bundle-images.adoc

ifeval::["{context}" == "osdk-golang-tutorial"]
:golang:
endif::[]
ifeval::["{context}" == "osdk-working-bundle-images"]
:golang:
endif::[]
ifeval::["{context}" == "osdk-java-tutorial"]
:java:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="osdk-deploy-olm_{context}"]
= Deploying an Operator with Operator Lifecycle Manager

Operator Lifecycle Manager (OLM) helps you to install, update, and manage the lifecycle of Operators and their associated services on a Kubernetes cluster. OLM is installed by default on {product-title} and runs as a Kubernetes extension so that you can use the web console and the OpenShift CLI (`oc`) for all Operator lifecycle management functions without any additional tools.

The Operator bundle format is the default packaging method for Operator SDK and OLM. You can use the Operator SDK to quickly run a bundle image on OLM to ensure that it runs properly.

.Prerequisites

- Operator SDK CLI installed on a development workstation
- Operator bundle image built and pushed to a registry
- OLM installed on a Kubernetes-based cluster (v1.16.0 or later if you use `apiextensions.k8s.io/v1` CRDs, for example {product-title} {product-version})
ifndef::openshift-dedicated,openshift-rosa[]
- Logged in to the cluster with `oc` using an account with `cluster-admin` permissions
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
- Logged in to the cluster with `oc` using an account with `dedicated-admin` permissions
endif::openshift-dedicated,openshift-rosa[]
ifdef::golang[]
- If your Operator is Go-based, your project must be updated to use supported images for running on {product-title}
endif::[]

.Procedure

* Enter the following command to run the Operator on the cluster:
+
[source,terminal]
----
$ operator-sdk run bundle \//<1>
    -n <namespace> \//<2>
    <registry>/<user>/<bundle_image_name>:<tag> <3>
----
<1> The `run bundle` command creates a valid file-based catalog and installs the Operator bundle on your cluster using OLM.
<2> Optional: By default, the command installs the Operator in the currently active project in your `~/.kube/config` file. You can add the `-n` flag to set a different namespace scope for the installation.
<3> If you do not specify an image, the command uses `quay.io/operator-framework/opm:latest` as the default index image. If you specify an image, the command uses the bundle image itself as the index image.
+
[IMPORTANT]
====
As of {product-title} 4.11, the `run bundle` command supports the file-based catalog format for Operator catalogs by default. The deprecated SQLite database format for Operator catalogs continues to be supported; however, it will be removed in a future release. It is recommended that Operator authors migrate their workflows to the file-based catalog format.
====
+
This command performs the following actions:
+
--
* Create an index image referencing your bundle image. The index image is opaque and ephemeral, but accurately reflects how a bundle would be added to a catalog in production.
* Create a catalog source that points to your new index image, which enables OperatorHub to discover your Operator.
* Deploy your Operator to your cluster by creating an `OperatorGroup`, `Subscription`, `InstallPlan`, and all other required resources, including RBAC.
--

ifeval::["{context}" == "osdk-golang-tutorial"]
:!golang:
endif::[]
ifeval::["{context}" == "osdk-working-bundle-images"]
:!golang:
endif::[]
ifeval::["{context}" == "osdk-java-tutorial"]
:!java:
endif::[]