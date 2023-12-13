// Module is included in the following assemblies:
//
// * cicd/gitops/configuring-resource-quota.adoc

:_mod-docs-content-type: PROCEDURE
[id="configuring-workloads_{context}"]
= Configuring workloads with resource requests and limits

[role="_abstract"]
You can create Argo CD custom resource workloads with resource requests and limits. This is required when you want to deploy the Argo CD instance in a namespace that is configured with resource quotas.

The following Argo CD instance deploys the Argo CD workloads such as `Application Controller`, `ApplicationSet Controller`, `Dex`, `Redis`,`Repo Server`, and `Server` with resource requests and limits. You can also create the other workloads with resource requirements in the same manner.

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example
spec:
  server:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 125m
        memory: 128Mi
    route:
      enabled: true
  applicationSet:
    resources:
      limits:
        cpu: '2'
        memory: 1Gi
      requests:
        cpu: 250m
        memory: 512Mi
  repo:
    resources:
      limits:
        cpu: '1'
        memory: 512Mi
      requests:
        cpu: 250m
        memory: 256Mi
  dex:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 250m
        memory: 128Mi
  redis:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 250m
        memory: 128Mi
  controller:
    resources:
      limits:
        cpu: '2'
        memory: 2Gi
      requests:
        cpu: 250m
        memory: 1Gi
----

