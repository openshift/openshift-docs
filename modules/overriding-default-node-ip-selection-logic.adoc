// This is included in the following assemblies:
//
// * troubleshooting-network-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="overriding-default-node-ip-selection-logic_{context}"]
= Optional: Overriding the default node IP selection logic

To override the default IP selection logic, you can create a hint file that includes the `NODEIP_HINT` variable to override the default IP selection logic. Creating a hint file allows you to select a specific node IP address from the interface in the subnet of the IP address specified in the `NODEIP_HINT` variable.

For example, if a node has two interfaces, `eth0` with an address of `10.0.0.10/24`, and `eth1` with an address of `192.0.2.5/24`, and the default route points to `eth0` (`10.0.0.10`),the node IP address would normally use the `10.0.0.10` IP address.

Users can configure the `NODEIP_HINT` variable to point at a known IP in the subnet, for example, a subnet gateway such as `192.0.2.1` so that the other subnet, `192.0.2.0/24`, is selected. As a result, the `192.0.2.5` IP address on `eth1` is used for the node.

The following procedure shows how to override the default node IP selection logic.

.Procedure

. Add a hint file to your `/etc/default/nodeip-configuration` file, for example:
+
[source,text]
----
NODEIP_HINT=192.0.2.1
----
+
[IMPORTANT]
====
* Do not use the exact IP address of a node as a hint, for example, `192.0.2.5`. Using the exact IP address of a node causes the node using the hint IP address to fail to configure correctly.
* The IP address in the hint file is only used to determine the correct subnet. It will not receive traffic as a result of appearing in the hint file.
====

. Generate the `base-64` encoded content by running the following command:
+
[source,terminal]
----
$ echo -n 'NODEIP_HINT=192.0.2.1' | base64 -w0
----
+
.Example output
+
[source,terminal]
----
Tk9ERUlQX0hJTlQ9MTkyLjAuMCxxxx==
----

. Activate the hint by creating a machine config manifest for both `master` and `worker` roles before deploying the cluster:
+
.99-nodeip-hint-master.yaml
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 99-nodeip-hint-master
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,<encoded_content> # <1>
        mode: 0644
        overwrite: true
        path: /etc/default/nodeip-configuration
----
+
<1> Replace `<encoded_contents>` with the  base64-encoded content of the `/etc/default/nodeip-configuration` file, for example, `Tk9ERUlQX0hJTlQ9MTkyLjAuMCxxxx==`. Note that a space is not acceptable after the comma and before the encoded content.
+
.99-nodeip-hint-worker.yaml
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
 labels:
   machineconfiguration.openshift.io/role: worker
   name: 99-nodeip-hint-worker
spec:
 config:
   ignition:
     version: 3.2.0
   storage:
     files:
     - contents:
         source: data:text/plain;charset=utf-8;base64,<encoded_content> # <1>
       mode: 0644
       overwrite: true
       path: /etc/default/nodeip-configuration
----
<1> Replace `<encoded_contents>` with the  base64-encoded content of the `/etc/default/nodeip-configuration` file, for example, `Tk9ERUlQX0hJTlQ9MTkyLjAuMCxxxx==`. Note that a space is not acceptable after the comma and before the encoded content.

. Save the manifest to the directory where you store your cluster configuration, for example, `~/clusterconfigs`.

. Deploy the cluster.
