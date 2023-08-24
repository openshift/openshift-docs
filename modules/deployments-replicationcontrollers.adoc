// Module included in the following assemblies:
//
// * applications/deployments/what-deployments-are.adoc

[id="deployments-replicationcontrollers_{context}"]
= Replication controllers

Similar to a replica set, a replication controller ensures that a specified number of replicas of a pod are running at all times. If pods exit or are deleted, the replication controller instantiates more up to the defined number. Likewise, if there are more running than desired, it deletes as many as necessary to match the defined amount. The difference between a replica set and a replication controller is that a replica set supports set-based selector requirements whereas a replication controller only supports equality-based selector requirements.

A replication controller configuration consists of:

* The number of replicas desired, which can be adjusted at run time.
* A `Pod` definition to use when creating a replicated pod.
* A selector for identifying managed pods.

A selector is a set of labels assigned to the pods that are managed by the replication controller. These labels are included in the `Pod` definition that the replication controller instantiates. The replication controller uses the selector to determine how many instances of the pod are already running in order to adjust as needed.

The replication controller does not perform auto-scaling based on load or traffic, as it does not track either. Rather, this requires its replica
count to be adjusted by an external auto-scaler.

[NOTE]
====
Use a `DeploymentConfig` to create a replication controller instead of creating replication controllers directly.

If you require custom orchestration or do not require updates, use replica sets instead of replication controllers.
====

The following is an example definition of a replication controller:

[source,yaml]
----
apiVersion: v1
kind: ReplicationController
metadata:
  name: frontend-1
spec:
  replicas: 1  <1>
  selector:    <2>
    name: frontend
  template:    <3>
    metadata:
      labels:  <4>
        name: frontend <5>
    spec:
      containers:
      - image: openshift/hello-openshift
        name: helloworld
        ports:
        - containerPort: 8080
          protocol: TCP
      restartPolicy: Always
----
<1> The number of copies of the pod to run.
<2> The label selector of the pod to run.
<3> A template for the pod the controller creates.
<4> Labels on the pod should include those from the label selector.
<5> The maximum name length after expanding any parameters is 63 characters.
