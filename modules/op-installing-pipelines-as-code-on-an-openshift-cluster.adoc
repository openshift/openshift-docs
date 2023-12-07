// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-pipelines-as-code-on-an-openshift-cluster_{context}"]
= Installing {pac} on an {product-title}

[role="_abstract"]
{pac} is installed in the `openshift-pipelines` namespace when you install the {pipelines-title} Operator. For more details, see _Installing {pipelines-shortname}_ in the _Additional resources_ section.

To disable the default installation of {pac} with the Operator, set the value of the `enable` parameter to `false` in the `TektonConfig` custom resource.

[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  platforms:
    openshift:
      pipelinesAsCode:
        enable: false
        settings:
          application-name: Pipelines as Code CI
          auto-configure-new-github-repo: "false"
          bitbucket-cloud-check-source-ip: "true"
          hub-catalog-name: tekton
          hub-url: https://api.hub.tekton.dev/v1
          remote-tasks: "true"
          secret-auto-create: "true"
# ...
----

Optionally, you can run the following command:

[source,terminal]
----
$ oc patch tektonconfig config --type="merge" -p '{"spec": {"platforms": {"openshift":{"pipelinesAsCode": {"enable": false}}}}}'
----

To enable the default installation of {pac} with the {pipelines-title} Operator, set the value of the `enable` parameter to `true` in the `TektonConfig` custom resource:

[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  platforms:
    openshift:
      pipelinesAsCode:
        enable: true
        settings:
          application-name: Pipelines as Code CI
          auto-configure-new-github-repo: "false"
          bitbucket-cloud-check-source-ip: "true"
          hub-catalog-name: tekton
          hub-url: https://api.hub.tekton.dev/v1
          remote-tasks: "true"
          secret-auto-create: "true"
# ...
----

Optionally, you can run the following command:

[source,terminal]
----
$ oc patch tektonconfig config --type="merge" -p '{"spec": {"platforms": {"openshift":{"pipelinesAsCode": {"enable": true}}}}}'
----
