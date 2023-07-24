// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc

ifdef::openshift-origin[]
:global_ns: olm
endif::[]
ifndef::openshift-origin[]
:global_ns: openshift-marketplace
endif::[]

[id="olm-catalogsource_{context}"]
= Catalog source

A _catalog source_ represents a store of metadata, typically by referencing an _index image_ stored in a container registry. Operator Lifecycle Manager (OLM) queries catalog sources to discover and install Operators and their dependencies. OperatorHub in the {product-title} web console also displays the Operators provided by catalog sources.

[TIP]
====
Cluster administrators can view the full list of Operators provided by an enabled catalog source on a cluster by using the *Administration* -> *Cluster Settings* -> *Configuration* -> *OperatorHub* page in the web console.
====

The `spec` of a `CatalogSource` object indicates how to construct a pod or how to communicate with a service that serves the Operator Registry gRPC API.

.Example `CatalogSource` object
[%collapsible]
====
[source,yaml,subs="attributes+"]
----
﻿apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  generation: 1
  name: example-catalog <1>
  namespace: {global_ns} <2>
  annotations:
    olm.catalogImageTemplate: <3>
      "quay.io/example-org/example-catalog:v{kube_major_version}.{kube_minor_version}.{kube_patch_version}"
spec:
  displayName: Example Catalog <4>
  image: quay.io/example-org/example-catalog:v1 <5>
  priority: -400 <6>
  publisher: Example Org
  sourceType: grpc <7>
  grpcPodConfig:
    securityContextConfig: <security_mode> <8>
    nodeSelector: <9>
      custom_label: <label>
    priorityClassName: system-cluster-critical <10>
    tolerations: <11>
      - key: "key1"
        operator: "Equal"
        value: "value1"
        effect: "NoSchedule"
  updateStrategy:
    registryPoll: <12>
      interval: 30m0s
status:
  connectionState:
    address: example-catalog.{global_ns}.svc:50051
    lastConnect: 2021-08-26T18:14:31Z
    lastObservedState: READY <13>
  latestImageRegistryPoll: 2021-08-26T18:46:25Z <14>
  registryService: <15>
    createdAt: 2021-08-26T16:16:37Z
    port: 50051
    protocol: grpc
    serviceName: example-catalog
    serviceNamespace: {global_ns}
----
<1> Name for the `CatalogSource` object. This value is also used as part of the name for the related pod that is created in the requested namespace.
<2> Namespace to create the catalog in. To make the catalog available cluster-wide in all namespaces, set this value to `{global_ns}`. The default Red Hat-provided catalog sources also use the `{global_ns}` namespace. Otherwise, set the value to a specific namespace to make the Operator only available in that namespace.
<3> Optional: To avoid cluster upgrades potentially leaving Operator installations in an unsupported state or without a continued update path, you can enable automatically changing your Operator catalog's index image version as part of cluster upgrades.
+
Set the `olm.catalogImageTemplate` annotation to your index image name and use one or more of the Kubernetes cluster version variables as shown when constructing the template for the image tag. The annotation overwrites the `spec.image` field at run time. See the "Image template for custom catalog sources" section for more details.
<4> Display name for the catalog in the web console and CLI.
<5> Index image for the catalog. Optionally, can be omitted when using the `olm.catalogImageTemplate` annotation, which sets the pull spec at run time.
<6> Weight for the catalog source. OLM uses the weight for prioritization during dependency resolution. A higher weight indicates the catalog is preferred over lower-weighted catalogs.
<7> Source types include the following:
+
--
* `grpc` with an `image` reference: OLM pulls the image and runs the pod, which is expected to serve a compliant API.
* `grpc` with an `address` field: OLM attempts to contact the gRPC API at the given address. This should not be used in most cases.
* `configmap`: OLM parses config map data and runs a pod that can serve the gRPC API over it.
--
<8> Specify the value of `legacy` or `restricted`. If the field is not set, the default value is `legacy`. In a future {product-title} release, it is planned that the default value will be `restricted`. If your catalog cannot run with `restricted` permissions, it is recommended that you manually set this field to `legacy`.
<9> Optional: For `grpc` type catalog sources, overrides the default node selector for the pod serving the content in `spec.image`, if defined.
<10> Optional: For `grpc` type catalog sources, overrides the default priority class name for the pod serving the content in `spec.image`, if defined. Kubernetes provides `system-cluster-critical` and `system-node-critical` priority classes by default. Setting the field to empty (`""`) assigns the pod the default priority. Other priority classes can be defined manually.
<11> Optional: For `grpc` type catalog sources, overrides the default tolerations for the pod serving the content in `spec.image`, if defined.
<12> Automatically check for new versions at a given interval to stay up-to-date.
<13> Last observed state of the catalog connection. For example:
+
--
* `READY`: A connection is successfully established.
* `CONNECTING`: A connection is attempting to establish.
* `TRANSIENT_FAILURE`: A temporary problem has occurred while attempting to establish a connection, such as a timeout. The state will eventually switch back to `CONNECTING` and try again.
--
+
See link:https://grpc.github.io/grpc/core/md_doc_connectivity-semantics-and-api.html[States of Connectivity] in the gRPC documentation for more details.
<14> Latest time the container registry storing the catalog image was polled to ensure the image is up-to-date.
<15> Status information for the catalog's Operator Registry service.
====

Referencing the `name` of a `CatalogSource` object in a subscription instructs OLM where to search to find a requested Operator:

.Example `Subscription` object referencing a catalog source
[%collapsible]
====
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
====

ifdef::openshift-origin[]
:!global_ns:
endif::[]
ifndef::openshift-origin[]
:!global_ns:
endif::[]
