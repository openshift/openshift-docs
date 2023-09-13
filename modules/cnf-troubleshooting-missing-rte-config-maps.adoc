// Module included in the following assemblies:
//
// *scalability_and_performance/cnf-numa-aware-scheduling.adoc

:_module-type: PROCEDURE
[id="cnf-troubleshooting-missing-rte-config-maps_{context}"]
= Correcting a missing resource topology exporter config map

If you install the NUMA Resources Operator in a cluster with misconfigured cluster settings, in some circumstances, the Operator is shown as active but the logs of the resource topology exporter (RTE) daemon set pods show that the configuration for the RTE is missing, for example:

[source,text]
----
Info: couldn't find configuration in "/etc/resource-topology-exporter/config.yaml"
----

This log message indicates that the `kubeletconfig` with the required configuration was not properly applied in the cluster, resulting in a missing RTE `configmap`. For example, the following cluster is missing a `numaresourcesoperator-worker` `configmap` custom resource (CR):

[source,terminal]
----
$ oc get configmap
----

.Example output
[source,terminal]
----
NAME                           DATA   AGE
0e2a6bd3.openshift-kni.io      0      6d21h
kube-root-ca.crt               1      6d21h
openshift-service-ca.crt       1      6d21h
topo-aware-scheduler-config    1      6d18h
----

In a correctly configured cluster, `oc get configmap` also returns a `numaresourcesoperator-worker` `configmap` CR.

.Prerequisites

* Install the {product-title} CLI (`oc`).

* Log in as a user with cluster-admin privileges.

* Install the NUMA Resources Operator and deploy the NUMA-aware secondary scheduler.

.Procedure

. Compare the values for `spec.machineConfigPoolSelector.matchLabels` in `kubeletconfig` and
`metadata.labels` in the `MachineConfigPool` (`mcp`) worker CR using the following commands:

..  Check the `kubeletconfig` labels by running the following command:
+
[source,terminal]
----
$ oc get kubeletconfig -o yaml
----
+
.Example output
[source,yaml]
----
machineConfigPoolSelector:
  matchLabels:
    cnf-worker-tuning: enabled
----

.. Check the `mcp` labels by running the following command:
+
[source,terminal]
----
$ oc get mcp worker -o yaml
----
+
.Example output
[source,yaml]
----
labels:
  machineconfiguration.openshift.io/mco-built-in: ""
  pools.operator.machineconfiguration.openshift.io/worker: ""
----
+
The `cnf-worker-tuning: enabled` label is not present in the `MachineConfigPool` object.

. Edit the `MachineConfigPool` CR to include the missing label, for example:
+
[source,terminal]
----
$ oc edit mcp worker -o yaml
----
+
.Example output
[source,yaml]
----
labels:
  machineconfiguration.openshift.io/mco-built-in: ""
  pools.operator.machineconfiguration.openshift.io/worker: ""
  cnf-worker-tuning: enabled
----

. Apply the label changes and wait for the cluster to apply the updated configuration. Run the following command:

.Verification

* Check that the missing `numaresourcesoperator-worker` `configmap` CR is applied:
+
[source,terminal]
----
$ oc get configmap
----
+
.Example output
[source,terminal]
----
NAME                           DATA   AGE
0e2a6bd3.openshift-kni.io      0      6d21h
kube-root-ca.crt               1      6d21h
numaresourcesoperator-worker   1      5m
openshift-service-ca.crt       1      6d21h
topo-aware-scheduler-config    1      6d18h
----
