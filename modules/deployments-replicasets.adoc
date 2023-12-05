// Module included in the following assemblies:
//
// * applications/deployments/what-deployments-are.adoc

[id="deployments-repliasets_{context}"]
= Replica sets

A `ReplicaSet` is a native Kubernetes API object that ensures a specified number of pod replicas are running at any given time. 

[NOTE]
====
Only use replica sets if you require custom update orchestration or do not require updates at all. Otherwise, use deployments. Replica sets can be used independently, but are used by deployments to orchestrate pod creation, deletion, and updates. Deployments manage their replica sets automatically, provide declarative updates to pods, and do not have to manually manage the replica sets that they create.
====

The following is an example `ReplicaSet` definition:

[source,yaml]
----
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend-1
  labels:
    tier: frontend
spec:
  replicas: 3
  selector: <1>
    matchLabels: <2>
      tier: frontend
    matchExpressions: <3>
      - {key: tier, operator: In, values: [frontend]}
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - image: openshift/hello-openshift
        name: helloworld
        ports:
        - containerPort: 8080
          protocol: TCP
      restartPolicy: Always
----
<1> A label query over a set of resources. The result of `matchLabels` and `matchExpressions` are logically conjoined.
<2> Equality-based selector to specify resources with labels that match the selector.
<3> Set-based selector to filter keys. This selects all resources with key equal to `tier` and value equal to `frontend`.
