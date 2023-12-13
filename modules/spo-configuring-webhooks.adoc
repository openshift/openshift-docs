// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-advanced.adoc

:_mod-docs-content-type: PROCEDURE
[id="spo-configuring-webhooks_{context}"]
= Configuring webhooks

Profile binding and profile recording objects can use webhooks. Profile binding and recording object configurations are `MutatingWebhookConfiguration` CRs, managed by the Security Profiles Operator.

To change the webhook configuration, the `spod` CR exposes a `webhookOptions` field that allows modification of the `failurePolicy`, `namespaceSelector`, and `objectSelector` variables. This allows you to set the webhooks to "soft-fail" or restrict them to a subset of a namespaces so that even if the webhooks failed, other namespaces or resources are not affected.

.Procedure

. Set the `recording.spo.io` webhook configuration to record only pods labeled with `spo-record=true` by creating the following patch file:
+
[source,yaml]
----
spec:
  webhookOptions:
    - name: recording.spo.io
      objectSelector:
        matchExpressions:
          - key: spo-record
            operator: In
            values:
              - "true"
----

. Patch the `spod/spod` instance by running the following command:
+
[source,terminal]
----
$ oc -n openshift-security-profiles patch spod \
    spod -p $(cat /tmp/spod-wh.patch) --type=merge
----

. To view the resulting `MutatingWebhookConfiguration` object, run the following command:
+
[source,terminal]
----
$ oc get MutatingWebhookConfiguration \
    spo-mutating-webhook-configuration -oyaml
----