// Module included in the following assemblies:
//
// * microshift//running_applications/microshift-applications.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-manifests-override-paths_{context}"]
= Override the list of manifest paths

You can override the list of default manifest paths by using a new single path, or by using a new glob pattern for multiple files. Use the following procedure to customize your manifest paths.

.Procedure

. Override the list of default paths by inserting your own values and running one of the following commands:

.. Set `manifests.kustomizePaths` to `<++"++/opt/alternate/path++"++>` in the configuration file for a single path.

.. Set `kustomizePaths` to `,++"++/opt/alternative/path.d/++*"++.` in the configuration file for a glob pattern.
+
[source,terminal]
----
manifests:
    kustomizePaths:
        - <location> <1>
----
<1> Set each location entry to an exact path by using `++"++/opt/alternate/path++"++` or a glob pattern by using `++"++/opt/alternative/path.d/++*"++`.

. To disable loading manifests, set the configuration option to an empty list.
+
[source,terminal]
----
manifests:
    kustomizePaths: []
----
+
[NOTE]
====
The configuration file overrides the defaults entirely. If the `kustomizePaths` value is set, only the values in the configuration file are used. Setting the value to an empty list disables manifest loading.
====