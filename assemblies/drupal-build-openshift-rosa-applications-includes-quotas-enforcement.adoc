// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quota-enforcement_{context}"]
= Quota enforcement

After a resource quota for a project is first created, the project restricts the
ability to create any new resources that may violate a quota constraint until it
has calculated updated usage statistics.

After a quota is created and usage statistics are updated, the project accepts
the creation of new content. When you create or modify resources, your quota
usage is incremented immediately upon the request to create or modify the
resource.

When you delete a resource, your quota use is decremented during the next full
recalculation of quota statistics for the project. A configurable amount of time
determines how long it takes to reduce quota usage statistics to their current
observed system value.

If project modifications exceed a quota usage limit, the server denies the
action, and an appropriate error message is returned to the user explaining the
quota constraint violated, and what their currently observed usage statistics
are in the system.
