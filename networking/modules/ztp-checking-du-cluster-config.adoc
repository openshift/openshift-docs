// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-vdu-validating-cluster-tuning.adoc

:_module-type: PROCEDURE
[id="ztp-checking-du-cluster-config_{context}"]
= Checking that the recommended cluster configurations are applied

You can check that clusters are running the correct configuration. The following procedure describes how to check the various configurations that you require to deploy a DU application in {product-title} {product-version} clusters.

.Prerequisites

* You have deployed a cluster and tuned it for vDU workloads.

* You have installed the OpenShift CLI (`oc`).

* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. Check that the default OperatorHub sources are disabled. Run the following command:
+
[source,terminal]
----
$ oc get operatorhub cluster -o yaml
----
+
.Example output
[source,yaml]
----
spec:
    disableAllDefaultSources: true
----

. Check that all required `CatalogSource` resources are annotated for workload partitioning (`PreferredDuringScheduling`) by running the following command:
+
[source,terminal]
----
$ oc get catalogsource -A -o jsonpath='{range .items[*]}{.metadata.name}{" -- "}{.metadata.annotations.target\.workload\.openshift\.io/management}{"\n"}{end}'
----
+
.Example output
[source,terminal]
----
certified-operators -- {"effect": "PreferredDuringScheduling"}
community-operators -- {"effect": "PreferredDuringScheduling"}
ran-operators -- <1>
redhat-marketplace -- {"effect": "PreferredDuringScheduling"}
redhat-operators -- {"effect": "PreferredDuringScheduling"}
----
<1> `CatalogSource` resources that are not annotated are also returned. In this example, the `ran-operators` `CatalogSource` resource is not annotated and does not have the `PreferredDuringScheduling` annotation.
+
[NOTE]
====
In a properly configured vDU cluster, only a single annotated catalog source is listed.
====

. Check that all applicable {product-title} Operator namespaces are annotated for workload partitioning. This includes all Operators installed with core {product-title} and the set of additional Operators included in the reference DU tuning configuration. Run the following command:
+
[source,terminal]
----
$ oc get namespaces -A -o jsonpath='{range .items[*]}{.metadata.name}{" -- "}{.metadata.annotations.workload\.openshift\.io/allowed}{"\n"}{end}'
----
+
.Example output
[source,terminal]
----
default --
openshift-apiserver -- management
openshift-apiserver-operator -- management
openshift-authentication -- management
openshift-authentication-operator -- management
----
+
[IMPORTANT]
====
Additional Operators must not be annotated for workload partitioning. In the output from the previous command, additional Operators should be listed without any value on the right side of the `--` separator.
====

. Check that the `ClusterLogging` configuration is correct. Run the following commands:

.. Validate that the appropriate input and output logs are configured:
+
[source,terminal]
----
$ oc get -n openshift-logging ClusterLogForwarder instance -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  creationTimestamp: "2022-07-19T21:51:41Z"
  generation: 1
  name: instance
  namespace: openshift-logging
  resourceVersion: "1030342"
  uid: 8c1a842d-80c5-447a-9150-40350bdf40f0
spec:
  inputs:
  - infrastructure: {}
    name: infra-logs
  outputs:
  - name: kafka-open
    type: kafka
    url: tcp://10.46.55.190:9092/test
  pipelines:
  - inputRefs:
    - audit
    name: audit-logs
    outputRefs:
    - kafka-open
  - inputRefs:
    - infrastructure
    name: infrastructure-logs
    outputRefs:
    - kafka-open
...
----

.. Check that the curation schedule is appropriate for your application:
+
[source,terminal]
----
$ oc get -n openshift-logging clusterloggings.logging.openshift.io instance -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  creationTimestamp: "2022-07-07T18:22:56Z"
  generation: 1
  name: instance
  namespace: openshift-logging
  resourceVersion: "235796"
  uid: ef67b9b8-0e65-4a10-88ff-ec06922ea796
spec:
  collection:
    logs:
      fluentd: {}
      type: fluentd
  curation:
    curator:
      schedule: 30 3 * * *
    type: curator
  managementState: Managed
