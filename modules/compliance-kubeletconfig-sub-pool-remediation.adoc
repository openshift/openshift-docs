// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-remediation.adoc

:_mod-docs-content-type: PROCEDURE
[id="compliance-kubeletconfig-sub-pool-remediation_{context}"]
= Remediating `KubeletConfig` sub pools

`KubeletConfig` remediation labels can be applied to `MachineConfigPool` sub-pools.

.Procedure

* Add a label to the sub-pool `MachineConfigPool` CR:
+
[source,terminal]
----
$ oc label mcp <sub-pool-name> pools.operator.machineconfiguration.openshift.io/<sub-pool-name>=
----