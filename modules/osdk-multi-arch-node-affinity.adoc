// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-multi-arch-support.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-multi-arch-node-affinity_{context}"]
= About node affinity rules for multi-architecture compute machines and Operator workloads

You must set node affinity rules to ensure your Operator workloads can run on multi-architecture compute machines. Node affinity is a set of rules used by the scheduler to define a pod's placement. Setting node affinity rules ensures your Operator's workloads are scheduled to compute machines with compatible architectures.

If your Operator performs better on particular architectures, you can set preferred node affinity rules to schedule pods to machines with the specified architectures.

For more information, see "About clusters with multi-architecture compute machines" and "Controlling pod placement on nodes using node affinity rules".
