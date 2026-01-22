// Module included in the following assembly:
//
// * gitops/run-gitops-control-plane-workload-on-infra-node.adoc

:_mod-docs-content-type: PROCEDURE
[id="add-infra-nodes_{context}"]
= Moving {gitops-shortname} workloads to infrastructure nodes

You can move the default workloads installed by the {gitops-title} to the infrastructure nodes. The workloads that can be moved are:

* `kam deployment`
* `cluster deployment` (backend service)
* `openshift-gitops-applicationset-controller deployment`
* `openshift-gitops-dex-server deployment`
* `openshift-gitops-redis deployment`
* `openshift-gitops-redis-ha-haproxy deployment`
* `openshift-gitops-repo-sever deployment`
* `openshift-gitops-server deployment`
* `openshift-gitops-application-controller statefulset`
* `openshift-gitops-redis-server statefulset`

.Procedure

. Label existing nodes as infrastructure by running the following command:
+
[source,terminal]
----
$ oc label node <node-name> node-role.kubernetes.io/infra=
----
. Edit the `GitOpsService` custom resource (CR) to add the infrastructure node selector:
+
[source,terminal]
----
$ oc edit gitopsservice -n openshift-gitops
----
. In the `GitOpsService` CR file, add `runOnInfra` field to the `spec` section and set it to `true`. This field moves the workloads in `openshift-gitops` namespace to the infrastructure nodes:
+
[source,yaml]
----
apiVersion: pipelines.openshift.io/v1alpha1
kind: GitopsService
metadata:
  name: cluster
spec:
  runOnInfra: true
----
. Optional: Apply taints and isolate the workloads on infrastructure nodes and prevent other workloads from scheduling on these nodes.
+
[source,terminal]
----
$ oc adm taint nodes -l node-role.kubernetes.io/infra
infra=reserved:NoSchedule infra=reserved:NoExecute
----
+
. Optional: If you apply taints to the nodes, you can add tolerations in the `GitOpsService` CR:
+
[source,yaml]
----
spec:
  runOnInfra: true
  tolerations:
  - effect: NoSchedule
    key: infra
    value: reserved
  - effect: NoExecute
    key: infra
    value: reserved
----

To verify that the workloads are scheduled on infrastructure nodes in the {gitops-title} namespace, click any of the pod names and ensure that the *Node selector* and *Tolerations* have been added.

[NOTE]
====
Any manually added *Node selectors* and *Tolerations* in the default Argo CD CR will be overwritten by the toggle and the tolerations in the `GitOpsService` CR.
====
