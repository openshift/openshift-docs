// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-interface-sysctl-sriov-device.adoc

:_mod-docs-content-type: CONCEPT
[id="nw-configure-sysctl-settings-flag-bonded_{context}"]
= Configuring sysctl settings for pods associated with bonded SR-IOV interface flag

You can set interface-level network `sysctl` settings for a pod connected to a bonded SR-IOV network device.

In this example, the specific network interface-level `sysctl` settings that can be configured are set on the bonded interface.

The `sysctl-tuning-test` is a namespace used in this example.

* Use the following command to create the `sysctl-tuning-test` namespace:
+
----
$ oc create namespace sysctl-tuning-test
----