// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-du-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-ran-redfish-operator_{context}"]
= {redfish-operator}

The {redfish-operator} is an optional Operator that runs exclusively on the managed spoke cluster. It relays Redfish hardware events to cluster applications.

[NOTE]
====
The {redfish-operator} is not included in the RAN DU use model reference configuration and is an optional feature.
If you want to use the {redfish-operator}, assign additional CPU resources from the application CPU budget.
====
