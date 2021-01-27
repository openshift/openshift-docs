// Module included in the following assemblies:
//
// * security/container_security/security-understanding.adoc

[id="security-understanding-containers_{context}"]
= What are containers?

Containers package an application and all its dependencies into a single image
that can be promoted from development, to test, to production, without change.
A container might be part of a larger application that works closely with other
containers. 

Containers provide consistency across environments and multiple deployment
targets: physical servers, virtual machines (VMs), and private or public cloud.

Some of the benefits of using containers include:

// image::whatarecontainers.png["What Are Containers?", align="center"]

[options="header"]
|===
|Infrastructure |Applications

|Sandboxed application processes on a shared Linux operating system kernel
|Package my application and all of its dependencies

|Simpler, lighter, and denser than virtual machines
|Deploy to any environment in seconds and enable CI/CD

|Portable across different environments
|Easily access and share containerized components
|===

See link:https://www.redhat.com/en/topics/containers[Understanding Linux containers] from the Red Hat Customer Portal
to find out more about Linux containers. To learn about RHEL container tools, see
link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index[Building, running, and managing containers] in the RHEL product documentation.
