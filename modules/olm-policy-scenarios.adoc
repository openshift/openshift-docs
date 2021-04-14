// Module included in the following assemblies:
//
// * operators/admin/olm-creating-policy.adoc

[id="olm-policy-scenarios_{context}"]
= Installation scenarios

When determining whether an Operator can be installed or upgraded on a cluster, Operator Lifecycle Manager (OLM) considers the following scenarios:

* A cluster administrator creates a new Operator group and specifies a service account. All Operator(s) associated with this Operator group are installed and run against the privileges granted to the service account.

* A cluster administrator creates a new Operator group and does not specify any service account. {product-title} maintains backward compatibility, so the default behavior remains and Operator installs and upgrades are permitted.

* For existing Operator groups that do not specify a service account, the default behavior remains and Operator installs and upgrades are permitted.

* A cluster administrator updates an existing Operator group and specifies a service account. OLM allows the existing Operator to continue to run with their current privileges. When such an existing Operator is going through an upgrade, it is reinstalled and run against the privileges granted to the service account like any new Operator.

* A service account specified by an Operator group changes by adding or removing permissions, or the existing service account is swapped with a new one. When existing Operators go through an upgrade, it is reinstalled and run against the privileges granted to the updated service account like any new Operator.

* A cluster administrator removes the service account from an Operator group. The default behavior remains and Operator installs and upgrades are permitted.
