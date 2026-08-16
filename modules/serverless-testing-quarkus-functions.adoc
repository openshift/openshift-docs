// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-testing-quarkus-functions_{context}"]
= Testing Quarkus functions

Quarkus functions can be tested locally on your computer. In the default project that is created when you create a function using `kn func create`, there is the  `src/test/` directory, which contains basic Maven tests. These tests can be extended as needed.

.Prerequisites

* You have created a Quarkus function.
* You have installed the Knative (`kn`) CLI.

.Procedure

. Navigate to the project folder for your function.

. Run the Maven tests:
+
[source,terminal]
----
$ ./mvnw test
----
