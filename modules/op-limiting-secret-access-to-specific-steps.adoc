// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-limiting-secret-access-to-specific-steps_{context}"]
= Limiting secret access to specific steps

By default, the secrets for {pipelines-shortname} are stored in the `$HOME/tekton/home` directory, and are available for all the steps in a task.

To limit a secret to specific steps, use the secret definition to specify a volume, and mount the volume in specific steps.
