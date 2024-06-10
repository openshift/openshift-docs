// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-configure-an-idp-and-grant-access_{context}"]
= Configuring an identity provider and granting cluster access

{product-title} (ROSA) includes a built-in OAuth server. After your ROSA cluster is created, you must configure OAuth to use an identity provider. You can then add members to your configured identity provider to grant them access to your cluster.

You can also grant the identity provider users with `cluster-admin` or `dedicated-admin` privileges as required.
