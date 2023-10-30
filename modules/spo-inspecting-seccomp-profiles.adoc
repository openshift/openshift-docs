// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-troubleshooting.adoc

:_mod-docs-content-type: PROCEDURE
[id="spo-inspecting-seccomp-profiles_{context}"]
= Inspecting seccomp profiles

Corrupted `seccomp` profiles can disrupt your workloads. Ensure that the user cannot abuse the system by not allowing other workloads to map any part of the path `/var/lib/kubelet/seccomp/operator`.

.Procedure

. Confirm that the profile is reconciled by running the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles logs openshift-security-profiles-<id>
----
+
.Example output
[%collapsible]
====
[source,terminal]
----
I1019 19:34:14.942464       1 main.go:90] setup "msg"="starting openshift-security-profiles"  "buildDate"="2020-10-19T19:31:24Z" "compiler"="gc" "gitCommit"="a3ef0e1ea6405092268c18f240b62015c247dd9d" "gitTreeState"="dirty" "goVersion"="go1.15.1" "platform"="linux/amd64" "version"="0.2.0-dev"
I1019 19:34:15.348389       1 listener.go:44] controller-runtime/metrics "msg"="metrics server is starting to listen"  "addr"=":8080"
I1019 19:34:15.349076       1 main.go:126] setup "msg"="starting manager"
I1019 19:34:15.349449       1 internal.go:391] controller-runtime/manager "msg"="starting metrics server"  "path"="/metrics"
I1019 19:34:15.350201       1 controller.go:142] controller "msg"="Starting EventSource" "controller"="profile" "reconcilerGroup"="security-profiles-operator.x-k8s.io" "reconcilerKind"="SeccompProfile" "source"={"Type":{"metadata":{"creationTimestamp":null},"spec":{"defaultAction":""}}}
I1019 19:34:15.450674       1 controller.go:149] controller "msg"="Starting Controller" "controller"="profile" "reconcilerGroup"="security-profiles-operator.x-k8s.io" "reconcilerKind"="SeccompProfile"
I1019 19:34:15.450757       1 controller.go:176] controller "msg"="Starting workers" "controller"="profile" "reconcilerGroup"="security-profiles-operator.x-k8s.io" "reconcilerKind"="SeccompProfile" "worker count"=1
I1019 19:34:15.453102       1 profile.go:148] profile "msg"="Reconciled profile from SeccompProfile" "namespace"="openshift-security-profiles" "profile"="nginx-1.19.1" "name"="nginx-1.19.1" "resource version"="728"
I1019 19:34:15.453618       1 profile.go:148] profile "msg"="Reconciled profile from SeccompProfile" "namespace"="openshift-security-profiles" "profile"="openshift-security-profiles" "name"="openshift-security-profiles" "resource version"="729"
----
====

. Confirm that the `seccomp` profiles are saved into the correct path by running the following command:
+
[source,terminal]
----
$ oc exec -t -n openshift-security-profiles openshift-security-profiles-<id> \
    -- ls /var/lib/kubelet/seccomp/operator/my-namespace/my-workload
----
+
.Example output
[source,terminal]
----
profile-block.json
profile-complain.json
----