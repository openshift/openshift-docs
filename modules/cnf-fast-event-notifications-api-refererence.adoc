// Module included in the following assemblies:
//
// * networking/ptp/using-ptp-events.adoc

:_mod-docs-content-type: PROCEDURE
[id="cnf-fast-event-notifications-api-refererence_{context}"]
= PTP events REST API reference

Use the PTP event notifications REST API to subscribe a cluster application to the PTP events that are generated on the parent node.

[id="api-ocloud-notifications-v1-subscriptions_{context}"]
== api/ocloudNotifications/v1/subscriptions

[discrete]
=== HTTP method

`GET api/ocloudNotifications/v1/subscriptions`

[discrete]
=== Description

Returns a list of subscriptions. If subscriptions exist, a `200 OK` status code is returned along with the list of subscriptions.

.Example API response
[source,json]
----
[
 {
  "id": "75b1ad8f-c807-4c23-acf5-56f4b7ee3826",
  "endpointUri": "http://localhost:9089/event",
  "uriLocation": "http://localhost:8089/api/ocloudNotifications/v1/subscriptions/75b1ad8f-c807-4c23-acf5-56f4b7ee3826",
  "resource": "/cluster/node/compute-1.example.com/ptp"
 }
]
----

[discrete]
=== HTTP method

`POST api/ocloudNotifications/v1/subscriptions`

[discrete]
=== Description

Creates a new subscription. If a subscription is successfully created, or if it already exists, a `201 Created` status code is returned.

.Query parameters
[cols=2*, width="60%", options="header"]
|====
|Parameter
|Type

|subscription
|data
|====

.Example payload
[source,json]
----
{
  "uriLocation": "http://localhost:8089/api/ocloudNotifications/v1/subscriptions",
  "resource": "/cluster/node/compute-1.example.com/ptp"
}
----

[id="api-ocloud-notifications-v1-subscriptions-subscription_id_{context}"]
== api/ocloudNotifications/v1/subscriptions/<subscription_id>

[discrete]
=== HTTP method

`GET api/ocloudNotifications/v1/subscriptions/<subscription_id>`

[discrete]
=== Description

Returns details for the subscription with ID `<subscription_id>`

.Query parameters
[cols=2*, width="60%", options="header"]
|====
|Parameter
|Type

|`<subscription_id>`
|string
|====

.Example API response
[source,json]
----
{
  "id":"48210fb3-45be-4ce0-aa9b-41a0e58730ab",
  "endpointUri": "http://localhost:9089/event",
  "uriLocation":"http://localhost:8089/api/ocloudNotifications/v1/subscriptions/48210fb3-45be-4ce0-aa9b-41a0e58730ab",
  "resource":"/cluster/node/compute-1.example.com/ptp"
}
----

[id="api-ocloudnotifications-v1-health_{context}"]
== api/ocloudNotifications/v1/health

[discrete]
=== HTTP method

`GET api/ocloudNotifications/v1/health/`

[discrete]
=== Description

Returns the health status for the `ocloudNotifications` REST API.

.Example API response
[source,terminal]
----
OK
----

[id="api-ocloudnotifications-v1-publishers_{context}"]
== api/ocloudNotifications/v1/publishers

[discrete]
=== HTTP method

`GET api/ocloudNotifications/v1/publishers`

[discrete]
=== Description

Returns an array of `os-clock-sync-state`, `ptp-clock-class-change`, `lock-state`, and `gnss-sync-status` details for the cluster node.
The system generates notifications when the relevant equipment state changes.

* `os-clock-sync-state` notifications describe the host operating system clock synchronization state. Can be in `LOCKED` or `FREERUN` state.
* `ptp-clock-class-change` notifications describe the current state of the PTP clock class.
* `lock-state` notifications describe the current status of the PTP equipment lock state. Can be in `LOCKED`, `HOLDOVER` or `FREERUN` state.
* `gnss-sync-status` notifications describe the GPS synchronization state with regard to the external GNSS clock signal. Can be in `LOCKED` or `FREERUN` state.

You can use equipment synchronization status subscriptions together to deliver a detailed view of the overall synchronization health of the system.

