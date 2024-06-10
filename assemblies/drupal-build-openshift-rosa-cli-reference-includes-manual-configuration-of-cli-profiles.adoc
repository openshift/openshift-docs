// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/managing-cli-profiles.adoc

:_mod-docs-content-type: CONCEPT
[id="manual-configuration-of-cli-profiles_{context}"]
= Manual configuration of CLI profiles

[NOTE]
====
This section covers more advanced usage of CLI configurations. In most situations, you can use the `oc login` and `oc project` commands to log in and switch between contexts and projects.
====

If you want to manually configure your CLI config files, you can use the `oc config` command instead of directly modifying the files. The `oc config` command includes a number of helpful sub-commands for this purpose:

.CLI configuration subcommands
[cols="1,8",options="header"]
|===

|Subcommand |Usage

a|`set-cluster`
a|Sets a cluster entry in the CLI config file. If the referenced cluster
nickname already exists, the specified information is merged in.
[source,terminal,options="nowrap"]
----
$ oc config set-cluster <cluster_nickname> [--server=<master_ip_or_fqdn>]
[--certificate-authority=<path/to/certificate/authority>]
[--api-version=<apiversion>] [--insecure-skip-tls-verify=true]
----

a|`set-context`
a|Sets a context entry in the CLI config file. If the referenced context
nickname already exists, the specified information is merged in.
[source,terminal,options="nowrap"]
----
$ oc config set-context <context_nickname> [--cluster=<cluster_nickname>]
[--user=<user_nickname>] [--namespace=<namespace>]
----

a|`use-context`
a|Sets the current context using the specified context nickname.
[source,terminal,options="nowrap"]
----
$ oc config use-context <context_nickname>
----

a|`set`
a|Sets an individual value in the CLI config file.
[source,terminal,options="nowrap"]
----
$ oc config set <property_name> <property_value>
----
The `<property_name>` is a dot-delimited name where each token represents either an attribute name or a map key. The `<property_value>` is the new value being set.

a|`unset`
a|Unsets individual values in the CLI config file.
[source,terminal,options="nowrap"]
----
$ oc config unset <property_name>
----
The `<property_name>` is a dot-delimited name where each token represents either an attribute name or a map key.

a|`view`
a|Displays the merged CLI configuration currently in use.
[source,terminal,options="nowrap"]
----
$ oc config view
----

Displays the result of the specified CLI config file.
[source,terminal,options="nowrap"]
----
$ oc config view --config=<specific_filename>
----
|===

.Example usage

* Log in as a user that uses an access token.
This token is used by the `alice` user:

[source,terminal,options="nowrap"]
----
$ oc login https://openshift1.example.com --token=ns7yVhuRNpDM9cgzfhhxQ7bM5s7N2ZVrkZepSRf4LC0
----

* View the cluster entry automatically created:

[source,terminal,options="nowrap"]
----
$ oc config view
----

.Example output
[source,terminal]
----
apiVersion: v1
clusters:
- cluster:
    insecure-skip-tls-verify: true
    server: https://openshift1.example.com
  name: openshift1-example-com
contexts:
- context:
    cluster: openshift1-example-com
    namespace: default
    user: alice/openshift1-example-com
  name: default/openshift1-example-com/alice
current-context: default/openshift1-example-com/alice
kind: Config
preferences: {}
users:
- name: alice/openshift1.example.com
  user:
    token: ns7yVhuRNpDM9cgzfhhxQ7bM5s7N2ZVrkZepSRf4LC0
----

* Update the current context to have users log in to the desired namespace:

[source,terminal]
----
$ oc config set-context `oc config current-context` --namespace=<project_name>
----

* Examine the current context, to confirm that the changes are implemented:

[source,terminal]
----
$ oc whoami -c
----

All subsequent CLI operations uses the new context, unless otherwise specified by overriding CLI options or until the context is switched.
