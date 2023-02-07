// Module included in the following assemblies:
//
// * security/container_security/security-network.adoc

[id="security-network-multiple-pod_{context}"]
= Using multiple pod networks

Each running container has only one network interface by default.
The Multus CNI plugin lets you create multiple CNI networks, and then
attach any of those networks to your pods. In that way, you can do
things like separate private data onto a more restricted network
and have multiple network interfaces on each node.
