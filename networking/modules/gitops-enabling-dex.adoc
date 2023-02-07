// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift

[id="enabling-dex_{context}"]
= Enabling Dex

Argo CD embeds and bundles Dex as part of its installation. Dex is an identity service that uses OpenID Connect to drive authentication for other apps.

.Procedure

. Enable Dex by updating the `Subscription` resource for the OpenShift GitOps Operator.
+
[source,yaml]
----
spec:
  config:
    env:
    - name: DISABLE_DEX
      Value: "false"
----
+
This update causes the `argocd-cluster-dex-server` instance to run.

. To enable login with {product-title}, update the `argo-cd` custom resource by adding the following field: 
+
[source,yaml]
----
spec:
  dex:
    openShiftOAuth: true
----

. Enable role-based access control (RBAC) on `argo-cd` by modifying the following fields:
+
[source,yaml]
----
spec:
  dex:
    openShiftOAuth: true
  rbac:
    defaultPolicy: 'role:readonly'
    policy: |
      g, system:cluster-admins, role:admin
    scopes: '[groups]'
----
