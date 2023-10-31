// Module included in the following assemblies:
//
// * nodes/cluster/limit-ranges.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-cluster-limit-ranges-about_{context}"]
= About limit ranges

A limit range, defined by a `LimitRange` object, restricts resource
consumption in a project. In the project you can set specific resource
limits for a pod, container, image, image stream, or
persistent volume claim (PVC).

All requests to create and modify resources are evaluated against each
`LimitRange` object in the project. If the resource violates any of the
enumerated constraints, the resource is rejected.

ifdef::openshift-online[]
[IMPORTANT]
====
For {product-title} Pro, the maximum pod memory is 3Gi. The minimum pod or
container memory that you can specify is 100Mi.

====
endif::[]

The following shows a limit range object for all components: pod, container,
image, image stream, or PVC. You can configure limits for any or all of these
components in the same object. You create a different limit range object for
each project where you want to control resources.

.Sample limit range object for a container

[source,yaml]
----
apiVersion: "v1"
kind: "LimitRange"
metadata:
  name: "resource-limits"
spec:
  limits:
    - type: "Container"
      max:
        cpu: "2"
        memory: "1Gi"
      min:
        cpu: "100m"
        memory: "4Mi"
      default:
        cpu: "300m"
        memory: "200Mi"
      defaultRequest:
        cpu: "200m"
        memory: "100Mi"
      maxLimitRequestRatio:
        cpu: "10"
----
