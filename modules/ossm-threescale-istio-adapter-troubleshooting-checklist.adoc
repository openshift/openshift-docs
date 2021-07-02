// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="ossm-threescale-istio-adapter-troubleshooting-checklist_{context}"]
= 3scale Istio adapter troubleshooting checklist

As the administrator installing the 3scale Istio adapter, there are a number of scenarios that might be causing your integration to not function properly. Use the following list to troubleshoot your installation:

* Incorrect YAML indentation.
* Missing YAML sections.
* Forgot to apply the changes in the YAML to the cluster.
* Forgot to label the service workloads with the `service-mesh.3scale.net/credentials` key.
* Forgot to label the service workloads with `service-mesh.3scale.net/service-id` when using handlers that do not contain a `service_id` so they are reusable per account.
* The _Rule_ custom resource points to the wrong handler or instance custom resources, or the references lack the corresponding namespace suffix.
* The _Rule_ custom resource `match` section cannot possibly match the service you are configuring, or it points to a destination workload that is not currently running or does not exist.
* Wrong access token or URL for the 3scale Admin Portal in the handler.
* The _Instance_ custom resource's `params/subject/properties` section fails to list the right parameters for `app_id`, `app_key`, or `client_id`, either because they specify the wrong location such as the query parameters, headers, and authorization claims, or the parameter names do not match the requests used for testing.
* Failing to use the configuration generator without realizing that it actually lives in the adapter container image and needs `oc exec` to invoke it.
