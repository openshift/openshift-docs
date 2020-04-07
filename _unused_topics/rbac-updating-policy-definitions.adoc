// Module included in the following assemblies:
//
// * orphaned

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
[id="updating-policy-definitions_{context}"]
= Updating policy definitions

During a cluster upgrade, and on every restart of any master, the
default cluster roles are automatically reconciled to restore any missing permissions.

If you customized default cluster roles and want to ensure a role reconciliation
does not modify them, you must take the following actions.

.Procedure

. Protect each role from reconciliation:
+
----
$ oc annotate clusterrole.rbac <role_name> --overwrite rbac.authorization.kubernetes.io/autoupdate=false
----
+
[WARNING]
====
You must manually update the roles that contain this setting to include any new
or required permissions after upgrading.
====

. Generate a default bootstrap policy template file:
+
----
$ oc adm create-bootstrap-policy-file --filename=policy.json
----
+
[NOTE]
====
The contents of the file vary based on the {product-title} version, but the file
contains only the default policies.
====

. Update the *_policy.json_* file to include any cluster role customizations.

. Use the policy file to automatically reconcile roles and role bindings that
are not reconcile protected:
+
----
$ oc auth reconcile -f policy.json
----

. Reconcile Security Context Constraints:
+
----
# oc adm policy reconcile-sccs \
    --additive-only=true \
    --confirm
----
endif::[]
