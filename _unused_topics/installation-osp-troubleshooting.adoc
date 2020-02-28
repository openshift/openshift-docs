// Module included in the following assemblies:
//
// * n/a

[id="installation-osp-customizing_{context}"]

= Troubleshooting {product-title} on OpenStack installations

// Structure as needed in the end. This is very much a WIP.
// A few more troubleshooting and/or known issues blurbs incoming

Unfortunately, there will always be some cases where {product-title} fails to install properly. In these events, it is helpful to understand the likely failure modes as well as how to troubleshoot the failure.

This document discusses some troubleshooting options for {rh-openstack}-based
deployments. For general tips on troubleshooting the installation program, see the [Installer Troubleshooting](../troubleshooting.md) guide.

== View instance logs

{rh-openstack} CLI tools must be installed, then:

----
$ openstack console log show <instance>
----

== Connect to instances via SSH

Get the IP address of the machine on the private network:
```
openstack server list | grep master
| 0dcd756b-ad80-42f1-987a-1451b1ae95ba | cluster-wbzrr-master-1     | ACTIVE    | cluster-wbzrr-openshift=172.24.0.21                | rhcos           | m1.s2.xlarge |
| 3b455e43-729b-4e64-b3bd-1d4da9996f27 | cluster-wbzrr-master-2     | ACTIVE    | cluster-wbzrr-openshift=172.24.0.18                | rhcos           | m1.s2.xlarge |
| 775898c3-ecc2-41a4-b98b-a4cd5ae56fd0 | cluster-wbzrr-master-0     | ACTIVE    | cluster-wbzrr-openshift=172.24.0.12                | rhcos           | m1.s2.xlarge |
```

And connect to it using the control plane machine currently holding the API as a jumpbox:

```
ssh -J core@${floating IP address}<1> core@<host>
```
<1> The floating IP address assigned to the control plane machine.
