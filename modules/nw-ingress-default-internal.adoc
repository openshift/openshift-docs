// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-default-internal_{context}"]
= Configuring the default Ingress Controller for your cluster to be internal

You can configure the `default` Ingress Controller for your cluster to be internal by deleting and recreating it.

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

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Configure the `default` Ingress Controller for your cluster to be internal by deleting and recreating it.
+
[source,terminal]
----
$ oc replace --force --wait --filename - <<EOF
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: default
spec:
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal
EOF
----
