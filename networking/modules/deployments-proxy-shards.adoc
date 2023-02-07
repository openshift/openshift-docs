// Module included in the following assemblies:
//
// * applications/deployments/route-based-deployment-strategies.adoc

[id="deployments-proxy-shard_{context}"]
= Proxy shards and traffic splitting

In production environments, you can precisely control the distribution of
traffic that lands on a particular shard. When dealing with large numbers of
instances, you can use the relative scale of individual shards to implement
percentage based traffic. That combines well with a _proxy shard_, which
forwards or splits the traffic it receives to a separate service or application
running elsewhere.

In the simplest configuration, the proxy forwards requests unchanged. In
more complex setups, you can duplicate the incoming requests and send to
both a separate cluster as well as to a local instance of the application, and
compare the result. Other patterns include keeping the caches of a DR
installation warm, or sampling incoming traffic for analysis purposes.

Any TCP (or UDP) proxy could be run under the desired shard. Use the `oc scale`
command to alter the relative number of instances serving requests under the
proxy shard. For more complex traffic management, consider customizing the
{product-title} router with proportional balancing capabilities.
