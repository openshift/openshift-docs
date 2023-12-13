// Module included in the following assemblies:
//
// * support/summarizing-cluster-specifications.adoc

:_mod-docs-content-type: PROCEDURE
[id="summarizing-cluster-specifications-through-clusterversion_{context}"]
= Summarizing cluster specifications by using a cluster version object

You can obtain a summary of {product-title} cluster specifications by querying the `clusterversion` resource.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Query cluster version, availability, uptime, and general status:
+
[source,terminal]
----
$ oc get clusterversion
----
+
.Example output
[source,text]
----
NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
version   4.13.8    True        False         8h      Cluster version is 4.13.8
----
. Obtain a detailed summary of cluster specifications, update availability, and update history:
+
[source,terminal]
----
$ oc describe clusterversion
----
+
.Example output
[source,text]
----
Name:         version
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  config.openshift.io/v1
Kind:         ClusterVersion
# ...
    Image:    quay.io/openshift-release-dev/ocp-release@sha256:a956488d295fe5a59c8663a4d9992b9b5d0950f510a7387dbbfb8d20fc5970ce
    URL:      https://access.redhat.com/errata/RHSA-2023:4456
    Version:  4.13.8
  History:
    Completion Time:    2023-08-17T13:20:21Z
    Image:              quay.io/openshift-release-dev/ocp-release@sha256:a956488d295fe5a59c8663a4d9992b9b5d0950f510a7387dbbfb8d20fc5970ce
    Started Time:       2023-08-17T12:59:45Z
    State:              Completed
    Verified:           false
    Version:            4.13.8
# ...
----
