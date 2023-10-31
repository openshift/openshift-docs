// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/understanding-service-binding-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="sbo-about-service-binding-operator_{context}"]
= About {servicebinding-title}

The {servicebinding-title} consists of a controller and an accompanying custom resource definition (CRD) for service binding. It manages the data plane for workloads and backing services. The Service Binding Controller reads the data made available by the control plane of backing services. Then, it projects this data to workloads according to the rules specified through the `ServiceBinding` resource.

As a result, the {servicebinding-title} enables workloads to use backing services or external services by automatically collecting and sharing binding data with the workloads. The process involves making the backing service bindable and binding the workload and the service together.

[id="making-an-operator-managed-backing-service-bindable_{context}"]
== Making an Operator-managed backing service bindable
To make a service bindable, as an Operator provider, you need to expose the binding data required by workloads to bind with the services provided by the Operator. You can provide the binding data either as annotations or as descriptors in the CRD of the Operator that manages the backing service.

[id="binding-a-workload-together-with-a-backing-service_{context}"]
== Binding a workload together with a backing service
By using the {servicebinding-title}, as an application developer, you need to declare the intent of establishing a binding connection. You must create a `ServiceBinding` CR  that references the backing service. This action triggers the {servicebinding-title} to project the exposed binding data into the workload. The {servicebinding-title} receives the declared intent and binds the workload together with the backing service.

The CRD of the {servicebinding-title} supports the following APIs:

* *Service Binding* with the `binding.operators.coreos.com` API group.

* *Service Binding (Spec API)* with the `servicebinding.io` API group.

With {servicebinding-title}, you can:

* Bind your workloads to Operator-managed backing services.
* Automate configuration of binding data.
* Provide service operators with a low-touch administrative experience to provision and manage access to services.
* Enrich the development lifecycle with a consistent and declarative service binding method that eliminates discrepancies in cluster environments.