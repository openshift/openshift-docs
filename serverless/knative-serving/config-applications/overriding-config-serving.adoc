:_mod-docs-content-type: ASSEMBLY
[id="overriding-config-serving"]
= Overriding Knative Serving system deployment configurations
include::_attributes/common-attributes.adoc[]
:context: overriding-config-serving

You can override the default configurations for some specific deployments by modifying the `deployments` spec in the `KnativeServing` custom resources (CRs).

[NOTE]
====
You can only override probes that are defined in the deployment by default.

All Knative Serving deployments define a readiness and a liveness probe by default, with these exceptions:

* `net-kourier-controller` and `3scale-kourier-gateway` only define a readiness probe.
* `net-istio-controller` and `net-istio-webhook` define no probes.
====

include::modules/knative-serving-CR-system-deployments.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* link:https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#probe-v1-core[Probe configuration section of the Kubernetes API documentation]
