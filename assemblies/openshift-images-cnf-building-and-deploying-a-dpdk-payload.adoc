:_mod-docs-content-type: ASSEMBLY
// Epic CNF-40
[id="cnf-building-and-deploying-a-dpdk-application"]
= Building and deploying a DPDK application using the S2I image
include::_attributes/common-attributes.adoc[]
:context: building-deploying-DPDK-using-s2i-image

toc::[]

The Data Plane Development Kit (DPDK) base image is a base image for DPDK
applications. It uses the Source-to-Image (S2I) build tool to automate the
building of application images.

Source-to-Image (S2I) is a tool for building reproducible and formatted
container images. It produces ready-to-run images by injecting application
source into a container image and assembling a new image. The new image
incorporates the base image (the builder) and built source. For more
information, see
xref:../cicd/builds/build-strategies.adoc#build-strategy-s2i_build-strategies[Source-to-Image
(S2I) build].

The DPDK base image comes preinstalled with DPDK, and with a build tool that can be used to
create a target image containing the DPDK libraries and the application provided by the user.

== Prerequisites

Before using the S2I tool, ensure that you have the following components installed and configured:

* Image Registry Operator:
See xref:../registry/configuring-registry-operator.adoc#configuring-registry-operator[Image Registry Operator in OpenShift Container Platform].

* SR-IOV Operator:
See xref:../networking/hardware_networks/about-sriov.adoc#about-sriov[About SR-IOV hardware on {product-title}].

* Performance AddOn Operator:
See xref:../scalability_and_performance/cnf-low-latency-tuning.adoc#cnf-low-latency-tuning[About CNF Performance Addon Operator].

This example application is the `test-pmd` application provided by dpdk.org.
For more information, see link:https://doc.dpdk.org/guides/testpmd_app_ug/[Testpmd Application User Guide].

.Building procedure

To build a target image, create a repository containing an application and the following two scripts:

* `build.sh` - for building the application
* `run.sh` - for running the application

This is an example of `build.sh`:

----
#!/usr/bin/env bash

make -C test-pmd

cp test-pmd/testpmd ./customtestpmd

echo "build done"
----

This is an example of `run.sh`:

----
#!/bin/bash -eux

export CPU=$(cat /sys/fs/cgroup/cpuset/cpuset.cpus)
echo ${CPU}
echo ${PCIDEVICE_OPENSHIFT_IO_DPDKNIC} # This is the resource name configured via
the SR-IOV operator.

if [ "$RUN_TYPE" == "testpmd" ]; then
envsubst < test-template.sh > test.sh
chmod +x test.sh
expect -f test.sh
fi

while true; do sleep inf; done;
----

The example `run.sh` will run the commands inside the `test-template.sh`.

----
spawn ./customtestpmd -l ${CPU} -w ${PCIDEVICE_OPENSHIFT_IO_DPDKNIC}
--iova-mode=va -- -i --portmask=0x1 --nb-cores=2 --forward-mode=mac --port-topology=loop
--no-mlockall
set timeout 10000
expect "testpmd>"
send -- "start\r"
sleep 20
expect "testpmd>"
send -- "stop\r"
expect "testpmd>"
send -- "quit\r"
expect eof
----

This file will run the `testpmd` compiled application from the build stage.
This spawns the `testpmd` interactive terminal then start a test workload and close it after 20 seconds.

The DPDK base image and the application repository are both used to build a target application image.
S2I copies the application from the repository to the DPDK base image, which then builds a target image using
DPDK base image resources and the copied application.

You can use the {product-title} BuildConfig to build a target image in a production environment.
The `build-config.yaml` file is the file you use to create your automated build.
It creates a new `dpdk` namespace and configures an `ImageStream` for the image
and starts a build.
The {product-registry} must be configured in the cluster.

----
---
apiVersion: image.openshift.io/v1
kind: ImageStream <1>
metadata:
  name: s2i-dpdk-app
  namespace: dpdk
spec: {}
---
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  labels:
    app: s2i-dpdk
    app.kubernetes.io/component: s2i-dpdk
    app.kubernetes.io/instance: s2i-dpdk
  name: s2i-dpdk
  namespace: dpdk
spec:
  failedBuildsHistoryLimit: 5
  nodeSelector: null
  output:  <2>
    to:
      kind: ImageStreamTag
      name: s2i-dpdk-app:latest
  postCommit: {}
  resources: {}
  runPolicy: Serial
  source:  <3>
    contextDir: tools/s2i-dpdk/test/test-app
    git:
      uri: <repo-uri> <4>
    type: Git
  strategy:  <5>
    sourceStrategy:
      from:
        kind: DockerImage
        name: registry.access.redhat.com/openshift4/dpdk-base-rhel8:v4.4
    type: Source
  successfulBuildsHistoryLimit: 5
  triggers:
    - type: ConfigChange
