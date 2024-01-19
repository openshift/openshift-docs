// Snippet included in the following modules:
//
// * /modules/apiserversource-yaml.adoc
// * /modules/odc-creating-apiserversource.adoc
// * /modules/apiserversource-kn.adoc

:_mod-docs-content-type: SNIPPET

[NOTE]
====
If you want to re-use an existing service account, you can modify your existing `ServiceAccount` resource to include the required permissions instead of creating a new resource.
====

. Create a service account, role, and role binding for the event source as a YAML file:
+
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: events-sa
  namespace: default <1>

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: event-watcher
  namespace: default <1>
rules:
  - apiGroups:
      - ""
    resources:
      - events
    verbs:
      - get
      - list
      - watch

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: k8s-ra-event-watcher
  namespace: default <1>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: event-watcher
subjects:
  - kind: ServiceAccount
    name: events-sa
    namespace: default <1>
----
<1> Change this namespace to the namespace that you have selected for installing the event source.

. Apply the YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----
