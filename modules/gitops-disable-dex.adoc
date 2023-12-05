// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-using-dex

:_mod-docs-content-type: PROCEDURE
[id="gitops-disable-dex_{context}"]
= Disabling Dex

Dex is installed by default for all the Argo CD instances created by the Operator. You can configure {gitops-title} to use Dex as the SSO authentication provider by setting the `.spec.dex` parameter.

[IMPORTANT]
====
In {gitops-title} v1.6.0, `DISABLE_DEX` is deprecated and is planned to be removed in {gitops-title} v1.10.0. Consider using the `.spec.sso.dex` parameter instead. See "Enabling or disabling Dex using .spec.sso".
====

.Procedure

* Set the environmental variable `DISABLE_DEX` to `true` in the YAML resource of the Operator:
+
[source,yaml]
----
...
spec:
  config:
    env:
    - name: DISABLE_DEX
      value: "true"
...
----