----

<1> The `kind` type specifies the defined image stream.

<2> The `output` type publishes the result of the image stream object.

<3> The `source` type contains the git repository and a context directory within the repository.

<4> The repository uri that contains the application and both the `build.sh` and the `run.sh` files.

<5> The `strategy` type contains a DPDK base image.

It is the `source` type and `strategy` type that build the image.

A complete guide to using BuildConfigs is available in
xref:../builds/understanding-buildconfigs.adoc#understanding-buildconfigs[Understanding
build configurations].

After the base DPDK image build is ready, you should configure the environment to be able to run the DPDK workload on it.

.Deployment procedure

. Create a performance profile to allocate Hugepages and isolated CPUs. For more
information, see
xref:../scalability_and_performance/cnf-low-latency-tuning.adoc#cnf-understanding-low-latency_{context}[Tuning nodes for low latency via PerformanceProfile].

. Create the SR-IOV network policy and the SR-IOV network attachment based on your network card type. For more information,
see xref:../networking/hardware_networks/using-dpdk-and-rdma.adoc#using-dpdk-and-rdma[Using Virtual Functions (VFs) with DPDK and RDMA modes].

. Using a deployment config resource instead of a regular deployment allows automatic redeploy of the workload whenever a new image is built.
You must create a special `SecurityContextConstraints` resource that will allow the `deployer` service account to create the
dpdk workload deployment and the deployment config resource pointing to the `ImageStream`.
+
`SecurityContextConstraints` example:
+
----
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: dpdk
allowHostDirVolumePlugin: true
allowHostIPC: false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegeEscalation: false
allowPrivilegedContainer: false
allowedCapabilities:
  - "*"
allowedUnsafeSysctls:
  - "*"
defaultAddCapabilities: null
fsGroup:
  type: RunAsAny
readOnlyRootFilesystem: false
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: RunAsAny
seccompProfiles:
  - "*"
users: <1>
  - system:serviceaccount:dpdk:deployer
volumes:
  - "*"
----
+
<1> This is a list of all the service accounts that will be part of the SCC.
You should add here all the namespaces that will deploy the dpdk workload in the following format `system:serviceaccount:<namespace>:deployer`.

. Apply the deployment config resource.
+
`DeploymentConfig` resource example:
+
----
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  labels:
    app: s2i-dpdk-app
    app.kubernetes.io/component: s2i-dpdk-app
    app.kubernetes.io/instance: s2i-dpdk-app
  name: s2i-dpdk-app
  namespace: dpdk
spec:
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    deploymentconfig: s2i-dpdk-app
  strategy:
    rollingParams:
      intervalSeconds: 1
      maxSurge: 25%
      maxUnavailable: 25%
      timeoutSeconds: 600
      updatePeriodSeconds: 1
    type: Rolling
  template:
    metadata:
      labels:
        deploymentconfig: s2i-dpdk-app
      annotations:
        k8s.v1.cni.cncf.io/networks: dpdk/dpdk-network  <1>
    spec:
      serviceAccount: deployer
      serviceAccountName: deployer
      securityContext:
        runAsUser: 0
      containers:
        - image: “<internal-registry-url>/<namespace>/<image-stream>:<tag>”  <2>
          securityContext:
            runAsUser: 0
            capabilities:
              add: ["IPC_LOCK","SYS_RESOURCE"]
          imagePullPolicy: Always
          name: s2i-dpdk-app
          terminationMessagePath: /dev/termination-log
          terminationMessagePolicy: File
          resources:  <3>
            limits:
              cpu: "4"
              hugepages-1Gi: 4Gi
              memory: 1000Mi
            requests:
              cpu: "4"
              hugepages-1Gi: 4Gi
              memory: 1000Mi
          volumeMounts:
            - mountPath: /mnt/huge
              name: hugepage
      dnsPolicy: ClusterFirst
      volumes:
      - name: hugepage
        emptyDir:
          medium: HugePages
      restartPolicy: Always
  test: false
  triggers:
    - type: ConfigChange
    - imageChangeParams:
        automatic: true
        containerNames:
          - s2i-dpdk-app
        from:  <4>
          kind: ImageStreamTag
          name: <image-stream>:<tag>
          namespace: <namespace>
      type: ImageChange
----
+
<1> The network attachment definition name.
<2> The image stream URL.
<3> The requested resource. The limit and request should be the same so the quality of service (QOS) will be guaranteed and the CPUs will be pinned.
<4> The image stream created to start a redeployment when a newly built image is pushed to the registry.
