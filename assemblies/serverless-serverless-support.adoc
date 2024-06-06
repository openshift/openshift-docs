:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-support"]
= {ServerlessProductName} support
:context: serverless-support

toc::[]

If you experience difficulty with a procedure described in this documentation, visit the Red Hat Customer Portal at http://access.redhat.com. You can use the Red Hat Customer Portal to search or browse through the Red Hat Knowledgebase of technical support articles about Red Hat products. You can also submit a support case to Red Hat Global Support Services (GSS), or access other product documentation.

If you have a suggestion for improving this guide or have found an error, you can submit a link:https://issues.redhat.com/secure/CreateIssueDetails!init.jspa?pid=12332330&summary=Documentation_issue&issuetype=1&components=12367614&priority=10200&versions=12385624[Jira issue] for the most relevant documentation component. Provide specific details, such as the section number, guide name, and {ServerlessProductName} version so we can easily locate the content.
// TODO: Update once https://issues.redhat.com/browse/OSDOCS-3730 is done to update this to Jira

// Generic help topics
ifdef::openshift-enterprise,openshift-dedicated[]

include::modules/support-knowledgebase-about.adoc[leveloffset=+1]
include::modules/support-knowledgebase-search.adoc[leveloffset=+1]
include::modules/support-submitting-a-case.adoc[leveloffset=+1]

endif::openshift-enterprise,openshift-dedicated[]

[id="serverless-support-gather-info"]
== Gathering diagnostic information for support

When you open a support case, it is helpful to provide debugging information about your cluster to Red Hat Support. The `must-gather` tool enables you to collect diagnostic information about your {product-title} cluster, including data related to {ServerlessProductName}. For prompt support, supply diagnostic information for both {product-title} and {ServerlessProductName}.

include::modules/about-must-gather.adoc[leveloffset=+2]
include::modules/serverless-about-collecting-data.adoc[leveloffset=+2]

