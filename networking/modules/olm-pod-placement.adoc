// Module included in the following assemblies:
//
// * operators/admin/olm-adding-operators-to-cluster.adoc

[id="olm-pod-placement_{context}"]
= Pod placement of Operator workloads

By default, Operator Lifecycle Manager (OLM) places pods on arbitrary worker nodes when installing an Operator or deploying Operand workloads. As an administrator, you can use projects with a combination of node selectors, taints, and tolerations to control the placement of Operators and Operands to specific nodes.

Controlling pod placement of Operator and Operand workloads has the following prerequisites:

. Determine a node or set of nodes to target for the pods per your requirements. If available, note an existing label, such as `node-role.kubernetes.io/app`, that identifies the node or nodes. Otherwise, add a label, such as `myoperator`, by using a compute machine set or editing the node directly. You will use this label in a later step as the node selector on your project.
. If you want to ensure that only pods with a certain label are allowed to run on the nodes, while steering unrelated workloads to other nodes, add a taint to the node or nodes by using a compute machine set or editing the node directly. Use an effect that ensures that new pods that do not match the taint cannot be scheduled on the nodes. For example, a `myoperator:NoSchedule` taint ensures that new pods that do not match the taint are not scheduled onto that node, but existing pods on the node are allowed to remain.
. Create a project that is configured with a default node selector and, if you added a taint, a matching toleration.

At this point, the project you created can be used to steer pods towards the specified nodes in the following scenarios:

For Operator pods::
Administrators can create a `Subscription` object in the project as described in the following section. As a result, the Operator pods are placed on the specified nodes.

For Operand pods::
Using an installed Operator, users can create an application in the project, which places the custom resource (CR) owned by the Operator in the project. As a result, the Operand pods are placed on the specified nodes, unless the Operator is deploying cluster-wide objects or resources in other namespaces, in which case this customized pod placement does not apply.
