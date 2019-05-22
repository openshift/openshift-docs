// Module included in the following assemblies:
//
// * TBD

[id="machine-configs-and-pools_{context}"]
= Machine Configs and Machine Config Pools
Machine Config Pools manage a cluster of nodes and their corresponding
Machine Configs. Machine Configs contain configuration information for a
cluster.

To list all Machine Config Pools that are known:

----
$ oc get machineconfigpools
NAME     CONFIG                                    UPDATED   UPDATING   DEGRADED
master   master-1638c1aea398413bb918e76632f20799   False     False      False
worker   worker-2feef4f8288936489a5a832ca8efe953   False     False      False
----

To list all Machine Configs:
----
$ oc get machineconfig
NAME                                      GENERATEDBYCONTROLLER   IGNITIONVERSION   CREATED   OSIMAGEURL
00-master                                 4.0.0-0.150.0.0-dirty   2.2.0             16m
00-master-ssh                             4.0.0-0.150.0.0-dirty                     16m
00-worker                                 4.0.0-0.150.0.0-dirty   2.2.0             16m
00-worker-ssh                             4.0.0-0.150.0.0-dirty                     16m
01-master-kubelet                         4.0.0-0.150.0.0-dirty   2.2.0             16m
01-worker-kubelet                         4.0.0-0.150.0.0-dirty   2.2.0             16m
master-1638c1aea398413bb918e76632f20799   4.0.0-0.150.0.0-dirty   2.2.0             16m
worker-2feef4f8288936489a5a832ca8efe953   4.0.0-0.150.0.0-dirty   2.2.0             16m
----

To list all KubeletConfigs:

----
$ oc get kubeletconfigs
----

To get more detailed information about a KubeletConfig, including the reason for
the current condition:

----
$ oc describe kubeletconfig <name>
----

For example:

----
# oc describe kubeletconfig set-max-pods

Name:         set-max-pods <1>
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  machineconfiguration.openshift.io/v1
Kind:         KubeletConfig
Metadata:
  Creation Timestamp:  2019-02-05T16:27:20Z
  Generation:          1
  Resource Version:    19694
  Self Link:           /apis/machineconfiguration.openshift.io/v1/kubeletconfigs/set-max-pods
  UID:                 e8ee6410-2962-11e9-9bcc-664f163f5f0f
Spec:
  Kubelet Config: <2>
    Max Pods:  100
  Machine Config Pool Selector: <3>
    Match Labels:
      Custom - Kubelet:  small-pods
Events:                    <none>
----

<1> The name of the KubeletConfig.
<2> The user defined configuration.
<3> The Machine Config Pool selector to apply the KubeletConfig to.