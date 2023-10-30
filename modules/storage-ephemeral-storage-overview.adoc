// Module included in the following assemblies:
//
// storage/understanding-persistent-storage.adoc[leveloffset=+1]
//* microshift_storage/understanding-ephemeral-storage-microshift.adoc


:_mod-docs-content-type: CONCEPT
[id=storage-ephemeral-storage-overview_{context}]
= Overview

In addition to persistent storage, pods and containers can require ephemeral or transient local storage for their operation. The lifetime of this ephemeral storage does not extend beyond the life of the individual pod, and this ephemeral storage cannot be shared across pods.

Pods use ephemeral local storage for scratch space, caching, and logs. Issues related to the lack of local storage accounting and isolation include the following:

* Pods cannot detect how much local storage is available to them.
* Pods cannot request guaranteed local storage.
* Local storage is a best-effort resource.
* Pods can be evicted due to other pods filling the local storage, after which new pods are not admitted until sufficient storage is reclaimed.

ifndef::microshift[]
Unlike persistent volumes, ephemeral storage is unstructured and the space is shared between all pods running on a node, in addition to other uses by the system, the container runtime, and {product-title}. The ephemeral storage framework allows pods to specify their transient local storage needs. It also allows {product-title} to schedule pods where appropriate, and to protect the node against excessive use of local storage.
endif::microshift[]

ifdef::microshift[]
Unlike persistent volumes, ephemeral storage is unstructured and the space is shared between all pods running on the node, other uses by the system, and {product-title}. The ephemeral storage framework allows pods to specify their transient local storage needs. It also allows {product-title} to protect the node against excessive use of local storage.
endif::microshift[]

While the ephemeral storage framework allows administrators and developers to better manage local storage, I/O throughput and latency are not directly effected.