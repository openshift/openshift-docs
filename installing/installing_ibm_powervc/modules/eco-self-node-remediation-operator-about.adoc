// Module included in the following assemblies:
//
// * nodes/nodes/eco-self-node-remediation-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="about-self-node-remediation-operator_{context}"]
= About the Self Node Remediation Operator

The Self Node Remediation Operator runs on the cluster nodes and reboots nodes that are identified as unhealthy. The Operator uses the `MachineHealthCheck` or `NodeHealthCheck` controller to detect the health of a node in the cluster. When a node is identified as unhealthy, the `MachineHealthCheck` or the `NodeHealthCheck` resource creates the `SelfNodeRemediation` custom resource (CR), which triggers the Self Node Remediation Operator.

The `SelfNodeRemediation` CR resembles the following YAML file:

[source,yaml]
----
apiVersion: self-node-remediation.medik8s.io/v1alpha1
kind: SelfNodeRemediation
metadata:
  name: selfnoderemediation-sample
  namespace: openshift-operators
spec:
status:
  lastError: <last_error_message> <1>
----

<1> Displays the last error that occurred during remediation. When remediation succeeds or if no errors occur, the field is left empty.

The Self Node Remediation Operator minimizes downtime for stateful applications and restores compute capacity if transient failures occur. You can use this Operator regardless of the management interface, such as IPMI or an API to provision a node, and regardless of the cluster installation type, such as installer-provisioned infrastructure or user-provisioned infrastructure.
