// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-nodejs-functions.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-nodejs-function-return-values_{context}"]
= Node.js function return values

Functions can return any valid JavaScript type or can have no return value. When a function has no return value specified, and no failure is indicated, the caller receives a `204 No Content` response.

Functions can also return a CloudEvent or a `Message` object in order to push events into the Knative Eventing system. In this case, the developer is not required to understand or implement the CloudEvent messaging specification. Headers and other relevant information from the returned values are extracted and sent with the response.

.Example
[source,javascript]
----
function handle(context, customer) {
  // process customer and return a new CloudEvent
  return new CloudEvent({
    source: 'customer.processor',
    type: 'customer.processed'
  })
}
----

[id="serverless-nodejs-function-return-values-headers_{context}"]
== Returning headers

You can set a response header by adding a `headers` property to the `return` object. These headers are extracted and sent with the response to the caller.

.Example response header
[source,javascript]
----
function handle(context, customer) {
  // process customer and return custom headers
  // the response will be '204 No content'
  return { headers: { customerid: customer.id } };
}
----

[id="serverless-nodejs-function-return-values-status-codes_{context}"]
== Returning status codes

You can set a status code that is returned to the caller by adding a `statusCode` property to the `return` object:

.Example status code
[source,javascript]
----
function handle(context, customer) {
  // process customer
  if (customer.restricted) {
    return { statusCode: 451 }
  }
}
----

Status codes can also be set for errors that are created and thrown by the function:

.Example error status code
[source,javascript]
----
function handle(context, customer) {
  // process customer
  if (customer.restricted) {
    const err = new Error(‘Unavailable for legal reasons’);
    err.statusCode = 451;
    throw err;
  }
}
----
