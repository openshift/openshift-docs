// Module is included in the following assemblies:
//
// * cicd/gitops/configuring-resource-quota.adoc

:_mod-docs-content-type: PROCEDURE
[id="patch-argocd-instance_{context}"]
= Patching Argo CD instance to update the resource requirements

[role="_abstract"]
You can update the resource requirements for all or any of the workloads post installation.

.Procedure
Update the `Application Controller` resource requests of an Argo CD instance in the Argo CD namespace.

[source,terminal]
----
oc -n argocd patch argocd example --type='json' -p='[{"op": "replace", "path": "/spec/controller/resources/requests/cpu", "value":"1"}]'

oc -n argocd patch argocd example --type='json' -p='[{"op": "replace", "path": "/spec/controller/resources/requests/memory", "value":"512Mi"}]'
----

