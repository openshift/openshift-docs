// Module included in the following assemblies:
//
// * builds/troubleshooting-builds.adoc

[id="builds-troubleshooting-access-resources_{context}"]
= Resolving denial for access to resources

If your request for access to resources is denied:

Issue::
A build fails with:

[source,terminal]
----
requested access to the resource is denied
----

Resolution::
You have exceeded one of the image quotas set on your project. Check your current quota and verify the limits applied and storage in use:

[source,terminal]
----
$ oc describe quota
----
