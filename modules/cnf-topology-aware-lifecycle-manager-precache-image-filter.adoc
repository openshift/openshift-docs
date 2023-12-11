// Module included in the following assemblies:
// Epic CNF-6848 (4.13), Story TELCODOCS-949
// * scalability_and_performance/cnf-talm-for-cluster-upgrades.adoc

:_mod-docs-content-type: CONCEPT
[id="talo-precache-feature-image-filter_{context}"]
= Using the container image pre-cache filter

The pre-cache feature typically downloads more images than a cluster needs for an update. You can control which pre-cache images are downloaded to a cluster. This decreases download time, and saves bandwidth and storage.

You can see a list of all images to be downloaded using the following command:

[source,terminal]
----
$ oc adm release info <ocp-version>
----

The following `ConfigMap` example shows how you can exclude images using the `excludePrecachePatterns` field.

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-group-upgrade-overrides
data:
  excludePrecachePatterns: |
    azure <1>
    aws
    vsphere
    alibaba
----
<1> {cgu-operator} excludes all images with names that include any of the patterns listed here.