:_mod-docs-content-type: ASSEMBLY
[id="ossm-extensions"]
= Extensions
include::_attributes/common-attributes.adoc[]
:context: ossm-extensions

toc::[]

You can use WebAssembly extensions to add new features directly into the {SMProductName} proxies. This lets you move even more common functionality out of your applications, and implement them in a single language that compiles to WebAssembly bytecode.

ifndef::openshift-rosa[]
[NOTE]
====
WebAssembly extensions are not supported on {ibm-z-name} and {ibm-power-name}.
====

endif::openshift-rosa[]

include::modules/ossm-extensions-overview.adoc[leveloffset=+1]

include::modules/ossm-extensions-wasmplugin-format.adoc[leveloffset=+1]

include::modules/ossm-extensions-ref-wasmplugin.adoc[leveloffset=+1]

include::modules/ossm-extensions-wasmplugin-deploy.adoc[leveloffset=+2]

include::modules/ossm-extensions-smextension-format.adoc[leveloffset=+1]

include::modules/ossm-extensions-ref-smextension.adoc[leveloffset=+1]

include::modules/ossm-extensions-smextension-deploy.adoc[leveloffset=+2]

include::modules/ossm-extensions-migration-overview.adoc[leveloffset=+1]

include::modules/ossm-extensions-migrating-to-wasmplugin.adoc[leveloffset=+2]
