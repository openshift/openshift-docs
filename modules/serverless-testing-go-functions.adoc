// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-typescript-functions.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-testing-go-functions_{context}"]
= Testing Go functions

Go functions can be tested locally on your computer. In the default project that is created when you create a function using `kn func create`, there is a `handle_test.go` file, which contains some basic tests. These tests can be extended as needed.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function by using `kn func create`.

.Procedure

. Navigate to the *test* folder for your function.

. Run the tests:
+
[source,terminal]
----
$ go test
----
