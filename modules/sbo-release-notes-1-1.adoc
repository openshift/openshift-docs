[id="sbo-release-notes-1-1_{context}"]
// Module included in the following assembly:
//
// * applications/connecting_applications_to_services/sbo-release-notes.adoc
:_mod-docs-content-type: REFERENCE
= Release notes for {servicebinding-title} 1.1

{servicebinding-title} is now available on {product-title} 4.7, 4.8, 4.9, and 4.10.

[id="new-features-1-1_{context}"]
== New features
This section highlights what is new in {servicebinding-title} 1.1:

* Service Binding Options
** Workload resource mapping: Define exactly where binding data needs to be projected for the secondary workloads.
** Bind new workloads using a label selector.


[id="fixed-issues-1-1_{context}"]
== Fixed issues
* Before this update, service bindings that used label selectors to pick up workloads did not project service binding data into the new workloads that matched the given label selectors. As a result, the Service Binding Operator could not periodically bind such new workloads. With this update, service bindings now project service binding data into the new workloads that match the given label selector. The Service Binding Operator now periodically attempts to find and bind such new workloads. link:https://issues.redhat.com/browse/APPSVC-1083[APPSVC-1083]


[id="known-issues-1-1_{context}"]
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