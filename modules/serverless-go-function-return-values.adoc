// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-go-functions.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-go-function-return-values_{context}"]
= Go function return values

Functions triggered by HTTP requests can set the response directly. You can configure the function to do this by using the Go link:https://golang.org/pkg/net/http/#ResponseWriter[http.ResponseWriter].

.Example HTTP response
[source,go]
----
func Handle(ctx context.Context, res http.ResponseWriter, req *http.Request) {
  // Set response
  res.Header().Add("Content-Type", "text/plain")
  res.Header().Add("Content-Length", "3")
  res.WriteHeader(200)
  _, err := fmt.Fprintf(res, "OK\n")
  if err != nil {
	fmt.Fprintf(os.Stderr, "error or response write: %v", err)
  }
}
----

Functions triggered by a cloud event might return nothing, `error`, or `CloudEvent` in order to push events into the Knative Eventing system. In this case, you must set a unique `ID`, proper `Source`, and a `Type` for the cloud event. The data can be populated from a defined structure, or from a `map`.

.Example CloudEvent response
[source,go]
----
func Handle(ctx context.Context, event cloudevents.Event) (resp *cloudevents.Event, err error) {
  // ...
  response := cloudevents.NewEvent()
  response.SetID("example-uuid-32943bac6fea")
  response.SetSource("purchase/getter")
  response.SetType("purchase")
  // Set the data from Purchase type
  response.SetData(cloudevents.ApplicationJSON, Purchase{
	CustomerId: custId,
	ProductId:  prodId,
  })
  // OR set the data directly from map
  response.SetData(cloudevents.ApplicationJSON, map[string]string{"customerId": custId, "productId": prodId})
  // Validate the response
  resp = &response
  if err = resp.Validate(); err != nil {
	fmt.Printf("invalid event created. %v", err)
  }
  return
}
----
