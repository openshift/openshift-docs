[id="sbo-release-notes-1-2_{context}"]
// Module included in the following assembly:
//
// * applications/connecting_applications_to_services/sbo-release-notes.adoc
:_mod-docs-content-type: REFERENCE
= Release notes for {servicebinding-title} 1.2

{servicebinding-title} 1.2 is now available on {product-title} 4.7, 4.8, 4.9, 4.10, and 4.11.

[id="new-features-1-2_{context}"]
== New features
This section highlights what is new in {servicebinding-title} 1.2:

* Enable {servicebinding-title} to consider optional fields in the annotations by setting the `optional` flag value to `true`.
* Support for `servicebinding.io/v1beta1` resources.
* Improvements to the discoverability of bindable services by exposing the relevant binding secret without requiring a workload to be present.

[id="known-issues-1-2_{context}"]
== Known issues
* Currently, when you install {servicebinding-title} on {product-title} 4.11, the memory footprint of {servicebinding-title} increases beyond expected limits. With low usage, however, the memory footprint stays within the expected ranges of your environment or scenarios. In comparison with {product-title} 4.10, under stress, both the average and maximum memory footprint increase considerably. This issue is evident in the previous versions of {servicebinding-title} as well. There is currently no workaround for this issue. link:https://issues.redhat.com/browse/APPSVC-1200[APPSVC-1200]

* By default, the projected files get their permissions set to 0644. {servicebinding-title} cannot set specific permissions due to a bug in Kubernetes that causes issues if the service expects specific permissions such as, `0600`. As a workaround, you can modify the code of the program or the application that is running inside a workload resource to copy the file to the `/tmp` directory and set the appropriate permissions. link:https://issues.redhat.com/browse/APPSVC-1127[APPSVC-1127]

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

* According to the specification, when you change the `ClusterWorkloadResourceMapping` resources, {servicebinding-title} must use the previous version of the `ClusterWorkloadResourceMapping` resource to remove the binding data that was being projected until now. Currently, when you change the `ClusterWorkloadResourceMapping` resources, the {servicebinding-title} uses the latest version of the `ClusterWorkloadResourceMapping` resource to remove the binding data. As a result, {the servicebinding-title} might remove the binding data incorrectly. As a workaround, perform the following steps:
+
--
. Delete any `ServiceBinding` resources that use the corresponding `ClusterWorkloadResourceMapping` resource.
. Modify the `ClusterWorkloadResourceMapping` resource.
. Re-apply the `ServiceBinding` resources that you previously removed in step 1.
--
+
link:https://issues.redhat.com/browse/APPSVC-1102[APPSVC-1102]