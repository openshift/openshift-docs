:_mod-docs-content-type: ASSEMBLY
[id="using-pod-level-bonding"]
= Using pod-level bonding
include::_attributes/common-attributes.adoc[]
:context: using-pod-level-bonding

toc::[]


:FeatureName: Bond Container Network Interface (CNI)

Bonding at the pod level is vital to enable workloads inside pods that require high availability and more throughput. With pod-level bonding, you can create a bond interface from multiple single root I/O virtualization (SR-IOV) virtual function interfaces in a kernel mode interface. The SR-IOV virtual functions are passed into the pod and attached to a kernel driver.

One scenario where pod level bonding is required is creating a bond interface from multiple SR-IOV virtual functions on different physical functions. Creating a bond interface from two different physical functions on the host can be used to achieve high availability and throughput at pod level.

For guidance on tasks such as creating a SR-IOV network, network policies, network attachment definitions and pods, see  xref:../../networking/hardware_networks/configuring-sriov-device.adoc#configuring-sriov-device[Configuring an SR-IOV network device].

include::modules/nw-sriov-cfg-bond-interface-with-virtual-functions.adoc[leveloffset=+1]