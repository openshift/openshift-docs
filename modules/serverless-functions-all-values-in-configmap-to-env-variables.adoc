// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-accessing-secrets-configmaps.adoc

[id="serverless-functions-all-values-in-configmap-to-env-variables_{context}"]
= Setting environment variables from all values defined in a config map

You can set an environment variable from all values defined in a config map. Values previously stored in a config map can then be accessed as environment variables by the function at runtime. This can be useful for simultaneously getting access to a collection of values stored in a config map, for example, a set of data pertaining to a user.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function.

.Procedure

. Open the `func.yaml` file for your function.

. For every config map for which you want to import all key-value pairs as environment variables, add the following YAML to the `envs` section:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- value: '{{ configMap:myconfigmap }}' <1>
----
<1> Substitute `myconfigmap` with the name of the target config map.
+
For example, to access all user data that is stored in `userdetailsmap`, use the following YAML:
+
[source,yaml]
----
name: test
namespace: ""
runtime: go
...
envs:
- value: '{{ configMap:userdetailsmap }}'
----

. Save the file.
