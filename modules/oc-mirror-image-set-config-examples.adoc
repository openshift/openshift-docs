// Module included in the following assemblies:
//
// * installing/disconnected_install/installing-mirroring-disconnected.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc

:_mod-docs-content-type: REFERENCE
[id="oc-mirror-image-set-examples_{context}"]
= Image set configuration examples

The following `ImageSetConfiguration` file examples show the configuration for various mirroring use cases.

// Moved to first; unchanged
[discrete]
[id="oc-mirror-image-set-examples-shortest-upgrade-path_{context}"]
== Use case: Including the shortest {product-title} update path

The following `ImageSetConfiguration` file uses a local storage backend and includes all {product-title} versions along the shortest update path from the minimum version of `4.11.37` to the maximum version of `4.12.15`.

.Example `ImageSetConfiguration` file
[source,yaml]
----
apiVersion: mirror.openshift.io/v1alpha2
kind: ImageSetConfiguration
storageConfig:
  local:
    path: /home/user/metadata
mirror:
  platform:
    channels:
      - name: stable-4.12
        minVersion: 4.11.37
        maxVersion: 4.12.15
        shortestPath: true
----

// Moved to second; unchanged
[discrete]
[id="oc-mirror-image-set-examples-minimum-to-latest_{context}"]
== Use case: Including all versions of {product-title} from a minimum to the latest version for multi-architecture releases

The following `ImageSetConfiguration` file uses a registry storage backend and includes all {product-title} versions starting at a minimum version of `4.13.4` to the latest version in the channel. On every invocation of oc-mirror with this image set configuration, the latest release of the `stable-4.13` channel is evaluated, so running oc-mirror at regular intervals ensures that you automatically receive the latest releases of {product-title} images.

By setting the value of `platform.architectures` to `multi`, you can ensure that the mirroring is supported for multi-architecture releases.

.Example `ImageSetConfiguration` file
[source,yaml]
----
apiVersion: mirror.openshift.io/v1alpha2
kind: ImageSetConfiguration
storageConfig:
  registry:
    imageURL: example.com/mirror/oc-mirror-metadata
    skipTLS: false
mirror:
  platform:
    architectures:
      - "multi"
    channels:
      - name: stable-4.13
        minVersion: 4.13.4
        maxVersion: 4.13.6
----

// Updated:
// - Added a note below about the maxVersion
// - Added a note about not necessarily getting all versions in the range
[discrete]
[id="oc-mirror-image-set-examples-operator-versions_{context}"]
== Use case: Including Operator versions from a minimum to the latest

The following `ImageSetConfiguration` file uses a local storage backend and includes only the Red Hat Advanced Cluster Security for Kubernetes Operator, versions starting at 4.0.1 and later in the `stable` channel.

[NOTE]
====
When you specify a minimum or maximum version range, you might not receive all Operator versions in that range.

By default, oc-mirror excludes any versions that are skipped or replaced by a newer version in the Operator Lifecycle Manager (OLM) specification. Operator versions that are skipped might be affected by a CVE or contain bugs. Use a newer version instead. For more information on skipped and replaced versions, see link:https://olm.operatorframework.io/docs/concepts/olm-architecture/operator-catalog/creating-an-update-graph/[Creating an update graph with OLM].

To receive all Operator versions in a specified range, you can set the `mirror.operators.full` field to `true`.
====

.Example `ImageSetConfiguration` file
[source,yaml,subs=attributes+]
----
apiVersion: mirror.openshift.io/v1alpha2
kind: ImageSetConfiguration
storageConfig:
  local:
    path: /home/user/metadata
mirror:
  operators:
    - catalog: registry.redhat.io/redhat/redhat-operator-index:v{product-version}
      packages:
        - name: rhacs-operator
          channels:
          - name: stable
            minVersion: 4.0.1
----

[NOTE]
====
To specify a maximum version instead of the latest, set the `mirror.operators.packages.channels.maxVersion` field.
====

[discrete]
[id="oc-mirror-image-set-examples-nutanix-operator_{context}"]
== Use case: Including the Nutanix CSI Operator
The following `ImageSetConfiguration` file uses a local storage backend and includes the Nutanix CSI Operator, the OpenShift Update Service (OSUS) graph image, and an additional Red Hat Universal Base Image (UBI).

.Example `ImageSetConfiguration` file
[source,yaml,subs=attributes+]
----
kind: ImageSetConfiguration
apiVersion: mirror.openshift.io/v1alpha2
storageConfig:
  registry:
    imageURL: mylocalregistry/ocp-mirror/openshift4
    skipTLS: false
