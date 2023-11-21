// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-pod-log-verbosity_{context}"]
= Configuring {VirtProductName} pod log verbosity

You can configure the verbosity level of {VirtProductName} pod logs by editing the `HyperConverged` custom resource (CR).

.Procedure

. To set log verbosity for specific components, open the `HyperConverged` CR in your default text editor by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc edit hyperconverged kubevirt-hyperconverged -n {CNVNamespace}
----

. Set the log level for one or more components by editing the `spec.logVerbosityConfig` stanza. For example:
+
[source,yaml]
----
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  logVerbosityConfig:
    kubevirt:
      virtAPI: 5 <1>
      virtController: 4
      virtHandler: 3
      virtLauncher: 2
      virtOperator: 6
----
<1> The log verbosity value must be an integer in the range `1–9`, where a higher number indicates a more detailed log. In this example, the `virtAPI` component logs are exposed if their priority level is `5` or higher.

. Apply your changes by saving and exiting the editor.