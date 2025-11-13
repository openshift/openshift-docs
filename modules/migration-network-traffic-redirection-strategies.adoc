// Module included in the following assemblies:
//
// * migrating_from_ocp_3_to_4/planning-considerations-3-4.adoc
// * migration_toolkit_for_containers/network-considerations-mtc.adoc

[id="migration-network-traffic-redirection-strategies_{context}"]
= Network traffic redirection strategies

After a successful migration, you must redirect network traffic of your stateless applications from the source cluster to the target cluster.

The strategies for redirecting network traffic are based on the following assumptions:

* The application pods are running on both the source and target clusters.
* Each application has a route that contains the source cluster hostname.
* The route with the source cluster hostname contains a CA certificate.
* For HTTPS, the target router CA certificate contains a Subject Alternative Name for the wildcard DNS record of the source cluster.

Consider the following strategies and select the one that meets your objectives.

* Redirecting all network traffic for all applications at the same time
+
Change the wildcard DNS record of the source cluster to point to the target cluster router's virtual IP address (VIP).
+
This strategy is suitable for simple applications or small migrations.

* Redirecting network traffic for individual applications
+
Create a DNS record for each application with the source cluster hostname pointing to the target cluster router's VIP. This DNS record takes precedence over the source cluster wildcard DNS record.

* Redirecting network traffic gradually for individual applications

. Create a proxy that can direct traffic to both the source cluster router's VIP and the target cluster router's VIP, for each application.
. Create a DNS record for each application with the source cluster hostname pointing to the proxy.
. Configure the proxy entry for the application to route a percentage of the traffic to the target cluster router's VIP and the rest of the traffic to the source cluster router's VIP.
. Gradually increase the percentage of traffic that you route to the target cluster router's VIP until all the network traffic is redirected.

* User-based redirection of traffic for individual applications
+
Using this strategy, you can filter TCP/IP headers of user requests to redirect network traffic for predefined groups of users. This allows you to test the redirection process on specific populations of users before redirecting the entire network traffic.

. Create a proxy that can direct traffic to both the source cluster router's VIP and the target cluster router's VIP, for each application.
. Create a DNS record for each application with the source cluster hostname pointing to the proxy.
. Configure the proxy entry for the application to route traffic matching a given header pattern, such as `test customers`, to the target cluster router's VIP and the rest of the traffic to the source cluster router's VIP.
. Redirect traffic to the target cluster router's VIP in stages until all the traffic is on the target cluster router's VIP.
