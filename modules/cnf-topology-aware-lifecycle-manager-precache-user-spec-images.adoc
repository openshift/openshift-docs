// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-talm-updating-managed-policies.adoc

:_mod-docs-content-type: CONCEPT
[id="talm-prechache-user-specified-images-concept_{context}"]
= Pre-caching user-specified images with {cgu-operator} on {sno} clusters

You can pre-cache application-specific workload images on {sno} clusters before upgrading your applications.

You can specify the configuration options for the pre-caching jobs using the following custom resources (CR):

* `PreCachingConfig` CR
* `ClusterGroupUpgrade` CR

[NOTE]
====
All fields in the `PreCachingConfig` CR are optional.
====

.Example PreCachingConfig CR
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: PreCachingConfig
metadata:
  name: exampleconfig
  namespace: exampleconfig-ns
spec:
  overrides: <1>
    platformImage: quay.io/openshift-release-dev/ocp-release@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
    operatorsIndexes:
      - registry.example.com:5000/custom-redhat-operators:1.0.0
    operatorsPackagesAndChannels:
      - local-storage-operator: stable
      - ptp-operator: stable
      - sriov-network-operator: stable
  spaceRequired: 30 Gi <2>
  excludePrecachePatterns: <3>
    - aws
    - vsphere
  additionalImages: <4>
    - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
    - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
    - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
----
<1>  By default, {cgu-operator} automatically populates the `platformImage`, `operatorsIndexes`, and the `operatorsPackagesAndChannels` fields from the policies of the managed clusters. You can specify values to override the default {cgu-operator}-derived values for these fields.
<2> Specifies the minimum required disk space on the cluster. If unspecified, {cgu-operator} defines a default value for {product-title} images. The disk space field must include an integer value and the storage unit. For example: `40 GiB`, `200 MB`, `1 TiB`.
<3> Specifies the images to exclude from pre-caching based on image name matching.
<4> Specifies the list of additional images to pre-cache.

.Example ClusterGroupUpgrade CR with PreCachingConfig CR reference
[source,yaml]
----
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu
spec:
  preCaching: true <1>
  preCachingConfigRef:
    name: exampleconfig <2>
    namespace: exampleconfig-ns <3>
----
<1> The `preCaching` field set to `true` enables the pre-caching job.
<2> The `preCachingConfigRef.name` field specifies the `PreCachingConfig` CR that you want to use.
<3> The `preCachingConfigRef.namespace` specifies the namespace of the `PreCachingConfig` CR that you want to use.