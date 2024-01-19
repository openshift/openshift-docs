// Module included in the following assemblies:
//
// * serverless/knative-serving/config-applications/serverless-configuration.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-config-emptydir_{context}"]
= Configuring the EmptyDir extension
// should probably be a procedure doc, but this is out of scope for the abstracts PR

The `kubernetes.podspec-volumes-emptydir` extension controls whether `emptyDir` volumes can be used with Knative Serving. To enable using `emptyDir` volumes, you must modify the `KnativeServing` custom resource (CR) to include the following YAML:

.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    features:
      kubernetes.podspec-volumes-emptydir: enabled
...
----
