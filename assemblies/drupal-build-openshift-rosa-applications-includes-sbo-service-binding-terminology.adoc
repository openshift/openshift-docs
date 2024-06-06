// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/understanding-service-binding-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="sbo-service-binding-terminology_{context}"]
= Service Binding terminology

This section summarizes the basic terms used in Service Binding.

[horizontal]
Service binding:: The representation of the action of providing information about a service to a workload. Examples include establishing the exchange of credentials between a Java application and a database that it requires.
Backing service:: Any service or software that the application consumes over the network as part of its normal operation. Examples include a database, a message broker, an application with REST endpoints, an event stream, an Application Performance Monitor (APM), or a Hardware Security Module (HSM).
Workload (application):: Any process running within a container. Examples include a Spring Boot application, a NodeJS Express application, or a Ruby on Rails application.
Binding data:: Information about a service that you use to configure the behavior of other resources within the cluster. Examples include credentials, connection details, volume mounts, or secrets.
Binding connection:: Any connection that establishes an interaction between the connected components, such as a bindable backing service and an application requiring that backing service.