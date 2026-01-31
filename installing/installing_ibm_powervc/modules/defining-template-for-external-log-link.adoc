// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

:_mod-docs-content-type: PROCEDURE
[id="defining-template-for-external-log-links_{context}"]
= Defining a template for an external log link

If you are connected to a service that helps you browse your logs, but you need
to generate URLs in a particular way, then you can define a template for your
link.

.Prerequisites

* You must have administrator privileges.

.Procedure

. From *Administration* -> *Custom Resource Definitions*, click on
*ConsoleExternalLogLink*.
. Select *Instances* tab
. Click *Create Console External Log Link* and edit the file:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleExternalLogLink
metadata:
  name: example
spec:
  hrefTemplate: >-
    https://example.com/logs?resourceName=${resourceName}&containerName=${containerName}&resourceNamespace=${resourceNamespace}&podLabels=${podLabels}
  text: Example Logs
----
