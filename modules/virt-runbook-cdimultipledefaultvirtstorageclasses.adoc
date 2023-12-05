// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-CDIMultipleDefaultVirtStorageClasses"]
= CDIMultipleDefaultVirtStorageClasses

[discrete]
[id="meaning-cdimultipledefaultvirtstorageclasses"]
== Meaning

This alert fires when more than one storage class has the annotation
`storageclass.kubevirt.io/is-default-virt-class: "true"`.

[discrete]
[id="impact-cdimultipledefaultvirtstorageclasses"]
== Impact

The `storageclass.kubevirt.io/is-default-virt-class: "true"` annotation
defines a default {VirtProductName} storage class.

If more than one default {VirtProductName} storage class
is defined, a data volume with no storage class specified
receives the most recently created default storage class.

[discrete]
[id="diagnosis-cdimultipledefaultvirtstorageclasses"]
== Diagnosis

Obtain a list of default {VirtProductName} storage classes by running
the following command:

[source,terminal]
----
$ oc get sc -o jsonpath='{.items[?(@.metadata.annotations.storageclass\.kubevirt\.io/is-default-virt-class=="true")].metadata.name}'
----

[discrete]
[id="mitigation-cdimultipledefaultvirtstorageclasses"]
== Mitigation

Ensure that only one default {VirtProductName} storage class
is defined by removing the annotation from the other storage classes.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case, attaching
the artifacts gathered during the diagnosis procedure.
