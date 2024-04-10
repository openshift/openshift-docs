// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc

ifeval::["{context}" == "installing-aws-user-infra"]
:cp-first: Amazon Web Services
:cp: AWS
:cp-template: CloudFormation
:aws:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-aws"]
:cp-first: Amazon Web Services
:cp: AWS
:cp-template: CloudFormation
:aws:
endif::[]
ifeval::["{context}" == "installing-azure-user-infra"]
:cp-first: Microsoft Azure
:cp: Azure
:cp-template-first: Azure Resource Manager
:cp-template: ARM
:azure:
endif::[]
ifeval::["{context}" == "installing-gcp-user-infra"]
:cp-first: Google Cloud Platform
:cp: GCP
:cp-template: Deployment Manager
:gcp:
endif::[]
ifeval::["{context}" == "installing-gcp-user-infra-vpc"]
:cp-first: Google Cloud Platform
:cp: GCP
:cp-template: Deployment Manager
:gcp:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-gcp"]
:cp-first: Google Cloud Platform
:cp: GCP
:cp-template: Deployment Manager
:gcp:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-vsphere"]
:cp-first: VMware vSphere
:cp: vSphere
:vsphere:
endif::[]
ifeval::["{context}" == "installing-vsphere"]
:cp-first: VMware vSphere
:cp: vSphere
:vsphere:
endif::[]
ifeval::["{context}" == "installing-vsphere-network-customizations"]
:cp-first: VMware vSphere
:cp: vSphere
:vsphere:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="installation-extracting-infraid_{context}"]
= Extracting the infrastructure name

ifdef::aws,gcp[]
The Ignition config files contain a unique cluster identifier that you can use to
uniquely identify your cluster in {cp-first} ({cp}). The infrastructure name is also used to locate the appropriate {cp} resources during an {product-title} installation. The provided {cp-template}
templates contain references to this infrastructure name, so you must extract
it.
endif::aws,gcp[]

ifdef::azure[]
The Ignition config files contain a unique cluster identifier that you can use to
uniquely identify your cluster in {cp-first}. The provided {cp-template-first} ({cp-template})
templates contain references to this infrastructure name, so you must extract
it.
endif::azure[]

ifdef::vsphere[]
The Ignition config files contain a unique cluster identifier that you can use to
uniquely identify your cluster in {cp-first}. If you plan to use the cluster identifier as the name of your virtual machine folder, you must extract it.
endif::vsphere[]

.Prerequisites

* You obtained the {product-title} installation program and the pull secret for your cluster.
* You generated the Ignition config files for your cluster.
* You installed the `jq` package.

.Procedure

* To extract and view the infrastructure name from the Ignition config file
metadata, run the following command:
+
[source,terminal]
----
$ jq -r .infraID <installation_directory>/metadata.json <1>
----
<1> For `<installation_directory>`, specify the path to the directory that you stored the
installation files in.
+
.Example output
[source,terminal]
----
openshift-vw9j6 <1>
----
<1> The output of this command is your cluster name and a random string.

ifeval::["{context}" == "installing-aws-user-infra"]
:!cp-first:
:!cp:
:!cp-template:
:!aws:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-aws"]
:!cp-first:
:!cp:
:!cp-template:
:!aws:
endif::[]
ifeval::["{context}" == "installing-azure-user-infra"]
:!cp-first:
:!cp:
:!cp-template-first:
:!cp-template:
:!azure:
endif::[]
ifeval::["{context}" == "installing-gcp-user-infra"]
:!cp-first:
:!cp:
:!cp-template:
:!gcp:
endif::[]
ifeval::["{context}" == "installing-gcp-user-infra-vpc"]
:!cp-first: Google Cloud Platform
:!cp: GCP
:!cp-template: Deployment Manager
:!gcp:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-gcp"]
:!cp-first:
:!cp:
:!cp-template:
:!gcp:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-vsphere"]
:!cp-first: VMware vSphere
:!cp: vSphere
:!vsphere:
endif::[]
ifeval::["{context}" == "installing-vsphere"]
:!cp-first: VMware vSphere
:!cp: vSphere
:!vsphere:
endif::[]
ifeval::["{context}" == "installing-vsphere-network-customizations"]
:!cp-first: VMware vSphere
:!cp: vSphere
:!vsphere:
endif::[]
