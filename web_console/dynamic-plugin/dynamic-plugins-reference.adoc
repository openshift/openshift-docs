:_mod-docs-content-type: ASSEMBLY
[id="dynamic-plugins-reference_{context}"]
= Dynamic plugin reference
include::_attributes/common-attributes.adoc[]
:context: dynamic-plugins-reference

toc::[]

You can add extensions that allow you to customize your plugin. Those extensions are then loaded to the console at run-time.

include::modules/dynamic-plugin-sdk-extensions.adoc[leveloffset=+1]

include::modules/dynamic-plugin-api.adoc[leveloffset=+1]

include::modules/troubleshooting-dynamic-plugin.adoc[leveloffset=+1]

ifndef::openshift-rosa,openshift-dedicated[]
[role="_additional-resources"]
.Additional resources
* xref:../../security/certificates/service-serving-certificate.adoc#understanding-service-serving_service-serving-certificate[Understanding service serving certificates]
endif::openshift-rosa,openshift-dedicated[]