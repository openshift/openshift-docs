// Module included in the following assemblies:
//
// *scalability_and_performance/cnf-numa-aware-scheduling.adoc

:_module-type: PROCEDURE
[id="cnf-creating-nrop-cr-with-manual-performance-settings_{context}"]
= Creating the NUMAResourcesOperator custom resource with manual performance settings

When you have installed the NUMA Resources Operator, then create the `NUMAResourcesOperator` custom resource (CR) that instructs the NUMA Resources Operator to install all the cluster infrastructure needed to support the NUMA-aware scheduler, including daemon sets and APIs.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.
* Install the NUMA Resources Operator.

.Procedure

. Optional: Create the `MachineConfigPool` custom resource that enables custom kubelet configurations for worker nodes:
+
[NOTE]
====
By default, {product-title} creates a `MachineConfigPool` resource for worker nodes in the cluster. You can create a custom `MachineConfigPool` resource if required.
====

.. Save the following YAML in the `nro-machineconfig.yaml` file:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  labels:
    cnf-worker-tuning: enabled
    machineconfiguration.openshift.io/mco-built-in: ""
    pools.operator.machineconfiguration.openshift.io/worker: ""
  name: worker
spec:
  machineConfigSelector:
    matchLabels:
      machineconfiguration.openshift.io/role: worker
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/worker: ""
----

.. Create the `MachineConfigPool` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nro-machineconfig.yaml
----

. Create the `NUMAResourcesOperator` custom resource:

.. Save the following YAML in the `nrop.yaml` file:
+
[source,yaml]
----
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesOperator
metadata:
  name: numaresourcesoperator
spec:
  nodeGroups:
  - machineConfigPoolSelector:
      matchLabels:
        pools.operator.machineconfiguration.openshift.io/worker: "" <1>
----
<1> Should match the label applied to worker nodes in the related `MachineConfigPool` CR.

.. Create the `NUMAResourcesOperator` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nrop.yaml
----

.Verification

* Verify that the NUMA Resources Operator deployed successfully by running the following command:
+
[source,terminal]
----
$ oc get numaresourcesoperators.nodetopology.openshift.io
----
+
.Example output
[source,terminal]
----
NAME                    AGE
numaresourcesoperator   10m
----
