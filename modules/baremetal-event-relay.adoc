// Module included in the following assemblies:
//
// * operators/operator-reference.adoc
[id="baremetal-event-relay_{context}"]
= {redfish-operator}

[discrete]
== Purpose
The OpenShift {redfish-operator} manages the life-cycle of the Bare Metal Event Relay. The Bare Metal Event Relay enables you to configure the types of cluster event that are monitored using Redfish hardware events.

[discrete]
== Configuration objects
You can use this command to edit the configuration after installation: for example, the webhook port.
You can edit configuration objects with:

[source,terminal]
----
$ oc -n [namespace] edit cm hw-event-proxy-operator-manager-config
----

[source,terminal]
----
apiVersion: controller-runtime.sigs.k8s.io/v1alpha1
kind: ControllerManagerConfig
health:
  healthProbeBindAddress: :8081
metrics:
  bindAddress: 127.0.0.1:8080
webhook:
  port: 9443
leaderElection:
  leaderElect: true
  resourceName: 6e7a703c.redhat-cne.org
----

[discrete]
== Project
link:https://github.com/redhat-cne/hw-event-proxy-operator[hw-event-proxy-operator]

[discrete]
== CRD
The proxy enables applications running on bare-metal clusters to respond quickly to Redfish hardware changes and failures such as breaches of temperature thresholds, fan failure, disk loss, power outages, and memory failure, reported using the HardwareEvent CR.

`hardwareevents.event.redhat-cne.org`:

* Scope: Namespaced
* CR: HardwareEvent
* Validation: Yes
