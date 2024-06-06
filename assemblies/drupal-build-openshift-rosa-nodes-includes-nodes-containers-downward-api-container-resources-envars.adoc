// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-containers-downward-api-container-resources-envars_{context}"]
= Consuming container resources using environment variables

When creating pods, you can use the Downward API to inject information about
computing resource requests and limits using environment variables.

When creating the pod configuration, specify environment variables that
correspond to the contents of the `resources` field in the `*spec.container*`
field.

[NOTE]
====
If the resource limits are not included in the container configuration, the
downward API defaults to the node's CPU and memory allocatable values.
====

.Procedure

. Create a new pod spec that contains the resources you want to inject:

.. Create a `pod.yaml` file similar to the following:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dapi-env-test-pod
spec:
  containers:
    - name: test-container
      image: gcr.io/google_containers/busybox:1.24
      command: [ "/bin/sh", "-c", "env" ]
      resources:
        requests:
          memory: "32Mi"
          cpu: "125m"
        limits:
          memory: "64Mi"
          cpu: "250m"
      env:
        - name: MY_CPU_REQUEST
          valueFrom:
            resourceFieldRef:
              resource: requests.cpu
        - name: MY_CPU_LIMIT
          valueFrom:
            resourceFieldRef:
              resource: limits.cpu
        - name: MY_MEM_REQUEST
          valueFrom:
            resourceFieldRef:
              resource: requests.memory
        - name: MY_MEM_LIMIT
          valueFrom:
            resourceFieldRef:
              resource: limits.memory
# ...
----

.. Create the pod from the `pod.yaml` file:
+
[source,terminal]
----
$ oc create -f pod.yaml
----
