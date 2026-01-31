// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-advanced.adoc

:_mod-docs-content-type: PROCEDURE
[id="spo-restrict-syscalls_{context}"]
= Restrict the allowed syscalls in seccomp profiles

The Security Profiles Operator does not restrict `syscalls` in `seccomp` profiles by default. You can define the list of allowed `syscalls` in the `spod` configuration.

.Procedure

* To define the list of `allowedSyscalls`, adjust the `spec` parameter by running the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles patch spod spod --type merge \
    -p '{"spec":{"allowedSyscalls": ["exit", "exit_group", "futex", "nanosleep"]}}'
----

[IMPORTANT]
====
The Operator will install only the `seccomp` profiles, which have a subset of `syscalls` defined into the allowed list. All profiles not complying with this ruleset are rejected.

When the list of allowed `syscalls` is modified in the `spod` configuration, the Operator will identify the already installed profiles which are non-compliant and remove them automatically.
====