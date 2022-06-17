// Module included in the following assemblies:
//
// * applications/red-hat-marketplace.adoc

[id="red-hat-marketplace-features_{context}"]
= Red Hat Marketplace features

Cluster administrators can use link:https://marketplace.redhat.com/en-us/documentation/getting-started[the Red Hat Marketplace] to manage software on {product-title}, give developers self-service access to deploy application instances, and correlate application usage against a quota.

[id="marketplace-clusters_{context}"]
== Connect {product-title} clusters to the Marketplace

Cluster administrators can install a common set of applications on {product-title} clusters that connect to the Marketplace. They can also use the Marketplace to track cluster usage against subscriptions or quotas. Users that they add by using the Marketplace have their product usage tracked and billed to their organization.

During the link:https://marketplace.redhat.com/en-us/documentation/clusters[cluster connection process],
a Marketplace Operator is installed that updates the image registry secret, manages the catalog, and reports application usage.

[id="marketplace-install-applications_{context}"]
== Install applications

Cluster administrators can link:https://marketplace.redhat.com/en-us/documentation/operators[install Marketplace applications] from within OperatorHub in {product-title}, or from the link:https://marketplace.redhat.com[Marketplace web application].

You can access installed applications from the web console by clicking **Operators > Installed Operators**.

[id="marketplace-deploy_{context}"]
== Deploy applications from different perspectives

You can deploy Marketplace applications from the web console's Administrator and Developer perspectives.

[discrete]
=== The Developer perspective

Developers can access newly installed capabilities by using the Developer perspective.

For example, after a database Operator is installed, a developer can create an instance from the catalog within their project. Database usage is aggregated and reported to the cluster administrator.

This perspective does not include Operator installation and application usage tracking.

[discrete]
=== The Administrator perspective

Cluster administrators can access Operator installation and application usage information from the Administrator perspective.

They can also launch application instances by browsing custom resource definitions (CRDs) in the *Installed Operators* list.