// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: CONCEPT
[id="kmm-debugging-and-troubleshooting_{context}"]
= Debugging and troubleshooting

If the kmods in your driver container are not signed or are signed with the wrong key, then the container can enter a `PostStartHookError` or `CrashLoopBackOff` status. You can verify by running the `oc describe` command on your container, which displays the following message in this scenario:

[source,terminal]
----
modprobe: ERROR: could not insert '<your_kmod_name>': Required key not available
----
