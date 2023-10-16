// Module included in the following assemblies:
//
// * updating/updating_a_cluster/update-using-custom-machine-config-pools.adoc

[id="update-using-custom-machine-config-pools-pause_{context}"]
= Pausing the machine config pools

In this canary rollout update process, after you label the nodes that you do not want to update with the rest of your {product-title} cluster and create the machine config pools (MCPs), you pause those MCPs. Pausing an MCP prevents the Machine Config Operator (MCO) from updating the nodes associated with that MCP.

To pause an MCP:

. Patch the MCP that you want paused:
+
[source,terminal]
----
$ oc patch mcp/<mcp_name> --patch '{"spec":{"paused":true}}' --type=merge
----
+
For example:
+
[source,terminal]
----
$  oc patch mcp/workerpool-canary --patch '{"spec":{"paused":true}}' --type=merge
----
+
.Example output
[source,terminal]
----
machineconfigpool.machineconfiguration.openshift.io/workerpool-canary patched
----

