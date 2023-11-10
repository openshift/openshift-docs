// Text snippet included in the following assemblies:
//

:_mod-docs-content-type: SNIPPET

[WARNING]
====
Operator Lifecycle Manager (OLM) creates the following cluster roles for each Operator group:

* `<operatorgroup_name>-admin`
* `<operatorgroup_name>-edit`
* `<operatorgroup_name>-view`

When you manually create an Operator group, you must specify a unique name that does not conflict with the existing cluster roles or other Operator groups on the cluster.
====
