// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-creating-broker-labeling_{context}"]
= Creating a broker by labeling a namespace

Brokers can be used in combination with triggers to deliver events from an event source to an event sink. You can create the `default` broker automatically by labelling a namespace that you own or have write permissions for.

[NOTE]
====
Brokers created using this method are not removed if you remove the label. You must manually delete them.
====

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your {product-title} cluster.
* Install the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

ifdef::openshift-dedicated,openshift-rosa[]
* You have cluster or dedicated administrator permissions.
endif::[]

.Procedure

* Label a namespace with `eventing.knative.dev/injection=enabled`:
+
[source,terminal]
----
$ oc label namespace <namespace> eventing.knative.dev/injection=enabled
----

.Verification

You can verify that the broker has been created successfully by using the `oc` CLI, or by observing it in the *Topology* view in the web console.

. Use the `oc` command to get the broker:
+
[source,terminal]
----
$ oc -n <namespace> get broker <broker_name>
----
+
.Example command
[source,terminal]
----
$ oc -n default get broker default
----
+
.Example output
[source,terminal]
----
NAME      READY     REASON    URL                                                                     AGE
default   True                http://broker-ingress.knative-eventing.svc.cluster.local/test/default   3m56s
----

. Optional: If you are using the {product-title} web console, you can navigate to the *Topology* view in the *Developer* perspective, and observe that the broker exists:
+
image::odc-view-broker.png[View the broker in the web console Topology view]
// need to add separate docs for broker in ODC - out of scope for this PR
