// Module included in the following assembly:
//
// jenkins/migrating-from-jenkins-to-openshift-pipelines.adoc

:_mod-docs-content-type: CONCEPT
[id="jt-comparison-of-jenkins-and-openshift-pipelines-concepts_{context}"]
= Comparison of Jenkins and {pipelines-shortname} concepts

You can review and compare the following equivalent terms used in Jenkins and {pipelines-shortname}.

== Jenkins terminology
Jenkins offers declarative and scripted pipelines that are extensible using shared libraries and plugins. Some basic terms in Jenkins are as follows:

* *Pipeline*: Automates the entire process of building, testing, and deploying applications by using link:https://groovy-lang.org/[Groovy] syntax.
* *Node*: A machine capable of either orchestrating or executing a scripted pipeline.
* *Stage*: A conceptually distinct subset of tasks performed in a pipeline. Plugins or user interfaces often use this block to display the status or progress of tasks.
* **Step**: A single task that specifies the exact action to be taken, either by using a command or a script.

== {pipelines-shortname} terminology
{pipelines-shortname} uses link:https://yaml.org/[YAML] syntax for declarative pipelines and consists of tasks. Some basic terms in {pipelines-shortname} are as follows:

* **Pipeline**: A set of tasks in a series, in parallel, or both.
* **Task**: A sequence of steps as commands, binaries, or scripts.
* **PipelineRun**: Execution of a pipeline with one or more tasks.
* **TaskRun**: Execution of a task with one or more steps.
+
[NOTE]
====
You can initiate a PipelineRun or a TaskRun with a set of inputs such as parameters and workspaces, and the execution results in a set of outputs and artifacts.
====
* **Workspace**: In {pipelines-shortname}, workspaces are conceptual blocks that serve the following purposes:

** Storage of inputs, outputs, and build artifacts.

** Common space to share data among tasks.

** Mount points for credentials held in secrets, configurations held in config maps, and common tools shared by an organization.

+
[NOTE]
====
In Jenkins, there is no direct equivalent of {pipelines-shortname} workspaces. You can think of the control node as a workspace, as it stores the cloned code repository, build history, and artifacts. When a job is assigned to a different node, the cloned code and the generated artifacts are stored in that node, but the control node maintains the build history.
====

== Mapping of concepts
The building blocks of Jenkins and {pipelines-shortname} are not equivalent, and a specific comparison does not provide a technically accurate mapping. The following terms and concepts in Jenkins and {pipelines-shortname} correlate in general:

.Jenkins and {pipelines-shortname} - basic comparison
[cols="1,1",options="header"]
|===
|Jenkins|{pipelines-shortname}
|Pipeline|Pipeline and PipelineRun
|Stage|Task
|Step|A step in a task
|===
