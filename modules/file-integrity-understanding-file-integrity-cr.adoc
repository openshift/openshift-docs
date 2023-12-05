// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-understanding.adoc

:_mod-docs-content-type: PROCEDURE
[id="understanding-file-integrity-custom-resource_{context}"]
=  Creating the FileIntegrity custom resource

An instance of a `FileIntegrity` custom resource (CR) represents a set of continuous file integrity scans for one or more nodes.

Each `FileIntegrity` CR is backed by a daemon set running AIDE on the nodes matching the `FileIntegrity` CR specification.

.Procedure

. Create the following example `FileIntegrity` CR named `worker-fileintegrity.yaml` to enable scans on worker nodes:
+
.Example FileIntegrity CR
[source,yaml]
----
apiVersion: fileintegrity.openshift.io/v1alpha1
kind: FileIntegrity
metadata:
  name: worker-fileintegrity
  namespace: openshift-file-integrity
spec:
  nodeSelector: <1>
      node-role.kubernetes.io/worker: ""
  tolerations: <2>
  - key: "myNode"
    operator: "Exists"
    effect: "NoSchedule"
  config: <3>
    name: "myconfig"
    namespace: "openshift-file-integrity"
    key: "config"
    gracePeriod: 20 <4>
    maxBackups: 5 <5>
    initialDelay: 60 <6>
  debug: false
status:
  phase: Active <7>
----
<1> Defines the selector for scheduling node scans.
<2> Specify `tolerations` to schedule on nodes with custom taints. When not specified, a default toleration allowing running on main and infra nodes is applied.
<3> Define a `ConfigMap` containing an AIDE configuration to use.
<4> The number of seconds to pause in between AIDE integrity checks. Frequent AIDE checks on a node might be resource intensive, so it can be useful to specify a longer interval. Default is 900 seconds (15 minutes).
<5> The maximum number of AIDE database and log backups (leftover from the re-init process) to keep on a node. Older backups beyond this number are automatically pruned by the daemon. Default is set to 5.
<6> The number of seconds to wait before starting the first AIDE integrity check. Default is set to 0.
<7> The running status of the `FileIntegrity` instance. Statuses are `Initializing`, `Pending`, or `Active`.
+
[horizontal]
`Initializing`:: The `FileIntegrity` object is currently initializing or re-initializing the AIDE database.
`Pending`:: The `FileIntegrity` deployment is still being created.
`Active`:: The scans are active and ongoing.

. Apply the YAML file to the `openshift-file-integrity` namespace:
+
[source,terminal]
----
$ oc apply -f worker-fileintegrity.yaml -n openshift-file-integrity
----

.Verification

* Confirm the `FileIntegrity` object was created successfully by running the following command:
+
[source,terminal]
----
$ oc get fileintegrities -n openshift-file-integrity
----
+
.Example output
+
[source,terminal]
----
NAME                   AGE
worker-fileintegrity   14s
----