// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-ocm-role.adoc
:_mod-docs-content-type: CONCEPT
[id="rosa-sts-about-ocm-role_{context}"]
= About the ocm-role IAM resource

You must create the `ocm-role` IAM resource to enable a Red Hat organization of users to create {product-title} (ROSA) clusters. Within the context of linking to AWS, a Red Hat organization is a single user within {cluster-manager}.

Some considerations for your `ocm-role` IAM resource are:

* Only one `ocm-role` IAM role can be linked per Red Hat organization; however, you can have any number of `ocm-role` IAM roles per AWS account. The web UI requires that only one of these roles can be linked at a time.
* Any user in a Red Hat organization may create and link an `ocm-role` IAM resource.
* Only the Red Hat Organization Administrator can unlink an `ocm-role` IAM resource. This limitation is to protect other Red Hat organization members from disturbing the interface capabilities of other users.
+
[NOTE]
====
If you just created a Red Hat account that is not part of an existing organization, this account is also the Red Hat Organization Administrator.
====
+
* See "Understanding the {cluster-manager} role" in the Additional resources of this section for a list of the AWS permissions policies for the basic and admin `ocm-role` IAM resources.

Using the ROSA CLI (`rosa`), you can link your IAM resource when you create it.

[NOTE]
====
"Linking" or "associating" your IAM resources with your AWS account means creating a trust-policy with your `ocm-role` IAM role and the Red Hat {cluster-manager} AWS role. After creating and linking your IAM resource, you see a trust relationship from your `ocm-role` IAM resource in AWS with the `arn:aws:iam::7333:role/RH-Managed-OpenShift-Installer` resource.
====

After a Red Hat Organization Administrator has created and linked an `ocm-role` IAM resource, all organization members may want to create and link their own `user-role` IAM role. This IAM resource only needs to be created and linked only once per user. If another user in your Red Hat organization has already created and linked an `ocm-role` IAM resource, you need to ensure you have created and linked your own `user-role` IAM role.
