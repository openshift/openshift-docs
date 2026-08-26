// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: CONCEPT
[id="op-changing-default-service-account_{context}"]
= Changing the default service account for {pipelines-shortname}

You can change the default service account for {pipelines-shortname} by editing the `default-service-account` field in the `.spec.pipeline` and `.spec.trigger` specifications. The default service account name is `pipeline`.

.Example
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    default-service-account: pipeline
  trigger:
    default-service-account: pipeline
    enable-api-fields: stable
----
