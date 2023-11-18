// Module included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

:_mod-docs-content-type: PROCEDURE
[id="lvms-dowloading-log-files-and-diagnostics_{context}"]
= Downloading log files and diagnostic information using must-gather

When {lvms} is unable to automatically resolve a problem, use the must-gather tool to collect the log files and diagnostic information so that you or the Red Hat Support can review the problem and determine a solution.

* Run the must-gather command from the client connected to {lvms} cluster by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc adm must-gather --image=registry.redhat.io/lvms4/lvms-must-gather-rhel9:v{product-version} --dest-dir=<directory-name>
----