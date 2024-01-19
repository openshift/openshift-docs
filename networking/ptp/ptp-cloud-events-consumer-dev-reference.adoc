:_mod-docs-content-type: ASSEMBLY
[id="ptp-cloud-events-consumer-dev-reference"]
= Developing PTP events consumer applications
include::_attributes/common-attributes.adoc[]
:context: ptp-consumer

toc::[]

When developing consumer applications that make use of Precision Time Protocol (PTP) events on a bare-metal cluster node, you need to deploy your consumer application and a `cloud-event-proxy` container in a separate application pod.
The `cloud-event-proxy` container receives the events from the PTP Operator pod and passes it to the consumer application.
The consumer application subscribes to the events posted in the `cloud-event-proxy` container by using a REST API.

For more information about deploying PTP events applications, see xref:../../networking/ptp/using-ptp-events.adoc#cnf-about-ptp-fast-event-notifications-framework_using-ptp-hardware-fast-events-framework[About the PTP fast event notifications framework].

[NOTE]
====
The following information provides general guidance for developing consumer applications that use PTP events.
A complete events consumer application example is outside the scope of this information.
====

include::modules/ptp-events-consumer-application.adoc[leveloffset=+1]

include::modules/ptp-reference-deployment-and-service-crs.adoc[leveloffset=+1]

include::modules/ptp-cloud-event-proxy-sidecar-api.adoc[leveloffset=+1]

include::modules/ptp-subscribing-consumer-app-to-events.adoc[leveloffset=+1]

include::modules/ptp-getting-the-current-ptp-clock-status.adoc[leveloffset=+1]

include::modules/ptp-verifying-events-consumer-app-is-receiving-events.adoc[leveloffset=+1]
