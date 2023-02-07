// Module included in the following assemblies:
//
// * architecture/architecture_rhcos.adoc

[id="digging-into-machine-config_{context}"]
= Changing Ignition configs after installation

Machine config pools manage a cluster of nodes and their corresponding machine
configs. Machine configs contain configuration information for a cluster.
To list all machine config pools that are known:

[source,terminal]
----
$ oc get machineconfigpools
----

.Example output
[source,terminal]
----
NAME   CONFIG                                  UPDATED UPDATING DEGRADED
master master-1638c1aea398413bb918e76632f20799 False   False    False
worker worker-2feef4f8288936489a5a832ca8efe953 False   False    False
----

To list all machine configs:

[source,terminal]
----
$ oc get machineconfig
----

.Example output
[source,terminal]
----
NAME                                      GENERATEDBYCONTROLLER   IGNITIONVERSION   CREATED   OSIMAGEURL

00-master                                 4.0.0-0.150.0.0-dirty   3.2.0             16m
00-master-ssh                             4.0.0-0.150.0.0-dirty                     16m
00-worker                                 4.0.0-0.150.0.0-dirty   3.2.0             16m
00-worker-ssh                             4.0.0-0.150.0.0-dirty                     16m
01-master-kubelet                         4.0.0-0.150.0.0-dirty   3.2.0             16m
01-worker-kubelet                         4.0.0-0.150.0.0-dirty   3.2.0             16m
master-1638c1aea398413bb918e76632f20799   4.0.0-0.150.0.0-dirty   3.2.0             16m
worker-2feef4f8288936489a5a832ca8efe953   4.0.0-0.150.0.0-dirty   3.2.0             16m
----

The Machine Config Operator acts somewhat differently than Ignition when it
comes to applying these machine configs. The machine configs are read in order
(from 00* to 99*). Labels inside the machine configs identify the type of node
each is for (master or worker). If the same file appears in multiple
machine config files, the last one wins. So, for example, any file that appears
in a 99* file would replace the same file that appeared in a 00* file.
The input `MachineConfig` objects are unioned into a "rendered" `MachineConfig`
object, which will be used as a target by the operator and is the value you
can see in the machine config pool.

To see what files are being managed from a machine config, look for "Path:"
inside a particular `MachineConfig` object. For example:

[source,terminal]
----
$ oc describe machineconfigs 01-worker-container-runtime | grep Path:
----

.Example output
[source,terminal]
----
            Path:            /etc/containers/registries.conf
            Path:            /etc/containers/storage.conf
            Path:            /etc/crio/crio.conf
----

Be sure to give the machine config file a later name
(such as 10-worker-container-runtime). Keep in mind that the content of each
file is in URL-style data. Then apply the new machine config to the cluster.
