// Module included in the following assemblies:
//
// * operators/understanding/olm-multitenancy.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-default-install-modes-behavior_{context}"]
= Default Operator install modes and behavior

When installing Operators with the web console as an administrator, you typically have two choices for the install mode, depending on the Operator's capabilities:

Single namespace:: Installs the Operator in the chosen single namespace, and makes all permissions that the Operator requests available in that namespace.

All namespaces:: Installs the Operator in the default `openshift-operators` namespace to watch and be made available to all namespaces in the cluster. Makes all permissions that the Operator requests available in all namespaces. In some cases, an Operator author can define metadata to give the user a second option for that Operator's suggested namespace.

This choice also means that users in the affected namespaces get access to the Operators APIs, which can leverage the custom resources (CRs) they own, depending on their role in the namespace:

* The `namespace-admin` and `namespace-edit` roles can read/write to the Operator APIs, meaning they can use them.
* The `namespace-view` role can read CR objects of that Operator.

For *Single namespace* mode, because the Operator itself installs in the chosen namespace, its pod and service account are also located there. For *All namespaces* mode, the Operator's privileges are all automatically elevated to cluster roles, meaning the Operator has those permissions in all namespaces.