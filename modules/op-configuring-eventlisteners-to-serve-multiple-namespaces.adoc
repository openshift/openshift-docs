// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="configuring-eventlisteners-to-serve-multiple-namespaces_{context}"]
= Configuring event listeners to serve multiple namespaces

[NOTE]
====
You can skip this section if you want to create a basic CI/CD pipeline. However, if your deployment strategy involves multiple namespaces, you can configure event listeners to serve multiple namespaces.
====

To increase reusability of `EvenListener` objects, cluster administrators can configure and deploy them as multi-tenant event listeners that serve multiple namespaces. 

[discrete]
.Procedure
. Configure cluster-wide fetch permission for the event listener.
.. Set a service account name to be used in the `ClusterRoleBinding` and `EventListener` objects. For example, `el-sa`.
+
.Example `ServiceAccount.yaml`
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: el-sa
---
----
.. In the `rules` section of the `ClusterRole.yaml` file, set appropriate permissions for every event listener deployment to function cluster-wide.
+
.Example `ClusterRole.yaml`
[source,yaml]
----
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: el-sel-clusterrole
rules:
- apiGroups: ["triggers.tekton.dev"]
  resources: ["eventlisteners", "clustertriggerbindings", "clusterinterceptors", "triggerbindings", "triggertemplates", "triggers"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["configmaps", "secrets"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["serviceaccounts"]
  verbs: ["impersonate"]
...
----
.. Configure cluster role binding with the appropriate service account name and cluster role name.
+
.Example `ClusterRoleBinding.yaml`
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: el-mul-clusterrolebinding
subjects:
- kind: ServiceAccount
  name: el-sa
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: el-sel-clusterrole
...
----

. In the `spec` parameter of the event listener, add the service account name, for example `el-sa`. Fill the `namespaceSelector` parameter with names of namespaces where event listener is intended to serve.
+
.Example `EventListener.yaml`
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: namespace-selector-listener
spec:
  serviceAccountName: el-sa
  namespaceSelector:
    matchNames:
    - default
    - foo
...
----

. Create a service account with the necessary permissions, for example `foo-trigger-sa`. Use it for role binding the triggers.
+
.Example `ServiceAccount.yaml`
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: foo-trigger-sa
  namespace: foo
...
----
+
.Example `RoleBinding.yaml`
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: triggercr-rolebinding
  namespace: foo
subjects:
- kind: ServiceAccount
  name: foo-trigger-sa
  namespace: foo
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: tekton-triggers-eventlistener-roles
...
----

. Create a trigger with the appropriate trigger template, trigger binding, and service account name.
+
.Example `Trigger.yaml`
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: Trigger
metadata:
  name: trigger
  namespace: foo
spec:
  serviceAccountName: foo-trigger-sa
  interceptors:
    - ref:
        name: "github"
      params:
        - name: "secretRef"
          value:
            secretName: github-secret
            secretKey: secretToken
        - name: "eventTypes"
          value: ["push"]
  bindings:
    - ref: vote-app
  template:
    ref: vote-app
...
----

