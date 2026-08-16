:_mod-docs-content-type: ASSEMBLY
[id="about-knative-serving"]
= Knative Serving
:context: about-knative-serving
include::_attributes/common-attributes.adoc[]

toc::[]

Knative Serving supports developers who want to create, deploy, and manage link:https://www.redhat.com/en/topics/cloud-native-apps[cloud-native applications]. It provides a set of objects as Kubernetes custom resource definitions (CRDs) that define and control the behavior of serverless workloads on an {product-title} cluster.

Developers use these CRDs to create custom resource (CR) instances that can be used as building blocks to address complex use cases. For example:

* Rapidly deploying serverless containers.
* Automatically scaling pods.

[id="about-knative-serving-resources_{context}"]
== Knative Serving resources

Service:: The `service.serving.knative.dev` CRD automatically manages the life cycle of your workload to ensure that the application is deployed and reachable through the network. It creates a route, a configuration, and a new revision for each change to a user created service, or custom resource. Most developer interactions in Knative are carried out by modifying services.

Revision:: The `revision.serving.knative.dev` CRD is a point-in-time snapshot of the code and configuration for each modification made to the workload. Revisions are immutable objects and can be retained for as long as necessary.

Route:: The `route.serving.knative.dev` CRD maps a network endpoint to one or more revisions. You can manage the traffic in several ways, including fractional traffic and named routes.

Configuration:: The `configuration.serving.knative.dev` CRD maintains the desired state for your deployment. It provides a clean separation between code and configuration. Modifying a configuration creates a new revision.
