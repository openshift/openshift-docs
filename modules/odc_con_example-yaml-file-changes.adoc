// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

:_mod-docs-content-type: CONCEPT

[id="con_example-yaml-file-changes_{context}"]
= Example YAML file changes

You can dynamically add the following snippets in the YAML editor for customizing a developer catalog.

Use the following snippet to display all the sub-catalogs by setting the _state_ type to *Enabled*.
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Enabled
----

Use the following snippet to disable all sub-catalogs by setting the _state_ type to *Disabled*:
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Disabled
----

Use the following snippet when a cluster administrator defines a list of sub-catalogs, which are enabled in the Web Console.
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Enabled
        enabled:
          - BuilderImage
          - Devfile
          - HelmChart
          - ...
----