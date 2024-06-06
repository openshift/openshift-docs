// Module included in the following assemblies:
// * openshift_images/images-understand.aodc

[id="containers-about_{context}"]
= Containers

The basic units of {product-title} applications are called containers. link:https://www.redhat.com/en/topics/containers#overview[Linux container technologies] are lightweight mechanisms for isolating running processes so that they are limited to interacting with only their designated resources. The word container is defined as a specific running or paused instance of a container image.

Many application instances can be running in containers on a single host without visibility into each others' processes, files, network, and so on. Typically, each container provides a single service, often called a micro-service, such as a web server or a database, though containers can be used for arbitrary workloads.

The Linux kernel has been incorporating capabilities for container technologies for years. The Docker project developed a convenient management interface for Linux containers on a host. More recently, the link:https://github.com/opencontainers/[Open Container Initiative] has developed open standards for container formats and container runtimes. {product-title} and Kubernetes add the ability to orchestrate OCI- and Docker-formatted containers across multi-host installations.

Though you do not directly interact with container runtimes when using {product-title}, understanding their capabilities and terminology is important for understanding their role in {product-title} and how your applications function inside of containers.

Tools such as link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html-single/managing_containers/#using_podman_to_work_with_containers[podman] can be used to replace `docker` command-line tools for running and managing containers directly. Using `podman`, you can experiment with containers separately from {product-title}.
