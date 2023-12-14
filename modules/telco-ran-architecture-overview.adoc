// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-design-spec.adoc

:_mod-docs-content-type: CONCEPT
[id="telco-ran-architecture-overview_{context}"]
= Deployment architecture overview

You deploy the {rds} {product-version} reference configuration to managed clusters from a centrally managed {rh-rhacm} hub cluster.
The reference design specification (RDS) includes configuration of the managed clusters and the hub cluster components.

.{rds-caps} deployment architecture overview
image::474_OpenShift_OpenShift_RAN_RDS_arch_updates_1023.png[A diagram showing two distinctive network far edge deployment processes, one show how the hub cluster uses {gitops-title} to install managed clusters, and the other showing how the hub cluster uses {cgu-operator-full} to apply policies to managed clusters]
