// Module included in the following assembly:
//
// * virt/storage/virt-automatic-bootsource-updates.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="virt-managing-auto-update-all-system-boot-sources_{context}"]
= Managing automatic updates for all system-defined boot sources

Disabling automatic boot source imports and updates can lower resource usage. In disconnected environments, disabling automatic boot source updates prevents `CDIDataImportCronOutdated` alerts from filling up logs.

To disable automatic updates for all system-defined boot sources, turn off the `enableCommonBootImageImport` feature gate by setting the value to `false`. Setting this value to `true` re-enables the feature gate and turns automatic updates back on.

[NOTE]
====
Custom boot sources are not affected by this setting.
====

.Procedure

* Toggle the feature gate for automatic boot source updates by editing the `HyperConverged` custom resource (CR).

** To disable automatic boot source updates, set the `spec.featureGates.enableCommonBootImageImport` field in the `HyperConverged` CR to `false`. For example:
+
[source,terminal,subs="attributes+"]
----
$ oc patch hyperconverged kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op": "replace", "path": \
  "/spec/featureGates/enableCommonBootImageImport", \
  "value": false}]'
----

** To re-enable automatic boot source updates, set the `spec.featureGates.enableCommonBootImageImport` field in the `HyperConverged` CR to `true`. For example:
+
[source,terminal,subs="attributes+"]
----
$ oc patch hyperconverged kubevirt-hyperconverged -n {CNVNamespace} \
  --type json -p '[{"op": "replace", "path": \
  "/spec/featureGates/enableCommonBootImageImport", \
  "value": true}]'
----