.Example API response
[source,json]
----
[
  {
    "id": "0fa415ae-a3cf-4299-876a-589438bacf75",
    "endpointUri": "http://localhost:9085/api/ocloudNotifications/v1/dummy",
    "uriLocation": "http://localhost:9085/api/ocloudNotifications/v1/publishers/0fa415ae-a3cf-4299-876a-589438bacf75",
    "resource": "/cluster/node/compute-1.example.com/sync/sync-status/os-clock-sync-state"
  },
  {
    "id": "28cd82df-8436-4f50-bbd9-7a9742828a71",
    "endpointUri": "http://localhost:9085/api/ocloudNotifications/v1/dummy",
    "uriLocation": "http://localhost:9085/api/ocloudNotifications/v1/publishers/28cd82df-8436-4f50-bbd9-7a9742828a71",
    "resource": "/cluster/node/compute-1.example.com/sync/ptp-status/ptp-clock-class-change"
  },
  {
    "id": "44aa480d-7347-48b0-a5b0-e0af01fa9677",
    "endpointUri": "http://localhost:9085/api/ocloudNotifications/v1/dummy",
    "uriLocation": "http://localhost:9085/api/ocloudNotifications/v1/publishers/44aa480d-7347-48b0-a5b0-e0af01fa9677",
    "resource": "/cluster/node/compute-1.example.com/sync/ptp-status/lock-state"
  },
  {
    "id": "778da345d-4567-67b0-a43f0-rty885a456",
    "endpointUri": "http://localhost:9085/api/ocloudNotifications/v1/dummy",
    "uriLocation": "http://localhost:9085/api/ocloudNotifications/v1/publishers/778da345d-4567-67b0-a43f0-rty885a456",
    "resource": "/cluster/node/compute-1.example.com/sync/gnss-status/gnss-sync-status"
  }
]
----

You can find `os-clock-sync-state`, `ptp-clock-class-change`, `lock-state`, and `gnss-sync-status` events in the logs for the `cloud-event-proxy` container. For example:

[source,terminal]
----
$ oc logs -f linuxptp-daemon-cvgr6 -n openshift-ptp -c cloud-event-proxy
----

.Example os-clock-sync-state event
[source,json]
----
{
   "id":"c8a784d1-5f4a-4c16-9a81-a3b4313affe5",
   "type":"event.sync.sync-status.os-clock-sync-state-change",
   "source":"/cluster/compute-1.example.com/ptp/CLOCK_REALTIME",
   "dataContentType":"application/json",
   "time":"2022-05-06T15:31:23.906277159Z",
   "data":{
      "version":"v1",
      "values":[
         {
            "resource":"/sync/sync-status/os-clock-sync-state",
            "dataType":"notification",
            "valueType":"enumeration",
            "value":"LOCKED"
         },
         {
            "resource":"/sync/sync-status/os-clock-sync-state",
            "dataType":"metric",
            "valueType":"decimal64.3",
            "value":"-53"
         }
      ]
   }
}
----

.Example ptp-clock-class-change event
[source,json]
----
{
   "id":"69eddb52-1650-4e56-b325-86d44688d02b",
   "type":"event.sync.ptp-status.ptp-clock-class-change",
   "source":"/cluster/compute-1.example.com/ptp/ens2fx/master",
   "dataContentType":"application/json",
   "time":"2022-05-06T15:31:23.147100033Z",
   "data":{
      "version":"v1",
      "values":[
         {
            "resource":"/sync/ptp-status/ptp-clock-class-change",
            "dataType":"metric",
            "valueType":"decimal64.3",
            "value":"135"
         }
      ]
   }
}
----

.Example lock-state event
[source,json]
----
{
   "id":"305ec18b-1472-47b3-aadd-8f37933249a9",
   "type":"event.sync.ptp-status.ptp-state-change",
   "source":"/cluster/compute-1.example.com/ptp/ens2fx/master",
   "dataContentType":"application/json",
   "time":"2022-05-06T15:31:23.467684081Z",
   "data":{
      "version":"v1",
      "values":[
         {
            "resource":"/sync/ptp-status/lock-state",
            "dataType":"notification",
            "valueType":"enumeration",
            "value":"LOCKED"
         },
         {
            "resource":"/sync/ptp-status/lock-state",
            "dataType":"metric",
            "valueType":"decimal64.3",
            "value":"62"
         }
      ]
   }
}
----

