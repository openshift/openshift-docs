// This module is included in the following assembly:
//
// *openshift-docs/cicd/pipelines/authenticating-pipelines-using-git-secret.adoc

[id="op-using-ssh-authentication-in-git-type-tasks_{context}"]
= Using SSH authentication in git type tasks

When invoking Git commands, you can use SSH authentication directly in the steps of a task. SSH authentication ignores the `$HOME` variable and only uses the user's home directory specified in the `/etc/passwd` file. So each step in a task must symlink the `/tekton/home/.ssh` directory to the home directory of the associated user.

However, explicit symlinks are not necessary when you use a pipeline resource of the `git` type, or the `git-clone` task available in the Tekton catalog.

As an example of using SSH authentication in `git` type tasks, refer to link:https://github.com/tektoncd/pipeline/blob/main/examples/v1beta1/taskruns/authenticating-git-commands.yaml[authenticating-git-commands.yaml].
