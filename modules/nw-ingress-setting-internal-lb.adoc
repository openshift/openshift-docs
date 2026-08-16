// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-setting-internal-lb_{context}"]
= Configuring an Ingress Controller to use an internal load balancer

When creating an Ingress Controller on cloud platforms, the Ingress Controller is published by a public cloud load balancer by default.
As an administrator, you can create an Ingress Controller that uses an internal cloud load balancer.

ifndef::openshift-rosa,openshift-dedicated[]
[WARNING]
====
If your cloud provider is Microsoft Azure, you must have at least one public load balancer that points to your nodes.
If you do not, all of your nodes will lose egress connectivity to the internet.
====
endif::openshift-rosa,openshift-dedicated[]

[IMPORTANT]
====
If you want to change the `scope` for an `IngressController`, you can change the `.spec.endpointPublishingStrategy.loadBalancer.scope` parameter after the custom resource (CR) is created.
====

.Diagram of LoadBalancer
image::202_OpenShift_Ingress_0222_load_balancer.png[{product-title} Ingress LoadBalancerService endpoint publishing strategy]

The preceding graphic shows the following concepts pertaining to {product-title} Ingress LoadBalancerService endpoint publishing strategy:

* You can load balance externally, using the cloud provider load balancer, or internally, using the OpenShift Ingress Controller Load Balancer.
* You can use the single IP address of the load balancer and more familiar ports, such as 8080 and 4200 as shown on the cluster depicted in the graphic.
* Traffic from the external load balancer is directed at the pods, and managed by the load balancer, as depicted in the instance of a down node.
See the link:https://kubernetes.io/docs/concepts/services-networking/service/#internal-load-balancer[Kubernetes Services documentation]
for implementation details.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create an `IngressController` custom resource (CR) in a file named `<name>-ingress-controller.yaml`, such as in the following example:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: <name> <1>
spec:
  domain: <domain> <2>
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal <3>
----
<1> Replace `<name>` with a name for the `IngressController` object.
<2> Specify the `domain` for the application published by the controller.
<3> Specify a value of `Internal` to use an internal load balancer.

. Create the Ingress Controller defined in the previous step by running the following command:
+
[source,terminal]
----
$ oc create -f <name>-ingress-controller.yaml <1>
----
<1> Replace `<name>` with the name of the `IngressController` object.

. Optional: Confirm that the Ingress Controller was created by running the following command:
+
[source,terminal]
----
$ oc --all-namespaces=true get ingresscontrollers
----
