// Module included in the following assemblies:
//
// * applications/projects/creating-project-other-user.adoc

:_mod-docs-content-type: PROCEDURE
[id="impersonation-project-creation_{context}"]
= Impersonating a user when you create a project

You can impersonate a different user when you create a project request. Because
`system:authenticated:oauth` is the only bootstrap group that can
create project requests, you must impersonate that group.

.Procedure

* To create a project request on behalf of a different user:
+
[source,terminal]
----
$ oc new-project <project> --as=<user> \
    --as-group=system:authenticated --as-group=system:authenticated:oauth
----
