// Module included in the following assemblies:
//
// * nodes/containers/nodes-containers-sysctls.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-starting-pod-safe-sysctls_{context}"]
= Starting a pod with safe sysctls

You can set sysctls on pods using the pod's `securityContext`. The `securityContext` applies to all containers in the same pod.

Safe sysctls are allowed by default.

This example uses the pod `securityContext` to set the following safe sysctls:

* `kernel.shm_rmid_forced`
* `net.ipv4.ip_local_port_range`
* `net.ipv4.tcp_syncookies`
* `net.ipv4.ping_group_range`

[WARNING]
====
To avoid destabilizing your operating system, modify sysctl parameters only after you understand their effects.
====

Use this procedure to start a pod with the configured sysctl settings.
[NOTE]
====
In most cases you modify an existing pod definition and add the `securityContext` spec.
====


.Procedure

. Create a YAML file `sysctl_pod.yaml` that defines an example pod and add the `securityContext` spec, as shown in the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-example
  namespace: default
spec:
  containers:
  - name: podexample
    image: centos
    command: ["bin/bash", "-c", "sleep INF"]
    securityContext:
      runAsUser: 2000 <1>
      runAsGroup: 3000 <2>
      allowPrivilegeEscalation: false <3>
      capabilities: <4>
        drop: ["ALL"]
  securityContext:
    runAsNonRoot: true <5>
    seccompProfile: <6>
      type: RuntimeDefault
    sysctls:
    - name: kernel.shm_rmid_forced
      value: "1"
    - name: net.ipv4.ip_local_port_range
      value: "32770       60666"
    - name: net.ipv4.tcp_syncookies
      value: "0"
    - name: net.ipv4.ping_group_range
      value: "0           200000000"
----
<1> `runAsUser` controls which user ID the container is run with.
<2> `runAsGroup` controls which primary group ID the containers is run with.
<3> `allowPrivilegeEscalation` determines if a pod can request to allow privilege escalation. If unspecified, it defaults to true. This boolean directly controls whether the `no_new_privs` flag gets set on the container process.
<4> `capabilities` permit privileged actions without giving full root access. This policy ensures all capabilities are dropped from the pod.
<5> `runAsNonRoot: true` requires that the container will run with a user with any UID other than 0.
<6> `RuntimeDefault` enables the default seccomp profile for a pod or container workload.

. Create the pod by running the following command:
+
[source,terminal]
----
$ oc apply -f sysctl_pod.yaml
----
+
. Verify that the pod is created by running the following command:
+
[source,terminal]
----
$ oc get pod
----
+
.Example output
[source,terminal]
----
NAME              READY   STATUS            RESTARTS   AGE
sysctl-example    1/1     Running           0          14s
----

. Log in to the pod by running the following command:
+
[source,terminal]
----
$ oc rsh sysctl-example
----

. Verify the values of the configured sysctl flags. For example, find the value `kernel.shm_rmid_forced` by running the following command:
+
[source,terminal]
----
sh-4.4# sysctl kernel.shm_rmid_forced
----
+
.Expected output
[source,terminal]
----
kernel.shm_rmid_forced = 1
----
