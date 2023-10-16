// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

[id="support-network-trace-methods_{context}"]
= Network trace methods

Collecting network traces, in the form of packet capture records, can assist Red Hat Support with troubleshooting network issues.

{product-title} supports two ways of performing a network trace.
Review the following table and choose the method that meets your needs.

.Supported methods of collecting a network trace
[cols="1,4a",options="header"]
|===

|Method
|Benefits and capabilities

|Collecting a host network trace
|You perform a packet capture for a duration that you specify on one or more nodes at the same time.
The packet capture files are transferred from nodes to the client machine when the specified duration is met.

You can troubleshoot why a specific action triggers network communication issues. Run the packet capture, perform the action that triggers the issue, and use the logs to diagnose the issue.

|Collecting a network trace from an {product-title} node or container
|You perform a packet capture on one node or one container.
You run the `tcpdump` command interactively, so you can control the duration of the packet capture.

You can start the packet capture manually, trigger the network communication issue, and then stop the packet capture manually.

This method uses the `cat` command and shell redirection to copy the packet capture data from the node or container to the client machine.

|===
