// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-HCOInstallationIncomplete"]
= HCOInstallationIncomplete

[discrete]
[id="meaning-hcoinstallationincomplete"]
== Meaning

This alert fires when the HyperConverged Cluster Operator (HCO) runs for
more than an hour without a `HyperConverged` custom resource (CR).

This alert has the following causes:

* During the installation process, you installed the HCO but you did not
create the `HyperConverged` CR.
* During the uninstall process, you removed the `HyperConverged` CR before
uninstalling the HCO and the HCO is still running.

[discrete]
[id="mitigation-hcoinstallationincomplete"]
== Mitigation

The mitigation depends on whether you are installing or uninstalling
the HCO:

* Complete the installation by creating a `HyperConverged` CR with its
default values:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: hco-operatorgroup
  namespace: kubevirt-hyperconverged
spec: {}
EOF
----

* Uninstall the HCO. If the uninstall process continues to run, you must
resolve that issue in order to cancel the alert.
