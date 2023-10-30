// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

:_mod-docs-content-type: PROCEDURE
[id="resolver-git-config-anon_{context}"]
= Configuring the Git resolver for anonymous Git cloning

If you want to use anonymous Git cloning, you can configure the default Git revision, fetch timeout, and default repository URL for pulling remote pipelines and tasks from a Git repository.

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----
. In the `TektonConfig` custom resource, edit the `pipeline.git-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    git-resolver-config:
      default-revision: main # <1>
      fetch-timeout: 1m # <2>
      default-url: https://github.com/tektoncd/catalog.git # <3>
----
<1> The default Git revision to use if none is specified.
<2> The maximum time any single Git clone resolution may take, for example, `1m`, `2s`, `700ms`. {pipelines-title} also enforces a global maximum timeout of 1 minute on all resolution requests.
<3> The default Git repository URL for anonymous cloning if none is specified.
