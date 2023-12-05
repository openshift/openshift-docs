// Module included in the following assemblies:
//
// * microshift/microshift-things-to-know.adoc

:_mod-docs-content-type: CONCEPT
[id="microshift-certificate-lifetime_{context}"]
= Security certificate lifetime

{microshift-short} certificates are separated into two basic groups:

. Short-lived certificates having certificate validity of one year.
. Long-lived certificates having certificate validity of 10 years.

Most server or leaf certificates are short-term.

An example of a long-lived certificate is the client certificate for `system:admin user` authentication, or the certificate of the signer of the `kube-apiserver` external serving certificate.

[id="microshift-certificate-rotation_{context}"]
== Certificate rotation
Certificates that are expired or close to their expiration dates need to be rotated to ensure continued {microshift-short} operation. When {microshift-short} restarts for any reason, certificates that are close to expiring are rotated. A certificate that is set to expire imminently, or has expired, can cause an automatic {microshift-short} restart to perform a rotation.

[NOTE]
====
If the rotated certificate is a Certificate Authority, all of the certificates it signed rotate.
====

[id="microshift-st-certificate-rotation_{context}"]
=== Short-term certificates
The following situations describe {microshift-short} actions during short-term certificate lifetimes:

. No rotation:
.. When a short-term certificate is up to 5 months old, no rotation occurs.

. Rotation at restart:
.. When a short-term certificate is 5 to 8 months old, it is rotated when {microshift-short} starts or restarts.

. Automatic restart for rotation:
.. When a short-term certificate is more than 8 months old, {microshift-short} can automatically restart to rotate and apply a new certificate.

[id="microshift-lt-certificate-rotation_{context}"]
=== Long-term certificates
The following situations describe {microshift-short} actions during long-term certificate lifetimes:

. No rotation:
.. When a long-term certificate is up to 8.5 years old, no rotation occurs.

. Rotation at restart:
.. When a long-term certificate is 8.5 to 9 years old, it is rotated when {microshift-short} starts or restarts.

. Automatic restart for rotation:
.. When a long-term certificate is more than 9 years old, {microshift-short} can automatically restart to rotate and apply a new certificate.
