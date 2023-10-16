// Module included in the following assemblies:
//
// * applications/pruning-objects.adoc

[id="pruning-basic-operations_{context}"]
= Basic pruning operations

The CLI groups prune operations under a common parent command:

[source,terminal]
----
$ oc adm prune <object_type> <options>
----

This specifies:

- The `<object_type>` to perform the action on, such as `groups`, `builds`,
`deployments`, or `images`.
- The `<options>` supported to prune that object type.
