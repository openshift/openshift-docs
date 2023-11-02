// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="interfacing-pipelines-as-code-with-custom-certificates_{context}"]
= Interfacing {pac} with custom certificates

[role="_abstract"]
To configure {pac} with a Git repository that is accessible with a privately signed or custom certificate, you can expose the certificate to {pac}.

.Procedure

* If you have installed {pac} using the {pipelines-title} Operator, you can add your custom certificate to the cluster using the `Proxy` object. The Operator exposes the certificate in all {pipelines-title} components and workloads, including {pac}.

