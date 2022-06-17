// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc

[id="olm-csv_{context}"]
= Cluster service version

A _cluster service version_ (CSV) represents a specific version of a running Operator on an {product-title} cluster. It is a YAML manifest created from Operator metadata that assists Operator Lifecycle Manager (OLM) in running the Operator in the cluster.

OLM requires this metadata about an Operator to ensure that it can be kept running safely on a cluster, and to provide information about how updates should be applied as new versions of the Operator are published. This is similar to packaging software for a traditional operating system; think of the packaging step for OLM as the stage at which you make your `rpm`, `deb`, or `apk` bundle.

A CSV includes the metadata that accompanies an Operator container image, used to populate user interfaces with information such as its name, version, description, labels, repository link, and logo.

A CSV is also a source of technical information required to run the Operator, such as which custom resources (CRs) it manages or depends on, RBAC rules, cluster requirements, and install strategies. This information tells OLM how to create required resources and set up the Operator as a deployment.

////
Metadata::
* Application metadata:
** Name, description, version (semver compliant), links, labels, icon, etc.

Install strategy::
* Type: Deployment
** Set of service accounts and required permissions
** Set of Deployments.

Custom Resource Definitions (CRDs)::
* Type
* Owned: Managed by this service
* Required: Must exist in the cluster for this service to run
* Resources: A list of resources that the Operator interacts with
* Descriptors: Annotate CRD spec and status fields to provide semantic information
////
