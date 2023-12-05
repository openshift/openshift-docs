// Module included in the following assemblies:
//
// * updating/preparing_for_updates/updating-cluster-prepare.adoc

:_mod-docs-content-type: PROCEDURE
[id="update-preparing-conditional_{context}"]
= Assessing the risk of conditional updates

A _conditional update_ is an update target that is available but not recommended due to a known risk that applies to your cluster.
The Cluster Version Operator (CVO) periodically queries the OpenShift Update Service (OSUS) for the most recent data about update recommendations, and some potential update targets might have risks associated with them.

The CVO evaluates the conditional risks, and if the risks are not applicable to the cluster, then the target version is available as a recommended update path for the cluster.
If the risk is determined to be applicable, or if for some reason CVO cannot evaluate the risk, then the update target is available to the cluster as a conditional update.

When you encounter a conditional update while you are trying to update to a target version, you must assess the risk of updating your cluster to that version.
Generally, if you do not have a specific need to update to that target version, it is best to wait for a recommended update path from Red Hat.

However, if you have a strong reason to update to that version, for example, if you need to fix an important CVE, then the benefit of fixing the CVE might outweigh the risk of the update being problematic for your cluster.
You can complete the following tasks to determine whether you agree with the Red Hat assessment of the update risk:

* Complete extensive testing in a non-production environment to the extent that you are comfortable completing the update in your production environment.
* Follow the links provided in the conditional update description, investigate the bug, and determine if it is likely to cause issues for your cluster. If you need help understanding the risk, contact Red Hat Support.