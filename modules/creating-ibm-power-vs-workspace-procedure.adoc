// * installing/installing_ibm_powervs/creating-ibm-power-vs-workspace.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-ibm-power-vs-workspace-procedure_{context}"]
= Creating an {ibm-power-server-title} workspace

Use the following procedure to create an {ibm-power-server-name} workspace.

.Procedure

. To create an {ibm-power-server-name} workspace, complete step 1 to step 5 from the {ibm-cloud-name} documentation for link:https://cloud.ibm.com/docs/power-iaas?topic=power-iaas-creating-power-virtual-server[Creating an {ibm-power-server-name}].

. After it has finished provisioning, retrieve the 32-character alphanumeric Globally Unique Identifier (GUID) of your new workspace by entering the following command:
+
[source,terminal]
----
$ ibmcloud resource service-instance <workspace name>
----
+
