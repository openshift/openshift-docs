[id="gitops-uninstalling-keycloak_{context}"]
= Uninstalling Keycloak

You can delete the Keycloak resources and their relevant configurations by removing the `SSO` field from the Argo CD Custom Resource (CR) file. After you remove the `SSO` field, the values in the file look similar to the following:

[source,yaml]
----
  apiVersion: argoproj.io/v1alpha1
  kind: ArgoCD
  metadata:
    name: example-argocd
    labels:
      example: basic
  spec:
    server:
      route:
       enabled: true
----

[NOTE]
====
A Keycloak application created by using this method is currently not persistent. Additional configurations created in the Argo CD Keycloak realm are deleted when the server restarts.
====
