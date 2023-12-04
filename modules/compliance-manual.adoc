// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-remediation.adoc

:_mod-docs-content-type: PROCEDURE
[id="compliance-manual_{context}"]
= Remediating a platform check manually

Checks for Platform scans typically have to be remediated manually by the administrator for two reasons:

* It is not always possible to automatically determine the value that must be set. One of the checks requires that a list of allowed registries is provided, but the scanner has no way of knowing which registries the organization wants to allow.

* Different checks modify different API objects, requiring automated remediation to possess `root` or superuser access to modify objects in the cluster, which is not advised.

.Procedure
. The example below uses the `ocp4-ocp-allowed-registries-for-import` rule, which would fail on a default {product-title} installation. Inspect the rule `oc get rule.compliance/ocp4-ocp-allowed-registries-for-import -oyaml`, the rule is to limit the registries the users are allowed to import images from by setting the `allowedRegistriesForImport` attribute, The _warning_ attribute of the rule also shows the API object checked, so it can be modified and remediate the issue:
+
[source,terminal]
----
$ oc edit image.config.openshift.io/cluster
----
+
.Example output
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  annotations:
    release.openshift.io/create-only: "true"
  creationTimestamp: "2020-09-10T10:12:54Z"
  generation: 2
  name: cluster
  resourceVersion: "363096"
  selfLink: /apis/config.openshift.io/v1/images/cluster
  uid: 2dcb614e-2f8a-4a23-ba9a-8e33cd0ff77e
spec:
  allowedRegistriesForImport:
  - domainName: registry.redhat.io
status:
  externalRegistryHostnames:
  - default-route-openshift-image-registry.apps.user-cluster-09-10-12-07.devcluster.openshift.com
  internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
----

. Re-run the scan:
+
[source,terminal]
----
$ oc -n openshift-compliance \
annotate compliancescans/rhcos4-e8-worker compliance.openshift.io/rescan=
----
