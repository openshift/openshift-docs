// Module included in the following assemblies:
//
// * networking/ptp/configuring-ptp.adoc

:_mod-docs-content-type: PROCEDURE
[id="cnf-about-collecting-nro-data_{context}"]
= Collecting PTP Operator data

You can use the `oc adm must-gather` command to collect information about your cluster, including features and objects associated with PTP Operator.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

* You have installed the {oc-first}.

* You have installed the PTP Operator.

.Procedure

* To collect PTP Operator data with `must-gather`, you must specify the PTP Operator `must-gather` image.
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --image=registry.redhat.io/openshift4/ptp-must-gather-rhel8:v{product-version}
----
