// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * post_installation_configuration/machine-configuration-tasks.adoc


ifeval::["{context}" == "installing-restricted-networks-bare-metal"]
:restricted:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-vsphere"]
:restricted:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="installation-special-config-chrony_{context}"]
= Configuring chrony time service

You
ifdef::restricted[must]
ifndef::restricted[can]
set the time server and related settings used by the chrony time service (`chronyd`)
by modifying the contents of the `chrony.conf` file and passing those contents
to your nodes as a machine config.

.Procedure

. Create a Butane config including the contents of the `chrony.conf` file. For example, to configure chrony on worker nodes, create a `99-worker-chrony.bu` file.
+
[NOTE]
====
See "Creating machine configs with Butane" for information about Butane.
====
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: {product-version}.0
metadata:
  name: 99-worker-chrony <1>
  labels:
    machineconfiguration.openshift.io/role: worker <1>
storage:
  files:
  - path: /etc/chrony.conf
    mode: 0644 <2>
    overwrite: true
    contents:
      inline: |
        pool 0.rhel.pool.ntp.org iburst <3>
        driftfile /var/lib/chrony/drift
        makestep 1.0 3
        rtcsync
        logdir /var/log/chrony
----
<1> On control plane nodes, substitute `master` for `worker` in both of these locations.
<2> Specify an octal value mode for the `mode` field in the machine config file. After creating the file and applying the changes, the `mode` is converted to a decimal value. You can check the YAML file with the command `oc get mc <mc-name> -o yaml`.
<3> Specify any valid, reachable time source, such as the one provided by your DHCP server.
ifndef::restricted[Alternately, you can specify any of the following NTP servers: `1.rhel.pool.ntp.org`, `2.rhel.pool.ntp.org`, or `3.rhel.pool.ntp.org`.]

. Use Butane to generate a `MachineConfig` object file, `99-worker-chrony.yaml`, containing the configuration to be delivered to the nodes:
+
[source,terminal]
----
$ butane 99-worker-chrony.bu -o 99-worker-chrony.yaml
----

. Apply the configurations in one of two ways:
+
* If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
+
* If the cluster is already running, apply the file:
+
[source,terminal]
----
$ oc apply -f ./99-worker-chrony.yaml
----

ifeval::["{context}" == "installing-restricted-networks-bare-metal"]
:!restricted:
endif::[]
ifeval::["{context}" == "installing-restricted-networks-vsphere"]
:!restricted:
endif::[]
