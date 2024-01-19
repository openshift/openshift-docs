// NOTE: The contents of this file are auto-generated
// This template is for admin ('oc adm ...') commands
// Uses 'source,bash' for proper syntax highlighting for comments in examples

:_mod-docs-content-type: REFERENCE
[id="microshift-cli-admin_{context}"]
= OpenShift CLI (oc) administrator commands



== oc adm inspect
Collect debugging data for a given resource

.Example usage
[source,bash,options="nowrap"]
----
  # Collect debugging data for a kubernetes service
  oc adm inspect service/kubernetes

  # Collect debugging data for a node
  oc adm inspect node/<node_name>

  # Collect debugging data for logicalvolumes in a CRD
  oc adm inspect crd/logicalvolumes.topolvm.io

  # Collect debugging data for routes.route.openshift.io in a CRD
  oc adm inspect crd/routes.route.openshift.io
----



== oc adm release extract
Extract the contents of an update payload to disk

.Example usage
[source,bash,options="nowrap"]
----
  # Use git to check out the source code for the current cluster release to DIR
  oc adm release extract --git=DIR

  # Extract cloud credential requests for AWS
  oc adm release extract --credentials-requests --cloud=aws

  # Use git to check out the source code for the current cluster release to DIR from linux/s390x image
  # Note: Wildcard filter is not supported; pass a single os/arch to extract
  oc adm release extract --git=DIR quay.io/openshift-release-dev/ocp-release:4.11.2 --filter-by-os=linux/s390x
----



== oc adm release info
Display information about a release

.Example usage
[source,bash,options="nowrap"]
----
  # Show information about the cluster's current release
  oc adm release info

  # Show the source code that comprises a release
  oc adm release info 4.11.2 --commit-urls

  # Show the source code difference between two releases
  oc adm release info 4.11.0 4.11.2 --commits

  # Show where the images referenced by the release are located
  oc adm release info quay.io/openshift-release-dev/ocp-release:4.11.2 --pullspecs

  # Show information about linux/s390x image
  # Note: Wildcard filter is not supported; pass a single os/arch to extract
  oc adm release info quay.io/openshift-release-dev/ocp-release:4.11.2 --filter-by-os=linux/s390x
----



== oc adm taint
Update the taints on nodes

.Example usage
[source,bash,options="nowrap"]
----
  # Update node 'foo' with a taint with key 'dedicated' and value 'special-user' and effect 'NoSchedule'
  # If a taint with that key and effect already exists, its value is replaced as specified
  oc adm taint nodes foo dedicated=special-user:NoSchedule

  # Remove from node 'foo' the taint with key 'dedicated' and effect 'NoSchedule' if one exists
  oc adm taint nodes foo dedicated:NoSchedule-

  # Remove from node 'foo' all the taints with key 'dedicated'
  oc adm taint nodes foo dedicated-

  # Add a taint with key 'dedicated' on nodes having label mylabel=X
  oc adm taint node -l myLabel=X  dedicated=foo:PreferNoSchedule

  # Add to node 'foo' a taint with key 'bar' and no value
  oc adm taint nodes foo bar:NoSchedule
----


