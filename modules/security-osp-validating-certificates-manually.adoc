// This is included in the following assemblies:
//
// * installing/installing_openstack/preparing-to-install-on-openstack.adoc

:_mod-docs-content-type: PROCEDURE
[id="security-osp-validating-certificates-manually_{context}"]
= Scanning {rh-openstack} endpoints for legacy HTTPS certificates manually

Beginning with {product-title} 4.10, HTTPS certificates must contain subject alternative name (SAN) fields. If you do not have access to the prerequisite tools that are listed in "Scanning {rh-openstack} endpoints for legacy HTTPS certificates", perform the following steps to scan each HTTPS endpoint in a {rh-openstack-first} catalog for legacy certificates that only contain the `CommonName` field.

[IMPORTANT]
====
{product-title} does not check the underlying {rh-openstack} infrastructure for legacy certificates prior to installation or updates. Use the following steps to check for these certificates yourself. Failing to update legacy certificates prior to installing or updating a cluster will result in cluster dysfunction.
====

.Procedure

. On a command line, run the following command to view the URL of {rh-openstack} public endpoints:
+
[source,terminal]
----
$ openstack catalog list
----
+
Record the URL for each HTTPS endpoint that the command returns.
. For each public endpoint, note the host and the port.
+
[TIP]
====
Determine the host of an endpoint by removing the scheme, the port, and the path.
====

. For each endpoint, run the following commands to extract the SAN field of the certificate:
.. Set a `host` variable:
+
[source,terminal]
----
$ host=<host_name>
----
.. Set a `port` variable:
+
[source,terminal]
----
$ port=<port_number>
----
+
If the URL of the endpoint does not have a port, use the value `443`.
.. Retrieve the SAN field of the certificate:
+
[source,terminal]
----
$ openssl s_client -showcerts -servername "$host" -connect "$host:$port" </dev/null 2>/dev/null \
    | openssl x509 -noout -ext subjectAltName
----
+
.Example output
[source,terminal]
----
X509v3 Subject Alternative Name:
    DNS:your.host.example.net
----
+
For each endpoint, look for output that resembles the previous example. If there is no output for an endpoint, the certificate of that endpoint is invalid and must be re-issued.

[IMPORTANT]
====
You must replace all legacy HTTPS certificates before you install {product-title} 4.10 or update a cluster to that version. Legacy certificates are rejected with the following message:

[source,txt]
----
x509: certificate relies on legacy Common Name field, use SANs instead
----
====
