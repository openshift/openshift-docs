// Module included in the following assembly:
//
// service_mesh/v2x/ossm-threescale-webassembly-module.adoc

[id="ossm-threescale-webassembly-module-mapping-rules-object_{context}"]
= The 3scale WebAssembly module mapping_rules object

The `mapping_rules` object is part of the `service` object. It specifies a set of REST path patterns and related 3scale metrics and count increments to use when the patterns match.

You need the value if no dynamic configuration is provided in the `system` top-level object. If the object is provided in addition to the `system` top-level entry, then the `mapping_rules` object is evaluated first.

`mapping_rules` is an array object. Each element of that array is a `mapping_rule` object. The evaluated matching mapping rules on an incoming request provide the set of 3scale `methods` for authorization and reporting to the _APIManager_. When multiple matching rules refer to the same `methods`, there is a summation of `deltas` when calling into 3scale. For example, if two rules increase the _Hits_ method twice with `deltas` of 1 and 3, a single method entry for Hits reporting to 3scale has a `delta` of 4.
