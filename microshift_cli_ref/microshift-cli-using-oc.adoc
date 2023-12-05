:_mod-docs-content-type: ASSEMBLY
[id="microshift-cli-using-oc"]
= Using the oc tool
include::_attributes/attributes-microshift.adoc[]
:context: microshift-using-oc

toc::[]

The optional OpenShift CLI (`oc`) tool provides a subset of `oc` commands for {product-title} deployments. Using `oc` is convenient if you are familiar with {OCP} and Kubernetes.

include::modules/microshift-cli-oc-about.adoc[leveloffset=+1]

[id="cli-using-cli_{context}"]
== Using the OpenShift CLI in {product-title}

Review the following sections to learn how to complete common tasks in {product-title} using the `oc` CLI.

[id="viewing-pods_{context}"]
=== Viewing pods

Use the `oc get pods` command to view the pods for the current project.

[NOTE]
====
When you run `oc` inside a pod and do not specify a namespace, the namespace of the pod is used by default.
====

[source,terminal]
----
$ oc get pods -o wide
----

.Example output
[source,terminal]
----
NAME                  READY   STATUS      RESTARTS   AGE     IP            NODE                           NOMINATED NODE
cakephp-ex-1-build    0/1     Completed   0          5m45s   10.131.0.10   ip-10-0-141-74.ec2.internal    <none>
cakephp-ex-1-deploy   0/1     Completed   0          3m44s   10.129.2.9    ip-10-0-147-65.ec2.internal    <none>
cakephp-ex-1-ktz97    1/1     Running     0          3m33s   10.128.2.11   ip-10-0-168-105.ec2.internal   <none>
----

[id="viewing-pod-logs_{context}"]
=== Viewing pod logs

Use the `oc logs` command to view logs for a particular pod.

[source,terminal]
----
$ oc logs cakephp-ex-1-deploy
----

.Example output
[source,terminal]
----
--> Scaling cakephp-ex-1 to 1
--> Success
----

[id="listing-supported-apis_{context}"]
=== Listing supported API resources

Use the `oc api-resources` command to view the list of supported API resources
on the server.

[source,terminal]
----
$ oc api-resources
----

.Example output
[source,terminal]
----
NAME                                  SHORTNAMES       APIGROUP                              NAMESPACED   KIND
bindings                                                                                     true         Binding
componentstatuses                     cs                                                     false        ComponentStatus
configmaps                            cm                                                     true         ConfigMap
...
----

// Getting help
include::modules/microshift-cli-oc-get-help.adoc[leveloffset=+1]

//Errors when using oc commands not enabled in MicroShift
include::modules/microshift-oc-apis-errors.adoc[leveloffset=+1]