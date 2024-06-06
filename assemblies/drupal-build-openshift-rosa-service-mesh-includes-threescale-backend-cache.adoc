// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

[id="threescale-backend-cache_{context}"]
= 3scale backend cache

The 3scale backend cache provides an authorization and reporting cache for clients of the 3scale Service Management API. This cache is embedded in the adapter to enable lower latencies in responses in certain situations assuming the administrator is willing to accept the trade-offs.

[NOTE]
====
3scale backend cache is disabled by default. 3scale backend cache functionality trades inaccuracy in rate limiting and potential loss of hits since the last flush was performed for low latency and higher consumption of resources in the processor and memory.
====

== Advantages of enabling backend cache

The following are advantages to enabling the backend cache:

* Enable the backend cache when you find latencies are high while accessing services managed by the 3scale Istio Adapter.
* Enabling the backend cache will stop the adapter from continually checking with the 3scale API manager for request authorizations, which will lower the latency.
** This creates an in-memory cache of 3scale authorizations for the 3scale Istio Adapter to store and reuse before attempting to contact the 3scale API manager for authorizations. Authorizations will then take much less time to be granted or denied.
* Backend caching is useful in cases when you are hosting the 3scale API manager in another geographical location from the service mesh running the 3scale Istio Adapter.
** This is generally the case with the 3scale Hosted (SaaS) platform, but also if a user hosts their 3scale API manager in another cluster located in a different geographical location, in a different availability zone, or in any case where the network overhead to reach the 3scale API manager is noticeable.


== Trade-offs for having lower latencies

The following are trade-offs for having lower latencies:

* Each 3scale adapter's authorization state updates every time a flush happens.
** This means two or more instances of the adapter will introduce more inaccuracy between flushing periods.
** There is a greater chance of too many requests being granted that exceed limits and introduce erratic behavior, which leads to some requests going through and some not, depending on which adapter processes each request.
* An adapter cache that cannot flush its data and update its authorization information risks shut down or crashing without reporting its information to the API manager.
* A fail open or fail closed policy will be applied when an adapter cache cannot determine whether a request must be granted or denied, possibly due to network connectivity issues in contacting the API manager.
* When cache misses occur, typically right after booting the adapter or after a long period of no connectivity, latencies will grow in order to query the API manager.
* An adapter cache must do much more work on computing authorizations than it would without an enabled cache, which will tax processor resources.
* Memory requirements will grow proportionally to the combination of the amount of limits, applications, and services managed by the cache.

== Backend cache configuration settings

The following points explain the backend cache configuration settings:

* Find the settings to configure the backend cache in the 3scale configuration options.
* The last 3 settings control enabling of backend cache:
** `PARAM_USE_CACHE_BACKEND` - set to true to enable backend cache.
** `PARAM_BACKEND_CACHE_FLUSH_INTERVAL_SECONDS` - sets time in seconds between consecutive attempts to flush cache data to the API manager.
** `PARAM_BACKEND_CACHE_POLICY_FAIL_CLOSED` - set whether or not to allow/open or deny/close requests to the services when there is not enough cached data and the 3scale API manager cannot be reached.
