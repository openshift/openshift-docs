// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-sts-user-role-iam-basic-role_{context}"]
= Creating a user-role IAM role

You can create your `user-role` IAM roles by using the command-line interface (CLI).

.Prerequisites

* You have an AWS account.
* You have installed and configured the latest {product-title} (ROSA) CLI, `rosa`, on your installation host.

.Procedure
* To create a `user-role` IAM role with basic privileges, run the following command:
+
[source,terminal]
----
$ rosa create user-role
----
+
This command allows you create the role by specifying specific attributes. The following example output shows the "auto mode" selected, which lets the ROSA CLI (`rosa`) to create your Operator roles and policies. See "Understanding the auto and manual deployment modes" in the Additional resources for more information.

.Example output
[source,terminal]
----
I: Creating User role
? Role prefix: ManagedOpenShift <1>
? Permissions boundary ARN (optional): <2>
? Role Path (optional): <3>
? Role creation mode: auto <4>
I: Creating ocm user role using 'arn:aws:iam::2066:user'
? Create the 'ManagedOpenShift-User.osdocs-Role' role? Yes <5>
I: Created role 'ManagedOpenShift-User.osdocs-Role' with ARN 'arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role'
I: Linking User role
? User Role ARN: arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role
? Link the 'arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role' role with account '1AGE'? Yes <6>
I: Successfully linked role ARN 'arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role' with account '1AGE'
----
<1> A prefix value for all of the created AWS resources. In this example, `ManagedOpenShift` prepends all of the AWS resources.
<2> The Amazon Resource Name (ARN) of the policy to set permission boundaries.
<3> Specify an IAM path for the user name.
<4> Choose the method to create your AWS roles. Using `auto`, the ROSA CLI generates and links the roles and policies. In the `auto` mode, you receive some different prompts to create the AWS roles.
<5> The `auto` method asks if you want to create a specific `user-role` using your prefix.
<6> Links the created role with your AWS organization.
