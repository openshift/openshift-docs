// Module included in the following assemblies:
//
// * nodes/nodes-pods-daemonsets.adoc

[id="nodes-pods-daemonsets-pods_{context}"]
= About Scheduling DaemonSets with the default scheduler

In {product-title}, the scheduler selects the Node that a Pod runs on. However, in previous versions of {product-title}, DaemonSet pods were created and scheduled by the DaemonSet controller. 

The `ScheduleDaemonSetPods` feature, enabled by default, forces {product-title} to schedule DaemonSets using the default scheduler, instead of the DaemonSet controller. 
The DaemonSet controller adds the `NodeAffinity` parameter to the DaemonSet pods, instead of the `.spec.nodeName` parameter. The default scheduler then binds the pod to the target host. If the DaemonSet pod is already configured for node affinity, the affinity is replaced. The DaemonSet controller only performs these operations when creating or modifying DaemonSet pods, and no changes are made to the `spec.template` parameter of the DaemonSet.

----
nodeAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
    - matchFields:
      - key: metadata.name
        operator: In
        values:
        - target-host-name
----

In addition, the DaemonSet controller adds the `node.kubernetes.io/unschedulable:NoSchedule` toleration to DaemonSet Pods. The default scheduler ignores unschedulable Nodes when scheduling DaemonSet Pods.
