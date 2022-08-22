// Module is included in the following assemblies:
//
// * openshift-docs/cicd/gitops/configuring-a-cluster-to-use-gitops.adoc

[id="in-built-permissions_{context}"]
= In-built permissions for Argo CD

This section lists the permissions that are granted to ArgoCD to manage specific cluster-scoped resources which include cluster operators, optional OLM operators, and user management. Note that ArgoCD is not granted `cluster-admin` permissions.

.Permissions granted to Argo CD
|==========================
|Resource group|What it configures for a user or an administrator
|operators.coreos.com      |Optional operators managed by OLM   
|user.openshift.io, rbac.authorization.k8s.io |Groups, Users, and their permissions
|config.openshift.io       |Control plane operators managed by CVO used to configure cluster-wide build configuration, registry configuration, and scheduler policies  
|storage.k8s.io       |Storage
|console.openshift.io|Console customization
|==========================
