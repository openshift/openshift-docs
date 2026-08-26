// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

:_mod-docs-content-type: CONCEPT
[id="serverless-quarkus-function-return-values_{context}"]
= Quarkus function return values

Functions can return an instance of any type from the list of permitted types. Alternatively, they can return the `Uni<T>` type, where the `<T>` type parameter can be of any type from the permitted types.

The `Uni<T>` type is useful if a function calls asynchronous APIs, because the returned object is serialized in the same format as the received object. For example:

* If a function receives an HTTP request, then the returned object is sent in the body of an HTTP response.

* If a function receives a `CloudEvent` object in binary encoding, then the returned object is sent in the data property of a binary-encoded `CloudEvent` object.

The following example shows a function that fetches a list of purchases:

.Example command
[source,java]
----
public class Functions {
    @Funq
    public List<Purchase> getPurchasesByName(String name) {
      // logic to retrieve purchases
    }
}
----

* Invoking this function through an HTTP request produces an HTTP response that contains a list of purchases in the body of the response.

* Invoking this function through an incoming `CloudEvent` object produces a `CloudEvent` response with a list of purchases in the `data` property.
