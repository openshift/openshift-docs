// Ths module is included in the following assembly:
//
// *openshift_pipelines/working-with-pipelines-web-console.adoc

:_mod-docs-content-type: PROCEDURE
[id="op-interacting-with-pipelines-using-the-developer-perspective_{context}"]
= Interacting with pipelines using the Developer perspective

[role="_abstract"]
The *Pipelines* view in the *Developer* perspective lists all the pipelines in a project, along with the following details:

* The namespace in which the pipeline was created
* The last pipeline run
* The status of the tasks in the pipeline run
* The status of the pipeline run
* The creation time of the last pipeline run

[Discrete]
.Procedure
. In the *Pipelines* view of the *Developer* perspective, select a project from the *Project* drop-down list to see the pipelines in that project.
. Click the required pipeline to see the *Pipeline details* page.
+
By default, the *Details* tab displays a visual representation of all the `serial` tasks, `parallel` tasks, `finally` tasks, and `when` expressions in the pipeline. The tasks and the `finally` tasks are listed in the lower right portion of the page.
+
To view the task details, click the listed *Tasks* and *Finally* tasks. In addition, you can do the following:
+
* Use the zoom in, zoom out, fit to screen, and reset view features using the standard icons displayed in the lower left corner of the *Pipeline details* visualization.
* Change the zoom factor of the pipeline visualization using the mouse wheel.
* Hover over the tasks and see the task details.
+
.Pipeline details
image::op-pipeline-details1.png[Pipeline details]
+
. Optional: On the *Pipeline details* page, click the *Metrics* tab to see the following information about pipelines:
** *Pipeline Success Ratio*
** *Number of Pipeline Runs*
** *Pipeline Run Duration*
** *Task Run Duration*
+
You can use this information to improve the pipeline workflow and eliminate issues early in the pipeline lifecycle.
+
. Optional: Click the *YAML* tab to edit the YAML file for the pipeline.
. Optional: Click the *Pipeline Runs* tab to see the completed, running, or failed runs for the pipeline.
+
The *Pipeline Runs* tab provides details about the pipeline run, the status of the task, and a link to debug failed pipeline runs. Use the Options menu {kebab} to stop a running pipeline, to rerun a pipeline using the same parameters and resources as that of the previous pipeline execution, or to delete a pipeline run.
+
* Click the required pipeline run to see the *Pipeline Run details* page. By default, the *Details* tab displays a visual representation of all the serial tasks, parallel tasks, `finally` tasks, and when expressions in the pipeline run. The results for successful runs are displayed under the *Pipeline Run results* pane at the bottom of the page. Additionally, you would only be able to see tasks from Tekton Hub which are supported by the cluster. While looking at a task, you can click the link beside it to jump to the task documentation.
+
[NOTE]
====
The *Details* section of the *Pipeline Run Details* page displays a *Log Snippet* of the failed pipeline run. *Log Snippet* provides a general error message and a snippet of the log. A link to the *Logs* section provides quick access to the details about the failed run.
====
* On the *Pipeline Run details* page, click the *Task Runs* tab to see the completed, running, and failed runs for the task.
+
The *Task Runs* tab provides information about the task run along with the links to its task and pod, and also the status and duration of the task run. Use the Options menu {kebab} to delete a task run.
+
[NOTE]
====
The *TaskRuns* list page features a *Manage columns* button, which you can also use to add a *Duration* column.
====
* Click the required task run to see the *Task Run details* page. The results for successful runs are displayed under the *Task Run results* pane at the bottom of the page.
+
[NOTE]
====
The *Details* section of the *Task Run details* page displays a *Log Snippet* of the failed task run. *Log Snippet* provides a general error message and a snippet of the log. A link to the *Logs* section provides quick access to the details about the failed task run.
====
. Click the *Parameters* tab to see the parameters defined in the pipeline. You can also add or edit additional parameters, as required.
. Click the *Resources* tab to see the resources defined in the pipeline. You can also add or edit additional resources, as required.