...
----

. Check that the web console is disabled (`managementState: Removed`) by running the following command:
+
[source,terminal]
----
$ oc get consoles.operator.openshift.io cluster -o jsonpath="{ .spec.managementState }"
----
+
.Example output
[source,terminal]
----
Removed
----

. Check that `chronyd` is disabled on the cluster node by running the following commands:
+
[source,terminal]
----
$ oc debug node/<node_name>
----
+
Check the status of `chronyd` on the node:
+
[source,terminal]
----
sh-4.4# chroot /host
----
+
[source,terminal]
----
sh-4.4# systemctl status chronyd
----
+
.Example output
[source,terminal]
----
● chronyd.service - NTP client/server
    Loaded: loaded (/usr/lib/systemd/system/chronyd.service; disabled; vendor preset: enabled)
    Active: inactive (dead)
      Docs: man:chronyd(8)
            man:chrony.conf(5)
----

. Check that the PTP interface is successfully synchronized to the primary clock using a remote shell connection to the `linuxptp-daemon` container and the PTP Management Client (`pmc`) tool:

.. Set the `$PTP_POD_NAME` variable with the name of the `linuxptp-daemon` pod by running the following command:
+
[source,terminal]
----
$ PTP_POD_NAME=$(oc get pods -n openshift-ptp -l app=linuxptp-daemon -o name)
----

.. Run the following command to check the sync status of the PTP device:
+
[source,terminal]
----
$ oc -n openshift-ptp rsh -c linuxptp-daemon-container ${PTP_POD_NAME} pmc -u -f /var/run/ptp4l.0.config -b 0 'GET PORT_DATA_SET'
----
+
.Example output
[source,terminal]
----
sending: GET PORT_DATA_SET
  3cecef.fffe.7a7020-1 seq 0 RESPONSE MANAGEMENT PORT_DATA_SET
    portIdentity            3cecef.fffe.7a7020-1
    portState               SLAVE
    logMinDelayReqInterval  -4
    peerMeanPathDelay       0
    logAnnounceInterval     1
    announceReceiptTimeout  3
    logSyncInterval         0
    delayMechanism          1
    logMinPdelayReqInterval 0
    versionNumber           2
  3cecef.fffe.7a7020-2 seq 0 RESPONSE MANAGEMENT PORT_DATA_SET
    portIdentity            3cecef.fffe.7a7020-2
    portState               LISTENING
    logMinDelayReqInterval  0
    peerMeanPathDelay       0
    logAnnounceInterval     1
    announceReceiptTimeout  3
    logSyncInterval         0
    delayMechanism          1
    logMinPdelayReqInterval 0
    versionNumber           2
----

.. Run the following `pmc` command to check the PTP clock status:
+
[source,terminal]
----
$ oc -n openshift-ptp rsh -c linuxptp-daemon-container ${PTP_POD_NAME} pmc -u -f /var/run/ptp4l.0.config -b 0 'GET TIME_STATUS_NP'
----
+
.Example output
[source,terminal]
----
sending: GET TIME_STATUS_NP
  3cecef.fffe.7a7020-0 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
    master_offset              10 <1>
    ingress_time               1657275432697400530
    cumulativeScaledRateOffset +0.000000000
    scaledLastGmPhaseChange    0
    gmTimeBaseIndicator        0
    lastGmPhaseChange          0x0000'0000000000000000.0000
    gmPresent                  true <2>
    gmIdentity                 3c2c30.ffff.670e00
----
<1> `master_offset` should be between -100 and 100 ns.
<2> Indicates that the PTP clock is synchronized to a master, and the local clock is not the grandmaster clock.

