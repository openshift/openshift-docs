// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/managing-cli-profiles.adoc

:_mod-docs-content-type: CONCEPT
[id="about-switches-between-cli-profiles_{context}"]
= About switches between CLI profiles

Contexts allow you to easily switch between multiple users across multiple
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
servers, or clusters, when using CLI operations. Nicknames make managing CLI configurations easier by providing short-hand references to contexts, user credentials, and cluster details.
After a user logs in with the `oc` CLI for the first time,
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
creates a `~/.kube/config` file if one does not already exist. As more authentication and connection details are provided to the CLI, either automatically during an `oc login` operation or by manually configuring CLI profiles, the updated information is stored in the configuration file:

.CLI config file

[source,yaml]
----
apiVersion: v1
clusters: <1>
- cluster:
    insecure-skip-tls-verify: true
    server: https://openshift1.example.com:8443
  name: openshift1.example.com:8443
- cluster:
    insecure-skip-tls-verify: true
    server: https://openshift2.example.com:8443
  name: openshift2.example.com:8443
contexts: <2>
- context:
    cluster: openshift1.example.com:8443
    namespace: alice-project
    user: alice/openshift1.example.com:8443
  name: alice-project/openshift1.example.com:8443/alice
- context:
    cluster: openshift1.example.com:8443
    namespace: joe-project
    user: alice/openshift1.example.com:8443
  name: joe-project/openshift1/alice
current-context: joe-project/openshift1.example.com:8443/alice <3>
kind: Config
preferences: {}
users: <4>
- name: alice/openshift1.example.com:8443
  user:
    token: xZHd2piv5_9vQrg-SKXRJ2Dsl9SceNJdhNTljEKTb8k
----

<1> The `clusters` section defines connection details for
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
clusters, including the address for their master server. In this example, one cluster is nicknamed `openshift1.example.com:8443` and another is nicknamed `openshift2.example.com:8443`.
<2> This `contexts` section defines two contexts: one nicknamed `alice-project/openshift1.example.com:8443/alice`, using the `alice-project` project, `openshift1.example.com:8443` cluster, and `alice` user, and another nicknamed `joe-project/openshift1.example.com:8443/alice`, using the `joe-project` project, `openshift1.example.com:8443` cluster and `alice` user.
<3> The `current-context` parameter shows that the `joe-project/openshift1.example.com:8443/alice` context is currently in use, allowing the `alice` user to work in the `joe-project` project on the `openshift1.example.com:8443` cluster.
<4> The `users` section defines user credentials. In this example, the user nickname `alice/openshift1.example.com:8443` uses an access token.

The CLI can support multiple configuration files which are loaded at runtime and merged together along with any override options specified from the command line. After you are logged in, you can use the `oc status` or `oc project` command to verify your current working environment:

.Verify the current working environment

[source,terminal,options="nowrap"]
----
$ oc status
----

.Example output
[source,terminal]
----
oc status
In project Joe's Project (joe-project)

service database (172.30.43.12:5434 -> 3306)
  database deploys docker.io/openshift/mysql-55-centos7:latest
    #1 deployed 25 minutes ago - 1 pod

service frontend (172.30.159.137:5432 -> 8080)
  frontend deploys origin-ruby-sample:latest <-
    builds https://github.com/openshift/ruby-hello-world with joe-project/ruby-20-centos7:latest
    #1 deployed 22 minutes ago - 2 pods

To see more information about a service or deployment, use 'oc describe service <name>' or 'oc describe dc <name>'.
You can use 'oc get all' to see lists of each of the types described in this example.
----

.List the current project
[source,terminal,options="nowrap"]
----
$ oc project
----

.Example output
[source,terminal]
----
Using project "joe-project" from context named "joe-project/openshift1.example.com:8443/alice" on server "https://openshift1.example.com:8443".
----

You can run the `oc login` command again and supply the required information during the interactive process, to log in using any other combination of user credentials and cluster details. A context is constructed based on the supplied information if one does not already exist. If you are already logged in and want to switch to another project the current user already has access to, use the `oc project` command and enter the name of the project:

[source,terminal,options="nowrap"]
----
$ oc project alice-project
----

.Example output
[source,terminal]
----
Now using project "alice-project" on server "https://openshift1.example.com:8443".
----

At any time, you can use the `oc config view` command to view your current CLI configuration, as seen in the output. Additional CLI configuration commands are also available for more advanced usage.

[NOTE]
====
If you have access to administrator credentials but are no longer logged in as the default system user `system:admin`, you can log back in as this user at any time as long as the credentials are still present in your CLI config file. The following command logs in and switches to the default project:

[source,terminal]
----
$ oc login -u system:admin -n default
----
====
