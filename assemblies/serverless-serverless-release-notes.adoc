:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-release-notes"]
= Release notes
:context: serverless-release-notes

toc::[]

[NOTE]
====
For additional information about the {ServerlessProductName} life cycle and supported platforms, refer to the link:https://access.redhat.com/support/policy/updates/openshift#ossrvless[Platform Life Cycle Policy].
====

Release notes contain information about new and deprecated features, breaking changes, and known issues. The following release notes apply for the most recent {ServerlessProductName} releases on {product-title}.

For an overview of {ServerlessProductName} functionality, see xref:../serverless/about/about-serverless.adoc#about-serverless[About {ServerlessProductName}].

[NOTE]
====
{ServerlessProductName} is based on the open source Knative project.

For details about the latest Knative component releases, see the link:https://knative.dev/blog/[Knative blog].
====

include::modules/serverless-api-versions.adoc[leveloffset=+1]
include::modules/serverless-tech-preview-features.adoc[leveloffset=+1]
include::modules/serverless-deprecated-removed-features.adoc[leveloffset=+1]

// Release notes included, most to least recent
// OCP + OSD + ROSA
include::modules/serverless-rn-1-28-0.adoc[leveloffset=+1]

// OCP + OSD + ROSA
include::modules/serverless-rn-1-27-0.adoc[leveloffset=+1]

// OCP + OSD + ROSA
include::modules/serverless-rn-1-26-0.adoc[leveloffset=+1]
// 1.26.0 additional resources
[role="_additional-resources"]
.Additional resources
* link:https://knative.dev/docs/eventing/experimental-features/new-trigger-filters/[Knative documentation on new trigger filters]

// OCP + OSD + ROSA
include::modules/serverless-rn-1-25-0.adoc[leveloffset=+1]
// 1.25.0 additional resources, OCP docs
ifdef::openshift-enterprise[]
[role="_additional-resources"]
.Additional resources
* xref:../serverless/knative-serving/config-applications/serverless-config-tls.adoc#serverless-config-tls[Configuring TLS authentication]
endif::[]

include::modules/serverless-rn-1-24-0.adoc[leveloffset=+1]
include::modules/serverless-rn-1-23-0.adoc[leveloffset=+1]

// 1.23.0 additional resources, OCP docs
ifdef::openshift-enterprise[]
[role="_additional-resources"]
.Additional resources
* xref:../openshift_images/using_images/using-s21-images.adoc#using-s21-images[Source-to-Image]
endif::[]

// OSD + OCP
ifdef::openshift-enterprise,openshift-dedicated[]
include::modules/serverless-rn-1-22-0.adoc[leveloffset=+1]
include::modules/serverless-rn-1-21-0.adoc[leveloffset=+1]
include::modules/serverless-rn-1-20-0.adoc[leveloffset=+1]
endif::[]

ifdef::openshift-enterprise[]
include::modules/serverless-rn-1-19-0.adoc[leveloffset=+1]
include::modules/serverless-rn-1-18-0.adoc[leveloffset=+1]
endif::[]
