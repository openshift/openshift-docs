// Module is included in the following assemblies:
//
// * cicd/gitops/configuring-resource-quota.adoc

:_mod-docs-content-type: PROCEDURE
[id="remove-resource-requirements_{context}"]
= Removing resource requests

[role="_abstract"]
You can also remove resource requirements for all or any of your workloads after installation.

.Procedure
Remove the `Application Controller` resource requests of an Argo CD instance in the Argo CD namespace.

[source,terminal]
----
oc -n argocd patch argocd example --type='json' -p='[{"op": "remove", "path": "/spec/controller/resources/requests/cpu"}]'

oc -n argocd argocd patch argocd example --type='json' -p='[{"op": "remove", "path": "/spec/controller/resources/requests/memory"}]'

----

