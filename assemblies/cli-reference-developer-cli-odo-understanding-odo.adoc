////
:_mod-docs-content-type: ASSEMBLY
[id="understanding-odo"]
= Understanding odo
include::_attributes/common-attributes.adoc[]
:context: understanding-odo

toc::[]

Red Hat OpenShift Developer CLI (`odo`) is a tool for creating applications on {product-title} and Kubernetes. With `{odo-title}`, you can develop, test, debug, and deploy microservices-based applications on a Kubernetes cluster without having a deep understanding of the platform.

`{odo-title}` follows a _create and push_ workflow. As a user, when you _create_, the information (or manifest) is stored in a configuration file. When you _push_, the corresponding resources are created on the Kubernetes cluster. All of this configuration is stored in the Kubernetes API for seamless accessibility and functionality.

`{odo-title}` uses _service_ and _link_ commands to link components and services together. `{odo-title}` achieves this by creating and deploying services based on Kubernetes Operators in the cluster. Services can be created using any of the Operators available on the Operator Hub. After linking a service, `odo` injects the service configuration into the component. Your application can then use this configuration to communicate with the Operator-backed service.

include::modules/odo-key-features.adoc[leveloffset=+1]
include::modules/odo-core-concepts.adoc[leveloffset=+1]
include::modules/odo-listing-components.adoc[leveloffset=+1]
include::modules/odo-telemetry.adoc[leveloffset=+1]
////