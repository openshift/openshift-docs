:_mod-docs-content-type: ASSEMBLY
[id="about-ptp"]
= About PTP in {product-title} cluster nodes
include::_attributes/common-attributes.adoc[]
:context: about-ptp

toc::[]

Precision Time Protocol (PTP) is used to synchronize clocks in a network.
When used in conjunction with hardware support, PTP is capable of sub-microsecond accuracy, and is more accurate than Network Time Protocol (NTP).

You can configure `linuxptp` services and use PTP-capable hardware in {product-title} cluster nodes.

Use the {product-title} web console or OpenShift CLI (`oc`) to install PTP by deploying the PTP Operator. The PTP Operator creates and manages the `linuxptp` services and provides the following features:

* Discovery of the PTP-capable devices in the cluster.

* Management of the configuration of `linuxptp` services.

* Notification of PTP clock events that negatively affect the performance and reliability of your application with the PTP Operator `cloud-event-proxy` sidecar.

[NOTE]
====
The PTP Operator works with PTP-capable devices on clusters provisioned only on bare-metal infrastructure.
====

include::modules/nw-ptp-introduction.adoc[leveloffset=+1]

[IMPORTANT]
====
Before enabling PTP, ensure that NTP is disabled for the required nodes. You can disable the chrony time service (`chronyd`) using a `MachineConfig` custom resource. For more information, see xref:../../post_installation_configuration/machine-configuration-tasks.adoc#cnf-disable-chronyd_post-install-machine-configuration-tasks[Disabling chrony time service].
====

include::modules/ptp-dual-nics.adoc[leveloffset=+1]

include::modules/ptp-linuxptp-introduction.adoc[leveloffset=+1]

include::modules/ptp-overview-of-gnss-grandmaster-clock.adoc[leveloffset=+1]
