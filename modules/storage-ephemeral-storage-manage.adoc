// Module included in the following assemblies:
//
// storage/understanding-persistent-storage.adoc[leveloffset=+1]
//* microshift_storage/understanding-ephemeral-storage-microshift.adoc
// storage/understanding-ephemeral-storage.adoc

[id=storage-ephemeral-storage-manage_{context}]
= Ephemeral storage management

Cluster administrators can manage ephemeral storage within a project by setting quotas that define the limit ranges and number of requests for ephemeral storage across all pods in a non-terminal state. Developers can also set requests and limits on this compute resource at the pod and container level.

You can manage local ephemeral storage by specifying requests and limits. Each container in a pod can specify the following:

* `spec.containers[].resources.limits.ephemeral-storage`
* `spec.containers[].resources.requests.ephemeral-storage`

Limits and requests for ephemeral storage are measured in byte quantities. You can express storage as a plain integer or as a fixed-point number using one of these suffixes: E, P, T, G, M, k. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki. For example, the following quantities all represent approximately the same value: 128974848, 129e6, 129M, and 123Mi. The case of the suffixes is significant. If you specify 400m of ephemeral storage, this requests 0.4 bytes, rather than 400 mebibytes (400Mi) or 400 megabytes (400M), which was probably what was intended.

The following example shows a pod with two containers. Each container requests 2GiB of local ephemeral storage. Each container has a limit of 4GiB of local ephemeral storage. Therefore, the pod has a request of 4GiB of local ephemeral storage, and a limit of 8GiB of local ephemeral storage.

[source, yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      requests:
        ephemeral-storage: "2Gi" <1>
      limits:
        ephemeral-storage: "4Gi" <2>
    volumeMounts:
    - name: ephemeral
      mountPath: "/tmp"
  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    resources:
      requests:
        ephemeral-storage: "2Gi" <1>
    volumeMounts:
    - name: ephemeral
      mountPath: "/tmp"
  volumes:
    - name: ephemeral
      emptyDir: {}
----
<1> Request for local ephemeral storage.
<2> Limit for local ephemeral storage.

This setting in the pod spec affects how the scheduler makes a decision on scheduling pods, and also how kubelet evict pods. First of all, the scheduler ensures that the sum of the resource requests of the scheduled containers is less than the capacity of the node. In this case, the pod can be assigned to a node only if its available ephemeral storage (allocatable resource) is more than 4GiB.

Secondly, at the container level, since the first container sets resource limit, kubelet eviction manager measures the disk usage of this container and evicts the pod if the storage usage of this container exceeds its limit (4GiB). At the pod level, kubelet works out an overall pod storage limit by adding up the limits of all the containers in that pod. In this case, the total storage usage at the pod level is the sum of the disk usage from all containers plus the pod's `emptyDir` volumes. If this total usage exceeds the overall pod storage limit (4GiB), then the kubelet also marks the pod for eviction.