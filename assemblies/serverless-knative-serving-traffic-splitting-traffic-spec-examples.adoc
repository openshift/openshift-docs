:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="traffic-spec-examples"]
= Traffic spec examples
:context: traffic-spec-examples

toc::[]

The following example shows a `traffic` spec where 100% of traffic is routed to the latest revision of the service. Under `status`, you can see the name of the latest revision that `latestRevision` resolves to:

[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example-service
  namespace: default
spec:
...
  traffic:
  - latestRevision: true
    percent: 100
status:
  ...
  traffic:
  - percent: 100
    revisionName: example-service
----

The following example shows a `traffic` spec where 100% of traffic is routed to the revision tagged as `current`, and the name of that revision is specified as `example-service`. The revision tagged as `latest` is kept available, even though no traffic is routed to it:

[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example-service
  namespace: default
spec:
...
  traffic:
  - tag: current
    revisionName: example-service
    percent: 100
  - tag: latest
    latestRevision: true
    percent: 0
----

The following example shows how the list of revisions in the `traffic` spec can be extended so that traffic is split between multiple revisions. This example sends 50% of traffic to the revision tagged as `current`, and 50% of traffic to the revision tagged as `candidate`. The revision tagged as `latest` is kept available, even though no traffic is routed to it:

[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example-service
  namespace: default
spec:
...
  traffic:
  - tag: current
    revisionName: example-service-1
    percent: 50
  - tag: candidate
    revisionName: example-service-2
    percent: 50
  - tag: latest
    latestRevision: true
    percent: 0
----
