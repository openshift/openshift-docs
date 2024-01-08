// Module included in the following assemblies:
//
// * cicd/gitops/setting-up-argocd-instance.adoc

:_mod-docs-content-type: PROCEDURE
[id="gitops-enable-replicas-for-argo-cd-server_{context}"]
= Enabling replicas for Argo CD server and repo server

Argo CD-server and Argo CD-repo-server workloads are stateless. To better distribute your workloads among pods, you can increase the number of Argo CD-server and  Argo CD-repo-server replicas. However, if a horizontal autoscaler is enabled on the Argo CD-server, it overrides the number of replicas you set.

.Procedure

* Set the `replicas` parameters for the `repo` and `server` spec to the number of replicas you want to run:
+
.Example Argo CD custom resource

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: repo
spec:
  repo:
    replicas: <number_of_replicas>
  server:
    replicas: <number_of_replicas>
    route:
      enabled: true
      path: /
      tls:
        insecureEdgeTerminationPolicy: Redirect
        termination: passthrough
      wildcardPolicy: None
----