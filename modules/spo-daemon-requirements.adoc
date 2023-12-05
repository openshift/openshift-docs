// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-advanced.adoc

:_mod-docs-content-type: PROCEDURE
[id="spo-daemon-requirements_{context}"]
= Customizing daemon resource requirements

The default resource requirements of the daemon container can be adjusted by using the field `daemonResourceRequirements`
from the `spod` configuration.

.Procedure

* To specify the memory and cpu requests and limits of the daemon container, run the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles patch spod spod --type merge -p \
    '{"spec":{"daemonResourceRequirements": { \
    "requests": {"memory": "256Mi", "cpu": "250m"}, \
    "limits": {"memory": "512Mi", "cpu": "500m"}}}}'
----