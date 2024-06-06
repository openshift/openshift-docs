// Module included in the following assemblies:
//
// * architecture/control-plane.adoc
// * operators/index.adoc


ifeval::["{context}" == "operators-overview"]
:index:
endif::[]

:_mod-docs-content-type: CONCEPT
ifndef::index[]
[id="operators-overview_{context}"]
= Operators in {product-title}
endif::[]

Operators are among the most important components of {product-title}. Operators are the preferred method of packaging, deploying, and managing services on the control plane. They can also provide advantages to applications that users run.

Operators integrate with Kubernetes APIs and CLI tools such as `kubectl` and `oc` commands. They provide the means of monitoring applications, performing health checks, managing over-the-air (OTA) updates, and ensuring that applications remain in your specified state.

ifndef::index[]
Operators also offer a more granular configuration experience. You configure each component by modifying the API that the Operator exposes instead of modifying a global configuration file.

Because CRI-O and the Kubelet run on every node, almost every other cluster function can be managed on the control plane by using Operators. Components that are added to the control plane by using Operators include critical networking and credential services.
endif::[]

While both follow similar Operator concepts and goals, Operators in {product-title} are managed by two different systems, depending on their purpose:

* Cluster Operators, which are managed by the Cluster Version Operator (CVO), are installed by default to perform cluster functions.
* Optional add-on Operators, which are managed by Operator Lifecycle Manager (OLM), can be made accessible for users to run in their applications.

ifeval::["{context}" == "operators-overview"]
:!index:
endif::[]
