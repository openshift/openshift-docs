// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc
//
// Currently only in the vSphere compute machine set content, but we will want this for other platforms such as AWS and GCP.

ifeval::["{context}" == "creating-machineset-vsphere"]
:vsphere:
endif::[]

:_mod-docs-content-type: CONCEPT
[id="compute-machineset-upi-reqs_{context}"]
= Requirements for clusters with user-provisioned infrastructure to use compute machine sets

To use compute machine sets on clusters that have user-provisioned infrastructure, you must ensure that you cluster configuration supports using the Machine API.

ifeval::["{context}" == "creating-machineset-vsphere"]
:!vsphere:
endif::[]
