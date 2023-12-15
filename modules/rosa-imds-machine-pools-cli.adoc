// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-imds-machine-pools-cli_{context}"]
= Enabling Instance Metadata Service on machine pools in CLI

You can select your Instance Metadata Service (IMDS) type when creating your cluster in your ROSA CLI. You can select to use both IMDSv1 and IMDSv2, or you can specify to only use IMDSv2.

.Prerequisites

* You installed and configured the latest AWS (`aws`), ROSA (`rosa`), and OpenShift (`oc`) CLIs on your workstation.
* You logged in to your Red Hat account by using the `rosa` CLI.
* You have the permissions to create and manage clusters.

.Procedure

. In your terminal, create a ROSA cluster with your specifications by running the following command:
+
[source,terminal]
----
$ rosa create cluster --cluster <name_of_cluster> --ec2-metadata-http-tokens <required_or_optional> <1>
----
+
<1> You can provide a value for the `--ec2-metadata-http-tokens` flag, either `required` to enable only IMDSv2 type, or `optional` for a combination of IMDSv1 and IMDSv2. If you do not include this flag, you must select your IMDS type during the cluster creation prompts.

. Confirm the selection:
+
[source,terminal]
----
? Configure the use of IMDSv2 for ec2 instances optional/required: required
----

.Verification

* After your cluster has been created, navigate to your cluster *Overview* tab in {cluster-manager-url} to see the *Instance Metadata Service (IMDS)* field that notes your IMDS version support.