// Module included in the following assemblies:
//
// * microshift_networking/microshift-firewall.adoc

:_mod-docs-content-type: PROCEDURE
[id="microshift-firewall-install_{context}"]
= Installing the firewalld service

If you are using {op-system-ostree}, firewalld should be installed. To use the service, you can simply configure it. The following procedure can be used if you do not have firewalld, but want to use it.

Install and run the `firewalld` service for {microshift-short} by using the following steps.

.Procedure

. Optional: Check for firewalld on your system by running the following command:
+
[source,terminal]
----
$ rpm -q firewalld
----

. If the `firewalld` service is not installed, run the following command:
+
[source,terminal]
----
$ sudo dnf install -y firewalld
----

. To start the firewall, run the following command:
+
[source,terminal]
----
$ sudo systemctl enable firewalld --now
----

