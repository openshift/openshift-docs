// Module included in the following assemblies:
//
// *scalability_and_performance/cnf-numa-aware-scheduling.adoc

:_module-type: PROCEDURE
[id="cnf-deploying-the-numa-aware-scheduler_{context}"]
= Deploying the NUMA-aware secondary pod scheduler

After you install the NUMA Resources Operator, do the following to deploy the NUMA-aware secondary pod scheduler:

* Configure the performance profile. 

* Deploy the NUMA-aware secondary scheduler.

.Prerequisites

* Install the OpenShift CLI (`oc`).

* Log in as a user with `cluster-admin` privileges.

* Create the required machine config pool.

* Install the NUMA Resources Operator.

.Procedure

. Create the `PerformanceProfile` custom resource (CR):

.. Save the following YAML in the `nro-perfprof.yaml` file:
+
[source,yaml]
----
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: perfprof-nrop
spec:
  cpu: <1>
    isolated: "4-51,56-103" 
    reserved: "0,1,2,3,52,53,54,55" 
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  numa:
    topologyPolicy: single-numa-node
----
<1> The `cpu.isolated` and `cpu.reserved` specifications define ranges for isolated and reserved CPUs. Enter valid values for your CPU configuration. See the _Additional resources_ section for more information about configuring a performance profile.

.. Create the `PerformanceProfile` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nro-perfprof.yaml
----
+
.Example output
[source,terminal]
----
performanceprofile.performance.openshift.io/perfprof-nrop created
----

. Create the `NUMAResourcesScheduler` custom resource that deploys the NUMA-aware custom pod scheduler:

.. Save the following YAML in the `nro-scheduler.yaml` file:
+
[source,yaml,subs="attributes+"]
----
apiVersion: nodetopology.openshift.io/v1
kind: NUMAResourcesScheduler
metadata:
  name: numaresourcesscheduler
spec:
  imageSpec: "registry.redhat.io/openshift4/noderesourcetopology-scheduler-container-rhel8:v{product-version}"
  cacheResyncPeriod: "5s" <1> 
----
<1> Enter an interval value in seconds for synchronization of the scheduler cache. A value of `5s` is typical for most implementations.
+
[NOTE]
====
* Enable the `cacheResyncPeriod` specification to help the NUMA Resource Operator report more exact resource availability by monitoring pending resources on nodes and synchronizing this information in the scheduler cache at a defined interval. This also helps to minimize `Topology Affinity Error` errors because of sub-optimal scheduling decisions. The lower the interval the greater the network load. The `cacheResyncPeriod` specification is disabled by default.

* Setting a value of `Enabled` for the `podsFingerprinting` specification in the `NUMAResourcesOperator` CR is a requirement for the implementation of the `cacheResyncPeriod` specification.
====

.. Create the `NUMAResourcesScheduler` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nro-scheduler.yaml
----

.Verification

. Verify that the performance profile was applied by running the following command:
+
[source,terminal]
----
$ oc describe performanceprofile <performance-profile-name>
----

. Verify that the required resources deployed successfully by running the following command:
+
[source,terminal]
----
$ oc get all -n openshift-numaresources
----
+
.Example output
[source,terminal]
----
NAME                                                    READY   STATUS    RESTARTS   AGE
pod/numaresources-controller-manager-7575848485-bns4s   1/1     Running   0          13m
pod/numaresourcesoperator-worker-dvj4n                  2/2     Running   0          16m
pod/numaresourcesoperator-worker-lcg4t                  2/2     Running   0          16m
pod/secondary-scheduler-56994cf6cf-7qf4q                1/1     Running   0          16m
NAME                                          DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR                     AGE
daemonset.apps/numaresourcesoperator-worker   2         2         2       2            2           node-role.kubernetes.io/worker=   16m
NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/numaresources-controller-manager   1/1     1            1           13m
deployment.apps/secondary-scheduler                1/1     1            1           16m
NAME                                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/numaresources-controller-manager-7575848485   1         1         1       13m
replicaset.apps/secondary-scheduler-56994cf6cf                1         1         1       16m
----
