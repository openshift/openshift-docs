// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-gitconfig-file_{context}"]
= Creating a secret from a .gitconfig file

If the cloning of your application is dependent on a `.gitconfig` file, then you can create a secret that contains it. Add it to the builder service account and then your `BuildConfig`.

.Procedure

* To create a secret from a `.gitconfig` file:

[source,terminal]
----
$ oc create secret generic <secret_name> --from-file=<path/to/.gitconfig>
----

[NOTE]
====
SSL verification can be turned off if `sslVerify=false` is set for the `http`
section in your `.gitconfig` file:

[source,text]
----
[http]
        sslVerify=false
----
====
