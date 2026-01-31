:_mod-docs-content-type: PROCEDURE
[id="serverless-build-events-kn_{context}"]
= Building events by using the kn-event plugin

You can use the builder-like interface of the `kn event build` command to build an event. You can then send that event at a later time or use it in another context.

.Prerequisites

* You have installed the Knative (`kn`) CLI.

.Procedure

* Build an event:
+
[source,terminal]
----
$ kn event build --field <field-name>=<value> --type <type-name> --id <id> --output <format>
----
where:
** The `--field` flag adds data to the event as a field-value pair. You can use it multiple times.
** The `--type` flag enables you to specify a string that designates the type of the event.
** The `--id` flag specifies the ID of the event.
** You can use the `json` or `yaml` arguments with the `--output` flag to change the output format of the event.
+
All of these flags are optional.
+
.Building a simple event
[source,terminal]
----
$ kn event build -o yaml
----
+
.Resultant event in the YAML format
[source,yaml]
----
data: {}
datacontenttype: application/json
id: 81a402a2-9c29-4c27-b8ed-246a253c9e58
source: kn-event/v0.4.0
specversion: "1.0"
time: "2021-10-15T10:42:57.713226203Z"
type: dev.knative.cli.plugin.event.generic
----
+
.Building a sample transaction event
[source,terminal]
----
$ kn event build \
    --field operation.type=local-wire-transfer \
    --field operation.amount=2345.40 \
    --field operation.from=87656231 \
    --field operation.to=2344121 \
    --field automated=true \
    --field signature='FGzCPLvYWdEgsdpb3qXkaVp7Da0=' \
    --type org.example.bank.bar \
    --id $(head -c 10 < /dev/urandom | base64 -w 0) \
    --output json
----
+
.Resultant event in the JSON format
[source,json]
----
{
  "specversion": "1.0",
  "id": "RjtL8UH66X+UJg==",
  "source": "kn-event/v0.4.0",
  "type": "org.example.bank.bar",
  "datacontenttype": "application/json",
  "time": "2021-10-15T10:43:23.113187943Z",
  "data": {
    "automated": true,
    "operation": {
      "amount": "2345.40",
      "from": 87656231,
      "to": 2344121,
      "type": "local-wire-transfer"
    },
    "signature": "FGzCPLvYWdEgsdpb3qXkaVp7Da0="
  }
}
----
