// Module included in the following assemblies:
//
// * nodes/nodes-pods-plugins.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-plugins-install_{context}"]
= Enabling Device Manager

Enable Device Manager to implement a device plugin to advertise specialized
hardware without any upstream code changes.

Device Manager provides a mechanism for advertising specialized node hardware resources
with the help of plugins known as device plugins.

. Obtain the label associated with the static `MachineConfigPool` CRD for the type of node you want to configure by entering the following command.
Perform one of the following steps:

.. View the machine config:
+
[source,terminal]
----
# oc describe machineconfig <name>
----
+
For example:
+
[source,terminal]
----
# oc describe machineconfig 00-worker
----
+
.Example output
[source,terminal]
----
Name:         00-worker
Namespace:
Labels:       machineconfiguration.openshift.io/role=worker <1>
----
<1> Label required for the Device Manager.

.Procedure

. Create a custom resource (CR) for your configuration change.
+
.Sample configuration for a Device Manager CR
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: devicemgr <1>
spec:
  machineConfigPoolSelector:
    matchLabels:
       machineconfiguration.openshift.io: devicemgr <2>
  kubeletConfig:
    feature-gates:
      - DevicePlugins=true <3>
----
<1> Assign a name to CR.
<2> Enter the label from the Machine Config Pool.
<3> Set `DevicePlugins` to 'true`.

. Create the Device Manager:
+
[source,terminal]
----
$ oc create -f devicemgr.yaml
----
+
.Example output
[source,terminal]
----
kubeletconfig.machineconfiguration.openshift.io/devicemgr created
----

. Ensure that Device Manager was actually enabled by confirming that
*_/var/lib/kubelet/device-plugins/kubelet.sock_* is created on the node. This is
the UNIX domain socket on which the Device Manager gRPC server listens for new
plugin registrations. This sock file is created when the Kubelet is started
only if Device Manager is enabled.
