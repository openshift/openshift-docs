// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/deploying-egress-router-ovn-redirection.adoc

ifeval::["{context}" == "deploying-egress-router-ovn-redirection"]
:redirect:
:router-type: redirect
// Like nw-egress-router-pod, monitor bz-1896170
:egress-pod-image-name: registry.redhat.com/openshift3/ose-pod
endif::[]

// Images are different for OKD
ifdef::openshift-origin[]

ifdef::redirect[]
:egress-pod-image-name: quay.io/openshift/origin-pod
endif::[]

endif::[]

[id="nw-egress-router-cni-pod_{context}"]
= Egress router pod specification for {router-type} mode

After you create a network attachment definition, you add a pod that references the definition.

.Example egress router pod specification
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Pod
metadata:
  name: egress-router-pod
  annotations:
    k8s.v1.cni.cncf.io/networks: egress-router-redirect  <1>
spec:
  containers:
    - name: egress-router-pod
      image: {egress-pod-image-name}
----
<1> The specified network must match the name of the network attachment definition. You can specify a namespace, interface name, or both, by replacing the values in the following pattern: `<namespace>/<network>@<interface>`. By default, Multus adds a secondary network interface to the pod with a name such as `net1`, `net2`, and so on.

// Clear temporary attributes
:!router-type:
:!egress-pod-image-name:
ifdef::redirect[]
:!redirect:
endif::[]
