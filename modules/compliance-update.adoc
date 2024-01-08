// Module included in the following assemblies:
//
// * security/compliance_operator/co-management/compliance-operator-manage.adoc

:_mod-docs-content-type: CONCEPT
[id="compliance-update_{context}"]
= Updating security content

Security content is included as container images that the `ProfileBundle` objects refer to. To accurately track updates to `ProfileBundles` and the custom resources parsed from the bundles such as rules or profiles, identify the container image with the compliance content using a digest instead of a tag:

[source,terminal]
----
$ oc -n openshift-compliance get profilebundles rhcos4 -oyaml
----

.Example output
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
  contentFile: ssg-rhcos4-ds.xml
  contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:900e... <1>
status:
  conditions:
  - lastTransitionTime: "2022-10-19T12:07:51Z"
    message: Profile bundle successfully parsed
    reason: Valid
    status: "True"
    type: Ready
  dataStreamStatus: VALID
----
<1>  Security container image.

Each `ProfileBundle` is backed by a deployment. When the Compliance Operator detects that the container image digest has changed, the deployment is updated to reflect the change and parse the content again. Using the digest instead of a tag ensures that you use a stable and predictable set of profiles.
