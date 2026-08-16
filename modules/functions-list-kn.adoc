// Module included in the following assemblies

// * /serverless/cli_tools/kn-func-ref.adoc

:_mod-docs-content-type: PROCEDURE
[id="functions-list-kn_{context}"]
= Listing existing functions

You can list existing functions by using `kn func list`. If you want to list functions that have been deployed as Knative services, you can also use `kn service list`.

.Procedure

* List existing functions:
+
[source,terminal]
----
$ kn func list [-n <namespace> -p <path>]
----
+
.Example output
[source,terminal]
----
NAME           NAMESPACE  RUNTIME  URL                                                                                      READY
example-function  default    node     http://example-function.default.apps.ci-ln-g9f36hb-d5d6b.origin-ci-int-aws.dev.rhcloud.com  True
----

* List functions deployed as Knative services:
+
[source,terminal]
----
$ kn service list -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME            URL                                                                                       LATEST                AGE   CONDITIONS   READY   REASON
example-function   http://example-function.default.apps.ci-ln-g9f36hb-d5d6b.origin-ci-int-aws.dev.rhcloud.com   example-function-gzl4c   16m   3 OK / 3     True
----
