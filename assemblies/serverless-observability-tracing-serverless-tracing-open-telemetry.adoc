:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-tracing-open-telemetry"]
= Using Red Hat OpenShift distributed tracing
:context: serverless-tracing-open-telemetry

You can use {DTProductName} with {ServerlessProductName} to monitor and troubleshoot serverless applications.

ifdef::openshift-enterprise[]
// we can only use this module for OCP until OSD docs have distributed tracing install docs available, since this is part of the prereqs
include::modules/serverless-open-telemetry.adoc[leveloffset=+1]
endif::[]
