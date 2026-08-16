// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: CONCEPT
[id="op-disabling-the-integretion-of-tekton-hub_{context}"]
= Disabling the integration of {tekton-hub}

You can disable the integration of {tekton-hub} in the web console *Developer* perspective by setting the `enable-devconsole-integration` parameter to `false` in the `TektonConfig` custom resource (CR).

.Example of disabling {tekton-hub}

[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  hub:
    params:
      - name: enable-devconsole-integration
        value: false
----
