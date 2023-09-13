// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc

[id="cli-using-cli_{context}"]
= Using the OpenShift CLI

Review the following sections to learn how to complete common tasks using the CLI.

ifndef::microshift[]
== Creating a project

Use the `oc new-project` command to create a new project.

[source,terminal]
----
$ oc new-project my-project
----

.Example output
[source,terminal]
----
Now using project "my-project" on server "https://openshift.example.com:6443".
----
endif::microshift[]

ifndef::microshift[]
== Creating a new app

Use the `oc new-app` command to create a new application.

[source,terminal]
----
$ oc new-app https://github.com/sclorg/cakephp-ex
----

.Example output
[source,terminal]
----
--> Found image 40de956 (9 days old) in imagestream "openshift/php" under tag "7.2" for "php"

...

    Run 'oc status' to view your app.
----
endif::microshift[]

== Viewing pods

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

== Viewing pod logs

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

ifndef::microshift[]
== Viewing the current project

Use the `oc project` command to view the current project.

[source,terminal]
----
$ oc project
----

.Example output
[source,terminal]
----
Using project "my-project" on server "https://openshift.example.com:6443".
----

== Viewing the status for the current project

Use the `oc status` command to view information about the current project, such
as services, deployments, and build configs.

[source,terminal]
----
$ oc status
----

.Example output
[source,terminal]
----
In project my-project on server https://openshift.example.com:6443

svc/cakephp-ex - 172.30.236.80 ports 8080, 8443
  dc/cakephp-ex deploys istag/cakephp-ex:latest <-
    bc/cakephp-ex source builds https://github.com/sclorg/cakephp-ex on openshift/php:7.2
    deployment #1 deployed 2 minutes ago - 1 pod

3 infos identified, use 'oc status --suggest' to see details.
----
endif::microshift[]

== Listing supported API resources

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
