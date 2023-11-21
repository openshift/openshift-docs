// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-custom-metrics-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-custom-monitoring-label-for-vms_{context}"]
= Creating a custom monitoring label for virtual machines

To enable queries to multiple virtual machines from a single service, add a custom label in the virtual machine's YAML file.

.Prerequisites

* Install the {product-title} CLI `oc`.
* Log in as a user with `cluster-admin` privileges.
* Access to the web console for stop and restart a virtual machine.

.Procedure
. Edit the `template` spec of your virtual machine configuration file. In this example, the label `monitor` has the value `metrics`.
+
[source,yaml]
----
spec:
  template:
    metadata:
      labels:
        monitor: metrics
----

. Stop and restart the virtual machine to create a new pod with the label name given to the `monitor` label.
