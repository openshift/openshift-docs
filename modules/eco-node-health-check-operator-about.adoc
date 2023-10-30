// Module included in the following assemblies:
//
// * nodes/nodes/eco-node-health-check-operator.adoc

:_mod-docs-content-type: CONCEPT
[id="about-node-health-check-operator_{context}"]
= About the Node Health Check Operator

The Node Health Check Operator detects the health of the nodes in a cluster. The `NodeHealthCheck` controller creates the `NodeHealthCheck` custom resource (CR), which defines a set of criteria and thresholds to determine the health of a node.

The Node Health Check Operator also installs the Self Node Remediation Operator as a default remediation provider.

When the Node Health Check Operator detects an unhealthy node, it creates a remediation CR that triggers the remediation provider. For example, the controller creates the `SelfNodeRemediation` CR, which triggers the Self Node Remediation Operator to remediate the unhealthy node.

The `NodeHealthCheck` CR resembles the following YAML file:

[source,yaml]
----
apiVersion: remediation.medik8s.io/v1alpha1
kind: NodeHealthCheck
metadata:
  name: nodehealthcheck-sample
spec:
  minHealthy: 51% <1>
  pauseRequests: <2>
    - <pause-test-cluster>
  remediationTemplate: <3>
    apiVersion: self-node-remediation.medik8s.io/v1alpha1
    name: self-node-remediation-resource-deletion-template
    namespace: openshift-operators
    kind: SelfNodeRemediationTemplate
  selector: <4>
    matchExpressions:
      - key: node-role.kubernetes.io/worker
        operator: Exists
  unhealthyConditions: <5>
    - type: Ready
      status: "False"
      duration: 300s <6>
    - type: Ready
      status: Unknown
      duration: 300s <6>
----

<1> Specifies the amount of healthy nodes(in percentage or number) required for a remediation provider to concurrently remediate nodes in the targeted pool. If the number of healthy nodes equals to or exceeds the limit set by `minHealthy`, remediation occurs. The default value is 51%.
<2> Prevents any new remediation from starting, while allowing any ongoing remediations to persist. The default value is empty. However, you can enter an array of strings that identify the cause of pausing the remediation. For example, `pause-test-cluster`.
+
[NOTE]
====
During the upgrade process, nodes in the cluster might become temporarily unavailable and get identified as unhealthy. In the case of worker nodes, when the Operator detects that the cluster is upgrading, it stops remediating new unhealthy nodes to prevent such nodes from rebooting.
====
<3> Specifies a remediation template from the remediation provider. For example, from the Self Node Remediation Operator.
<4> Specifies a `selector` that matches labels or expressions that you want to check. The default value is empty, which selects all nodes.
<5> Specifies a list of the conditions that determine whether a node is considered unhealthy.
<6> Specifies the timeout duration for a node condition. If a condition is met for the duration of the timeout, the node will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy node.

[id="understanding-nhc-operator-workflow_{context}"]
== Understanding the Node Health Check Operator workflow

When a node is identified as unhealthy, the Node Health Check Operator checks how many other nodes are unhealthy. If the number of healthy nodes exceeds the amount that is specified in the `minHealthy` field of the `NodeHealthCheck` CR, the controller creates a remediation CR from the details that are provided in the external remediation template by the remediation provider. After remediation, the kubelet updates the node's health status.

When the node turns healthy, the controller deletes the external remediation template.

[id="how-nhc-prevent-conflict-with-mhc_{context}"]
== About how node health checks prevent conflicts with machine health checks

When both, node health checks and machine health checks are deployed, the node health check avoids conflict with the machine health check.

[NOTE]
====
{product-title} deploys `machine-api-termination-handler` as the default `MachineHealthCheck` resource.
====

The following list summarizes the system behavior when node health checks and machine health checks are deployed:

* If only the default machine health check exists, the node health check continues to identify unhealthy nodes. However, the node health check ignores unhealthy nodes in a Terminating state. The default machine health check handles the unhealthy nodes with a Terminating state.
+
.Example log message
[source,terminal]
----
INFO MHCChecker	ignoring unhealthy Node, it is terminating and will be handled by MHC	{"NodeName": "node-1.example.com"}
----

* If the default machine health check is modified (for example, the `unhealthyConditions` is  `Ready`), or if additional machine health checks are created, the node health check is disabled.
+
.Example log message
----
INFO controllers.NodeHealthCheck disabling NHC in order to avoid conflict with custom MHCs configured in the cluster {"NodeHealthCheck": "/nhc-worker-default"}
----

* When, again, only the default machine health check exists, the node health check is re-enabled.
+
.Example log message
----
INFO controllers.NodeHealthCheck re-enabling NHC, no conflicting MHC configured in the cluster {"NodeHealthCheck": "/nhc-worker-default"}
----
