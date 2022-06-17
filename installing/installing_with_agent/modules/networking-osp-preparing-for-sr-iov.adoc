[id="networking-osp-preparing-for-sr-iov_{context}"]
= Preparing a cluster that runs on {rh-openstack} for SR-IOV

Before you use link:https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html-single/network_functions_virtualization_planning_and_configuration_guide/index#assembly_sriov_parameters[single root I/O virtualization (SR-IOV)] on a cluster that runs on {rh-openstack-first}, make the {rh-openstack} metadata service mountable as a drive and enable the No-IOMMU Operator for the virtual function I/O (VFIO) driver.