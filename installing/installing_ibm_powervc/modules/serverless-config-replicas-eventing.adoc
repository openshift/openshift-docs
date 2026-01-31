// Module included in the following assemblies:
//
// * /serverless/eventing/tuning/serverless-ha.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-config-replicas-eventing_{context}"]
= Configuring high availability replicas for Knative Eventing

High availability (HA) is available by default for the Knative Eventing `eventing-controller`, `eventing-webhook`, `imc-controller`, `imc-dispatcher`, and `mt-broker-controller` components, which are configured to have two replicas each by default. You can change the number of replicas for these components by modifying the `spec.high-availability.replicas` value in the `KnativeEventing` custom resource (CR).

[NOTE]
====
For Knative Eventing, the `mt-broker-filter` and `mt-broker-ingress` deployments are not scaled by HA. If multiple deployments are needed, scale these components manually.
====

.Prerequisites

ifdef::openshift-enterprise[]
* You have access to an {product-title} account with cluster administrator access.
endif::[]

ifdef::openshift-dedicated,openshift-rosa[]
* You have access to an {product-title} account with cluster administrator or dedicated administrator access.
endif::[]

* The {ServerlessOperatorName} and Knative Eventing are installed on your cluster.

.Procedure

. In the {product-title} web console *Administrator* perspective, navigate to *OperatorHub* -> *Installed Operators*.

. Select the `knative-eventing` namespace.

. Click *Knative Eventing* in the list of *Provided APIs* for the {ServerlessOperatorName} to go to the *Knative Eventing* tab.

. Click *knative-eventing*, then go to the *YAML* tab in the *knative-eventing* page.
+
image::eventing-YAML-HA.png[Knative Eventing YAML]

. Modify the number of replicas in the `KnativeEventing` CR:
+
.Example YAML
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeEventing
metadata:
  name: knative-eventing
  namespace: knative-eventing
spec:
  high-availability:
    replicas: 3
----
