// Module included in the following assemblies:
//
// * scalability_and_performance/understanding-node-observability-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="workflow-node-observability-operator_{context}"]
= Workflow of the Node Observability Operator

The following workflow outlines on how to query the profiling data using the Node Observability Operator:

. Install the Node Observability Operator in the {product-title} cluster.
. Create a NodeObservability custom resource to enable the CRI-O profiling on the worker nodes of your choice.
. Run the profiling query to generate the profiling data.
