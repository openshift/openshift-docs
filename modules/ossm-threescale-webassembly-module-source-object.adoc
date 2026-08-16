// Module included in the following assembly:
//
// service_mesh/v2x/ossm-threescale-webassembly-module.adoc

[id="ossm-threescale-webassembly-module-source-object_{context}"]
= The 3scale WebAssembly module source object

A `source` object exists as part of an array of sources within any of the `credentials` object fields. The object field name, referred to as a `source`-type is any one of the following:

* `header`: The lookup query receives HTTP request headers as input.
* `query_string`: The `lookup query` receives the URL query string parameters as input.
* `filter`: The `lookup query` receives filter metadata as input.

All `source`-type objects have at least the following two fields:

.`source`-type object fields
|===
|Name |Description |Required

a|`keys`
a|An array of strings, each one a `key`, referring to entries found in the input data.
|Yes

a|`ops`
a|An array of `operations` that perform a `key` entry match. The array is a pipeline where operations receive inputs and generate outputs on the next operation. An `operation` failing to provide an output resolves the `lookup query` as failed. The pipeline order of the operations determines the evaluation order.
|Optional
|===

The `filter` field name has a required `path` entry to show the path in the metadata you use to look up data.

When a `key` matches the input data, the rest of the keys are not evaluated and the source resolution algorithm jumps to executing the `operations` (`ops`) specified, if any. If no `ops` are specified, the result value of the matching `key`, if any, is returned.

`Operations` provide a way to specify certain conditions and transformations for inputs you have after the first phase looks up a `key`. Use `operations` when you need to transform, decode, and assert properties, however they do not provide a mature language to deal with all needs and lack _Turing-completeness_.

A stack stored the outputs of `operations`. When evaluated, the `lookup query` finishes by assigning the value or values at the bottom of the stack, depending on how many values the credential consumes.
