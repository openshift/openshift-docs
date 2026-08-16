// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: CONCEPT
[id="op-disabling-the-service-monitor_{context}"]
= Disabling the service monitor

You can disable the service monitor, which is part of {pipelines-shortname}, to expose the telemetry data. To disable the service monitor, set the `enableMetrics` parameter to `false` in the `.spec.pipeline` specification of the `TektonConfig` custom resource (CR):

.Example
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    params:
       - name: enableMetrics
         value: 'false'
----


