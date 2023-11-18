:_mod-docs-content-type: ASSEMBLY
[id="serverless-pingsource"]
= Creating a ping source
:context: serverless-pingsource
include::_attributes/common-attributes.adoc[]

toc::[]

A ping source is an event source that can be used to periodically send ping events with a constant payload to an event consumer. A ping source can be used to schedule sending events, similar to a timer.

// dev console
include::modules/serverless-pingsource-odc.adoc[leveloffset=+1]
// kn commands
include::modules/serverless-pingsource-kn.adoc[leveloffset=+1]
include::modules/specifying-sink-flag-kn.adoc[leveloffset=+2]
// YAML
include::modules/serverless-pingsource-yaml.adoc[leveloffset=+1]
