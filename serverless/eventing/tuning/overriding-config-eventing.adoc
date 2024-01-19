:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="overriding-config-eventing"]
=  Overriding Knative Eventing system deployment configurations
:context: overriding-config-eventing

toc::[]

You can override the default configurations for some specific deployments by modifying the `deployments` spec in the `KnativeEventing` custom resource (CR). Currently, overriding default configuration settings is supported for the `eventing-controller`, `eventing-webhook`, and `imc-controller` fields, as well as for the `readiness` and `liveness` fields for probes.

[IMPORTANT]
====
The `replicas` spec cannot override the number of replicas for deployments that use the Horizontal Pod Autoscaler (HPA), and does not work for the `eventing-webhook` deployment.
====

[NOTE]
====
You can only override probes that are defined in the deployment by default.

All Knative Serving deployments define a readiness and a liveness probe by default, with these exceptions:

* `net-kourier-controller` and `3scale-kourier-gateway` only define a readiness probe.
* `net-istio-controller` and `net-istio-webhook` define no probes.
====

include::modules/knative-eventing-CR-system-deployments.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* link:https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#probe-v1-core[Probe configuration section of the Kubernetes API documentation]
