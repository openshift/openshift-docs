:_mod-docs-content-type: ASSEMBLY
[id="osdk-multi-platform-support"]
= Configuring Operator projects for multi-platform support
include::_attributes/common-attributes.adoc[]
:context: osdk-multi-arch

toc::[]

Operator projects that support multiple architectures and operating systems, or _platforms_, can run on more Kubernetes and {product-title} clusters than Operator projects that support only a single platform. Example architectures include `amd64`, `arm64`, `ppc64le`, and `s390x`. Example operating systems include Linux and Windows.

Perform the following actions to ensure your Operator project can run on multiple {product-title} platforms:

* Build a manifest list that specifies the platforms that your Operator supports.
* Set your Operator's node affinity to support multi-architecture compute machines.

include::modules/osdk-multi-arch-building-images.adoc[leveloffset=+1]
include::modules/osdk-multi-arch-node-affinity.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../nodes/scheduling/nodes-scheduler-node-affinity.adoc#nodes-scheduler-node-affinity[Controlling pod placement on nodes using node affinity rules]
* xref:../../nodes/scheduling/nodes-scheduler-node-affinity.adoc#olm-overriding-operator-pod-affinity_nodes-scheduler-node-affinity[Using node affinity to control where an Operator is installed]
* xref:../../post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-configuration.adoc#post-install-multi-architecture-configuration[About clusters with multi-architecture compute machines]

include::modules/osdk-multi-arch-node-reqs.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* xref:../../nodes/scheduling/nodes-scheduler-node-affinity.adoc#nodes-scheduler-node-affinity-configuring-required_nodes-scheduler-node-affinity[Configuring a required node affinity rule]
* xref:../../nodes/scheduling/nodes-scheduler-node-affinity.adoc#nodes-scheduler-node-affinity-example_nodes-scheduler-node-affinity[Sample node affinity rules]

include::modules/osdk-multi-arch-node-preference.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* xref:../../nodes/scheduling/nodes-scheduler-node-affinity.adoc#nodes-scheduler-node-affinity-configuring-preferred_nodes-scheduler-node-affinity[Configuring a preferred node affinity rule]

[id="next-steps_osdk-multi-arch-support"]
== Next steps

* xref:../../operators/operator_sdk/osdk-generating-csvs.adoc#olm-enabling-operator-for-multi-arch_osdk-generating-csvs[Label the platforms your Operator supports for Operator Lifecycle Manager (OLM)]
* Bundle your Operator and Deploy with OLM
** xref:../../operators/operator_sdk/golang/osdk-golang-tutorial.adoc#osdk-bundle-deploy-olm_osdk-golang-tutorial[Go-based Operator projects]
** xref:../../operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc#osdk-bundle-deploy-olm_osdk-ansible-tutorial[Ansible-based Operator projects]
** xref:../../operators/operator_sdk/helm/osdk-helm-tutorial.html#osdk-bundle-deploy-olm_osdk-helm-tutorial[Helm-based Operator projects]
* xref:../../operators/operator_sdk/osdk-bundle-validate.html#osdk-multi-arch-validate_osdk-bundle-validate[Validate your Operator's multi-platform readiness]
