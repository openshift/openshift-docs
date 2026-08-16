// Ths module is included in the following assembly:
//
// *cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

:_mod-docs-content-type: CONCEPT
[id="op-configuring-pull-request-capabilities-in-GitHub-interceptor_{context}"]
= Configuring pull request capabilities in GitHub Interceptor

With GitHub Interceptor, you can create logic that validates and filters GitHub webhooks. For example, you can validate the webhook’s origin and filter incoming events based on specified criteria. When you use GitHub Interceptor to filter event data, you can specify the event types that Interceptor can accept in a field.
In {pipelines-title}, you can use the following capabilities of GitHub Interceptor:

* Filter pull request events based on the files that have been changed
* Validate pull requests based on configured GitHub owners
