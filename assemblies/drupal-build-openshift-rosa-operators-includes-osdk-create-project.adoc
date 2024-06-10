// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc
// * operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc
// * operators/operator_sdk/helm/osdk-helm-tutorial.adoc

ifeval::["{context}" == "osdk-golang-tutorial"]
:golang:
:type: Go
:app: memcached
endif::[]
ifeval::["{context}" == "osdk-ansible-tutorial"]
:ansible:
:type: Ansible
:app: memcached
endif::[]
ifeval::["{context}" == "osdk-helm-tutorial"]
:helm:
:type: Helm
:app: nginx
endif::[]
ifeval::["{context}" == "osdk-java-tutorial"]
:java:
:type: Java
:app: memcached
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="osdk-create-project_{context}"]
= Creating a project

Use the Operator SDK CLI to create a project called `{app}-operator`.

.Procedure

. Create a directory for the project:
+
[source,terminal,subs="attributes+"]
----
$ mkdir -p $HOME/projects/{app}-operator
----

. Change to the directory:
+
[source,terminal,subs="attributes+"]
----
$ cd $HOME/projects/{app}-operator
----

ifdef::golang[]
. Activate support for Go modules:
+
[source,terminal]
----
$ export GO111MODULE=on
----
endif::[]

. Run the `operator-sdk init` command
ifdef::ansible[]
with the `ansible` plugin
endif::[]
ifdef::helm[]
with the `helm` plugin
endif::[]
ifdef::java[]
with the `quarkus` plugin
endif::[]
to initialize the project:
+
[source,terminal,subs="attributes+"]
ifdef::golang[]
----
$ operator-sdk init \
    --domain=example.com \
    --repo=github.com/example-inc/{app}-operator
----
+
[NOTE]
====
The `operator-sdk init` command uses the Go plugin by default.
====
+
The `operator-sdk init` command generates a `go.mod` file to be used with link:https://golang.org/ref/mod[Go modules]. The `--repo` flag is required when creating a project outside of `$GOPATH/src/`, because generated files require a valid module path.
endif::[]
ifdef::ansible[]
----
$ operator-sdk init \
    --plugins=ansible \
    --domain=example.com
----
endif::[]
ifdef::helm[]
----
$ operator-sdk init \
    --plugins=helm \
    --domain=example.com \
    --group=demo \
    --version=v1 \
    --kind=Nginx
----
+
[NOTE]
====
By default, the `helm` plugin initializes a project using a boilerplate Helm chart. You can use additional flags, such as the `--helm-chart` flag, to initialize a project using an existing Helm chart.
====
+
The `init` command creates the `nginx-operator` project specifically for watching a resource with API version `example.com/v1` and kind `Nginx`.

. For Helm-based projects, the `init` command generates the RBAC rules in the `config/rbac/role.yaml` file based on the resources that would be deployed by the default manifest for the chart. Verify that the rules generated in this file meet the permission requirements of the Operator.
endif::[]
ifdef::java[]
----
$ operator-sdk init \
    --plugins=quarkus \
    --domain=example.com \
    --project-name=memcached-operator
----
endif::[]

ifeval::["{context}" == "osdk-golang-tutorial"]
:!golang:
:!type:
:!app:
endif::[]
ifeval::["{context}" == "osdk-ansible-tutorial"]
:!ansible:
:!type:
:!app:
endif::[]
ifeval::["{context}" == "osdk-helm-tutorial"]
:!helm:
:!type:
:!app:
endif::[]
ifeval::["{context}" == "osdk-java-tutorial"]
:!java:
:!type:
:!app:
endif::[]