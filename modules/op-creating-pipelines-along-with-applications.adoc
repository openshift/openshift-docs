// This module is included in the following assembly:
//
// *openshift_pipelines/working-with-pipelines-web-console.adoc

:_mod-docs-content-type: CONCEPT
[id="op-creating-pipelines-along-with-applications_{context}"]
= Creating {pipelines-shortname} along with applications

[role="_abstract"]
To create pipelines along with applications, use the *From Git* option in the *Add+* view of the *Developer* perspective. You can view all of your available pipelines and select the pipelines you want to use to create applications while importing your code or deploying an image.

The Tekton Hub Integration is enabled by default and you can see tasks from the Tekton Hub that are supported by your cluster. Administrators can opt out of the Tekton Hub Integration and the Tekton Hub tasks will no longer be displayed. You can also check whether a webhook URL exists for a generated pipeline. Default webhooks are added for the pipelines that are created using the *+Add* flow and the URL is visible in the side panel of the selected resources in the Topology view.

[role="_additional-resources"]
For more information, see xref:../../applications/creating_applications/odc-creating-applications-using-developer-perspective.adoc#odc-importing-codebase-from-git-to-create-application_odc-creating-applications-using-developer-perspective[Creating applications using the Developer perspective].
