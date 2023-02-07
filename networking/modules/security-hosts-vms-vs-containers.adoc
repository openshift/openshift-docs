// Module included in the following assemblies:
//
// * security/container_security/security-hosts-vms.adoc

[id="security-hosts-vms-vs-containers_{context}"]
= Comparing virtualization and containers

Traditional virtualization provides another way to keep application
environments separate on the same physical host. However, virtual machines
work in a different way than containers.
Virtualization relies on a hypervisor spinning up guest
virtual machines (VMs), each of which has its own operating system (OS),
represented by a running kernel, as well as the running application and its dependencies.

With VMs, the hypervisor isolates the guests from each other and from the host
kernel. Fewer individuals and processes have access to the hypervisor, reducing
the attack surface on the physical server. That said, security must still be
monitored: one guest VM might be able to use hypervisor bugs to gain access to
another VM or the host kernel. And, when the OS needs to be patched, it must be
patched on all guest VMs using that OS.

Containers can be run inside guest VMs, and there might be use cases where this is
desirable. For example, you might be deploying a traditional application in a
container, perhaps to lift-and-shift an application to the cloud.

Container separation on a single host, however, provides a more lightweight,
flexible, and easier-to-scale deployment solution. This deployment model is
particularly appropriate for cloud-native applications. Containers are
generally much smaller than VMs and consume less memory and CPU.

ifndef::openshift-origin[]
See link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html/overview_of_containers_in_red_hat_systems/introduction_to_linux_containers#linux_containers_compared_to_kvm_virtualization[Linux Containers Compared to KVM Virtualization]
in the {op-system-base} 7 container documentation to learn about the differences between container and VMs.
endif::[]

