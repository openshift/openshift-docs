:_mod-docs-content-type: REFERENCE
[id="odo-catalog_{context}"]
= odo catalog

`odo` uses different _catalogs_ to deploy _components_ and _services_.

== Components

`odo` uses the portable _devfile_ format to describe the components. It can connect to various devfile registries to download devfiles for different languages and frameworks.
See `odo registry` for more information.

=== Listing components

To list all the _devfiles_ available on the different registries, run the command:

[source,terminal]
----
$ odo catalog list components
----

.Example output
[source,terminal]
----
 NAME             DESCRIPTION                          REGISTRY
 go               Stack with the latest Go version     DefaultDevfileRegistry
 java-maven       Upstream Maven and OpenJDK 11        DefaultDevfileRegistry
 nodejs           Stack with Node.js 14                DefaultDevfileRegistry
 php-laravel      Stack with Laravel 8                 DefaultDevfileRegistry
 python           Python Stack with Python 3.7         DefaultDevfileRegistry
 [...]
----

=== Getting information about a component

To get more information about a specific component, run the command:

[source,terminal]
----
$ odo catalog describe component
----

For example, run the command:

[source,terminal]
----
$ odo catalog describe component nodejs
----

.Example output
[source,terminal]
----
* Registry: DefaultDevfileRegistry <1>

Starter Projects: <2>
---
name: nodejs-starter
attributes: {}
description: ""
subdir: ""
projectsource:
  sourcetype: ""
  git:
    gitlikeprojectsource:
      commonprojectsource: {}
      checkoutfrom: null
      remotes:
        origin: https://github.com/odo-devfiles/nodejs-ex.git
  zip: null
  custom: null
----
<1> _Registry_ is the registry from which the devfile is retrieved.
<2> _Starter projects_ are sample projects in the same language and framework of the devfile, that can help you start a new project.


See `odo create` for more information on creating a project from a starter project.


== Services

`odo` can deploy _services_ with the help of _Operators_.

Only Operators deployed with the help of the https://olm.operatorframework.io/[_Operator Lifecycle Manager_] are supported by odo.

////
See link:/docs/getting-started/cluster-setup/kubernetes#installing-the-operator-lifecycle-manager-olm[Installing the Operator Lifecycle Manager (OLM)] for more information.
////

=== Listing services

To list the available Operators and their associated services, run the command:

[source,terminal]
----
$ odo catalog list services
----

.Example output
[source,terminal]
----
 Services available through Operators
 NAME                                 CRDs
 postgresql-operator.v0.1.1           Backup, Database
 redis-operator.v0.8.0                RedisCluster, Redis
----

In this example, two Operators are installed in the cluster. The `postgresql-operator.v0.1.1` Operator deploys services related to PostgreSQL: `Backup` and `Database`.
The `redis-operator.v0.8.0` Operator deploys services related to Redis: `RedisCluster` and `Redis`.

[NOTE]
====
To get a list of all the available Operators, `odo` fetches the ClusterServiceVersion (CSV) resources of the current namespace that are in a _Succeeded_ phase.
For Operators that support cluster-wide access, when a new namespace is created, these resources are automatically added to it. However, it may take some time before they are in the _Succeeded_ phase, and `odo` may return an empty list until the resources are ready.
====

=== Searching services

To search for a specific service by a keyword, run the command:

[source,terminal]
----
$ odo catalog search service
----

For example, to retrieve the PostgreSQL services, run the command:

[source,terminal]
----
$ odo catalog search service postgres
----

.Example output
[source,terminal]
----
 Services available through Operators
 NAME                           CRDs
 postgresql-operator.v0.1.1     Backup, Database
----

You will see a list of Operators that contain the searched keyword in their name.

=== Getting information about a service

To get more information about a specific service, run the command:

[source,terminal]
----
$ odo catalog describe service
----

For example:

[source,terminal]
----
$ odo catalog describe service postgresql-operator.v0.1.1/Database
----

.Example output
[source,terminal]
----
KIND:    Database
VERSION: v1alpha1

DESCRIPTION:
     Database is the Schema for the Database API

FIELDS:
   awsAccessKeyId (string)
     AWS S3 accessKey/token ID

     Key ID of AWS S3 storage. Default Value: nil Required to create the Secret
     with the data to allow send the backup files to AWS S3 storage.
[...]
----

A service is represented in the cluster by a CustomResourceDefinition (CRD) resource. The previous command displays the details about the CRD such as  `kind`, `version`, and the list of fields available to define an instance of this custom resource.

The list of fields is extracted from the _OpenAPI schema_ included in the CRD. This information is optional in a CRD, and if it is not present, it is extracted from the ClusterServiceVersion (CSV) resource representing the service instead.

It is also possible to request the description of an Operator-backed service, without providing CRD type information. To describe the Redis Operator on a cluster, without CRD, run the following command:


[source,terminal]
----
$ odo catalog describe service redis-operator.v0.8.0
----

.Example output
[source,terminal]
----
NAME:	redis-operator.v0.8.0
DESCRIPTION:

	A Golang based redis operator that will make/oversee Redis
	standalone/cluster mode setup on top of the Kubernetes. It can create a
	redis cluster setup with best practices on Cloud as well as the Bare metal
	environment. Also, it provides an in-built monitoring capability using

... (cut short for beverity)

	Logging Operator is licensed under [Apache License, Version
	2.0](https://github.com/OT-CONTAINER-KIT/redis-operator/blob/master/LICENSE)


CRDs:
	NAME           DESCRIPTION
	RedisCluster   Redis Cluster
	Redis          Redis
----
