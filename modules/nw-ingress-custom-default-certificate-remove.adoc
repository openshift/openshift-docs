// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-custom-default-certificate-remove_{context}"]
= Removing a custom default certificate

As an administrator, you can remove a custom certificate that you configured an Ingress Controller to use.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).
* You previously configured a custom default certificate for the Ingress Controller.

.Procedure

* To remove the custom certificate and restore the certificate that ships with {product-title}, enter the following command:
+
[source,terminal]
----
$ oc patch -n openshift-ingress-operator ingresscontrollers/default \
  --type json -p $'- op: remove\n  path: /spec/defaultCertificate'
----
+
There can be a delay while the cluster reconciles the new certificate configuration.

.Verification

* To confirm that the original cluster certificate is restored, enter the following command:
+
[source,terminal]
----
$ echo Q | \
  openssl s_client -connect console-openshift-console.apps.<domain>:443 -showcerts 2>/dev/null | \
  openssl x509 -noout -subject -issuer -enddate
----
+
where:
+
--
`<domain>`:: Specifies the base domain name for your cluster.
--
+
.Example output
[source,text]
----
subject=CN = *.apps.<domain>
issuer=CN = ingress-operator@1620633373
notAfter=May 10 10:44:36 2023 GMT
----
