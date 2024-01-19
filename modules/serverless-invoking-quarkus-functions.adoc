// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

:_mod-docs-content-type: CONCEPT
[id="serverless-invoking-quarkus-functions_{context}"]
= About invoking Quarkus functions

You can create a Quarkus project that responds to cloud events, or one that responds to simple HTTP requests. Cloud events in Knative are transported over HTTP as a POST request, so either function type can listen and respond to incoming HTTP requests.

When an incoming request is received, Quarkus functions are invoked with an instance of a permitted type.

.Function invocation options
[options="header",cols="d,d,m"]
|====
|Invocation method |Data type contained in the instance |Example of data
|HTTP POST request | JSON object in the body of the request |`{ "customerId": "0123456", "productId": "6543210" }`
|HTTP GET request | Data in the query string |`?customerId=0123456&productId=6543210`
|`CloudEvent` | JSON object in the `data` property |`{ "customerId": "0123456", "productId": "6543210" }`
|====

The following example shows a function that receives and processes the `customerId` and `productId` purchase data that is listed in the previous table:

.Example Quarkus function
[source,java]
----
public class Functions {
    @Funq
    public void processPurchase(Purchase purchase) {
        // process the purchase
    }
}
----

The corresponding `Purchase` JavaBean class that contains the purchase data looks as follows:

.Example class
[source,java]
----
public class Purchase {
    private long customerId;
    private long productId;
    // getters and setters
}
----

[id="serverless-invoking-quarkus-functions-examples_{context}"]
== Invocation examples

The following example code defines three functions named `withBeans`, `withCloudEvent`, and `withBinary`;

.Example
[source,java]
----
import io.quarkus.funqy.Funq;
import io.quarkus.funqy.knative.events.CloudEvent;

public class Input {
    private String message;

    // getters and setters
}

public class Output {
    private String message;

    // getters and setters
}

public class Functions {
    @Funq
    public Output withBeans(Input in) {
        // function body
    }

    @Funq
    public CloudEvent<Output> withCloudEvent(CloudEvent<Input> in) {
        // function body
    }

    @Funq
    public void withBinary(byte[] in) {
        // function body
    }
}
----

The `withBeans` function of the `Functions` class can be invoked by:

* An HTTP POST request with a JSON body:
+
[source,terminal]
----
$ curl "http://localhost:8080/withBeans" -X POST \
    -H "Content-Type: application/json" \
    -d '{"message": "Hello there."}'
----
* An HTTP GET request with query parameters:
+
[source,terminal]
----
$ curl "http://localhost:8080/withBeans?message=Hello%20there." -X GET
----
* A `CloudEvent` object in binary encoding:
+
[source,terminal]
----
$ curl "http://localhost:8080/" -X POST \
  -H "Content-Type: application/json" \
  -H "Ce-SpecVersion: 1.0" \
  -H "Ce-Type: withBeans" \
  -H "Ce-Source: cURL" \
  -H "Ce-Id: 42" \
  -d '{"message": "Hello there."}'
----
* A `CloudEvent` object in structured encoding:
+
[source,terminal]
----
$ curl http://localhost:8080/ \
    -H "Content-Type: application/cloudevents+json" \
    -d '{ "data": {"message":"Hello there."},
          "datacontenttype": "application/json",
          "id": "42",
          "source": "curl",
          "type": "withBeans",
          "specversion": "1.0"}'
----

The `withCloudEvent` function of the `Functions` class can be invoked by using a `CloudEvent` object, similarly to the `withBeans` function. However, unlike `withBeans`, `withCloudEvent` cannot be invoked with a plain HTTP request.

The `withBinary` function of the `Functions` class can be invoked by:

* A `CloudEvent` object in binary encoding:
+
[source]
----
$ curl "http://localhost:8080/" -X POST \
  -H "Content-Type: application/octet-stream" \
  -H "Ce-SpecVersion: 1.0"\
  -H "Ce-Type: withBinary" \
  -H "Ce-Source: cURL" \
  -H "Ce-Id: 42" \
  --data-binary '@img.jpg'
----
* A `CloudEvent` object in structured encoding:
+
[source]
----
$ curl http://localhost:8080/ \
  -H "Content-Type: application/cloudevents+json" \
  -d "{ \"data_base64\": \"$(base64 --wrap=0 img.jpg)\",
        \"datacontenttype\": \"application/octet-stream\",
        \"id\": \"42\",
        \"source\": \"curl\",
        \"type\": \"withBinary\",
        \"specversion\": \"1.0\"}"
----
