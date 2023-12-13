// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

:_mod-docs-content-type: REFERENCE
[id="what-information-is-collected_{context}"]
= Information collected by Telemetry

The following information is collected by Telemetry:

[id="system-information_{context}"]
== System information

* Version information, including the {product-title} cluster version and installed update details that are used to determine update version availability
* Update information, including the number of updates available per cluster, the channel and image repository used for an update, update progress information, and the number of errors that occur in an update
* The unique random identifier that is generated during an installation
* Configuration details that help Red Hat Support to provide beneficial support for customers, including node configuration at the cloud infrastructure level, hostnames, IP addresses, Kubernetes pod names, namespaces, and services
* The {product-title} framework components installed in a cluster and their condition and status
* Events for all namespaces listed as "related objects" for a degraded Operator
* Information about degraded software
* Information about the validity of certificates
* The name of the provider platform that {product-title} is deployed on and the data center location

[id="sizing-information_{context}"]
== Sizing Information

* Sizing information about clusters, machine types, and machines, including the number of CPU cores and the amount of RAM used for each
ifdef::virt-cluster[]
* The number of running virtual machine instances in a cluster
endif::virt-cluster[]
* The number of etcd members and the number of objects stored in the etcd cluster
ifndef::openshift-dedicated[]
* Number of application builds by build strategy type
endif::openshift-dedicated[]

[id="usage-information_{context}"]
== Usage information

* Usage information about components, features, and extensions
* Usage details about Technology Previews and unsupported configurations

Telemetry does not collect identifying information such as usernames or passwords. Red Hat does not intend to collect personal information. If Red Hat discovers that personal information has been inadvertently received, Red Hat will delete such information. To the extent that any telemetry data constitutes personal data, please refer to the link:https://www.redhat.com/en/about/privacy-policy[Red Hat Privacy Statement] for more information about Red Hat's privacy practices.

