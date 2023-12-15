// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-security.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-cert-manage-verify-cert_{context}"]
= Verifying your certificates

Use the Bookinfo sample application to verify that the workload certificates are signed by the certificates that were plugged into the CA. This process requires that you have `openssl` installed on your machine.

. To extract certificates from bookinfo workloads use the following command:
+
[source,terminal]
----
$ sleep 60
$ oc -n bookinfo exec "$(oc -n bookinfo get pod -l app=productpage -o jsonpath={.items..metadata.name})" -c istio-proxy -- openssl s_client -showcerts -connect details:9080 > bookinfo-proxy-cert.txt
$ sed -n '/-----BEGIN CERTIFICATE-----/{:start /-----END CERTIFICATE-----/!{N;b start};/.*/p}' bookinfo-proxy-cert.txt > certs.pem
$ awk 'BEGIN {counter=0;} /BEGIN CERT/{counter++} { print > "proxy-cert-" counter ".pem"}' < certs.pem
----
+
After running the command, you should have three files in your working directory: `proxy-cert-1.pem`, `proxy-cert-2.pem` and `proxy-cert-3.pem`.

. Verify that the root certificate is the same as the one specified by the administrator. Replace `<path>` with the path to your certificates.
+
[source,terminal]
----
$ openssl x509 -in <path>/root-cert.pem -text -noout > /tmp/root-cert.crt.txt
----
+
Run the following syntax at the terminal window.
+
[source,terminal]
----
$ openssl x509 -in ./proxy-cert-3.pem -text -noout > /tmp/pod-root-cert.crt.txt
----
+
Compare the certificates by running the following syntax at the terminal window.
+
[source,terminal]
----
$ diff -s /tmp/root-cert.crt.txt /tmp/pod-root-cert.crt.txt
----
+
You should see the following result:
`Files /tmp/root-cert.crt.txt and /tmp/pod-root-cert.crt.txt are identical`


. Verify that the CA certificate is the same as the one specified by the administrator. Replace `<path>` with the path to your certificates.
+
[source,terminal]
----
$ openssl x509 -in <path>/ca-cert.pem -text -noout > /tmp/ca-cert.crt.txt
----
Run the following syntax at the terminal window.
+
[source,terminal]
----
$ openssl x509 -in ./proxy-cert-2.pem -text -noout > /tmp/pod-cert-chain-ca.crt.txt
----
Compare the certificates by running the following syntax at the terminal window.
+
[source,terminal]
----
$ diff -s /tmp/ca-cert.crt.txt /tmp/pod-cert-chain-ca.crt.txt
----
You should see the following result:
`Files /tmp/ca-cert.crt.txt and /tmp/pod-cert-chain-ca.crt.txt are identical.`

. Verify the certificate chain from the root certificate to the workload certificate. Replace `<path>` with the path to your certificates.
+
[source,terminal]
----
$ openssl verify -CAfile <(cat <path>/ca-cert.pem <path>/root-cert.pem) ./proxy-cert-1.pem
----
You should see the following result:
`./proxy-cert-1.pem: OK`