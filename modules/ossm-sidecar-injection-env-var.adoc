// Module included in the following assemblies:
//
// * service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
// * service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-sidecar-injection-env-var_{context}"]
= Setting proxy environment variables through annotations

Configuration for the Envoy sidecar proxies is managed by the `ServiceMeshControlPlane`.

You can set environment variables for the sidecar proxy for applications by adding pod annotations to the deployment in the `injection-template.yaml` file. The environment variables are injected to the sidecar.

.Example injection-template.yaml
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource
spec:
  replicas: 7
  selector:
    matchLabels:
      app: resource
  template:
    metadata:
      annotations:
        sidecar.maistra.io/proxyEnv: "{ \"maistra_test_env\": \"env_value\", \"maistra_test_env_2\": \"env_value_2\" }"
----

[WARNING]
====
You should never include `maistra.io/` labels and annotations when creating your own custom resources.  These labels and annotations indicate that the resources are generated and managed by the Operator. If you are copying content from an Operator-generated resource when creating your own resources, do not include labels or annotations that start with `maistra.io/`.  Resources that include these labels or annotations will be overwritten or deleted by the Operator during the next reconciliation.
====
