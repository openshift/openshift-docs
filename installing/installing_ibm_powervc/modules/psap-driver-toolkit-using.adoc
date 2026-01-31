// Module included in the following assemblies:
//
// * hardware_enablement/psap-driver-toolkit.adoc

:_mod-docs-content-type: PROCEDURE
[id="using-the-driver-toolkit_{context}"]
= Using the Driver Toolkit

As an example, the Driver Toolkit can be used as the base image for building a very simple kernel module called `simple-kmod`.

[NOTE]
====
The Driver Toolkit includes the necessary dependencies, `openssl`, `mokutil`, and `keyutils`, needed to sign a kernel module. However, in this example, the `simple-kmod` kernel module is not signed and therefore cannot be loaded on systems with `Secure Boot` enabled.
====

[id="create-simple-kmod-image_{context}"]
== Build and run the simple-kmod driver container on a cluster

.Prerequisites

* You have a running {product-title} cluster.
* You set the Image Registry Operator state to `Managed` for your cluster.
* You installed the OpenShift CLI (`oc`).
* You are logged into the OpenShift CLI as a user with `cluster-admin` privileges.

.Procedure

Create a namespace. For example:
[source,terminal]
-----
$ oc new-project simple-kmod-demo
-----

. The YAML defines an `ImageStream` for storing the `simple-kmod` driver container image, and a `BuildConfig` for building the container. Save this YAML as `0000-buildconfig.yaml.template`.
+
[source,yaml]
----
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  labels:
    app: simple-kmod-driver-container
  name: simple-kmod-driver-container
  namespace: simple-kmod-demo
spec: {}
---
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  labels:
    app: simple-kmod-driver-build
  name: simple-kmod-driver-build
  namespace: simple-kmod-demo
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  runPolicy: "Serial"
  triggers:
    - type: "ConfigChange"
    - type: "ImageChange"
  source:
    dockerfile: |
      ARG DTK
      FROM ${DTK} as builder

      ARG KVER

      WORKDIR /build/

      RUN git clone https://github.com/openshift-psap/simple-kmod.git

      WORKDIR /build/simple-kmod

      RUN make all install KVER=${KVER}

      FROM registry.redhat.io/ubi8/ubi-minimal

      ARG KVER

      # Required for installing `modprobe`
      RUN microdnf install kmod

      COPY --from=builder /lib/modules/${KVER}/simple-kmod.ko /lib/modules/${KVER}/
      COPY --from=builder /lib/modules/${KVER}/simple-procfs-kmod.ko /lib/modules/${KVER}/
      RUN depmod ${KVER}
  strategy:
    dockerStrategy:
      buildArgs:
        - name: KMODVER
          value: DEMO
          # $ oc adm release info quay.io/openshift-release-dev/ocp-release:<cluster version>-x86_64 --image-for=driver-toolkit
        - name: DTK
          value: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:34864ccd2f4b6e385705a730864c04a40908e57acede44457a783d739e377cae
        - name: KVER
          value: 4.18.0-372.26.1.el8_6.x86_64
  output:
    to:
      kind: ImageStreamTag
      name: simple-kmod-driver-container:demo
----

. Substitute the correct driver toolkit image for the {product-title} version you are running in place of “DRIVER_TOOLKIT_IMAGE” with the following commands.
+
[source,terminal]
----
$ OCP_VERSION=$(oc get clusterversion/version -ojsonpath={.status.desired.version})
----
+
[source,terminal]
----
$ DRIVER_TOOLKIT_IMAGE=$(oc adm release info $OCP_VERSION --image-for=driver-toolkit)
----
+
[source,terminal]
----
$ sed "s#DRIVER_TOOLKIT_IMAGE#${DRIVER_TOOLKIT_IMAGE}#" 0000-buildconfig.yaml.template > 0000-buildconfig.yaml
----

. Create the image stream and build config with
+
[source,terminal]
----
$ oc create -f 0000-buildconfig.yaml
----

. After the builder pod completes successfully, deploy the driver container image as a `DaemonSet`.

.. The driver container must run with the privileged security context in order to load the kernel modules on the host. The following YAML file contains the RBAC rules and the `DaemonSet` for running the driver container. Save this YAML as `1000-drivercontainer.yaml`.
+
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: simple-kmod-driver-container
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: simple-kmod-driver-container
rules:
- apiGroups:
  - security.openshift.io
  resources:
  - securitycontextconstraints
  verbs:
  - use
  resourceNames:
  - privileged
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: simple-kmod-driver-container
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: simple-kmod-driver-container
subjects:
- kind: ServiceAccount
  name: simple-kmod-driver-container
userNames:
- system:serviceaccount:simple-kmod-demo:simple-kmod-driver-container
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: simple-kmod-driver-container
spec:
  selector:
    matchLabels:
      app: simple-kmod-driver-container
  template:
    metadata:
      labels:
        app: simple-kmod-driver-container
    spec:
      serviceAccount: simple-kmod-driver-container
      serviceAccountName: simple-kmod-driver-container
      containers:
      - image: image-registry.openshift-image-registry.svc:5000/simple-kmod-demo/simple-kmod-driver-container:demo
        name: simple-kmod-driver-container
        imagePullPolicy: Always
        command: [sleep, infinity]
        lifecycle:
          postStart:
            exec:
              command: ["modprobe", "-v", "-a" , "simple-kmod", "simple-procfs-kmod"]
          preStop:
            exec:
              command: ["modprobe", "-r", "-a" , "simple-kmod", "simple-procfs-kmod"]
        securityContext:
          privileged: true
      nodeSelector:
        node-role.kubernetes.io/worker: ""
----

.. Create the RBAC rules and daemon set:
+
[source,terminal]
----
$ oc create -f 1000-drivercontainer.yaml
----

. After the pods are running on the worker nodes, verify that the `simple_kmod` kernel module is loaded successfully on the host machines with `lsmod`.

.. Verify that the pods are running:
+
[source,terminal]
----
$ oc get pod -n simple-kmod-demo
----
+
.Example output
[source,terminal]
----
NAME                                 READY   STATUS      RESTARTS   AGE
simple-kmod-driver-build-1-build     0/1     Completed   0          6m
simple-kmod-driver-container-b22fd   1/1     Running     0          40s
simple-kmod-driver-container-jz9vn   1/1     Running     0          40s
simple-kmod-driver-container-p45cc   1/1     Running     0          40s
----

.. Execute the `lsmod` command in the driver container pod:
+
[source,terminal]
----
$ oc exec -it pod/simple-kmod-driver-container-p45cc -- lsmod | grep simple
----
+
.Example output
[source,terminal]
----
simple_procfs_kmod     16384  0
simple_kmod            16384  0
----
