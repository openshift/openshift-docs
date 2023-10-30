// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-across-multiple-projects.adoc

:_mod-docs-content-type: PROCEDURE
[id="quotas-viewing-clusterresourcequotas_{context}"]
= Viewing applicable cluster resource quotas

A project administrator is not allowed to create or modify the multi-project quota that limits his or her project, but the administrator is allowed to view the multi-project quota documents that are applied to his or her project. The project administrator can do this via the `AppliedClusterResourceQuota` resource.

.Procedure

. To view quotas applied to a project, run:
+
[source,terminal]
----
$ oc describe AppliedClusterResourceQuota
----
+
.Example output
[source,terminal]
----
Name:   for-user
Namespace:  <none>
Created:  19 hours ago
Labels:   <none>
Annotations:  <none>
Label Selector: <null>
AnnotationSelector: map[openshift.io/requester:<user-name>]
Resource  Used  Hard
--------  ----  ----
pods        1     10
secrets     9     20
----
