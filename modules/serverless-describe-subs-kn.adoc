// Module included in the following assemblies:
//
// * /serverless/develop/serverless-subs.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-describe-subs-kn_{context}"]
= Describing subscriptions by using the Knative CLI

You can use the `kn subscription describe` command to print information about a subscription in the terminal by using the Knative (`kn`) CLI. Using the Knative CLI to describe subscriptions provides a more streamlined and intuitive user interface than viewing YAML files directly.

.Prerequisites

* You have installed the Knative (`kn`) CLI.
* You have created a subscription in your cluster.

.Procedure

* Describe a subscription:
+
[source,terminal]
----
$ kn subscription describe <subscription_name>
----
+
.Example output
[source,terminal]
----
Name:            my-subscription
Namespace:       default
Annotations:     messaging.knative.dev/creator=openshift-user, messaging.knative.dev/lastModifier=min ...
Age:             43s
Channel:         Channel:my-channel (messaging.knative.dev/v1)
Subscriber:
  URI:           http://edisplay.default.example.com
Reply:
  Name:          default
  Resource:      Broker (eventing.knative.dev/v1)
DeadLetterSink:
  Name:          my-sink
  Resource:      Service (serving.knative.dev/v1)

Conditions:
  OK TYPE                  AGE REASON
  ++ Ready                 43s
  ++ AddedToChannel        43s
  ++ ChannelReady          43s
  ++ ReferencesResolved    43s
----