mirror:
  platform:
    channels:
    - name: stable-4.11
      type: ocp
    graph: true
  operators:
  - catalog: registry.redhat.io/redhat/certified-operator-index:v{product-version}
    packages:
    - name: nutanixcsioperator
      channels:
      - name: stable
  additionalImages:
  - name: registry.redhat.io/ubi9/ubi:latest
----

// New example; including the default channel
[discrete]
[id="oc-mirror-image-set-examples-default-channel_{context}"]
== Use case: Including the default Operator channel

The following `ImageSetConfiguration` file includes the `stable-5.7` and `stable` channels for the OpenShift Elasticsearch Operator. Even if only the packages from the `stable-5.7` channel are needed, the `stable` channel must also be included in the `ImageSetConfiguration` file, because it is the default channel for the Operator. You must always include the default channel for the Operator package even if you do not use the bundles in that channel.

[TIP]
====
You can find the default channel by running the following command: `oc mirror list operators --catalog=<catalog_name> --package=<package_name>`.
====

.Example `ImageSetConfiguration` file
[source,yaml,subs=attributes+]
----
apiVersion: mirror.openshift.io/v1alpha2
kind: ImageSetConfiguration
storageConfig:
  registry:
    imageURL: example.com/mirror/oc-mirror-metadata
    skipTLS: false
mirror:
  operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:v{product-version}
    packages:
    - name: elasticsearch-operator
      channels:
      - name: stable-5.7
      - name: stable
----

// New example; Entire catalog; all versions
[discrete]
[id="oc-mirror-image-set-examples-entire-catalog-full_{context}"]
== Use case: Including an entire catalog (all versions)

The following `ImageSetConfiguration` file sets the `mirror.operators.full` field to `true` to include all versions for an entire Operator catalog.

.Example `ImageSetConfiguration` file
[source,yaml,subs=attributes+]
----
apiVersion: mirror.openshift.io/v1alpha2
kind: ImageSetConfiguration
storageConfig:
  registry:
    imageURL: example.com/mirror/oc-mirror-metadata
    skipTLS: false
mirror:
  operators:
    - catalog: registry.redhat.io/redhat/redhat-operator-index:v{product-version}
      full: true
----

// New example; Entire catalog; heads only
// - Included 'targetCatalog' in example
[discrete]
[id="oc-mirror-image-set-examples-entire-catalog-heads_{context}"]
== Use case: Including an entire catalog (channel heads only)

The following `ImageSetConfiguration` file includes the channel heads for an entire Operator catalog.

By default, for each Operator in the catalog, oc-mirror includes the latest Operator version (channel head) from the default channel. If you want to mirror all Operator versions, and not just the channel heads, you must set the `mirror.operators.full` field to `true`.

This example also uses the `targetCatalog` field to specify an alternative namespace and name to mirror the catalog as.

.Example `ImageSetConfiguration` file
[source,yaml,subs=attributes+]
----
apiVersion: mirror.openshift.io/v1alpha2
kind: ImageSetConfiguration
storageConfig:
  registry:
    imageURL: example.com/mirror/oc-mirror-metadata
    skipTLS: false
mirror:
  operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:v{product-version}
    targetCatalog: my-namespace/my-operator-catalog
----

// Moved to last; unchanged
[discrete]
[id="oc-mirror-image-set-examples-helm_{context}"]
== Use case: Including arbitrary images and helm charts

The following `ImageSetConfiguration` file uses a registry storage backend and includes helm charts and an additional Red Hat Universal Base Image (UBI).

.Example `ImageSetConfiguration` file
[source,yaml,subs=attributes+]
----
apiVersion: mirror.openshift.io/v1alpha2
kind: ImageSetConfiguration
archiveSize: 4
storageConfig:
  registry:
    imageURL: example.com/mirror/oc-mirror-metadata
    skipTLS: false
mirror:
 platform:
   architectures:
     - "s390x"
   channels:
     - name: stable-{product-version}
 operators:
   - catalog: registry.redhat.io/redhat/redhat-operator-index:v{product-version}
 helm:
   repositories:
     - name: redhat-helm-charts
       url: https://raw.githubusercontent.com/redhat-developer/redhat-helm-charts/master
       charts:
         - name: ibm-mongodb-enterprise-helm
           version: 0.2.0
 additionalImages:
   - name: registry.redhat.io/ubi9/ubi:latest
----
