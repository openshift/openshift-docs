// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/odo-architecture.adoc

[id="openshift-source-to-image_{context}"]

= OpenShift source-to-image 

OpenShift Source-to-Image (S2I) is an open-source project which helps in building artifacts from source code and injecting these into container images. S2I produces ready-to-run images by building source code without the need of a Dockerfile.
{odo-title} uses S2I builder image for executing developer source code inside a container.
