:_mod-docs-content-type: ASSEMBLY
[id="cli-getting-started"]
= Getting started with the OpenShift CLI
include::_attributes/common-attributes.adoc[]
:context: cli-developer-commands

toc::[]

// About the CLI
include::modules/cli-about-cli.adoc[leveloffset=+1]

[id="installing-openshift-cli"]
== Installing the OpenShift CLI

You can install the OpenShift CLI (`oc`) either by downloading the binary or by using an RPM.

// Installing the CLI by downloading the binary
include::modules/cli-installing-cli.adoc[leveloffset=+2]

// Installing the CLI by using the web console
include::modules/cli-installing-cli-web-console.adoc[leveloffset=+2]

// Installing the CLI on Linux by using the web console
include::modules/cli-installing-cli-web-console-linux.adoc[leveloffset=+3]

// Installing the CLI on Windows by using the web console
include::modules/cli-installing-cli-web-console-windows.adoc[leveloffset=+3]

// Installing the CLI on macOS by using the web console
include::modules/cli-installing-cli-web-console-macos.adoc[leveloffset=+3]

ifndef::openshift-origin[]
// Installing the CLI by using an RPM
include::modules/cli-installing-cli-rpm.adoc[leveloffset=+2]
endif::[]

// Installing the CLI by using Homebrew
include::modules/cli-installing-cli-brew.adoc[leveloffset=+2]

// Logging in to the CLI
include::modules/cli-logging-in.adoc[leveloffset=+1]

// Logging in to the CLI by using the web
include::modules/cli-logging-in-web.adoc[leveloffset=+1]

// Using the CLI
include::modules/cli-using-cli.adoc[leveloffset=+1]

// Getting help
include::modules/cli-getting-help.adoc[leveloffset=+1]

// Logging out of the CLI
include::modules/cli-logging-out.adoc[leveloffset=+1]
