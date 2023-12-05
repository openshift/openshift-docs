// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-pod-topology-spread-constraints

:_mod-docs-content-type: CONCEPT
[id="nodes-scheduler-pod-topology-spread-constraints-about_{context}"]
= About pod topology spread constraints

By using a _pod topology spread constraint_, you provide fine-grained control over the distribution of pods across failure domains to help achieve high availability and more efficient resource utilization.

{product-title} administrators can label nodes to provide topology information, such as regions, zones, nodes, or other user-defined domains. After these labels are set on nodes, users can then define pod topology spread constraints to control the placement of pods across these topology domains.

You specify which pods to group together, which topology domains they are spread among, and the acceptable skew. Only pods within the same namespace are matched and grouped together when spreading due to a constraint.

// TODO Mention about relationship to affinity/anti-affinity?
