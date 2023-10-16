// Module included in the following assemblies:
//
// * TBD

[id="running-modified-installation_{context}"]
= Running a modified {product-title} installation

Running a default {product-title} {product-version} cluster is the best way to ensure that the {product-title} cluster you get will be easy to install, maintain, and upgrade going forward. However, because you may want to add to or change your {product-title} cluster, openshift-install offers several ways to modify the default installation or add to it later. These include:

* Creating an install-config file: Changing the contents of the install-config file, to identify things like the cluster name and credentials, is fully supported.
* Creating ignition-config files: Viewing ignition-config files, which define how individual nodes are configured when they are first deployed, is fully supported. However, changing those files is not supported.
* Creating Kubernetes (manifests) and {product-title} (openshift) manifest files: You can view manifest files in the manifests and openshift directories to see how Kubernetes and {product-title} features are configured, respectively. Changing those files is not supported.

Whether you want to change your {product-title} installation or simply gain a deeper understanding of the details of the installation process, the goal of this section is to step you through an {product-title} installation. Along the way, it covers:

* The underlying activities that go on under the covers to bring up an {product-title} cluster
* Major components that are leveraged ({op-system}, Ignition, Terraform, and so on)
* Opportunities to customize the install process (install configs, Ignition configs, manifests, and so on)
