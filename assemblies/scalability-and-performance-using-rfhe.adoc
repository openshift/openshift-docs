:_mod-docs-content-type: ASSEMBLY
[id="using-rfhe"]
= Monitoring bare-metal events with the {redfish-operator}
include::_attributes/common-attributes.adoc[]
:context: using-rfhe

toc::[]

:FeatureName: Bare Metal Event Relay
include::snippets/technology-preview.adoc[]

[id="about-using-redfish-hardware-events"]
== About bare-metal events

Use the {redfish-operator} to subscribe applications that run in your {product-title} cluster to events that are generated on the underlying bare-metal host. The Redfish service publishes events on a node and transmits them on an advanced message queue to subscribed applications.

Bare-metal events are based on the open Redfish standard that is developed under the guidance of the Distributed Management Task Force (DMTF). Redfish provides a secure industry-standard protocol with a REST API. The protocol is used for the management of distributed, converged or software-defined resources and infrastructure.

Hardware-related events published through Redfish includes:

* Breaches of temperature limits
* Server status
* Fan status

Begin using bare-metal events by deploying the {redfish-operator} Operator and subscribing your application to the service. The {redfish-operator} Operator installs and manages the lifecycle of the Redfish bare-metal event service.

[NOTE]
====
The {redfish-operator} works only with Redfish-capable devices on single-node clusters provisioned on bare-metal infrastructure.
====

include::modules/nw-rfhe-introduction.adoc[leveloffset=+1]

include::modules/nw-rfhe-installing-operator-cli.adoc[leveloffset=+2]

include::modules/nw-rfhe-installing-operator-web-console.adoc[leveloffset=+2]

include::modules/hw-installing-amq-interconnect-messaging-bus.adoc[leveloffset=+1]

[id="subscribing-hw-events"]
== Subscribing to Redfish BMC bare-metal events for a cluster node

You can subscribe to Redfish BMC events generated on a node in your cluster by creating a `BMCEventSubscription` custom resource (CR) for the node, creating a `HardwareEvent` CR for the event, and creating a `Secret` CR for the BMC.

include::modules/nw-rfhe-creating-bmc-event-sub.adoc[leveloffset=+2]

include::modules/nw-rfhe-quering-redfish-hardware-event-subs.adoc[leveloffset=+2]

include::modules/nw-rfhe-creating-hardware-event.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../storage/persistent_storage/persistent_storage_local/persistent-storage-local.adoc#persistent-storage-using-local-volume[Persistent storage using local volumes]

include::modules/cnf-rfhe-notifications-api-refererence.adoc[leveloffset=+1]

include::modules/cnf-migrating-from-amqp-to-http-transport.adoc[leveloffset=+1]
