// Module included in the following assemblies:
//
// * operators/operator_sdk/helm/osdk-helm-tutorial.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-helm-logic_{context}"]
= Understanding the Operator logic

For this example, the `nginx-operator` project executes the following reconciliation logic for each `Nginx` custom resource (CR):

* Create an Nginx deployment if it does not exist.
* Create an Nginx service if it does not exist.
* Create an Nginx ingress if it is enabled and does not exist.
* Ensure that the deployment, service, and optional ingress match the desired configuration as specified by the `Nginx` CR, for example the replica count, image, and service type.

By default, the `nginx-operator` project watches `Nginx` resource events as shown in the `watches.yaml` file and executes Helm releases using the specified chart:

[source,yaml]
----
# Use the 'create api' subcommand to add watches to this file.
- group: demo
  version: v1
  kind: Nginx
  chart: helm-charts/nginx
# +kubebuilder:scaffold:watch
----
