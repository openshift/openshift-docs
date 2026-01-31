// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: CONCEPT
[id="op-custom-parameter-expansion_{context}"]
= Custom parameter expansion

You can use {pac} to expand a custom parameter within your `PipelineRun` resource by using the `params` field. You can specify a value for the custom parameter inside the template of the `Repository` custom resource (CR). The specified value replaces the custom parameter in your pipeline run.

You can use custom parameters in the following scenarios:

* To define a URL parameter, such as a registry URL that varies based on a push or a pull request.
* To define a parameter, such as an account UUID that an administrator can manage without necessitating changes to the `PipelineRun` execution in the Git repository.

[NOTE]
====
Use the custom parameter expansion feature only when you cannot use the Tekton `PipelineRun` parameters because Tekton parameters are defined in a `Pipeline` resource and customized alongside it inside a Git repository. However, custom parameters are defined and customized where the `Repository` CR is located. So, you cannot manage your CI/CD pipeline from a single point.
====

The following example shows a custom parameter named `company` in the `Repository` CR:

[source,yaml]
----
...
spec:
  params:
    - name: company
      value: "ABC Company"
...
----

The value `ABC Company` replaces the parameter name `company` in your pipeline run and in the remotely fetched tasks.

You can also retrieve the value for a custom parameter from a Kubernetes secret, as shown in the following example:

[source,yaml]
----
...
spec:
  params:
    - name: company
      secretRef:
        name: my-secret
        key: companyname
...
----

{pac} parses and uses custom parameters in the following manner:

* If you have a `value` and a `secretRef` defined, {pac} uses the `value`.
* If you do not have a `name` in the `params` section, {pac} does not parse the parameter.
* If you have multiple `params` with the same `name`, {pac} uses the last parameter.

You can also define a custom parameter and use its expansion only when specified conditions were matched for a CEL filter. The following example shows a CEL filter applicable on a custom parameter named `company` when a pull request event is triggered:

[source,yaml]
----
...
spec:
  params:
    - name: company
      value: "ABC Company"
      filter:
        - name: event
          value: |
      pac.event_type == "pull_request"
...
----

[NOTE]
====
When you have multiple parameters with the same name and different filters, {pac} uses the first parameter that matches the filter. So, {pac} allows you to expand parameters according to different event types. For example, you can combine a push and a pull request event.
====
