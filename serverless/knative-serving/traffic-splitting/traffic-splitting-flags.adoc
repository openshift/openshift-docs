:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="traffic-splitting-flags"]
= CLI flags for traffic splitting
:context: traffic-splitting-flags

toc::[]

The Knative (`kn`) CLI supports traffic operations on the traffic block of a service as part of the `kn service update` command.

// kn flags
include::modules/serverless-traffic-splitting-flags-kn.adoc[leveloffset=+1]


// creating custom URLs by using tags
include::modules/serverless-custom-revision-urls.adoc[leveloffset=+2]