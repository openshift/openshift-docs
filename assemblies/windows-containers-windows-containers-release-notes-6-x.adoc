:_mod-docs-content-type: ASSEMBLY
[id="windows-containers-release-notes-6-x"]
= {productwinc} release notes
include::_attributes/common-attributes.adoc[]
:context: windows-containers-release-notes

toc::[]

[id="about-windows-containers"]
== About {productwinc}

Windows Container Support for Red Hat OpenShift enables running Windows compute nodes in an {product-title} cluster. Running Windows workloads is possible by using the Red Hat Windows Machine Config Operator (WMCO) to install and manage Windows nodes. With Windows nodes available, you can run Windows container workloads in {product-title}.

The release notes for Red Hat OpenShift for Windows Containers tracks the development of the WMCO, which provides all Windows container workload capabilities in {product-title}.

ifndef::openshift-origin[]
[id="getting-support"]
== Getting support

// wording taken and modified from https://access.redhat.com/support/policy/updates/openshift#windows

Windows Container Support for Red Hat OpenShift is provided and available as an optional, installable component. Windows Container Support for Red Hat OpenShift is not part of the {product-title} subscription. It requires an additional Red Hat subscription and is supported according to the link:https://access.redhat.com/support/offerings/production/soc/[Scope of coverage] and link:https://access.redhat.com/support/offerings/production/sla[Service level agreements].

You must have this separate subscription to receive support for Windows Container Support for Red Hat OpenShift. Without this additional Red Hat subscription, deploying Windows container workloads in production clusters is not supported. You can request support through the link:http://access.redhat.com/[Red Hat Customer Portal].

For more information, see the Red Hat OpenShift Container Platform Life Cycle Policy document for link:https://access.redhat.com/support/policy/updates/openshift#windows[{productwinc}].

If you do not have this additional Red Hat subscription, you can use the Community Windows Machine Config Operator, a distribution that lacks official support.
endif::openshift-origin[]

[id="wmco-6-0-0"]
== Release notes for Red Hat Windows Machine Config Operator 6.0.0

This release of the WMCO provides bug fixes for running Windows compute nodes in an {product-title} cluster. The components of the WMCO 6.0.0 were released in

=== New features and improvements
[id="wmco-6.0.0-node-certificates"]
==== Windows node certificates are updated

With this release, the WMCO updates the Windows node certificates when the kubelet client certificate authority (CA) certificate is rotated.

[id="wmco-6-0-0-new-features"]
=== New features

[id="wmco-6-0-0-containerd"]
==== Containerd is the default container runtime

Because the Docker runtime is deprecated in Kubernetes 1.24, containerD is now the default runtime for WMCO-supported Windows nodes. Upon the installation of or an upgrade to WMCO 6.0.0, containerd is installed as a Windows service. The kubelet now uses containerd for image pulls instead of the Docker runtime. Users no longer need to enable the Docker-formatted container runtime or install the Docker container runtime on Bring-Your-Own-Host (BYOH) instances. You can continue to use nodes based on VM images that use Docker. containerd can run along with the Docker service.

The WMCO supports a Windows golden image with or without Docker for vSphere and Bring-Your-Own-Host (BYOH) Windows instances.

include::modules/wmco-prerequisites.adoc[leveloffset=+1]

include::modules/windows-containers-release-notes-limitations.adoc[leveloffset=+1]

