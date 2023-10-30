// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: PROCEDURE
[id="op-configuring-pipelines-control-plane_{context}"]
= Configuring the {pipelines-title} control plane

You can customize the {pipelines-shortname} control plane by editing the configuration fields in the `TektonConfig` custom resource (CR). The {pipelines-title} Operator automatically adds the configuration fields with their default values so that you can use the {pipelines-shortname} control plane.

.Procedure

. In the *Administrator* perspective of the web console, navigate to *Administration* → *CustomResourceDefinitions*.

. Use the *Search by name* box to search for the `tektonconfigs.operator.tekton.dev` custom resource definition (CRD). Click *TektonConfig* to see the CRD details page.

. Click the *Instances* tab.

. Click the *config* instance to see the `TektonConfig` CR details.

. Click the *YAML* tab.

. Edit the `TektonConfig` YAML file based on your requirements.
+
.Example of `TektonConfig` CR with default values
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    running-in-environment-with-injected-sidecars: true
    metrics.taskrun.duration-type: histogram
    metrics.pipelinerun.duration-type: histogram
    await-sidecar-readiness: true
    params:
      - name: enableMetrics
        value: 'true'
    default-service-account: pipeline
    require-git-ssh-secret-known-hosts: false
    enable-tekton-oci-bundles: false
    metrics.taskrun.level: task
    metrics.pipelinerun.level: pipeline
    enable-api-fields: stable
    enable-provenance-in-status: false
    enable-custom-tasks: true
    disable-creds-init: false
    disable-affinity-assistant: true
----
