// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-migrating-to-v0-1-0.adoc

:_mod-docs-content-type: PROCEDURE
[id="migrating-custom-types-from-pkg-apis_{context}"]
= Migrating custom types from pkg/apis

Migrate your project's custom types to the updated Operator SDK v0.1.0 usage.

.Prerequisites

- Operator SDK v0.1.0 CLI installed on the development workstation
- `memcached-operator` project previously deployed using an earlier version of
Operator SDK
- New project created using Operator SDK v0.1.0

.Procedure

. *Create the scaffold API for custom types.*

.. Create the API for your custom resource (CR) in the new project with
`operator-sdk add api --api-version=<apiversion> --kind=<kind>`:
+
[source,terminal]
----
$ cd memcached-operator
$ operator-sdk add api --api-version=cache.example.com/v1alpha1 --kind=Memcached

$ tree pkg/apis
pkg/apis/
├── addtoscheme_cache_v1alpha1.go
├── apis.go
└── cache
    └── v1alpha1
        ├── doc.go
        ├── memcached_types.go
        ├── register.go
        └── zz_generated.deepcopy.go
----

.. Repeat the previous command for as many custom types as you had defined in your
old project. Each type will be defined in the file
`pkg/apis/<group>/<version>/<kind>_types.go`.

. *Copy the contents of the type.*

.. Copy the `Spec` and `Status` contents of the
`pkg/apis/<group>/<version>/types.go` file from the old project to the new
project's `pkg/apis/<group>/<version>/<kind>_types.go` file.

.. Each `<kind>_types.go` file has an `init()` function. Be sure not to remove that
since that registers the type with the Manager's scheme:
+
[source,golang]
----
func init() {
	SchemeBuilder.Register(&Memcached{}, &MemcachedList{})
----
