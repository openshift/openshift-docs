// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-advanced.adoc

:_mod-docs-content-type: PROCEDURE
[id="spo-log-enricher_{context}"]
= Using the log enricher

The Security Profiles Operator contains a log enrichment feature, which is disabled by default. The log enricher container runs with `privileged` permissions to read the audit logs from the local node. The log enricher runs within the host PID namespace, `hostPID`.

[IMPORTANT]
====
The log enricher must have permissions to read the host processes.
====

.Procedure

. Patch the `spod` configuration to enable the log enricher by running the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles patch spod spod \
    --type=merge -p '{"spec":{"enableLogEnricher":true}}'
----
+
.Example output
[source,terminal]
----
securityprofilesoperatordaemon.security-profiles-operator.x-k8s.io/spod patched
----
+
[NOTE]
====
The Security Profiles Operator will re-deploy the `spod` daemon set automatically.
====

. View the audit logs by running the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles logs -f ds/spod log-enricher
----
+
.Example output
[source,terminal]
----
I0623 12:51:04.257814 1854764 deleg.go:130] setup "msg"="starting component: log-enricher"  "buildDate"="1980-01-01T00:00:00Z" "compiler"="gc" "gitCommit"="unknown" "gitTreeState"="clean" "goVersion"="go1.16.2" "platform"="linux/amd64" "version"="0.4.0-dev"
I0623 12:51:04.257890 1854764 enricher.go:44] log-enricher "msg"="Starting log-enricher on node: 127.0.0.1"
I0623 12:51:04.257898 1854764 enricher.go:46] log-enricher "msg"="Connecting to local GRPC server"
I0623 12:51:04.258061 1854764 enricher.go:69] log-enricher "msg"="Reading from file /var/log/audit/audit.log"
2021/06/23 12:51:04 Seeked /var/log/audit/audit.log - &{Offset:0 Whence:2}
----