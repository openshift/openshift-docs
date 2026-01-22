// Module included in the following assemblies:
//
// * scalability_and_performance/ibm-z-recommended-host-practices.adoc

:_mod-docs-content-type: CONCEPT
[id="ibm-z-disable-thp_{context}"]
= Disable Transparent Huge Pages

Transparent Huge Pages (THP) attempt to automate most aspects of creating, managing, and using huge pages. Since THP automatically manages the huge pages, this is not always handled optimally for all types of workloads. THP can lead to performance regressions, since many applications handle huge pages on their own. Therefore, consider disabling THP.
