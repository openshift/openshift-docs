// Module included in the following assemblies:
//
// * operators/understanding/olm-packaging-format.adoc

[id="olm-fb-catalogs-prop_{context}"]
= Properties

Properties are arbitrary pieces of metadata that can be attached to file-based catalog schemas. The `type` field is a string that effectively specifies the semantic and syntactic meaning of the `value` field. The value can be any arbitrary JSON or YAML.

OLM defines a handful of property types, again using the reserved `olm.*` prefix.

[id="olm-fb-catalogs-package-prop_{context}"]
== olm.package property

The `olm.package` property defines the package name and version. This is a required property on bundles, and there must be exactly one of these properties. The `packageName` field must match the bundle's first-class `package` field, and the `version` field must be a valid semantic version.

.`olm.package` property
[%collapsible]
====
[source,go]
----
#PropertyPackage: {
  type: "olm.package"
  value: {
    packageName: string & !=""
    version: string & !=""
  }
}
----
====

[id="olm-fb-catalogs-gvk-prop_{context}"]
== olm.gvk property

The `olm.gvk` property defines the group/version/kind (GVK) of a Kubernetes API that is provided by this bundle. This property is used by OLM to resolve a bundle with this property as a dependency for other bundles that list the same GVK as a required API. The GVK must adhere to Kubernetes GVK validations.

.`olm.gvk` property
[%collapsible]
====
[source,go]
----
#PropertyGVK: {
  type: "olm.gvk"
  value: {
    group: string & !=""
    version: string & !=""
    kind: string & !=""
  }
}
----
====

[id="olm-fb-catalogs-package-reqd-prop_{context}"]
== olm.package.required

The `olm.package.required` property defines the package name and version range of another package that this bundle requires. For every required package property a bundle lists, OLM ensures there is an Operator installed on the cluster for the listed package and in the required version range. The `versionRange` field must be a valid semantic version (semver) range.

.`olm.package.required` property
[%collapsible]
====
[source,go]
----
#PropertyPackageRequired: {
  type: "olm.package.required"
  value: {
    packageName: string & !=""
    versionRange: string & !=""
  }
}
----
====

[id="olm-fb-catalogs-gvk-reqd-prop_{context}"]
== olm.gvk.required

The `olm.gvk.required` property defines the group/version/kind (GVK) of a Kubernetes API that this bundle requires. For every required GVK property a bundle lists, OLM ensures there is an Operator installed on the cluster that provides it. The GVK must adhere to Kubernetes GVK validations.

.`olm.gvk.required` property
[%collapsible]
====
[source,terminal]
----
#PropertyGVKRequired: {
  type: "olm.gvk.required"
  value: {
    group: string & !=""
    version: string & !=""
    kind: string & !=""
  }
}
----
====
