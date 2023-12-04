// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-typescript-functions.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-typescript-functions-context-objects_{context}"]
= TypeScript context objects

To invoke a function, you provide a `context` object as the first parameter. Accessing properties of the `context` object can provide information about the incoming HTTP request.

.Example context object
[source,javascript]
----
function handle(context:Context): string
----

This information includes the HTTP request method, any query strings or headers sent with the request, the HTTP version, and the request body. Incoming requests that contain a `CloudEvent` attach the incoming instance of the CloudEvent to the context object so that it can be accessed by using `context.cloudevent`.

[id="serverless-typescript-functions-context-objects-methods_{context}"]
== Context object methods

The `context` object has a single method, `cloudEventResponse()`, that accepts a data value and returns a CloudEvent.

In a Knative system, if a function deployed as a service is invoked by an event broker sending a CloudEvent, the broker examines the response. If the response is a CloudEvent, this event is handled by the broker.

.Example context object method
[source,javascript]
----
// Expects to receive a CloudEvent with customer data
export function handle(context: Context, cloudevent?: CloudEvent): CloudEvent {
  // process the customer
  const customer = cloudevent.data;
  const processed = processCustomer(customer);
  return context.cloudEventResponse(customer)
    .source('/customer/process')
    .type('customer.processed')
    .response();
}
----

[id="serverless-typescript-functions-context-types_{context}"]
== Context types

The TypeScript type definition files export the following types for use in your functions.

.Exported type definitions
[source,javascript]
----
// Invokable is the expeted Function signature for user functions
export interface Invokable {
    (context: Context, cloudevent?: CloudEvent): any
}

// Logger can be used for structural logging to the console
export interface Logger {
  debug: (msg: any) => void,
  info:  (msg: any) => void,
  warn:  (msg: any) => void,
  error: (msg: any) => void,
  fatal: (msg: any) => void,
  trace: (msg: any) => void,
}

// Context represents the function invocation context, and provides
// access to the event itself as well as raw HTTP objects.
export interface Context {
    log: Logger;
    req: IncomingMessage;
    query?: Record<string, any>;
    body?: Record<string, any>|string;
    method: string;
    headers: IncomingHttpHeaders;
    httpVersion: string;
    httpVersionMajor: number;
    httpVersionMinor: number;
    cloudevent: CloudEvent;
    cloudEventResponse(data: string|object): CloudEventResponse;
}

// CloudEventResponse is a convenience class used to create
// CloudEvents on function returns
export interface CloudEventResponse {
    id(id: string): CloudEventResponse;
    source(source: string): CloudEventResponse;
    type(type: string): CloudEventResponse;
    version(version: string): CloudEventResponse;
    response(): CloudEvent;
}
----

[id="serverless-typescript-functions-context-objects-cloudevent-data_{context}"]
== CloudEvent data

If the incoming request is a CloudEvent, any data associated with the CloudEvent is extracted from the event and provided as a second parameter. For example, if a CloudEvent is received that contains a JSON string in its data property that is similar to the following:

[source,json]
----
{
  "customerId": "0123456",
  "productId": "6543210"
}
----

When invoked, the second parameter to the function, after the `context` object, will be a JavaScript object that has `customerId` and `productId` properties.

.Example signature
[source,javascript]
----
function handle(context: Context, cloudevent?: CloudEvent): CloudEvent
----

The `cloudevent` parameter in this example is a JavaScript object that contains the `customerId` and `productId` properties.
