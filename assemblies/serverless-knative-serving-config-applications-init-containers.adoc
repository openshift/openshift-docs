:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="init-containers"]
= Init containers
:context: init-containers

link:https://kubernetes.io/docs/concepts/workloads/pods/init-containers/[Init containers] are specialized containers that are run before application containers in a pod. They are generally used to implement initialization logic for an application, which may include running setup scripts or downloading required configurations. You can enable the use of init containers for Knative services by modifying the `KnativeServing` custom resource (CR).

[NOTE]
====
Init containers may cause longer application start-up times and should be used with caution for serverless applications, which are expected to scale up and down frequently.
====

// enable init containers
include::modules/serverless-admin-init-containers.adoc[leveloffset=+1]