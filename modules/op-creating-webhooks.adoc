// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-webhooks_{context}"]
= Creating webhooks

_Webhooks_ are HTTP POST messages that are received by the event listeners whenever a configured event occurs in your repository. The event payload is then mapped to trigger bindings, and processed by trigger templates. The trigger templates eventually start one or more pipeline runs, leading to the creation and deployment of Kubernetes resources.

In this section, you will configure a webhook URL on your forked Git repositories `pipelines-vote-ui` and `pipelines-vote-api`. This URL points to the publicly accessible `EventListener` service route.

[NOTE]
====
Adding webhooks requires administrative privileges to the repository. If you do not have administrative access to your repository, contact your system administrator for adding webhooks.
====

[discrete]
.Procedure

. Get the webhook URL:
+
* For a secure HTTPS connection:
+
----
$ echo "URL: $(oc  get route el-vote-app --template='https://{{.spec.host}}')"
----
+
* For an HTTP (insecure) connection:
+
----
$ echo "URL: $(oc  get route el-vote-app --template='http://{{.spec.host}}')"
----
+
Note the URL obtained in the output.

. Configure webhooks manually on the front-end repository:

.. Open the front-end Git repository `pipelines-vote-ui` in your browser.
.. Click *Settings* -> *Webhooks* -> *Add Webhook*
.. On the *Webhooks/Add Webhook* page:
+
... Enter the webhook URL from step 1 in *Payload URL* field
... Select *application/json* for the *Content type*
... Specify the secret in the *Secret* field
... Ensure that the *Just the push event* is selected
... Select *Active*
... Click *Add Webhook*

. Repeat step 2 for the back-end repository `pipelines-vote-api`.
