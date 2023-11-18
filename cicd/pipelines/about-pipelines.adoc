:_mod-docs-content-type: ASSEMBLY
[id="about-pipelines"]
= About {pipelines-title}
:context: about-pipelines
include::_attributes/common-attributes.adoc[]

toc::[]

{pipelines-title} is a cloud-native, continuous integration and continuous delivery (CI/CD) solution based on Kubernetes resources. It uses Tekton building blocks to automate deployments across multiple platforms by abstracting away the underlying implementation details. Tekton introduces a number of standard custom resource definitions (CRDs) for defining CI/CD pipelines that are portable across Kubernetes distributions.

[NOTE]
====
Because {pipelines-title} releases on a different cadence from {product-title}, the {pipelines-title} documentation is now available as separate documentation sets for each minor version of the product.

The {pipelines-title} documentation is available at link:https://docs.openshift.com/pipelines/[].

Documentation for specific versions is available using the version selector drop-down list, or directly by adding the version to the URL, for example, link:https://docs.openshift.com/pipelines/1.11[].

In addition, the {pipelines-title} documentation is also available on the Red Hat Customer Portal at https://access.redhat.com/documentation/en-us/red_hat_openshift_pipelines/[].


For additional information about the {pipelines-title} life cycle and supported platforms, refer to the link:https://access.redhat.com/support/policy/updates/openshift#pipelines[Platform Life Cycle Policy].
====

// add something about CLI tools?

