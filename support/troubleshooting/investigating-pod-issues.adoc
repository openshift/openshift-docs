:_mod-docs-content-type: ASSEMBLY
[id="investigating-pod-issues"]
= Investigating pod issues
include::_attributes/common-attributes.adoc[]
:context: investigating-pod-issues

toc::[]

{product-title} leverages the Kubernetes concept of a pod, which is one or more containers deployed together on one host. A pod is the smallest compute unit that can be defined, deployed, and managed on {product-title} {product-version}.

After a pod is defined, it is assigned to run on a node until its containers exit, or until it is removed. Depending on policy and exit code, Pods are either removed after exiting or retained so that their logs can be accessed.

The first thing to check when pod issues arise is the pod's status. If an explicit pod failure has occurred, observe the pod's error state to identify specific image, container, or pod network issues. Focus diagnostic data collection according to the error state. Review pod event messages, as well as pod and container log information. Diagnose issues dynamically by accessing running Pods on the command line, or start a debug pod with root access based on a problematic pod's deployment configuration.

// Understanding pod error states
include::modules/understanding-pod-error-states.adoc[leveloffset=+1]

// Reviewing pod status
include::modules/reviewing-pod-status.adoc[leveloffset=+1]

// Inspecting pod and container logs
include::modules/inspecting-pod-and-container-logs.adoc[leveloffset=+1]

// Accessing running pods
include::modules/accessing-running-pods.adoc[leveloffset=+1]

// Starting debug pods with root access
include::modules/starting-debug-pods-with-root-access.adoc[leveloffset=+1]

// Copying files to and from pods and containers
include::modules/copying-files-pods-and-containers.adoc[leveloffset=+1]
