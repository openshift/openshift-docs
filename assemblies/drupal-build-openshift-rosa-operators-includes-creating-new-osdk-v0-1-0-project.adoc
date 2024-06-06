// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-migrating-to-v0-1-0.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-new-operator-sdk-v0-1-0-project_{context}"]
= Creating a new Operator SDK v0.1.0 project

Rename your Operator SDK v0.0.x project and create a new v0.1.0 project in its
place.

.Prerequisites

- Operator SDK v0.1.0 CLI installed on the development workstation
- `memcached-operator` project previously deployed using an earlier version of
Operator SDK

.Procedure

. Ensure the SDK version is v0.1.0:
+
[source,terminal]
----
$ operator-sdk --version
operator-sdk version 0.1.0
----

. Create a new project:
+
[source,terminal]
----
$ mkdir -p $GOPATH/src/github.com/example-inc/
$ cd $GOPATH/src/github.com/example-inc/
$ mv memcached-operator old-memcached-operator
$ operator-sdk new memcached-operator --skip-git-init
$ ls
memcached-operator old-memcached-operator
----

. Copy `.git` from the old project:
+
[source,terminal]
----
$ cp -rf old-memcached-operator/.git memcached-operator/.git
----
