:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="traffic-splitting-using-cli"]
= Traffic splitting using the Knative CLI
:context: traffic-splitting-using-cli

Using the Knative (`kn`) CLI to create traffic splits provides a more streamlined and intuitive user interface over modifying YAML files directly. You can use the `kn service update` command to split traffic between revisions of a service.

// kn CLI
include::modules/serverless-create-traffic-split-kn.adoc[leveloffset=+1]

