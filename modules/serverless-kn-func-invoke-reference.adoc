// Module included in the following assemblies:
//
// * serverless/reference/kn-func-ref.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-kn-func-invoke-reference_{context}"]
= kn func invoke optional parameters

You can specify optional parameters for the request by using the following `kn func invoke` CLI command flags.

[options="header",cols="1,3"]
|===
| Flags | Description
| `-t`, `--target` | Specifies the target instance of the invoked function, for example, `local` or `remote` or `https://staging.example.com/`. The default target is `local`.
| `-f`, `--format` | Specifies the format of the message, for example, `cloudevent` or `http`.
| `--id` | Specifies a unique string identifier for the request.
| `-n`, `--namespace` | Specifies the namespace on the cluster.
| `--source` | Specifies sender name for the request. This corresponds to the CloudEvent `source` attribute.
| `--type` | Specifies the type of request, for example, `boson.fn`. This corresponds to the CloudEvent `type` attribute.
| `--data` | Specifies content for the request. For CloudEvent requests, this is the CloudEvent `data` attribute.
| `--file` | Specifies path to a local file containing data to be sent.
| `--content-type` | Specifies the MIME content type for the request.
| `-p`, `--path` | Specifies path to the project directory.
| `-c`, `--confirm` | Enables prompting to interactively confirm all options.
| `-v`, `--verbose` | Enables printing verbose output.
| `-h`, `--help` | Prints information on usage of `kn func invoke`.
|===

[id="serverless-kn-func-invoke-main-parameters_{context}"]
== Main parameters

The following parameters define the main properties of the `kn func invoke` command:

Event target (`-t`, `--target`):: The target instance of the invoked function. Accepts the `local` value for a locally deployed function, the `remote` value for a remotely deployed function, or a URL for a function deployed to an arbitrary endpoint. If a target is not specified, it defaults to `local`.
Event message format (`-f`, `--format`):: The message format for the event, such as `http` or `cloudevent`. This defaults to the format of the template that was used when creating the function.
Event type (`--type`):: The type of event that is sent. You can find information about the `type` parameter that is set in the documentation for each event producer. For example, the API server source might set the `type` parameter of produced events as `dev.knative.apiserver.resource.update`.
Event source (`--source`):: The unique event source that produced the event. This might be a URI for the event source, for example `https://10.96.0.1/`, or the name of the event source.
Event ID (`--id`):: A random, unique ID that is created by the event producer.
Event data (`--data`):: Allows you to specify a `data` value for the event sent by the `kn func invoke` command. For example, you can specify a `--data` value such as `"Hello World"` so that the event contains this data string. By default, no data is included in the events created by `kn func invoke`.
+
[NOTE]
====
Functions that have been deployed to a cluster can respond to events from an existing event source that provides values for properties such as `source` and `type`. These events often have a `data` value in JSON format, which captures the domain specific context of the event. By using the CLI flags noted in this document, developers can simulate those events for local testing.
====
+
You can also send event data using the `--file` flag to provide a local file containing data for the event. In this case, specify the content type using `--content-type`.
Data content type (`--content-type`):: If you are using the `--data` flag to add data for events, you can use the `--content-type` flag to specify what type of data is carried by the event. In the previous example, the data is plain text, so you might specify `kn func invoke --data "Hello world!" --content-type "text/plain"`.

[id="serverless-kn-func-invoke-example-commands_{context}"]
== Example commands

This is the general invocation of the `kn func invoke` command:

[source,terminal]
----
$ kn func invoke --type <event_type> --source <event_source> --data <event_data> --content-type <content_type> --id <event_ID> --format <format> --namespace <namespace>
----

For example, to send a "Hello world!" event, you can run:

[source,terminal]
----
$ kn func invoke --type ping --source example-ping --data "Hello world!" --content-type "text/plain" --id example-ID --format http --namespace my-ns
----

[id="serverless-kn-func-invoke-example-commands-specifying-file-with-data_{context}"]
=== Specifying the file with data

To specify the file on disk that contains the event data, use the `--file` and `--content-type` flags:

[source,terminal]
----
$ kn func invoke --file <path> --content-type <content-type>
----

For example, to send JSON data stored in the `test.json` file, use this command:

[source,terminal]
----
$ kn func invoke --file ./test.json --content-type application/json
----

[id="serverless-kn-func-invoke-example-commands-specifying-function-project_{context}"]
=== Specifying the function project

You can specify a path to the function project by using the `--path` flag:

[source,terminal]
----
$ kn func invoke --path <path_to_function>
----

For example, to use the function project located in the `./example/example-function` directory, use this command:

[source,terminal]
----
$ kn func invoke --path ./example/example-function
----

[id="serverless-kn-func-invoke-example-commands-specifying-where-function-is-deployed_{context}"]
=== Specifying where the target function is deployed

By default, `kn func invoke` targets the local deployment of the function:

[source,terminal]
----
$ kn func invoke
----

To use a different deployment, use the `--target` flag:

[source,terminal]
----
$ kn func invoke --target <target>
----

For example, to use the function deployed on the cluster, use the `--target remote` flag:

[source,terminal]
----
$ kn func invoke --target remote
----

To use the function deployed at an arbitrary URL, use the `--target <URL>` flag:

[source,terminal]
----
$ kn func invoke --target "https://my-event-broker.example.com"
----

You can explicitly target the local deployment. In this case, if the function is not running locally, the command fails:

[source,terminal]
----
$ kn func invoke --target local
----
