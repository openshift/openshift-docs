:_mod-docs-content-type: ASSEMBLY
[id="about-hardware-enablement"]
= About specialized hardware and driver enablement
include::_attributes/common-attributes.adoc[]
:context: about-hardware-enablement

toc::[]

The Driver Toolkit (DTK) is a container image in the {product-title} payload which is meant to be used as a base image on which to build driver containers. The Driver Toolkit image contains the kernel packages commonly required as dependencies to build or install kernel modules as well as a few tools needed in driver containers. The version of these packages will match the kernel version running on the RHCOS nodes in the corresponding {product-title} release.

Driver containers are container images used for building and deploying out-of-tree kernel modules and drivers on container operating systems such as {op-system-first}. Kernel modules and drivers are software libraries running with a high level of privilege in the operating system kernel. They extend the kernel functionalities or provide the hardware-specific code required to control new devices. Examples include hardware devices like field-programmable gate arrays (FPGA) or graphics processing units (GPU), and software-defined storage solutions, which all require kernel modules on client machines. Driver containers are the first layer of the software stack used to enable these technologies on {product-title} deployments.