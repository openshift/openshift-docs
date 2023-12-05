// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

:_mod-docs-content-type: PROCEDURE

[id="jt-migrating-from-jenkins-plugins-to-openshift-pipelines-hub-tasks_{context}"]
= Migrating from Jenkins plugins to Tekton Hub tasks

You can extend the capability of Jenkins by using link:https://plugins.jenkinsci.org[plugins]. To achieve similar extensibility in {pipelines-shortname}, use any of the tasks available from link:https://hub.tekton.dev[Tekton Hub].

For example, consider the link:https://hub.tekton.dev/tekton/task/git-clone[git-clone] task in Tekton Hub, which corresponds to the link:https://plugins.jenkins.io/git/[git plugin] for Jenkins.

.Example: `git-clone` task from Tekton Hub
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
 name: demo-pipeline
spec:
 params:
   - name: repo_url
   - name: revision
 workspaces:
   - name: source
 tasks:
   - name: fetch-from-git
     taskRef:
       name: git-clone
     params:
       - name: url
         value: $(params.repo_url)
       - name: revision
         value: $(params.revision)
     workspaces:
     - name: output
       workspace: source
----
