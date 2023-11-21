// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-seccomp.adoc
// * security/security_profiles_operator/spo-selinux.adoc

:_mod-docs-content-type: CONCEPT
[id="spo-selinux-runasany_{context}"]

= About seLinuxContext: RunAsAny

Recording of SELinux policies is implemented with a webhook that injects a special SELinux type to the pods being recorded. The SELinux type makes the pod run in `permissive` mode, logging all the AVC denials into `audit.log`. By default, a workload is not allowed to run with a custom SELinux policy, but uses an auto-generated type.

To record a workload, the workload must use a service account that has permissions to use an SCC that allows the webhook to inject the permissive SELinux type. The `privileged` SCC contains `seLinuxContext: RunAsAny`.

In addition, the namespace must be labeled with `pod-security.kubernetes.io/enforce: privileged` if your cluster enables the link:https://kubernetes.io/docs/concepts/security/pod-security-admission/[Pod Security Admission] because only the `privileged` link:https://kubernetes.io/docs/concepts/security/pod-security-standards/#privileged[Pod Security Standard] allows using a custom SELinux policy.
