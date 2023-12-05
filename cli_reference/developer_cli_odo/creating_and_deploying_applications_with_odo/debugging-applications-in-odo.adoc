:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id='debugging-applications-in-odo']
= Debugging applications in `{odo-title}`
:context: debugging-applications-in-odo

toc::[]

With `{odo-title}`, you can attach a debugger to remotely debug your application. This feature is only supported for NodeJS and Java components.

Components created with `{odo-title}` run in the debug mode by default.  A debugger agent runs on the component, on a specific port. To start debugging your application, you must start port forwarding and attach the local debugger bundled in your Integrated development environment (IDE).

include::modules/developer-cli-odo-debugging-an-application.adoc[leveloffset=+1]
include::modules/developer-cli-odo-configuring-debugging-parameters.adoc[leveloffset=+1]
