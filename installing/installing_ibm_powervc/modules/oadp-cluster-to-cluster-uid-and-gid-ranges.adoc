// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/advanced-topics.adoc


:_mod-docs-content-type: CONCEPT
[id="oadp-cluster-to-cluster-uid-and-gid-ranges_{context}"]
= UID and GID ranges

If you back up data from one cluster and restore it to another cluster,  problems might occur with UID (User ID) and GID (Group ID) ranges. The following section explains these potential issues and mitigations:

Summary of the issues::
The namespace UID and GID ranges might change depending on the destination cluster. OADP does not back up and restore OpenShift UID range metadata. If the backed up application requires a specific UID, ensure the range is availableupon restore. For more information about OpenShift's UID and GID ranges, see link:https://cloud.redhat.com/blog/a-guide-to-openshift-and-uids[A Guide to OpenShift and UIDs].

Detailed description of the issues::
When you create a namespace in {product-title} by using the shell command `oc create namespace`, {product-title} assigns the namespace a unique User ID (UID) range from its available pool of UIDs, a Supplemental Group (GID) range, and unique SELinux MCS labels. This information is stored in the `metadata.annotations` field of the cluster. This information is part of the Security Context Constraints (SCC) annotations, which comprise of the following components:

* `openshift.io/sa.scc.mcs`
* `openshift.io/sa.scc.supplemental-groups`
* `openshift.io/sa.scc.uid-range`

When you use OADP to restore the namespace, it automatically uses the information in `metadata.annotations` without resetting it for the destination cluster. As a result, the workload might not have access to the backed up data if any of the following is true:

* There is an existing namespace with other SCC annotations, for example, on another cluster. In this case, OADP uses the existing namespace during the backup instead of the namespace you want to restore.
* A label selector was used during the backup, but the namespace in which the workloads are executed does not have the label. In this case, OADP does not back up the namespace, but creates a new namespace during the restore that does not contain the annotations of the backed up namespace. This results in a new UID range being assigned to the namespace.
+
This can be an issue for customer workloads if {product-title} assigns a pod a `securityContext` UID to a pod based on namespace annotations that have changed since the persistent volume data was backed up.
* The UID of the container no longer matches the UID of the file owner.
* An error occurs because {product-title} has not changed the UID range of the destination cluster to match the backup cluster data. As a result, the backup cluster has a different UID than the destination cluster, which means that the application cannot read or write data on the destination cluster.

Mitigations::

You can use one or more of the following mitigations to resolve the UID and GID range issues:

* Simple mitigations:

** If you use a label selector in the `Backup` CR to filter the objects to include in the backup, be sure to add this label selector to the namespace that contains the workspace.
** Remove any pre-existing version of a namespace on the destination cluster before attempting to restore a namespace with the same name.

* Advanced mitigations:
** Fix UID ranges after migration by link:https://access.redhat.com/articles/6844071[Resolving overlapping UID ranges in OpenShift namespaces after migration]. Step 1 is optional.

For an in-depth discussion of UID and GID ranges in {product-title} with an emphasis on overcoming issues in backing up data on one cluster and restoring it on another, see link:https://cloud.redhat.com/blog/a-guide-to-openshift-and-uids[A Guide to OpenShift and UIDs].
