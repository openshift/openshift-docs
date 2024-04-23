:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="traffic-splitting-overview"]
= Traffic splitting overview
:context: traffic-splitting-overview

toc::[]

In a Knative application, traffic can be managed by creating a traffic split. A traffic split is configured as part of a route, which is managed by a Knative service.

image::knative-service-architecture.png[Traffic management for a Knative application]

Configuring a route allows requests to be sent to different revisions of a service. This routing is determined by the `traffic` spec of the `Service` object.
// add additional resources link to knative services /apps docs

A `traffic` spec declaration consists of one or more revisions, each responsible for handling a portion of the overall traffic. The percentages of traffic routed to each revision must add up to 100%, which is ensured by a Knative validation.

The revisions specified in a `traffic` spec can either be a fixed, named revision, or can point to the “latest” revision, which tracks the head of the list of all revisions for the service. The "latest" revision is a type of floating reference that updates if a new revision is created. Each revision can have a tag attached that creates an additional access URL for that revision.

The `traffic` spec can be modified by:

* Editing the YAML of a `Service` object directly.
* Using the Knative (`kn`) CLI `--traffic` flag.
* Using the {product-title} web console.

When you create a Knative service, it does not have any default `traffic` spec settings.

////
# move this to services / apps docs eventually, also include diagram again there

Each time the configuration of a service is updated, a new revision for the service is created.

A revision is a point-in-time snapshot of the code and configuration for each modification made to a Knative service. Revisions are immutable objects and can be retained for as long as they are required or used. Knative Serving revisions can be automatically scaled up and down according to incoming traffic.
////
