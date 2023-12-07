// Module included in the following assemblies:
//
// * operators/admin/olm-status.adoc
// * support/troubleshooting/troubleshooting-operator-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-status-viewing-cli_{context}"]
= Viewing Operator subscription status by using the CLI

You can view Operator subscription status by using the CLI.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List Operator subscriptions:
+
[source,terminal]
----
$ oc get subs -n <operator_namespace>
----

. Use the `oc describe` command to inspect a `Subscription` resource:
+
[source,terminal]
----
$ oc describe sub <subscription_name> -n <operator_namespace>
----

. In the command output, find the `Conditions` section for the status of Operator subscription condition types. In the following example, the `CatalogSourcesUnhealthy` condition type has a status of `false` because all available catalog sources are healthy:
+
.Example output
[source,terminal]
----
Name:         cluster-logging
Namespace:    openshift-logging
Labels:       operators.coreos.com/cluster-logging.openshift-logging=
Annotations:  <none>
API Version:  operators.coreos.com/v1alpha1
Kind:         Subscription
# ...
Conditions:
   Last Transition Time:  2019-07-29T13:42:57Z
   Message:               all available catalogsources are healthy
   Reason:                AllCatalogSourcesHealthy
   Status:                False
   Type:                  CatalogSourcesUnhealthy
# ...
----

[NOTE]
====
Default {product-title} cluster Operators are managed by the Cluster Version Operator (CVO) and they do not have a `Subscription` object. Application Operators are managed by Operator Lifecycle Manager (OLM) and they have a `Subscription` object.
====
