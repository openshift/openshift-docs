// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-golang-multi-group-apis_{context}"]
= About multi-group APIs

Before you create an API and controller, consider whether your Operator requires multiple API groups. This tutorial covers the default case of a single group API, but to change the layout of your project to support multi-group APIs, you can run the following command:

[source,terminal]
----
$ operator-sdk edit --multigroup=true
----

This command updates the `PROJECT` file, which should look like the following example:

[source,yaml]
----
domain: example.com
layout: go.kubebuilder.io/v3
multigroup: true
...
----

For multi-group projects, the API Go type files are created in the `apis/<group>/<version>/` directory, and the controllers are created in the `controllers/<group>/` directory. The Dockerfile is then updated accordingly.

.Additional resource

* For more details on migrating to a multi-group project, see the link:https://book.kubebuilder.io/migration/multi-group.html[Kubebuilder documentation].
