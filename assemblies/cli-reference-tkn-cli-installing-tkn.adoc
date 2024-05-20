:_mod-docs-content-type: ASSEMBLY
[id='installing-tkn']
= Installing tkn
include::_attributes/common-attributes.adoc[]
:context: installing-tkn

toc::[]

Use the CLI tool to manage {pipelines-title} from a terminal. The following section describes how to install the CLI tool on different platforms.

ifndef::openshift-rosa,openshift-dedicated[]
You can also find the URL to the latest binaries from the {product-title} web console by clicking the *?* icon in the upper-right corner and selecting *Command Line Tools*.
endif::openshift-rosa,openshift-dedicated[]
:FeatureName: Running {pipelines-title} on ARM hardware
include::snippets/technology-preview.adoc[]

[NOTE]
====
Both the archives and the RPMs contain the following executables:

* tkn
* tkn-pac
ifndef::openshift-rosa,openshift-dedicated[]
* opc
endif::openshift-rosa,openshift-dedicated[]
====
ifndef::openshift-rosa,openshift-dedicated[]
:FeatureName: Running {pipelines-title} with the `opc` CLI tool
include::snippets/technology-preview.adoc[]
endif::openshift-rosa,openshift-dedicated[]
// Install tkn on Linux
include::modules/op-installing-tkn-on-linux.adoc[leveloffset=+1]

// Install tkn on Linux using RPM
include::modules/op-installing-tkn-on-linux-using-rpm.adoc[leveloffset=+1]

//Install tkn on Windows
include::modules/op-installing-tkn-on-windows.adoc[leveloffset=+1]

//Install tkn on macOS
include::modules/op-installing-tkn-on-macos.adoc[leveloffset=+1]
