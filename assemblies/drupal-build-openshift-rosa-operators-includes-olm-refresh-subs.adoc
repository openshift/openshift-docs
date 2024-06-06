// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc
// * serverless/install/removing-openshift-serverless.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-refresh-subs_{context}"]
= Refreshing failing subscriptions

In Operator Lifecycle Manager (OLM), if you subscribe to an Operator that references images that are not accessible on your network, you can find jobs in the `openshift-marketplace` namespace that are failing with the following errors:

.Example output
[source,terminal]
----
ImagePullBackOff for
Back-off pulling image "example.com/openshift4/ose-elasticsearch-operator-bundle@sha256:6d2587129c846ec28d384540322b40b05833e7e00b25cca584e004af9a1d292e"
----

.Example output
[source,terminal]
----
rpc error: code = Unknown desc = error pinging docker registry example.com: Get "https://example.com/v2/": dial tcp: lookup example.com on 10.0.0.1:53: no such host
----

As a result, the subscription is stuck in this failing state and the Operator is unable to install or upgrade.

You can refresh a failing subscription by deleting the subscription, cluster service version (CSV), and other related objects. After recreating the subscription, OLM then reinstalls the correct version of the Operator.

.Prerequisites

* You have a failing subscription that is unable to pull an inaccessible bundle image.
* You have confirmed that the correct bundle image is accessible.

.Procedure

. Get the names of the `Subscription` and `ClusterServiceVersion` objects from the namespace where the Operator is installed:
+
[source,terminal]
----
$ oc get sub,csv -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME                                                       PACKAGE                  SOURCE             CHANNEL
subscription.operators.coreos.com/elasticsearch-operator   elasticsearch-operator   redhat-operators   5.0

NAME                                                                         DISPLAY                            VERSION    REPLACES   PHASE
clusterserviceversion.operators.coreos.com/elasticsearch-operator.5.0.0-65   OpenShift Elasticsearch Operator   5.0.0-65              Succeeded
----

. Delete the subscription:
+
[source,terminal]
----
$ oc delete subscription <subscription_name> -n <namespace>
----

. Delete the cluster service version:
+
[source,terminal]
----
$ oc delete csv <csv_name> -n <namespace>
----

. Get the names of any failing jobs and related config maps in the `openshift-marketplace` namespace:
+
[source,terminal]
----
$ oc get job,configmap -n openshift-marketplace
----
+
.Example output
[source,terminal]
----
NAME                                                                        COMPLETIONS   DURATION   AGE
job.batch/1de9443b6324e629ddf31fed0a853a121275806170e34c926d69e53a7fcbccb   1/1           26s        9m30s

NAME                                                                        DATA   AGE
configmap/1de9443b6324e629ddf31fed0a853a121275806170e34c926d69e53a7fcbccb   3      9m30s
----

. Delete the job:
+
[source,terminal]
----
$ oc delete job <job_name> -n openshift-marketplace
----
+
This ensures pods that try to pull the inaccessible image are not recreated.

. Delete the config map:
+
[source,terminal]
----
$ oc delete configmap <configmap_name> -n openshift-marketplace
----

. Reinstall the Operator using OperatorHub in the web console.

.Verification

* Check that the Operator has been reinstalled successfully:
+
[source,terminal]
----
$ oc get sub,csv,installplan -n <namespace>
----
