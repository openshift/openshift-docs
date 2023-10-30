// Module included in the following assemblies:
//
// * installing/installing_vsphere/installing-vsphere-post-installation-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="configuring-vSphere-connection-settings_{context}"]
= Configuring the vSphere connection settings

[role="_abstract"]
Modify the following vSphere configuration settings as required:

* vCenter address
* vCenter cluster
* vCenter username
* vCenter password
* vCenter address
* vSphere data center
* vSphere datastore
* Virtual machine folder

.Prerequisites
* The {ai-full} has finished installing the cluster successfully.
* The cluster is connected to `https://console.redhat.com`.

.Procedure
. In the Administrator perspective, navigate to *Home -> Overview*.
. Under *Status*, click *vSphere connection* to open the *vSphere connection configuration* wizard.
. In the *vCenter* field, enter the network address of the vSphere vCenter server. This can be either a domain name or an IP address. It appears in the vSphere web client URL; for example `https://[your_vCenter_address]/ui`.
. In the *vCenter cluster* field, enter the name of the vSphere vCenter cluster where {product-title} is installed.
+
[IMPORTANT]
====
This step is mandatory if you installed {product-title} 4.13 or later.
====

. In the *Username* field, enter your vSphere vCenter username.
. In the *Password* field, enter your vSphere vCenter password.
+
[WARNING]
====
The system stores the username and password in the `vsphere-creds` secret in the `kube-system` namespace of the cluster. An incorrect vCenter username or password makes the cluster nodes unschedulable.
====
+
. In the *Datacenter* field, enter the name of the vSphere data center that contains the virtual machines used to host the cluster; for example, `SDDC-Datacenter`.
. In the *Default data store* field, enter the path and name of the vSphere data store that stores the persistent data volumes; for example, `/SDDC-Datacenter/datastore/datastorename`.
+
[WARNING]
====
Updating the vSphere data center or default data store after the configuration has been saved detaches any active vSphere `PersistentVolumes`.
====
+
. In the *Virtual Machine Folder* field, enter the data center folder that contains the virtual machine of the cluster; for example, `/SDDC-Datacenter/vm/ci-ln-hjg4vg2-c61657-t2gzr`. For the {product-title} installation to succeed, all virtual machines comprising the cluster must be located in a single data center folder.
. Click *Save Configuration*. This updates the `cloud-provider-config` ConfigMap resource in the `openshift-config` namespace, and starts the configuration process.
. Reopen the *vSphere connection configuration* wizard and expand the *Monitored operators* panel. Check that the status of the operators is either *Progressing* or *Healthy*.
