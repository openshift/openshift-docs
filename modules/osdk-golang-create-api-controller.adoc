// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-golang-create-api-controller_{context}"]
= Creating an API and controller

Use the Operator SDK CLI to create a custom resource definition (CRD) API and controller.

.Procedure

. Run the following command to create an API with group `cache`, version, `v1`, and kind `Memcached`:
+
[source,terminal]
----
$ operator-sdk create api \
    --group=cache \
    --version=v1 \
    --kind=Memcached
----

. When prompted, enter `y` for creating both the resource and controller:
+
[source,terminal]
----
Create Resource [y/n]
y
Create Controller [y/n]
y
----
+
.Example output
[source,terminal]
----
Writing scaffold for you to edit...
api/v1/memcached_types.go
controllers/memcached_controller.go
...
----

This process generates the `Memcached` resource API at `api/v1/memcached_types.go` and the controller at `controllers/memcached_controller.go`.
