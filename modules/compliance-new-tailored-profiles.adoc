// Module included in the following assemblies:
//
// * security/compliance_operator/co-scans/compliance-operator-tailor.adoc

:_mod-docs-content-type: PROCEDURE
[id="compliance-new-tailored-profiles_{context}"]
= Creating a new tailored profile

You can write a tailored profile from scratch by using the `TailoredProfile` object. Set an appropriate `title` and `description` and leave the `extends` field empty. Indicate to the Compliance Operator what type of scan this custom profile will generate:

* Node scan: Scans the Operating System.
* Platform scan: Scans the {product-title} configuration.

.Procedure

* Set the following annotation on the `TailoredProfile` object:

.Example `new-profile.yaml`
[source,yaml]
----
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: new-profile
  annotations:
    compliance.openshift.io/product-type: Node <1>
spec:
  extends: ocp4-cis-node <2>
  description: My custom profile <3>
  title: Custom profile <4>
  enableRules:
    - name: ocp4-etcd-unique-ca
      rationale: We really need to enable this
  disableRules:
    - name: ocp4-file-groupowner-cni-conf
      rationale: This does not apply to the cluster
----
<1> Set `Node` or `Platform` accordingly.
<2> The `extends` field is optional.
<3> Use the `description` field to describe the function of the new `TailoredProfile` object.
<4> Give your `TailoredProfile` object a title with the `title` field.
+
[NOTE]
====
Adding the `-node` suffix to the `name` field of the `TailoredProfile` object is similar to adding the `Node` product type annotation and generates an Operating System scan.
====