.. Check that the expected `master offset` value corresponding to the value in `/var/run/ptp4l.0.config` is found in the `linuxptp-daemon-container` log:
+
[source,terminal]
----
$ oc logs $PTP_POD_NAME -n openshift-ptp -c linuxptp-daemon-container
----
+
.Example output
[source,terminal]
----
phc2sys[56020.341]: [ptp4l.1.config] CLOCK_REALTIME phc offset  -1731092 s2 freq -1546242 delay    497
ptp4l[56020.390]: [ptp4l.1.config] master offset         -2 s2 freq   -5863 path delay       541
ptp4l[56020.390]: [ptp4l.0.config] master offset         -8 s2 freq  -10699 path delay       533
----

. Check that the SR-IOV configuration is correct by running the following commands:

.. Check that the `disableDrain` value in the `SriovOperatorConfig` resource is set to `true`:
+
[source,terminal]
----
$ oc get sriovoperatorconfig -n openshift-sriov-network-operator default -o jsonpath="{.spec.disableDrain}{'\n'}"
----
+
.Example output
[source,terminal]
----
true
----

.. Check that the `SriovNetworkNodeState` sync status is `Succeeded` by running the following command:
+
[source,terminal]
----
$ oc get SriovNetworkNodeStates -n openshift-sriov-network-operator -o jsonpath="{.items[*].status.syncStatus}{'\n'}"
----
+
.Example output
[source,terminal]
----
Succeeded
----

.. Verify that the expected number and configuration of virtual functions (`Vfs`) under each interface configured for SR-IOV is present and correct in the `.status.interfaces` field. For example:
+
[source,terminal]
----
$ oc get SriovNetworkNodeStates -n openshift-sriov-network-operator -o yaml
----
+
.Example output
+
[source,yaml]
----
apiVersion: v1
items:
- apiVersion: sriovnetwork.openshift.io/v1
  kind: SriovNetworkNodeState
...
  status:
    interfaces:
    ...
    - Vfs:
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.0
        vendor: "8086"
        vfID: 0
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.1
        vendor: "8086"
        vfID: 1
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.2
        vendor: "8086"
        vfID: 2
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.3
        vendor: "8086"
        vfID: 3
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.4
        vendor: "8086"
        vfID: 4
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.5
        vendor: "8086"
        vfID: 5
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.6
        vendor: "8086"
        vfID: 6
      - deviceID: 154c
        driver: vfio-pci
        pciAddress: 0000:3b:0a.7
        vendor: "8086"
        vfID: 7
----

. Check that the cluster performance profile is correct. The `cpu` and `hugepages` sections will vary depending on your hardware configuration. Run the following command:
+
[source,terminal]
----
$ oc get PerformanceProfile openshift-node-performance-profile -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  creationTimestamp: "2022-07-19T21:51:31Z"
  finalizers:
  - foreground-deletion
  generation: 1
  name: openshift-node-performance-profile
  resourceVersion: "33558"
  uid: 217958c0-9122-4c62-9d4d-fdc27c31118c
spec:
  additionalKernelArgs:
  - idle=poll
  - rcupdate.rcu_normal_after_boot=0
  - efi=runtime
  cpu:
    isolated: 2-51,54-103
    reserved: 0-1,52-53
  hugepages:
    defaultHugepagesSize: 1G
    pages:
    - count: 32
      size: 1G
  machineConfigPoolSelector:
    pools.operator.machineconfiguration.openshift.io/master: ""
  net:
    userLevelNetworking: true
  nodeSelector:
    node-role.kubernetes.io/master: ""
  numa:
    topologyPolicy: restricted
  realTimeKernel:
    enabled: true
status:
  conditions:
  - lastHeartbeatTime: "2022-07-19T21:51:31Z"
    lastTransitionTime: "2022-07-19T21:51:31Z"
    status: "True"
    type: Available
  - lastHeartbeatTime: "2022-07-19T21:51:31Z"
    lastTransitionTime: "2022-07-19T21:51:31Z"
    status: "True"
    type: Upgradeable
  - lastHeartbeatTime: "2022-07-19T21:51:31Z"
    lastTransitionTime: "2022-07-19T21:51:31Z"
    status: "False"
    type: Progressing
  - lastHeartbeatTime: "2022-07-19T21:51:31Z"
    lastTransitionTime: "2022-07-19T21:51:31Z"
    status: "False"
    type: Degraded
  runtimeClass: performance-openshift-node-performance-profile
  tuned: openshift-cluster-node-tuning-operator/openshift-node-performance-openshift-node-performance-profile
