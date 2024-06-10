// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-trigger-management_{context}"]
= Trigger management commands

== eventlistener
Manage EventListeners.

.Example: Display help
[source,terminal]
----
$ tkn eventlistener -h
----

== eventlistener delete
Delete an EventListener.

.Example: Delete `mylistener1` and `mylistener2` EventListeners in a namespace
[source,terminal]
----
$ tkn eventlistener delete mylistener1 mylistener2 -n myspace
----
== eventlistener describe
Describe an EventListener.

.Example: Describe the `mylistener` EventListener in a namespace
[source,terminal]
----
$ tkn eventlistener describe mylistener -n myspace
----

== eventlistener list
List EventListeners.

.Example: List all the EventListeners in a namespace
[source,terminal]
----
$ tkn eventlistener list -n myspace
----

== eventlistener logs
Display logs of an EventListener.

.Example: Display the logs of the `mylistener` EventListener in a namespace
[source,terminal]
----
$ tkn eventlistener logs mylistener -n myspace
----

== triggerbinding
Manage TriggerBindings.

.Example: Display TriggerBindings help
[source,terminal]
----
$ tkn triggerbinding -h
----

== triggerbinding delete
Delete a TriggerBinding.

.Example: Delete `mybinding1` and `mybinding2` TriggerBindings in a namespace
[source,terminal]
----
$ tkn triggerbinding delete mybinding1 mybinding2 -n myspace
----
== triggerbinding describe
Describe a TriggerBinding.

.Example: Describe the `mybinding` TriggerBinding in a namespace
[source,terminal]
----
$ tkn triggerbinding describe mybinding -n myspace
----

== triggerbinding list
List TriggerBindings.

.Example: List all the TriggerBindings in a namespace
[source,terminal]
----
$ tkn triggerbinding list -n myspace
----

== triggertemplate
Manage TriggerTemplates.

.Example: Display TriggerTemplate help
[source,terminal]
----
$ tkn triggertemplate -h
----
== triggertemplate delete
Delete a TriggerTemplate.

.Example: Delete `mytemplate1` and `mytemplate2` TriggerTemplates in a namespace
[source,terminal]
----
$ tkn triggertemplate delete mytemplate1 mytemplate2 -n `myspace`
----
== triggertemplate describe
Describe a TriggerTemplate.

.Example: Describe the `mytemplate` TriggerTemplate in a namespace
[source,terminal]
----
$ tkn triggertemplate describe mytemplate -n `myspace`
----

== triggertemplate list
List TriggerTemplates.

.Example: List all the TriggerTemplates in a namespace
[source,terminal]
----
$ tkn triggertemplate list -n myspace
----
== clustertriggerbinding
Manage ClusterTriggerBindings.

.Example: Display ClusterTriggerBindings help
[source,terminal]
----
$ tkn clustertriggerbinding -h
----

== clustertriggerbinding delete
Delete a ClusterTriggerBinding.

.Example: Delete `myclusterbinding1` and `myclusterbinding2` ClusterTriggerBindings
[source,terminal]
----
$ tkn clustertriggerbinding delete myclusterbinding1 myclusterbinding2
----
== clustertriggerbinding describe
Describe a ClusterTriggerBinding.

.Example: Describe the `myclusterbinding` ClusterTriggerBinding
[source,terminal]
----
$ tkn clustertriggerbinding describe myclusterbinding
----

== clustertriggerbinding list
List ClusterTriggerBindings.

.Example: List all ClusterTriggerBindings
[source,terminal]
----
$ tkn clustertriggerbinding list
----
