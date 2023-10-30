// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-yaml.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-functions-func-yaml-environment-variables_{context}"]
= Referencing local environment variables from func.yaml fields

If you want to avoid storing sensitive information such as an API key in the function configuration, you can add a reference to an environment variable available in the local environment. You can do this by modifying the `envs` field in the `func.yaml` file.

.Prerequisites

* You need to have the function project created.
* The local environment needs to contain the variable that you want to reference.

.Procedure

* To refer to a local environment variable, use the following syntax:
+
[source]
----
{{ env:ENV_VAR }}
----
+
Substitute `ENV_VAR` with the name of the variable in the local environment that you want to use.
+
For example, you might have the `API_KEY` variable available in the local environment. You can assign its value to the `MY_API_KEY` variable, which you can then directly use within your function:
+
.Example function
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- name: MY_API_KEY
  value: '{{ env:API_KEY }}'
...
----
