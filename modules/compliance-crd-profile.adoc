// Module included in the following assemblies:
//
// * security/compliance_operator/co-concepts/compliance-operator-crd.adoc

:_mod-docs-content-type: CONCEPT
[id="profile-object_{context}"]
= Profile object

The `Profile` object defines the rules and variables that can be evaluated for a certain compliance standard. It contains parsed out details about an OpenSCAP profile, such as its XCCDF identifier and profile checks for a `Node` or `Platform` type. You can either directly use the `Profile` object or further customize it using a `TailorProfile` object.

[NOTE]
====
You cannot create or modify the `Profile` object manually because it is derived from a single `ProfileBundle` object. Typically, a single `ProfileBundle` object can include several `Profile` objects.
====

.Example `Profile` object
[source,yaml]
----
apiVersion: compliance.openshift.io/v1alpha1
description: <description of the profile>
id: xccdf_org.ssgproject.content_profile_moderate <1>
kind: Profile
metadata:
  annotations:
    compliance.openshift.io/product: <product name>
    compliance.openshift.io/product-type: Node <2>
  creationTimestamp: "YYYY-MM-DDTMM:HH:SSZ"
  generation: 1
  labels:
    compliance.openshift.io/profile-bundle: <profile bundle name>
  name: rhcos4-moderate
  namespace: openshift-compliance
  ownerReferences:
  - apiVersion: compliance.openshift.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: ProfileBundle
    name: <profile bundle name>
    uid: <uid string>
  resourceVersion: "<version number>"
  selfLink: /apis/compliance.openshift.io/v1alpha1/namespaces/openshift-compliance/profiles/rhcos4-moderate
  uid: <uid string>
rules: <3>
- rhcos4-account-disable-post-pw-expiration
- rhcos4-accounts-no-uid-except-zero
- rhcos4-audit-rules-dac-modification-chmod
- rhcos4-audit-rules-dac-modification-chown
title: <title of the profile>
----
<1> Specify the XCCDF name of the profile. Use this identifier when you define a `ComplianceScan` object as the value of the profile attribute of the scan.
<2> Specify either a `Node` or `Platform`. Node profiles scan the cluster nodes and platform profiles scan the Kubernetes platform.
<3> Specify the list of rules for the profile. Each rule corresponds to a single check.
