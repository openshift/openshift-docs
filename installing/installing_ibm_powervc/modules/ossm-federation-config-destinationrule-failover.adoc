////
This module included in the following assemblies:
* service_mesh/v2x/ossm-federation.adoc
////
:_mod-docs-content-type: PROCEDURE
[id="ossm-federation-config-destinationrule-failover_{context}"]
= Configuring a DestinationRule for failover

Create a `DestinationRule` resource that configures the following:

* Outlier detection for the service. This is required in order for failover to function properly. In particular, it configures the sidecar proxies to know when endpoints for a service are unhealthy, eventually triggering a failover to the next locality.

* Failover policy between regions. This ensures that failover beyond a region boundary will behave predictably.

.Procedure

. Log in to the {product-title} CLI as a user with the `cluster-admin` role. Enter the following command. Then, enter your username and password when prompted.
+
[source,terminal]
----
$ oc login --username=<NAMEOFUSER> <API token> https://<HOSTNAME>:6443
----
+
. Change to the project where you installed the {SMProductShortName} control plane.
+
[source,terminal]
----
$ oc project <smcp-system>
----
+
For example, `green-mesh-system`.
+
[source,terminal]
----
$ oc project green-mesh-system
----
+
. Create a `DestinationRule` file based on the following example where if green-mesh is unavailable, the traffic should be routed from the green-mesh in the `us-east` region to the red-mesh in `us-west`.
+
.Example `DestinationRule`
[source,yaml]
----
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: default-failover
  namespace: bookinfo
spec:
  host: "ratings.bookinfo.svc.cluster.local"
  trafficPolicy:
    loadBalancer:
      localityLbSetting:
        enabled: true
        failover:
          - from: us-east
            to: us-west
    outlierDetection:
      consecutive5xxErrors: 3
      interval: 10s
      baseEjectionTime: 1m
----
+
. Deploy the `DestinationRule`, where `<DestinationRule>` includes the full path to your file, enter the following command:
+
[source,terminal]
----
$ oc create -n <application namespace> -f <DestinationRule.yaml>
----
+
For example:
+
[source,terminal]
----
$ oc create -n bookinfo -f green-mesh-us-west-DestinationRule.yaml
----