.Example gnss-sync-status event
[source,json]
----
{
  "id": "435e1f2a-6854-4555-8520-767325c087d7",
  "type": "event.sync.gnss-status.gnss-state-change",
  "source": "/cluster/node/compute-1.example.com/sync/gnss-status/gnss-sync-status",
  "dataContentType": "application/json",
  "time": "2023-09-27T19:35:33.42347206Z",
  "data": {
    "version": "v1",
    "values": [
      {
        "resource": "/cluster/node/compute-1.example.com/ens2fx/master",
        "dataType": "notification",
        "valueType": "enumeration",
        "value": "LOCKED"
      },
      {
        "resource": "/cluster/node/compute-1.example.com/ens2fx/master",
        "dataType": "metric",
        "valueType": "decimal64.3",
        "value": "5"
      }
    ]
  }
}
----

[id="resource-address-current-state_{context}"]
== api/ocloudNotifications/v1/<resource_address>/CurrentState

[discrete]
=== HTTP method

`GET api/ocloudNotifications/v1/cluster/node/<node_name>/sync/ptp-status/lock-state/CurrentState`

`GET api/ocloudNotifications/v1/cluster/node/<node_name>/sync/sync-status/os-clock-sync-state/CurrentState`

`GET api/ocloudNotifications/v1/cluster/node/<node_name>/sync/ptp-status/ptp-clock-class-change/CurrentState`

[discrete]
=== Description

Configure the `CurrentState` API endpoint to return the current state of the `os-clock-sync-state`, `ptp-clock-class-change`, `lock-state` events for the cluster node.

* `os-clock-sync-state` notifications describe the host operating system clock synchronization state. Can be in `LOCKED` or `FREERUN` state.
* `ptp-clock-class-change` notifications describe the current state of the PTP clock class.
* `lock-state` notifications describe the current status of the PTP equipment lock state. Can be in `LOCKED`, `HOLDOVER` or `FREERUN` state.

.Query parameters
[cols=2*, width="60%", options="header"]
|====
|Parameter
|Type

|`<resource_address>`
|string
|====

.Example lock-state API response
[source,json]
----
{
  "id": "c1ac3aa5-1195-4786-84f8-da0ea4462921",
  "type": "event.sync.ptp-status.ptp-state-change",
  "source": "/cluster/node/compute-1.example.com/sync/ptp-status/lock-state",
  "dataContentType": "application/json",
  "time": "2023-01-10T02:41:57.094981478Z",
  "data": {
    "version": "v1",
    "values": [
      {
        "resource": "/cluster/node/compute-1.example.com/ens5fx/master",
        "dataType": "notification",
        "valueType": "enumeration",
        "value": "LOCKED"
      },
      {
        "resource": "/cluster/node/compute-1.example.com/ens5fx/master",
        "dataType": "metric",
        "valueType": "decimal64.3",
        "value": "29"
      }
    ]
  }
}
----

.Example os-clock-sync-state API response
[source,json]
----
{
  "specversion": "0.3",
  "id": "4f51fe99-feaa-4e66-9112-66c5c9b9afcb",
  "source": "/cluster/node/compute-1.example.com/sync/sync-status/os-clock-sync-state",
  "type": "event.sync.sync-status.os-clock-sync-state-change",
  "subject": "/cluster/node/compute-1.example.com/sync/sync-status/os-clock-sync-state",
  "datacontenttype": "application/json",
  "time": "2022-11-29T17:44:22.202Z",
  "data": {
    "version": "v1",
    "values": [
      {
        "resource": "/cluster/node/compute-1.example.com/CLOCK_REALTIME",
        "dataType": "notification",
        "valueType": "enumeration",
        "value": "LOCKED"
      },
      {
        "resource": "/cluster/node/compute-1.example.com/CLOCK_REALTIME",
        "dataType": "metric",
        "valueType": "decimal64.3",
        "value": "27"
      }
    ]
  }
}
----

.Example ptp-clock-class-change API response
[source,json]
----
{
  "id": "064c9e67-5ad4-4afb-98ff-189c6aa9c205",
  "type": "event.sync.ptp-status.ptp-clock-class-change",
  "source": "/cluster/node/compute-1.example.com/sync/ptp-status/ptp-clock-class-change",
  "dataContentType": "application/json",
  "time": "2023-01-10T02:41:56.785673989Z",
  "data": {
    "version": "v1",
    "values": [
      {
        "resource": "/cluster/node/compute-1.example.com/ens5fx/master",
        "dataType": "metric",
        "valueType": "decimal64.3",
        "value": "165"
      }
    ]
  }
}
----
