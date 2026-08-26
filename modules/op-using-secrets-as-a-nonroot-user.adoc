// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-using-secrets-as-a-nonroot-user_{context}"]
= Using secrets as a non-root user

You might need to use secrets as a non-root user in certain scenarios, such as:

* The users and groups that the containers use to execute runs are randomized by the platform.
* The steps in a task define a non-root security context.
* A task specifies a global non-root security context, which applies to all steps in a task.

In such scenarios, consider the following aspects of executing task runs and pipeline runs as a non-root user:

* SSH authentication for Git requires the user to have a valid home directory configured in the `/etc/passwd` directory. Specifying a UID that has no valid home directory results in authentication failure.
* SSH authentication ignores the `$HOME` environment variable. So you must or symlink the appropriate secret files from the `$HOME` directory defined by {pipelines-shortname} (`/tekton/home`), to the non-root user's valid home directory.

In addition, to configure SSH authentication in a non-root security context, refer to the link:https://github.com/tektoncd/pipeline/blob/main/examples/v1beta1/taskruns/authenticating-git-commands.yaml[example for authenticating git commands].
