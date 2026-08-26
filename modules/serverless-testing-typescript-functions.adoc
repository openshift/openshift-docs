// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-typescript-functions.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-testing-typescript-functions_{context}"]
= Testing TypeScript functions

TypeScript functions can be tested locally on your computer. In the default project that is created when you create a function using `kn func create`, there is a *test* folder that contains some simple unit and integration tests.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function by using `kn func create`.

.Procedure

. If you have not previously run tests, install the dependencies first:
+
[source,terminal]
----
$ npm install
----

. Navigate to the *test* folder for your function.

. Run the tests:
+
[source,terminal]
----
$ npm test
----
