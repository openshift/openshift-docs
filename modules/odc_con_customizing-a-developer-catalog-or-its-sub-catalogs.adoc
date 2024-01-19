// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

:_mod-docs-content-type: CONCEPT

[id="odc_con_customizing-a-developer-catalog-or-its-sub-catalogs_{context}"]
= Developer catalog and sub-catalog customization

As a cluster administrator, you have the ability to organize and manage the Developer catalog or its sub-catalogs. You can enable or disable the sub-catalog types or disable the entire developer catalog.

The `developerCatalog.types` object includes the following parameters that you must define in a snippet to use them in the YAML view:

* `state`: Defines if a list of developer catalog types should be enabled or disabled.
* `enabled`: Defines a list of developer catalog types (sub-catalogs) that are visible to users.
* `disabled`: Defines a list of developer catalog types (sub-catalogs) that are not visible to users.

You can enable or disable the following developer catalog types (sub-catalogs) using the YAML view or the form view.

* `Builder Images`
* `Templates`
* `Devfiles`
* `Samples`
* `Helm Charts`
* `Event Sources`
* `Event Sinks`
* `Operator Backed`



