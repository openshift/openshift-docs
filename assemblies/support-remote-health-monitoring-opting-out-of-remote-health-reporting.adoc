:_mod-docs-content-type: ASSEMBLY
[id="opting-out-remote-health-reporting"]
= Opting out of remote health reporting
include::_attributes/common-attributes.adoc[]
ifdef::openshift-dedicated[]
include::_attributes/attributes-openshift-dedicated.adoc[]
endif::[]
:context: opting-out-remote-health-reporting

toc::[]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
You may choose to opt out of reporting health and usage data for your cluster.
endif::[]

// moved OSD note on not able to opt out to about telemetery

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]

To opt out of remote health reporting, you must:

. xref:../../support/remote_health_monitoring/opting-out-of-remote-health-reporting.adoc#insights-operator-new-pull-secret_opting-out-remote-health-reporting[Modify the global cluster pull secret] to disable remote health reporting.
. xref:../../support/remote_health_monitoring/opting-out-of-remote-health-reporting.adoc#images-update-global-pull-secret_opting-out-remote-health-reporting[Update the cluster] to use this modified pull secret.

include::modules/telemetry-consequences-of-disabling-telemetry.adoc[leveloffset=+1]

include::modules/insights-operator-new-pull-secret-disabled.adoc[leveloffset=+1]

include::modules/insights-operator-register-disconnected-cluster.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../support/remote_health_monitoring/opting-out-of-remote-health-reporting.adoc#telemetry-consequences-of-disabling-telemetry_opting-out-remote-health-reporting[Consequences of disabling remote health reporting]
* link:https://access.redhat.com/documentation/en-us/subscription_central/2023/html/getting_started_with_the_subscriptions_service/con-how-does-subscriptionwatch-show-data_assembly-viewing-understanding-subscriptionwatch-data-ctxt[How does the subscriptions service show my subscription data?](Getting Started with the Subscription Service)

include::modules/images-update-global-pull-secret.adoc[leveloffset=+1]

endif::[]
