// Module included in the following assemblies:
//
// * nodes/containers/nodes-containers-sysctls.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-containers-starting-pod-with-unsafe-sysctls_{context}"]
= Starting a pod with unsafe sysctls

A pod with unsafe sysctls fails to launch on any node unless the cluster administrator explicitly enables unsafe sysctls for that node. As with node-level sysctls, use the taints and toleration feature or labels on nodes to schedule those pods onto the right nodes.

The following example uses the pod `securityContext` to set a safe sysctl `kernel.shm_rmid_forced` and two unsafe sysctls, `net.core.somaxconn` and `kernel.msgmax`. There is no distinction between _safe_ and _unsafe_ sysctls in the specification.

[WARNING]
====
To avoid destabilizing your operating system, modify sysctl parameters only after you understand their effects.
====

The following example illustrates what happens when you add safe and unsafe sysctls to a pod specification:

.Procedure

. Create a YAML file `sysctl-example-unsafe.yaml` that defines an example pod and add the `securityContext` specification, as shown in the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-example-unsafe
spec:
  containers:
  - name: podexample
    image: centos
    command: ["bin/bash", "-c", "sleep INF"]
    securityContext:
      runAsUser: 2000
      runAsGroup: 3000
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
    sysctls:
    - name: kernel.shm_rmid_forced
      value: "0"
    - name: net.core.somaxconn
      value: "1024"
    - name: kernel.msgmax
      value: "65536"
----

. Create the pod using the following command:
+
[source,terminal]
----
$ oc apply -f sysctl-example-unsafe.yaml
----

. Verify that the pod is scheduled but does not deploy because unsafe sysctls are not allowed for the node using the following command:
+
[source,terminal]
----
$ oc get pod
----
+
.Example output
[source,terminal]
----
NAME                       READY             STATUS            RESTARTS   AGE
sysctl-example-unsafe      0/1               SysctlForbidden   0          14s
----
