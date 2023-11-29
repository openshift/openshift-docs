// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-working-bundle-images.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-bundle-upgrade-olm_{context}"]
= Testing an Operator upgrade on Operator Lifecycle Manager

You can quickly test upgrading your Operator by using Operator Lifecycle Manager (OLM) integration in the Operator SDK, without requiring you to manually manage index images and catalog sources.

The `run bundle-upgrade` subcommand automates triggering an installed Operator to upgrade to a later version by specifying a bundle image for the later version.

.Prerequisites

- Operator installed with OLM either by using the `run bundle` subcommand or with traditional OLM installation
- A bundle image that represents a later version of the installed Operator

.Procedure

. If your Operator has not already been installed with OLM, install the earlier version either by using the `run bundle` subcommand or with traditional OLM installation.
+
[NOTE]
====
If the earlier version of the bundle was installed traditionally using OLM, the newer bundle that you intend to upgrade to must not exist in the index image referenced by the catalog source. Otherwise, running the `run bundle-upgrade` subcommand will cause the registry pod to fail because the newer bundle is already referenced by the index that provides the package and cluster service version (CSV).
====
+
For example, you can use the following `run bundle` subcommand for a Memcached Operator by specifying the earlier bundle image:
+
[source,terminal]
----
$ operator-sdk run bundle <registry>/<user>/memcached-operator:v0.0.1
----
+
.Example output
[source,terminal]
----
INFO[0006] Creating a File-Based Catalog of the bundle "quay.io/demo/memcached-operator:v0.0.1"
INFO[0008] Generated a valid File-Based Catalog
INFO[0012] Created registry pod: quay-io-demo-memcached-operator-v1-0-1
INFO[0012] Created CatalogSource: memcached-operator-catalog
INFO[0012] OperatorGroup "operator-sdk-og" created
INFO[0012] Created Subscription: memcached-operator-v0-0-1-sub
INFO[0015] Approved InstallPlan install-h9666 for the Subscription: memcached-operator-v0-0-1-sub
INFO[0015] Waiting for ClusterServiceVersion "my-project/memcached-operator.v0.0.1" to reach 'Succeeded' phase
INFO[0015] Waiting for ClusterServiceVersion ""my-project/memcached-operator.v0.0.1" to appear
INFO[0026] Found ClusterServiceVersion "my-project/memcached-operator.v0.0.1" phase: Pending
INFO[0028] Found ClusterServiceVersion "my-project/memcached-operator.v0.0.1" phase: Installing
INFO[0059] Found ClusterServiceVersion "my-project/memcached-operator.v0.0.1" phase: Succeeded
INFO[0059] OLM has successfully installed "memcached-operator.v0.0.1"
----

. Upgrade the installed Operator by specifying the bundle image for the later Operator version:
+
[source,terminal]
----
$ operator-sdk run bundle-upgrade <registry>/<user>/memcached-operator:v0.0.2
----
+
.Example output
[source,terminal]
----
INFO[0002] Found existing subscription with name memcached-operator-v0-0-1-sub and namespace my-project
INFO[0002] Found existing catalog source with name memcached-operator-catalog and namespace my-project
INFO[0008] Generated a valid Upgraded File-Based Catalog
INFO[0009] Created registry pod: quay-io-demo-memcached-operator-v0-0-2
INFO[0009] Updated catalog source memcached-operator-catalog with address and annotations
INFO[0010] Deleted previous registry pod with name "quay-io-demo-memcached-operator-v0-0-1"
INFO[0041] Approved InstallPlan install-gvcjh for the Subscription: memcached-operator-v0-0-1-sub
INFO[0042] Waiting for ClusterServiceVersion "my-project/memcached-operator.v0.0.2" to reach 'Succeeded' phase
INFO[0019] Found ClusterServiceVersion "my-project/memcached-operator.v0.0.2" phase: Pending
INFO[0042] Found ClusterServiceVersion "my-project/memcached-operator.v0.0.2" phase: InstallReady
INFO[0043] Found ClusterServiceVersion "my-project/memcached-operator.v0.0.2" phase: Installing
INFO[0044] Found ClusterServiceVersion "my-project/memcached-operator.v0.0.2" phase: Succeeded
INFO[0044] Successfully upgraded to "memcached-operator.v0.0.2"
----

. Clean up the installed Operators:
+
[source,terminal]
----
$ operator-sdk cleanup memcached-operator
----
