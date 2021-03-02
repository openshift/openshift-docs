// Module included in the following assemblies:
//
// * operators/operator_sdk/helm/osdk-helm-support.adoc

[id="osdk-helm-charts_{context}"]
= Helm charts

One of the Operator SDK options for generating an Operator project includes leveraging an existing Helm chart to deploy Kubernetes resources as a unified application, without having to write any Go code. Such Helm-based Operators are designed to excel at stateless applications that require very little logic when rolled out, because changes should be applied to the Kubernetes objects that are generated as part of the chart. This may sound limiting, but can be sufficient for a surprising amount of use-cases as shown by the proliferation of Helm charts built by the Kubernetes community.

The main function of an Operator is to read from a custom object that represents your application instance and have its desired state match what is running. In the case of a Helm-based Operator, the `spec` field of the object is a list of configuration options that are typically described in the Helm `values.yaml` file. Instead of setting these values with flags using the Helm CLI (for example, `helm install -f values.yaml`), you can express them within a custom resource (CR), which, as a native Kubernetes object, enables the benefits of RBAC applied to it and an audit trail.

For an example of a simple CR called `Tomcat`:

[source,yaml]
----
apiVersion: apache.org/v1alpha1
kind: Tomcat
metadata:
  name: example-app
spec:
  replicaCount: 2
----

The `replicaCount` value, `2` in this case, is propagated into the template of the chart where the following is used:

[source,yaml]
----
{{ .Values.replicaCount }}
----

After an Operator is built and deployed, you can deploy a new instance of an app by creating a new instance of a CR, or list the different instances running in all environments using the `oc` command:

[source,terminal]
----
$ oc get Tomcats --all-namespaces
----

There is no requirement use the Helm CLI or install Tiller; Helm-based Operators import code from the Helm project. All you have to do is have an instance of the Operator running and register the CR with a custom resource definition (CRD). Because it obeys RBAC, you can more easily prevent production changes.
