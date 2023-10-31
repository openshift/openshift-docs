// Module included in the following assemblies:
//* rosa_architecture/rosa-sts-about-iam-resources.adoc
// * support/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-sts-ocm-roles-and-permissions-iam-basic-role_{context}"]
= Creating an ocm-role IAM role

You create your `ocm-role` IAM roles by using the command-line interface (CLI).

.Prerequisites

* You have an AWS account.
* You have Red Hat Organization Administrator privileges in the {cluster-manager} organization.
* You have the permissions required to install AWS account-wide roles.
* You have installed and configured the latest {product-title} (ROSA) CLI, `rosa`, on your installation host.

.Procedure
* To create an ocm-role IAM role with basic privileges, run the following command:
+
[source,terminal]
----
$ rosa create ocm-role
----
+
* To create an ocm-role IAM role with admin privileges, run the following command:
+
[source,terminal]
----
$ rosa create ocm-role --admin
----
+
This command allows you create the role by specifying specific attributes. The following example output shows the "auto mode" selected, which lets the ROSA CLI (`rosa`) create your Operator roles and policies. See "Methods of account-wide role creation" in the Additional resources for more information.

.Example output
[source,terminal]
----
I: Creating ocm role
? Role prefix: ManagedOpenShift <1>
? Enable admin capabilities for the OCM role (optional): No <2>
? Permissions boundary ARN (optional): <3>
? Role Path (optional): <4>
? Role creation mode: auto <5>
I: Creating role using 'arn:aws:iam::<ARN>:user/<UserName>'
? Create the 'ManagedOpenShift-OCM-Role-182' role? Yes <6>
I: Created role 'ManagedOpenShift-OCM-Role-182' with ARN  'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182'
I: Linking OCM role
? OCM Role ARN: arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182 <7>
? Link the 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' role with organization '<AWS ARN>'? Yes <8>
I: Successfully linked role-arn 'arn:aws:iam::<ARN>:role/ManagedOpenShift-OCM-Role-182' with organization account '<AWS ARN>'
----

<1> A prefix value for all of the created AWS resources. In this example, `ManagedOpenShift` prepends all of the AWS resources.
<2> Choose if you want this role to have the additional admin permissions.
+
[NOTE]
====
You do not see this prompt if you used the `--admin` option.
====
+
<3> The Amazon Resource Name (ARN) of the policy to set permission boundaries.
<4> Specify an IAM path for the user name.
<5> Choose the method to create your AWS roles. Using `auto`, the ROSA CLI generates and links the roles and policies. In the `auto` mode, you receive some different prompts to create the AWS roles.
<6> The `auto` method asks if you want to create a specific `ocm-role` using your prefix.
<7> Confirm that you want to associate your IAM role with your {cluster-manager}.
<8> Links the created role with your AWS organization.
