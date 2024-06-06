// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-setting-a-custom-default-certificate_{context}"]
= Setting a custom default certificate

As an administrator, you can configure an Ingress Controller to use a custom
certificate by creating a Secret resource and editing the `IngressController`
custom resource (CR).

.Prerequisites

* You must have a certificate/key pair in PEM-encoded files, where the
certificate is signed by a trusted certificate authority or by a private trusted
certificate authority that you configured in a custom PKI.

* Your certificate meets the following requirements:

** The certificate is valid for the ingress domain.

** The certificate uses the `subjectAltName` extension to specify a wildcard domain, such as `*.apps.ocp4.example.com`.

* You must have an `IngressController` CR. You may use the default one:
+
[source,terminal]
----
$ oc --namespace openshift-ingress-operator get ingresscontrollers
----
+
.Example output
[source,terminal]
----
NAME      AGE
default   10m
----

[NOTE]
====
If you have intermediate certificates, they must be included in the `tls.crt`
file of the secret containing a custom default certificate. Order matters when
specifying a certificate; list your intermediate certificate(s) after any server
certificate(s).
====

.Procedure

The following assumes that the custom certificate and key pair are in the
`tls.crt` and `tls.key` files in the current working directory. Substitute the
actual path names for `tls.crt` and `tls.key`. You also may substitute another
name for `custom-certs-default` when creating the Secret resource and
referencing it in the IngressController CR.

[NOTE]
====
This action will cause the Ingress Controller to be redeployed, using a rolling deployment strategy.
====

. Create a Secret resource containing the custom certificate in the
`openshift-ingress` namespace using the `tls.crt` and `tls.key` files.
+
[source,terminal]
----
$ oc --namespace openshift-ingress create secret tls custom-certs-default --cert=tls.crt --key=tls.key
----
+
. Update the IngressController CR to reference the new certificate secret:
+
[source,terminal]
----
$ oc patch --type=merge --namespace openshift-ingress-operator ingresscontrollers/default \
  --patch '{"spec":{"defaultCertificate":{"name":"custom-certs-default"}}}'
----
+
. Verify the update was effective:
+
[source,terminal]
----
$ echo Q |\
  openssl s_client -connect console-openshift-console.apps.<domain>:443 -showcerts 2>/dev/null |\
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
subject=C = US, ST = NC, L = Raleigh, O = RH, OU = OCP4, CN = *.apps.example.com
issuer=C = US, ST = NC, L = Raleigh, O = RH, OU = OCP4, CN = example.com
notAfter=May 10 08:32:45 2022 GM
----
+
[TIP]
====
You can alternatively apply the following YAML to set a custom default certificate:

[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  defaultCertificate:
    name: custom-certs-default
----
====
+
The certificate secret name should match the value used to update the CR.

Once the IngressController CR has been modified, the Ingress Operator
updates the Ingress Controller's deployment to use the custom certificate.
