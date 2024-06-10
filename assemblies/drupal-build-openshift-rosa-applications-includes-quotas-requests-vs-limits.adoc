// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quotas-requests-vs-limits_{context}"]
= Requests versus limits

When allocating compute resources, each container might specify a request and a
limit value each for CPU, memory, and ephemeral storage. Quotas can restrict any
of these values.

If the quota has a value specified for `requests.cpu` or `requests.memory`,
then it requires that every incoming container make an explicit request for
those resources. If the quota has a value specified for `limits.cpu` or
`limits.memory`, then it requires that every incoming container specify an
explicit limit for those resources.
