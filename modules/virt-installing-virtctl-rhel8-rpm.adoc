// Module included in the following assemblies:
//
// * virt/getting_started/virt-using-the-cli-tools.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-installing-virtctl-rhel8-rpm_{context}"]
= Installing the virtctl RPM package on {op-system-base} 8

You can install the `virtctl` RPM package on {op-system-base-full} 8 by enabling the {VirtProductName} repository and then installing the `kubevirt-virtctl` RPM package.

.Prerequisites

* Each host in your cluster must be registered with Red Hat Subscription Manager (RHSM) and have an active {product-title} subscription.

.Procedure

. Enable the {VirtProductName} repository by using the `subscription-manager` CLI tool to run the following command:
+
[source,terminal,subs="attributes+"]
----
# subscription-manager repos --enable cnv-{VirtVersion}-for-rhel-8-x86_64-rpms
----

. Install the `kubevirt-virtctl` RPM package by running the following command:
+
[source,terminal]
----
# yum install kubevirt-virtctl
----
