// Module included in the following assemblies:
//
// * security/pod-vulnerability-scan.adoc

:_mod-docs-content-type: PROCEDURE
[id="security-pod-scan-query-cli_{context}"]
= Querying image vulnerabilities from the CLI

Using the `oc` command, you can display information about vulnerabilities detected by the {rhq-cso}.

.Prerequisites

* You have installed the {rhq-cso} on your {product-title} instance.

.Procedure

. Enter the following command to query for detected container image vulnerabilities:
+
[source,terminal]
----
$ oc get vuln --all-namespaces
----
+
.Example output
[source,terminal]
----
NAMESPACE     NAME              AGE
default       sha256.ca90...    6m56s
skynet        sha256.ca90...    9m37s
----

. To display details for a particular vulnerability, append the vulnerability name and its namespace to the `oc describe` command. The following example shows an active container whose image includes an RPM package with a vulnerability:
+
[source,terminal]
----
$ oc describe vuln --namespace mynamespace sha256.ac50e3752...
----
+
.Example output
[source,terminal]
----
Name:         sha256.ac50e3752...
Namespace:    quay-enterprise
...
Spec:
  Features:
    Name:            nss-util
    Namespace Name:  centos:7
    Version:         3.44.0-3.el7
    Versionformat:   rpm
    Vulnerabilities:
      Description: Network Security Services (NSS) is a set of libraries...
----
