// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/getting-started.adoc
// * microshift_cli_ref/microshift_oc_cli_install.adoc

:_mod-docs-content-type: PROCEDURE
[id="cli-installing-cli-rpm_{context}"]
= Installing the OpenShift CLI by using an RPM

For {op-system-base-full}, you can install the {oc-first} as an RPM if you have an active {product-title}
ifdef::openshift-rosa[]
(ROSA)
endif::openshift-rosa[]
subscription on your Red Hat account.

[NOTE]
====
It is not supported to install the OpenShift CLI (`oc`) as an RPM for {op-system-base-full} 9. You must install the OpenShift CLI for {op-system-base} 9 by downloading the binary.
====

.Prerequisites

* Must have root or sudo privileges.

.Procedure

. Register with Red Hat Subscription Manager:
+
[source,terminal]
----
# subscription-manager register
----

. Pull the latest subscription data:
+
[source,terminal]
----
# subscription-manager refresh
----

. List the available subscriptions:
+
[source,terminal]
----
# subscription-manager list --available --matches '*OpenShift*'
----

. In the output for the previous command, find the pool ID for
ifndef::openshift-rosa[]
an {product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
a ROSA
endif::openshift-rosa[]
subscription and attach the subscription to the registered system:
+
[source,terminal]
----
# subscription-manager attach --pool=<pool_id>
----

. Enable the repositories required by
ifndef::openshift-rosa[]
{product-title} {product-version}.
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA.
endif::openshift-rosa[]
+
[source,terminal,subs="attributes+"]
----
# subscription-manager repos --enable="rhocp-{product-version}-for-rhel-8-x86_64-rpms"
----

. Install the `openshift-clients` package:
+
[source,terminal]
----
# yum install openshift-clients
----

After you install the CLI, it is available using the `oc` command:

[source,terminal]
----
$ oc <command>
----
