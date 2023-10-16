// Module included in the following assemblies:
//
// * nodes/cluster/limit-ranges.adoc

[id="nodes-cluster-limit-creating_{context}"]
= Creating a Limit Range

To apply a limit range to a project:

. Create a `LimitRange` object with your required specifications:
+
[source,yaml]
----
apiVersion: "v1"
kind: "LimitRange"
metadata:
  name: "resource-limits" <1>
spec:
  limits:
    - type: "Pod" <2>
      max:
        cpu: "2"
        memory: "1Gi"
      min:
        cpu: "200m"
        memory: "6Mi"
    - type: "Container" <3>
      max:
        cpu: "2"
        memory: "1Gi"
      min:
        cpu: "100m"
        memory: "4Mi"
      default: <4>
        cpu: "300m"
        memory: "200Mi"
      defaultRequest: <5>
        cpu: "200m"
        memory: "100Mi"
      maxLimitRequestRatio: <6>
        cpu: "10"
    - type: openshift.io/Image <7>
      max:
        storage: 1Gi
    - type: openshift.io/ImageStream <8>
      max:
        openshift.io/image-tags: 20
        openshift.io/images: 30
    - type: "PersistentVolumeClaim" <9>
      min:
        storage: "2Gi"
      max:
        storage: "50Gi"
----
<1> Specify a name for the `LimitRange` object.
<2> To set limits for a pod, specify the minimum and maximum CPU and memory requests as needed.
<3> To set limits for a container, specify the minimum and maximum CPU and memory requests as needed.
<4> Optional. For a container, specify the default amount of CPU or memory that a container can use, if not specified in the `Pod` spec.
<5> Optional. For a container, specify the default amount of CPU or memory that a container can request, if not specified in the `Pod` spec.
<6> Optional. For a container, specify the maximum limit-to-request ratio that can be specified in the `Pod` spec.
<7> To set limits for an Image object, set the maximum size of an image that can be pushed to an {product-registry}.
<8> To set limits for an image stream, set the maximum number of image tags and references that can be in the `ImageStream` object file, as needed.
<9> To set limits for a persistent volume claim, set the minimum and maximum amount of storage that can be requested.

. Create the object:
+
[source,terminal]
----
$ oc create -f <limit_range_file> -n <project> <1>
----
<1> Specify the name of the YAML file you created and the project where you want the limits to apply.
