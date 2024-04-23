:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="ha-replicas-serving"]
= High availability for Knative services
:context: ha-replicas-serving

High availability (HA) is available by default for the Knative Serving `activator`, `autoscaler`, `autoscaler-hpa`, `controller`, `webhook`, `kourier-control`, and `kourier-gateway` components, which are configured to have two replicas each by default. You can change the number of replicas for these components by modifying the `spec.high-availability.replicas` value in the `KnativeServing` custom resource (CR).

include::modules/serverless-config-replicas-serving.adoc[leveloffset=+1]
