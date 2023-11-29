// Module included in the following assemblies:
//
// * networking/hardware_networks/using-dpdk-and-rdma.adoc

:_mod-docs-content-type: REFERENCE
[id="nw-sriov-dpdk-base-workload_{context}"]
= Example DPDK base workload

The following is an example of a Data Plane Development Kit (DPDK) container:
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: dpdk-test
---
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: '[ <1>
     {
      "name": "dpdk-network-1",
      "namespace": "dpdk-test"
     },
     {
      "name": "dpdk-network-2",
      "namespace": "dpdk-test"
     }
   ]'
    irq-load-balancing.crio.io: "disable" <2>
    cpu-load-balancing.crio.io: "disable"
    cpu-quota.crio.io: "disable"
  labels:
    app: dpdk
  name: testpmd
  namespace: dpdk-test
spec:
  runtimeClassName: performance-performance <3>
  containers:
    - command:
        - /bin/bash
        - -c
        - sleep INF
      image: registry.redhat.io/openshift4/dpdk-base-rhel8
      imagePullPolicy: Always
      name: dpdk
      resources: <4>
        limits:
          cpu: "16"
          hugepages-1Gi: 8Gi
          memory: 2Gi
        requests:
          cpu: "16"
          hugepages-1Gi: 8Gi
          memory: 2Gi
      securityContext:
        capabilities:
          add:
            - IPC_LOCK
            - SYS_RESOURCE
            - NET_RAW
            - NET_ADMIN
        runAsUser: 0
      volumeMounts:
        - mountPath: /mnt/huge
          name: hugepages
  terminationGracePeriodSeconds: 5
  volumes:
    - emptyDir:
        medium: HugePages
      name: hugepages
----
<1> Request the SR-IOV networks you need. Resources for the devices will be injected automatically.
<2> Disable the CPU and IRQ load balancing base. See _Disabling interrupt processing for individual pods_ for more information.
<3> Set the `runtimeClass` to `performance-performance`. Do not set the `runtimeClass` to `HostNetwork` or `privileged`.
<4> Request an equal number of resources for requests and limits to start the pod with `Guaranteed` Quality of Service (QoS).

[NOTE]
====
Do not start the pod with `SLEEP` and then exec into the pod to start the testpmd or the DPDK workload. This can add additional interrupts as the `exec` process is not pinned to any CPU.
====
