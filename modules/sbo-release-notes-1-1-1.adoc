[id="sbo-release-notes-1-1-1_{context}"]
// Module included in the following assembly:
//
// * applications/connecting_applications_to_services/sbo-release-notes.adoc
:_mod-docs-content-type: REFERENCE
= Release notes for {servicebinding-title} 1.1.1

{servicebinding-title} 1.1.1 is now available on {product-title} 4.7, 4.8, 4.9, and 4.10.

[id="fixed-issues-1-1-1_{context}"]
== Fixed issues
* Before this update, a security vulnerability `CVE-2021-38561` was noted for {servicebinding-title} Helm chart. This update fixes the `CVE-2021-38561` error and updates the `golang.org/x/text` package from v0.3.6 to v0.3.7. link:https://issues.redhat.com/browse/APPSVC-1124[APPSVC-1124]

* Before this update, users of the Developer Sandbox did not have sufficient permissions to read `ClusterWorkloadResourceMapping` resources. As a result, {servicebinding-title} prevented all service bindings from being successful. With this update, the {servicebinding-title} now includes the appropriate role-based access control (RBAC) rules for any authenticated subject including the Developer Sandbox users. These RBAC rules allow the {servicebinding-title} to `get`, `list`, and `watch` the `ClusterWorkloadResourceMapping` resources for the Developer Sandbox users and to process service bindings successfully. link:https://issues.redhat.com/browse/APPSVC-1135[APPSVC-1135]

[id="known-issues-1-1-1_{context}"]
== Known issues
* There is currently a known issue with installing {servicebinding-title} in a single namespace installation mode. The absence of an appropriate namespace-scoped role-based access control (RBAC) rule prevents the successful binding of an application to a few known Operator-backed services that the {servicebinding-title} can automatically detect and bind to. When this happens, it generates an error message similar to the following example:
+
.Example error message
[source,text]
----
`postgresclusters.postgres-operator.crunchydata.com "hippo" is forbidden:
        User "system:serviceaccount:my-petclinic:service-binding-operator" cannot
        get resource "postgresclusters" in API group "postgres-operator.crunchydata.com"
        in the namespace "my-petclinic"`
----
+
Workaround 1: Install the {servicebinding-title} in the `all namespaces` installation mode. As a result, the appropriate cluster-scoped RBAC rule now exists and the binding succeeds.
+
Workaround 2: If you cannot install the {servicebinding-title} in the `all namespaces` installation mode, install the following role binding into the namespace where the {servicebinding-title} is installed:
+
.Example: Role binding for Crunchy Postgres Operator
[source,yaml]
----
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: service-binding-crunchy-postgres-viewer
subjects:
  - kind: ServiceAccount
    name: service-binding-operator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: service-binding-crunchy-postgres-viewer-role
----
link:https://issues.redhat.com/browse/APPSVC-1062[APPSVC-1062]

* Currently, when you modify the `ClusterWorkloadResourceMapping` resources, the {servicebinding-title} does not implement correct behavior. As a workaround, perform the following steps:
+
--
. Delete any `ServiceBinding` resources that use the corresponding `ClusterWorkloadResourceMapping` resource.
. Modify the `ClusterWorkloadResourceMapping` resource.
. Re-apply the `ServiceBinding` resources that you previously removed in step 1.
--
+
link:https://issues.redhat.com/browse/APPSVC-1102[APPSVC-1102]