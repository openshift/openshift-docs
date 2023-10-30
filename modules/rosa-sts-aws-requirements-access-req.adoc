// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-aws-prereqs.adoc
:_mod-docs-content-type: CONCEPT
[id="rosa-access-requirements_{context}"]
= Access requirements

* Red Hat must have AWS console access to the customer-provided AWS account. Red Hat protects and manages this access.
* You must not use the AWS account to elevate your permissions within the {product-title} (ROSA) cluster.
* Actions available in the ROSA CLI (`rosa`) or {cluster-manager-url} console must not be directly performed in your AWS account.
* You do not need to have a preconfigured domain to deploy ROSA clusters. If you wish to use a custom domain, see the Additional resources for information.
