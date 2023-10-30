// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-python-functions.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-python-function-return-values_{context}"]
= Python function return values

Functions can return any value supported by link:https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses[Flask]. This is because the invocation framework proxies these values directly to the Flask server.

.Example
[source,python]
----
def main(context: Context):
    body = { "message": "Howdy!" }
    headers = { "content-type": "application/json" }
    return body, 200, headers
----

Functions can set both headers and response codes as secondary and tertiary response values from function invocation.

[id="serverless-python-function-return-values-returning-events_{context}"]
== Returning CloudEvents

Developers can use the `@event` decorator to tell the invoker that the function return value must be converted to a CloudEvent before sending the response.

.Example
[source,python]
----
@event("event_source"="/my/function", "event_type"="my.type")
def main(context):
    # business logic here
    data = do_something()
    # more data processing
    return data
----

This example sends a CloudEvent as the response value, with a type of `"my.type"` and a source of `"/my/function"`. The CloudEvent link:https://github.com/cloudevents/spec/blob/v1.0.1/spec.md#event-data[`data` property] is set to the returned `data` variable. The `event_source` and `event_type` decorator attributes are both optional.
