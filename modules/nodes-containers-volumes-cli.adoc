// Module included in the following assemblies:
//
// * nodes/nodes-containers-volumes.adoc

[id="nodes-containers-volumes-cli_{context}"]
= Working with volumes using the {product-title} CLI

You can use the CLI command `oc set volume` to add and remove volumes and
volume mounts for any object that has a pod template like replication controllers or
deployment configs. You can also list volumes in pods or any
object that has a pod template.

The `oc set volume` command uses the following general syntax:

[source,terminal]
----
$ oc set volume <object_selection> <operation> <mandatory_parameters> <options>
----


Object selection::
Specify one of the following for the `object_selection` parameter in the `oc set volume` command:

[id="vol-object-selection_{context}"]
.Object Selection
[cols="3a*",options="header"]
|===

|Syntax |Description |Example

|`_<object_type>_ _<name>_`
|Selects `_<name>_` of type `_<object_type>_`.
|`deploymentConfig registry`

|`_<object_type>_/_<name>_`
|Selects `_<name>_` of type `_<object_type>_`.
|`deploymentConfig/registry`

|`_<object_type>_`
`--selector=_<object_label_selector>_`
|Selects resources of type `_<object_type>_` that matched the given label
selector.
|`deploymentConfig`
`--selector="name=registry"`

|`_<object_type>_ --all`
|Selects all resources of type `_<object_type>_`.
|`deploymentConfig --all`

|`-f` or
`--filename=_<file_name>_`
|File name, directory, or URL to file to use to edit the resource.
|`-f registry-deployment-config.json`
|===


Operation::
Specify `--add` or `--remove` for the `operation` parameter in the `oc set volume` command.

Mandatory parameters::
Any mandatory parameters are specific to the
selected operation and are discussed in later sections.

Options::
Any options are specific to the
selected operation and are discussed in later sections.