----
+
[NOTE]
====
CPU settings are dependent on the number of cores available on the server and should align with workload partitioning settings. `hugepages` configuration is server and application dependent.
====

. Check that the `PerformanceProfile` was successfully applied to the cluster by running the following command:
+
[source,terminal]
----
$ oc get performanceprofile openshift-node-performance-profile -o jsonpath="{range .status.conditions[*]}{ @.type }{' -- '}{@.status}{'\n'}{end}"
----
+
.Example output
[source,terminal]
----
Available -- True
Upgradeable -- True
Progressing -- False
Degraded -- False
----

. Check the `Tuned` performance patch settings by running the following command:
+
[source,terminal]
----
$ oc get tuneds.tuned.openshift.io -n openshift-cluster-node-tuning-operator performance-patch -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  creationTimestamp: "2022-07-18T10:33:52Z"
  generation: 1
  name: performance-patch
  namespace: openshift-cluster-node-tuning-operator
  resourceVersion: "34024"
  uid: f9799811-f744-4179-bf00-32d4436c08fd
spec:
  profile:
  - data: |
      [main]
      summary=Configuration changes profile inherited from performance created tuned
      include=openshift-node-performance-openshift-node-performance-profile
      [bootloader]
      cmdline_crash=nohz_full=2-23,26-47 <1>
      [sysctl]
      kernel.timer_migration=1
      [scheduler]
      group.ice-ptp=0:f:10:*:ice-ptp.*
      [service]
      service.stalld=start,enable
      service.chronyd=stop,disable
    name: performance-patch
  recommend:
  - machineConfigLabels:
      machineconfiguration.openshift.io/role: master
    priority: 19
    profile: performance-patch
----
<1> The cpu list in `cmdline=nohz_full=` will vary based on your hardware configuration.

. Check that cluster networking diagnostics are disabled by running the following command:
+
[source,terminal]
----
$ oc get networks.operator.openshift.io cluster -o jsonpath='{.spec.disableNetworkDiagnostics}'
----
+
.Example output
[source,terminal]
----
true
----

. Check that the `Kubelet` housekeeping interval is tuned to slower rate. This is set in the `containerMountNS` machine config. Run the following command:
+
[source,terminal]
----
$ oc describe machineconfig container-mount-namespace-and-kubelet-conf-master | grep OPENSHIFT_MAX_HOUSEKEEPING_INTERVAL_DURATION
----
+
.Example output
[source,terminal]
----
Environment="OPENSHIFT_MAX_HOUSEKEEPING_INTERVAL_DURATION=60s"
----

. Check that Grafana and `alertManagerMain` are disabled and that the Prometheus retention period is set to 24h by running the following command:
+
[source,terminal]
----
$ oc get configmap cluster-monitoring-config -n openshift-monitoring -o jsonpath="{ .data.config\.yaml }"
----
+
.Example output
[source,terminal]
----
grafana:
  enabled: false
alertmanagerMain:
  enabled: false
prometheusK8s:
   retention: 24h
----

.. Use the following commands to verify that Grafana and `alertManagerMain` routes are not found in the cluster:
+
[source,terminal]
----
$ oc get route -n openshift-monitoring alertmanager-main
----
+
[source,terminal]
----
$ oc get route -n openshift-monitoring grafana
----
+
Both queries should return `Error from server (NotFound)` messages.

. Check that there is a minimum of 4 CPUs allocated as `reserved` for each of the `PerformanceProfile`, `Tuned` performance-patch, workload partitioning, and kernel command line arguments by running the following command:
+
[source,terminal]
----
$ oc get performanceprofile -o jsonpath="{ .items[0].spec.cpu.reserved }"
----
+
.Example output
[source,terminal]
----
0-3
----
+
[NOTE]
====
Depending on your workload requirements, you might require additional reserved CPUs to be allocated.
====
