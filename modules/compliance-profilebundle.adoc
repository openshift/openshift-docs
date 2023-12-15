// Module included in the following assemblies:
//
// * security/compliance_operator/co-management/compliance-operator-manage.adoc

:_mod-docs-content-type: CONCEPT
[id="compliance-profilebundle_{context}"]
= ProfileBundle CR example

The `ProfileBundle` object requires two pieces of information: the URL of a container image that contains the `contentImage` and the file that contains the compliance content. The `contentFile` parameter is relative to the root of the file system. You can define the built-in `rhcos4` `ProfileBundle` object as shown in the following example:

[source,yaml]
----
apiVersion: compliance.openshift.io/v1alpha1
kind: ProfileBundle
metadata:
  creationTimestamp: "2022-10-19T12:06:30Z"
  finalizers:
  - profilebundle.finalizers.compliance.openshift.io
  generation: 1
  name: rhcos4
  namespace: openshift-compliance
  resourceVersion: "46741"
  uid: 22350850-af4a-4f5c-9a42-5e7b68b82d7d
spec:
  contentFile: ssg-rhcos4-ds.xml <1>
  contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:900e... <2>
status:
  conditions:
  - lastTransitionTime: "2022-10-19T12:07:51Z"
    message: Profile bundle successfully parsed
    reason: Valid
    status: "True"
    type: Ready
  dataStreamStatus: VALID
----
<1> Location of the file containing the compliance content.
<2> Content image location.
+
[IMPORTANT]
====
The base image used for the content images must include `coreutils`.
====
