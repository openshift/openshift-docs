// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quotas-scopes_{context}"]
= Quota scopes

Each quota can have an associated set of _scopes_. A quota only measures usage
for a resource if it matches the intersection of enumerated scopes.

Adding a scope to a quota restricts the set of resources to which that quota can
apply. Specifying a resource outside of the allowed set results in a validation
error.

|===

|Scope |Description

|`BestEffort`
|Match pods that have best effort quality of service for either `cpu` or
`memory`.

|`NotBestEffort`
|Match pods that do not have best effort quality of service for `cpu` and
`memory`.
|===

A `BestEffort` scope restricts a quota to limiting the following resources:

- `pods`

A `NotBestEffort` scope restricts a quota to tracking the following resources:

- `pods`
- `memory`
- `requests.memory`
- `limits.memory`
- `cpu`
- `requests.cpu`
- `limits.cpu`
