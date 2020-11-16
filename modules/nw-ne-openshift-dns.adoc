// Module included in the following assemblies:
// * understanding-networking.adoc


[id="nw-ne-openshift-dns_{context}"]
= {product-title} DNS

If you are running multiple services, such as front-end and back-end services for
use with multiple pods, environment variables are created for user names,
service IPs, and more so the front-end pods can communicate with the back-end
services. If the service is deleted and recreated, a new IP address can be
assigned to the service, and requires the front-end pods to be recreated to pick
up the updated values for the service IP environment variable. Additionally, the
back-end service must be created before any of the front-end pods to ensure that
the service IP is generated properly, and that it can be provided to the
front-end pods as an environment variable.

For this reason, {product-title} has a built-in DNS so that the services can be
reached by the service DNS as well as the service IP/port.
