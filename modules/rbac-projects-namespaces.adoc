// Module included in the following assemblies:
//
// * authentication/using-rbac.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="rbac-projects-namespaces_{context}"]
= Projects and namespaces

A Kubernetes _namespace_ provides a mechanism to scope resources in a cluster.
The
https://kubernetes.io/docs/tasks/administer-cluster/namespaces/[Kubernetes documentation]
has more information on namespaces.

Namespaces provide a unique scope for:

* Named resources to avoid basic naming collisions.
* Delegated management authority to trusted users.
* The ability to limit community resource consumption.

Most objects in the system are scoped by namespace, but some are
excepted and have no namespace, including nodes and users.

A _project_ is a Kubernetes namespace with additional annotations and is the central vehicle
by which access to resources for regular users is managed.
A project allows a community of users to organize and manage their content in
isolation from other communities. Users must be given access to projects by administrators,
or if allowed to create projects, automatically have access to their own projects.

Projects can have a separate `name`, `displayName`, and `description`.

- The mandatory `name` is a unique identifier for the project and is most visible when using the CLI tools or API. The maximum name length is 63 characters.
- The optional `displayName` is how the project is displayed in the web console (defaults to `name`).
- The optional `description` can be a more detailed description of the project and is also visible in the web console.

Each project scopes its own set of:

[cols="1,4",options="header"]
|===

|Object
|Description

|`Objects`
|Pods, services, replication controllers, etc.

|`Policies`
|Rules for which users can or cannot perform actions on objects.

|`Constraints`
|Quotas for each kind of object that can be limited.

|`Service accounts`
|Service accounts act automatically with designated access to objects in the project.

|===

ifndef::openshift-dedicated,openshift-rosa[]
Cluster administrators
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
Administrators with the `dedicated-admin` role
endif::openshift-dedicated,openshift-rosa[]
can create projects and delegate administrative rights for the project to any member of the user community.
ifndef::openshift-dedicated,openshift-rosa[]
Cluster administrators
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
Administrators with the `dedicated-admin` role
endif::openshift-dedicated,openshift-rosa[]
can also allow developers to create their own projects.

Developers and administrators can interact with projects by using the CLI or the
web console.
