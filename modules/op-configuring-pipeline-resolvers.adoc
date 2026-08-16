// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: CONCEPT
[id="op-configuring-pipeline-resolvers_{context}"]
= Configuring pipeline resolvers

You can configure pipeline resolvers in the `TektonConfig` custom resource (CR). You can enable or disable these pipeline resolvers:

* `enable-bundles-resolver`
* `enable-cluster-resolver`
* `enable-git-resolver`
* `enable-hub-resolver`

.Example
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    enable-bundles-resolver: true
    enable-cluster-resolver: true
    enable-git-resolver: true
    enable-hub-resolver: true
----

You can also provide resolver specific configurations in the `TektonConfig` CR. For example, define the following fields in the `map[string]string` format to set configurations for each pipeline resolver:

.Example
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    bundles-resolver-config:
      default-service-account: pipelines
    cluster-resolver-config:
      default-namespace: test
    git-resolver-config:
      server-url: localhost.com
    hub-resolver-config:
      default-tekton-hub-catalog: tekton
----
