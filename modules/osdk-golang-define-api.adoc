// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-golang-define-api_{context}"]
= Defining the API

Define the API for the `Memcached` custom resource (CR).

.Procedure

. Modify the Go type definitions at `api/v1/memcached_types.go` to have the following `spec` and `status`:
+
[source,go]
----
// MemcachedSpec defines the desired state of Memcached
type MemcachedSpec struct {
	// +kubebuilder:validation:Minimum=0
	// Size is the size of the memcached deployment
	Size int32 `json:"size"`
}

// MemcachedStatus defines the observed state of Memcached
type MemcachedStatus struct {
	// Nodes are the names of the memcached pods
	Nodes []string `json:"nodes"`
}
----

. Update the generated code for the resource type:
+
[source,terminal]
----
$ make generate
----
+
[TIP]
====
After you modify a `*_types.go` file, you must run the `make generate` command to update the generated code for that resource type.
====
+
The above Makefile target invokes the `controller-gen` utility to update the `api/v1/zz_generated.deepcopy.go` file. This ensures your API Go type definitions implement the `runtime.Object` interface that all Kind types must implement.
