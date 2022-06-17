// Module included in the following assemblies:
//
// * networking/configuring-ipfailover.adoc

[id="nw-ipfailover-environment-variables_{context}"]
= IP failover environment variables

The following table contains the variables used to configure IP failover.

.IP failover environment variables
[cols="3a,1a,4a",options="header"]
|===

| Variable Name | Default | Description

|`OPENSHIFT_HA_MONITOR_PORT`
|`80`
|The IP failover pod tries to open a TCP connection to this port on each Virtual IP (VIP). If connection is established, the service is considered to be running. If this port is set to `0`, the test always passes.

|`OPENSHIFT_HA_NETWORK_INTERFACE`
|
|The interface name that IP failover uses to send Virtual Router Redundancy Protocol (VRRP) traffic. The default value is `eth0`.

|`OPENSHIFT_HA_REPLICA_COUNT`
|`2`
|The number of replicas to create. This must match `spec.replicas` value in IP failover deployment configuration.

|`OPENSHIFT_HA_VIRTUAL_IPS`
|
|The list of IP address ranges to replicate. This must be provided. For example, `1.2.3.4-6,1.2.3.9`.

|`OPENSHIFT_HA_VRRP_ID_OFFSET`
|`0`
|The offset value used to set the virtual router IDs. Using different offset values allows multiple IP failover configurations to exist within the same cluster. The default offset is `0`, and the allowed range is `0` through `255`.

|`OPENSHIFT_HA_VIP_GROUPS`
|
|The number of groups to create for VRRP. If not set, a group is created for each virtual IP range specified with the `OPENSHIFT_HA_VIP_GROUPS` variable.

|`OPENSHIFT_HA_IPTABLES_CHAIN`
|INPUT
|The name of the iptables chain, to automatically add an `iptables` rule to allow the VRRP traffic on. If the value is not set, an `iptables` rule is not added. If the chain does not exist, it is not created.

|`OPENSHIFT_HA_CHECK_SCRIPT`
|
|The full path name in the pod file system of a script that is periodically run to verify the application is operating.

|`OPENSHIFT_HA_CHECK_INTERVAL`
|`2`
|The period, in seconds, that the check script is run.

|`OPENSHIFT_HA_NOTIFY_SCRIPT`
|
|The full path name in the pod file system of a script that is run whenever the state changes.

|`OPENSHIFT_HA_PREEMPTION`
|`preempt_nodelay 300`
|The strategy for handling a new higher priority host. The `nopreempt` strategy does not move master from the lower priority host to the higher priority host.
|===
