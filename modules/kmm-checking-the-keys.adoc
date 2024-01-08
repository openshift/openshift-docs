// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: PROCEDURE
[id="kmm-checking-the-keys_{context}"]
= Checking the keys

After you have added the keys, you must check them to ensure they are set correctly.

.Procedure

. Check to ensure the public key secret is set correctly:
+
[source,terminal]
----
$ oc get secret -o yaml <certificate secret name> | awk '/cert/{print $2; exit}' | base64 -d  | openssl x509 -inform der -text
----
+
This should display a certificate with a Serial Number, Issuer, Subject, and more.

. Check to ensure the private key secret is set correctly:
+
[source,terminal]
----
$ oc get secret -o yaml <private key secret name> | awk '/key/{print $2; exit}' | base64 -d
----
+
This should display the key enclosed in the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.
