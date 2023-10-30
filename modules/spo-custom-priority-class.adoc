// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-advanced.adoc

:_mod-docs-content-type: PROCEDURE
[id="spo-custom-priority-class_{context}"]
= Setting a custom priority class name for the spod daemon pod

The default priority class name of the `spod` daemon pod is set to `system-node-critical`. A custom priority class name can be configured in the `spod` configuration by setting a value in the `priorityClassName` field.

.Procedure

* Configure the priority class name by running the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles patch spod spod --type=merge -p '{"spec":{"priorityClassName":"my-priority-class"}}'
----
+
.Example output
[source,terminal]
----
securityprofilesoperatordaemon.openshift-security-profiles.x-k8s.io/spod patched
----