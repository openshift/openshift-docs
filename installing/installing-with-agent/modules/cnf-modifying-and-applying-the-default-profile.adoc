// CNF-950 4.7 Modifying and applying the default profile
// Module included in the following assemblies:
//
// *scalability_and_performance/cnf-provisioning-and-deploying-a-distributed-unit.adoc

[id="cnf-modifying-and-applying-the-default-profile_{context}"]
= Modifying and applying the default profile

You can apply the profile manually or with the toolset of your choice, such as ArgoCD.

[NOTE]
====
This procedure applies the DU profile step-by-step. If the profile is pulled together into a single project and applied in one step, issues will occur between the MCO and
the SRIOV operators if an Intel NIC is used for networking traffic. To avoid a race condition between the MCO and the SRIOV Operators, it is recommended that the DU application be applied in three steps:

. Apply the profile without SRIOV.
. Wait for the cluster to settle.
. Apply the SRIOV portion.
====
