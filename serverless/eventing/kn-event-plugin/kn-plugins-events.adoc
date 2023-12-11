:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="kn-plugins-events"]
= Knative CLI plugins
:context: kn-plugins-events

toc::[]

The Knative (`kn`) CLI supports the use of plugins, which enable you to extend the functionality of your `kn` installation by adding custom commands and other shared commands that are not part of the core distribution. Knative (`kn`) CLI plugins are used in the same way as the main `kn` functionality.

Currently, Red Hat supports the `kn-source-kafka` plugin and the `kn-event` plugin.

:FeatureName: The `kn-event` plugin
include::snippets/technology-preview.adoc[leveloffset=+1]
// kn event commands
include::modules/serverless-build-events-kn.adoc[leveloffset=+1]
include::modules/serverless-send-events-kn.adoc[leveloffset=+1]
