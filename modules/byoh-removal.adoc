// Module included in the following assemblies:
//
// * windows_containers/creating_windows_machinesets/byoh-windows-instance.adoc

[id="removing-byoh-windows-instance"]
= Removing BYOH Windows instances
You can remove BYOH instances attached to the cluster by deleting the instance's entry in the config map. Deleting an instance reverts that instance back to its state prior to adding to the cluster. Any logs and container runtime artifacts are not added to these instances.

For an instance to be cleanly removed, it must be accessible with the current private key provided to WMCO. For example, to remove the `10.1.42.1` instance from the previous example, the config map would be changed to the following:

[source,yaml]
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: windows-instances
  namespace: openshift-windows-machine-config-operator
data:
  instance.example.com: |-
    username=core
----

Deleting `windows-instances` is viewed as a request to deconstruct all Windows instances added as nodes.
