// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-across-multiple-projects.adoc

[id="quotas-selection-granularity_{context}"]
= Selection granularity

Because of the locking consideration when claiming quota allocations, the number of
active projects selected by a multi-project quota is an important consideration.
Selecting more than 100 projects under a single multi-project quota can have
detrimental effects on API server responsiveness in those projects.
