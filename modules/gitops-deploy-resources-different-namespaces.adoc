// Module included in the following assemblies:
//
// * cicd/gitops/setting-up-argocd-instance.adoc

:_mod-docs-content-type: PROCEDURE
[id="gitops-deploy-resources-different-namespaces_{context}"]
= Deploying resources to a different namespace

To allow Argo CD to manage resources in other namespaces apart from where it is installed, configure the target namespace with a `argocd.argoproj.io/managed-by` label.

.Procedure

* Configure the namespace:
+
[source,terminal]
----
$ oc label namespace <namespace> \
argocd.argoproj.io/managed-by=<namespace> <1>
----
<1> The namespace where Argo CD is installed.

