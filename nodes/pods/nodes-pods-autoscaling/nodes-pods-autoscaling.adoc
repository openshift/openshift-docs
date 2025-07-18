:_mod-docs-content-type: ASSEMBLY
:context: nodes-pods-autoscaling
[id='nodes-pods-autoscaling']
= Automatically scaling pods with the horizontal pod autoscaler
include::_attributes/common-attributes.adoc[]

toc::[]

As a developer, you can use a horizontal pod autoscaler (HPA) to
specify how {product-title} should automatically increase or decrease the scale of
a replication controller or deployment configuration, based on metrics collected
from the pods that belong to that replication controller or deployment
configuration. You can create an HPA for any deployment, deployment config, replica set, replication controller, or stateful set.

For information on scaling pods based on custom metrics, see xref:../../nodes/cma/nodes-cma-autoscaling-custom.adoc#nodes-cma-autoscaling-custom[Automatically scaling pods based on custom metrics].


[NOTE]
====
It is recommended to use a `Deployment` object or `ReplicaSet` object unless you need a specific feature or behavior provided by other objects. For more information on
these objects, see xref:../../applications/deployments/what-deployments-are.adoc#what-deployments-are[Understanding deployments].
====

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

include::modules/nodes-pods-autoscaling-about.adoc[leveloffset=+1]

include::modules/nodes-pods-autoscaling-workflow-hpa.adoc[leveloffset=+1]

include::modules/nodes-pods-autoscaling-requests-and-limits-hpa.adoc[leveloffset=+1]

include::modules/nodes-pods-autoscaling-best-practices-hpa.adoc[leveloffset=+1]

include::modules/nodes-pods-autoscaling-policies.adoc[leveloffset=+2]

include::modules/nodes-pods-autoscaling-creating-web-console.adoc[leveloffset=+1]

include::modules/nodes-pods-autoscaling-creating-cpu.adoc[leveloffset=+1]

include::modules/nodes-pods-autoscaling-creating-memory.adoc[leveloffset=+1]

include::modules/nodes-pods-autoscaling-status-about.adoc[leveloffset=+1]

include::modules/nodes-pods-autoscaling-status-viewing.adoc[leveloffset=+2]


[role="_additional-resources"]
== Additional resources
* xref:../../applications/deployments/what-deployments-are.adoc#what-deployments-are[Understanding deployments and deployment configs].
* https://cloud.redhat.com/blog/horizontal-pod-autoscaling-of-quarkus-application-based-on-memory-utilization[Horizontal Pod Autoscaling of Quarkus Application Based on Memory Utilization].
