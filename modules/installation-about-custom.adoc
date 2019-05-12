// Module included in the following assemblies:
//
// * orphaned

[id="installation-about-custom_{context}"]
= About the custom installation

You can use the {product-title} installation program to customize four levels
of the program:

* {product-title} itself
* The cluster platform
* Kubernetes
* The cluster operating system

Changes to {product-title} and its platform are managed and supported, but
changes to Kubernetes and the cluster operating system currently are not. If
you customize unsupported levels program levels, future installation and
upgrades might fail.

When you select values for the prompts that the installation program presents,
you customize {product-title}. You can further modify the cluster platform
by modifying the `install-config.yaml` file that the installation program
uses to deploy your cluster. In this file, you can make changes like setting the
number of machines that the control plane uses, the type of virtual machine
that the cluster deploys, or the CIDR range for the Kubernetes service network.

It is possible, but not supported, to modify the Kubernetes objects that are injected into the cluster.
A common modification is additional manifests in the initial installation.
No validation is available to confirm the validity of any modifications that
you make to these manifests, so if you modify these objects, you might render
your cluster non-functional.
[IMPORTANT]
====
Modifying the Kubernetes objects is not supported.
====

Similarly it is possible, but not supported, to modify the
Ignition config files for the bootstrap and other machines. No validation is
available to confirm the validity of any modifications that
you make to these Ignition config files, so if you modify these objects, you might render
your cluster non-functional.

[IMPORTANT]
====
Modifying the Ignition config files is not supported.
====

To complete a custom installation, you use the installation program to generate
the installation files and then customize them.
The installation status is stored in a hidden
file in the asset directory and contains all of the installation files.
