:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="traffic-splitting-revisions"]
= Splitting traffic between revisions
:context: traffic-splitting-revisions

toc::[]

After you create a serverless application, the application is displayed in the *Topology* view of the *Developer* perspective in the {product-title} web console. The application revision is represented by the node, and the Knative service is indicated by a quadrilateral around the node.

Any new change in the code or the service configuration creates a new revision, which is a snapshot of the code at a given time. For a service, you can manage the traffic between the revisions of the service by splitting and routing it to the different revisions as required.

// ODC
include::modules/odc-splitting-traffic-between-revisions-using-developer-perspective.adoc[leveloffset=+1]