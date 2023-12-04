// Module included in the following assemblies:
//
// * registry/accessing-the-registry.adoc

:_mod-docs-content-type: PROCEDURE
[id="checking-the-status-of-registry-pods_{context}"]
= Checking the status of the registry pods

ifndef::openshift-dedicated,openshift-rosa[]
As a cluster administrator,
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
As an administrator with the `dedicated-admin` role,
endif::openshift-dedicated,openshift-rosa[]
you can list the image registry pods running in the `openshift-image-registry` project and check their status.

.Prerequisites

ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* List the pods in the `openshift-image-registry` project and view their status:
+
[source,terminal]
----
$ oc get pods -n openshift-image-registry
----
+
.Example output
[source,terminal]
----
NAME READY STATUS RESTARTS AGE
cluster-image-registry-operator-764bd7f846-qqtpb 1/1 Running 0 78m
image-registry-79fb4469f6-llrln 1/1 Running 0 77m
node-ca-hjksc 1/1 Running 0 73m
node-ca-tftj6 1/1 Running 0 77m
node-ca-wb6ht 1/1 Running 0 77m
node-ca-zvt9q 1/1 Running 0 74m
----
