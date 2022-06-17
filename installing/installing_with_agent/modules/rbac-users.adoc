// Module included in the following assemblies:
//
// * authentication/understanding-authentication.adoc

[id="rbac-users_{context}"]
= Users

A _user_ in {product-title} is an entity that can make requests to the
{product-title} API. An {product-title} `User` object represents an actor which
can be granted permissions in the system by adding roles to them or to their
groups. Typically, this represents the account of a developer or
administrator that is interacting with {product-title}.

Several types of users can exist:

[cols="1,4",options="header"]
|===

|User type
|Description

|`Regular users`
|This is the way most interactive {product-title} users are
represented. Regular users are created automatically in the system upon
first login or can be created via the API. Regular users are represented
with the `User` object. Examples: `joe` `alice`

|`System users`
|Many of these are created automatically when the infrastructure
 is defined, mainly for the purpose of enabling the infrastructure to
 interact with the API securely. They include a cluster administrator
 (with access to everything), a per-node user, users for use by routers
 and registries, and various others. Finally, there is an `anonymous`
 system user that is used by default for unauthenticated requests. Examples:
`system:admin` `system:openshift-registry` `system:node:node1.example.com`

|`Service accounts`
|These are special system users associated with projects; some are created automatically when
the project is first created, while project administrators can create more
for the purpose of defining access to the contents of each project.
Service accounts are represented with the `ServiceAccount` object. Examples:
`system:serviceaccount:default:deployer` `system:serviceaccount:foo:builder`

|===

Each user must authenticate in
some way to access {product-title}. API requests with no authentication
or invalid authentication are authenticated as requests by the `anonymous`
system user. After authentication, policy determines what the user is
authorized to do.
