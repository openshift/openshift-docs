// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

:_mod-docs-content-type: REFERENCE
[id="rosa-cluster-cli-autoscale-parameters_{context}"]
= Cluster autoscaling parameters using the ROSA CLI

You can add the following parameters to the cluster creation command to configure autoscaler parameters when using the ROSA CLI (`rosa`).

.Configurable autoscaler parameters available with the ROSA CLI (`rosa`)

[cols="4",options="header"]
|===
|Setting
|Description
|Type or Range
|Example/Instruction

|`--autoscaler-balance-similar-node-groups`
|Identify node groups with the same instance type and label set, and try to balance respective sizes of those node groups.
|`boolean`
|Add it to set to true, omit the option to set to false.

|`--autoscaler-skip-nodes-with-local-storage`
|If set, the cluster autoscaler does not delete nodes with pods that have local storage, for example, EmptyDir or HostPath.
|`boolean`
|Add it to set to true, omit the option to set to false.

|`--autoscaler-log-verbosity _int_`
|Autoscaler log level. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-log-verbosity 4`

|`--autoscaler-max-pod-grace-period _int_`
|Gives pods graceful termination time before scaling down, measured in seconds. Replace _int_ in the command with the number of seconds you want to use.
|`integer`
|`--autoscaler-max-pod-grace-period 0`

|`--autoscaler-pod-priority-threshold _int_`
|The priority that a pod must exceed to cause the cluster autoscaler to deploy additional nodes. Replace _int_ in the command with the number you want to use, can be negative.
|`integer`
|`--autoscaler-pod-priority-threshold -10`

|`--autoscaler-gpu-limit _stringArray_`
|Minimum and maximum number of different GPUs in cluster. Cluster autoscaler does not scale the cluster less than or greater than these numbers. The format must be a comma-separated list of "<gpu_type>,<min>,<max>".
|`array`
|`--autoscaler-gpu-limit nvidia.com/gpu,0,10  --autoscaler-gpu-limit amd.com/gpu,1,5`

|`--autoscaler-ignore-daemonsets-utilization`
|If set, the cluster-autoscaler ignores daemon set pods when calculating resource utilization for scaling down.
|`boolean`
|Add it to set to true, omit the option to set to false.

|`--autoscaler-max-node-provision-time _string_`
|Maximum time that the cluster autoscaler waits for a node to be provisioned. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-max-node-provision-time 35m`

|`--autoscaler-balancing-ignored-labels _strings_`
|A comma-separated list of label keys that the cluster autoscaler should ignore when comparing node groups for similarity. Replace _strings_ in the command with the relevant labels..
|`string`
|`--autoscaler-balancing-ignored-labels topology.ebs.csi.aws.com/zone,alpha.eksctl.io/instance-id`

|`--autoscaler-max-nodes-total _int_`
|Maximum amount of nodes in the cluster, including the autoscaled nodes. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-max-nodes-total 180`

|`--autoscaler-min-cores _int_`
|Minimum number of cores to deploy in the cluster. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-min-cores 0`

|`--autoscaler-max-cores _int_`
|Maximum number of cores to deploy in the cluster. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-max-cores 100`

|`--autoscaler-min-memory _int_`
|Minimum amount of memory, in GiB, in the cluster. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-min-memory 0`

|`--autoscaler-max-memory _int_`
|Maximum amount of memory, in GiB, in the cluster. Replace _int_ in the command with the number you want to use.
|`integer`
|`--autoscaler-max-memory 4096`

|`--autoscaler-scale-down-enabled`
|If set, the cluster autoscaler should scale down the cluster.
|`boolean`
|Add it to set to true, omit the option to set to false.

|`--autoscaler-scale-down-unneeded-time _string_`
|How long a node should be unneeded before it is eligible for scale down. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-scale-down-unneeded-time 1h`

|`--autoscaler-scale-down-utilization-threshold _float_`
|Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down. Value must be between 0 and 1.
|`float`
|`--autoscaler-scale-down-utilization-threshold 0.5`

|`--autoscaler-scale-down-delay-after-add _string_`
|How long after scale up that scale down evaluation resumes. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-scale-down-delay-after-add 1h`

|`--autoscaler-scale-down-delay-after-delete _string_`
|How long after node deletion that scale down evaluation resumes. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-scale-down-delay-after-delete 1h`

|`--autoscaler-scale-down-delay-after-failure _string_`
|How long after scale down failure that scale down evaluation resumes. Replace _string_ in the command with an integer and time unit (ns,us,µs,ms,s,m,h).
|`string`
|`--autoscaler-scale-down-delay-after-failure 1h`

|===
