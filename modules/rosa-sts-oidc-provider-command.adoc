// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-oidc-overview.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-sts-oidc-provider-for-operators-aws-cli_{context}"]
= Creating an OIDC provider using the CLI

You can create an OIDC provider that is hosted in your AWS account with the {product-title} (ROSA) CLI, `rosa`.

.Prerequisites

* You have installed the latest version of the ROSA CLI.

.Procedure

* To create an OIDC provider, by using an unregistered or a registered OIDC configuration.
** Unregistered OIDC configurations require you to create the OIDC provider through the cluster. Run the following to create the OIDC provider:
+
[source,terminal]
----
$ rosa create oidc-provider --mode manual --cluster <cluster_name>
----
+
[NOTE]
====
When using `manual` mode, the `aws` command is printed to the terminal for your review. After reviewing the `aws` command, you must run it manually. Alternatively, you can specify `--mode auto` with the `rosa create` command to run the `aws` command immediately.
====
+
.Command output
[source,terminal]
----
aws iam create-open-id-connect-provider \
	--url https://oidc.op1.openshiftapps.com/<oidc_config_id> \// <1>
	--client-id-list openshift sts.<aws_region>.amazonaws.com \
	--thumbprint-list <thumbprint> <2>
----
<1> The URL used to reach the OpenID Connect (OIDC) identity provider after the cluster is created.
<2> The thumbprint is generated automatically when you run the `rosa create oidc-provider` command. For more information about using thumbprints with AWS Identity and Access Management (IAM) OIDC identity providers, see link:https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html[the AWS documentation].

** Registered OIDC configurations use an OIDC configuration ID. Run the following command with your OIDC configuration ID:
+
[source,terminal]
----
$ rosa create oidc-provider --oidc-config-id <oidc_config_id> --mode auto -y
----
+
.Command output
[source,terminal]
----
I: Creating OIDC provider using 'arn:aws:iam::4540112244:user/userName'
I: Created OIDC provider with ARN 'arn:aws:iam::4540112244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/241rh9ql5gpu99d7leokhvkp8icnalpf'
----
