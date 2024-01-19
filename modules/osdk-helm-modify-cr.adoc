// Module included in the following assemblies:
//
// * operators/operator_sdk/helm/osdk-helm-tutorial.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-helm-modify-cr_{context}"]
= Modifying the custom resource spec

Helm uses a concept called link:https://helm.sh/docs/intro/using_helm/#customizing-the-chart-before-installing[values] to provide customizations to the defaults of a Helm chart, which are defined in the `values.yaml` file.

You can override these defaults by setting the desired values in the custom resource (CR) spec. You can use the number of replicas as an example.

.Procedure

. The `helm-charts/nginx/values.yaml` file has a value called `replicaCount` set to `1` by default. To have two Nginx instances in your deployment, your CR spec must contain `replicaCount: 2`.
+
Edit the `config/samples/demo_v1_nginx.yaml` file to set `replicaCount: 2`:
+
[source,yaml]
----
apiVersion: demo.example.com/v1
kind: Nginx
metadata:
  name: nginx-sample
...
spec:
...
  replicaCount: 2
----

. Similarly, the default service port is set to `80`. To use `8080`, edit the `config/samples/demo_v1_nginx.yaml` file to set `spec.port: 8080`,which adds the service port override:
+
[source,yaml]
----
apiVersion: demo.example.com/v1
kind: Nginx
metadata:
  name: nginx-sample
spec:
  replicaCount: 2
  service:
    port: 8080
----

The Helm Operator applies the entire spec as if it was the contents of a values file, just like the `helm install -f ./overrides.yaml` command.
