// Module included in the following assemblies:
//
// * networking/rosa-shared-vpc-config.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-sharing-vpc-dns-and-roles_{context}"]
= Step Two - Cluster Creator: Reserving your DNS and creating cluster operator roles

After the *VPC Owner* creates a virtual private cloud, subnets, and an IAM role for sharing the VPC resources, reserve an `openshiftapps.com` DNS domain and create Operator roles to communicate back to the *VPC Owner*.

[NOTE]
====
For shared VPC clusters, you can choose to create the Operator roles after the cluster creation steps. The cluster will be in a `waiting` state until the Ingress Operator role ARN is added to the shared VPC role trusted relationships.
====

image::372_OpenShift_on_AWS_persona_worflows_0923_2.png[]
.Prerequisites

* You have the `SharedVPCRole` ARN for the IAM role from the *VPC Owner*.

.Procedure

. Reserve an `openshiftapps.com` DNS domain with the following command:
+
[source,terminal]
----
$ rosa create dns-domain
----
+
The command creates a reserved `openshiftapps.com` DNS domain.
+
[source,terminal]
----
I: DNS domain '14eo.p1.openshiftapps.com' has been created.
I: To view all DNS domains, run 'rosa list dns-domains'
----
. Create an OIDC configuration.
+
Review this article for more information on the link:https://access.redhat.com/articles/7031018[OIDC configuration process]. The following command produces the OIDC configuration ID that you need:
+
[source,terminal]
----
$ rosa create oidc-config
----
+
You receive confirmation that the command created an OIDC configuration:
+
[source,terminal]
----
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
	rosa create operator-roles --prefix <user-defined> --oidc-config-id 25tu67hq45rto1am3slpf5lq6jargg
----

. Create the Operator roles by entering the following command:
+
[source,terminal]
----
$ rosa create operator-roles --oidc-config-id <oidc-config-ID> <1>
    --installer-role-arn <Installer_Role> <2>
    --shared-vpc-role-arn <Created_VPC_Role_Arn> <3>
    --prefix <operator-prefix> <4>
----
+
--
<1> Provide the OIDC configuration ID that you created in the previous step.
<2> Provide your installer ARN that was created as part of the `rosa create account-roles` process.
<3> Provide the ARN for the role that the *VPC Owner* created.
<4> Provide a prefix for the Operator roles.
--
+
[NOTE]
====
The Installer account role and the shared VPC role must have a one-to-one relationship. If you want to create multiple shared VPC roles, you should create one set of account roles per shared VPC role.
====

. After you create the Operator roles, share the full domain name, which is created with `<intended_cluster_name>.<reserved_dns_domain>`, your _Ingress Operator Cloud Credentials_ role's ARN, and your _Installer_ role's ARN with the *VPC Owner* to continue configuration.
+
The shared information resembles these examples:
+
* ``my-rosa-cluster.14eo.p1.openshiftapps.com``
* ``arn:aws:iam::111122223333:role/ManagedOpenShift-Installer-Role``
* ``arn:aws:iam::111122223333:role/my-rosa-cluster-openshift-ingress-operator-cloud-credentials``

