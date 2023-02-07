// Module included in the following assemblies:
//
// * monitoring/using-rfhe.adoc

:_module-type: PROCEDURE
[id="nw-rfhe-querying-redfish-hardware-event-subs_{context}"]
= Querying Redfish bare-metal event subscriptions with curl

Some hardware vendors limit the amount of Redfish hardware event subscriptions. You can query the number of Redfish event subscriptions by using `curl`.

.Prerequisites
* Get the user name and password for the BMC.
* Deploy a bare-metal node with a Redfish-enabled Baseboard Management Controller (BMC) in your cluster, and enable Redfish hardware events on the BMC.

.Procedure

. Check the current subscriptions for the BMC by running the following `curl` command:
+
[source,terminal]
----
$ curl --globoff -H "Content-Type: application/json" -k -X GET --user <bmc_username>:<password> https://<bmc_ip_address>/redfish/v1/EventService/Subscriptions
----
+
where:
+
--
bmc_ip_address:: is the IP address of the BMC where the Redfish events are generated.
--
+
.Example output
[source,terminal]
----
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
100 435 100 435 0 0 399 0 0:00:01 0:00:01 --:--:-- 399
{
  "@odata.context": "/redfish/v1/$metadata#EventDestinationCollection.EventDestinationCollection",
  "@odata.etag": ""
  1651137375 "",
  "@odata.id": "/redfish/v1/EventService/Subscriptions",
  "@odata.type": "#EventDestinationCollection.EventDestinationCollection",
  "Description": "Collection for Event Subscriptions",
  "Members": [
  {
    "@odata.id": "/redfish/v1/EventService/Subscriptions/1"
  }],
  "Members@odata.count": 1,
  "Name": "Event Subscriptions Collection"
}
----
+
In this example, a single subscription is configured: `/redfish/v1/EventService/Subscriptions/1`.

. Optional: To remove the `/redfish/v1/EventService/Subscriptions/1` subscription with `curl`, run the following command, specifying the BMC username and password:
+
[source,terminal]
----
$ curl --globoff -L -w "%{http_code} %{url_effective}\n" -k -u <bmc_username>:<password >-H "Content-Type: application/json" -d '{}' -X DELETE https://<bmc_ip_address>/redfish/v1/EventService/Subscriptions/1
----
+
where:
+
--
bmc_ip_address:: is the IP address of the BMC where the Redfish events are generated.
--



