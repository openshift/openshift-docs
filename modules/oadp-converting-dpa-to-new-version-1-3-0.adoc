// Module included in the following assemblies:
//
// * backup_and_restore/oadp-release-notes-1-3.adoc

:_mod-docs-content-type: PROCEDURE

[id="oadp-converting-dpa-to-new-version-1-3-0_{context}"]
= Converting DPA to the new version

If you need to move backups off cluster with the Data Mover, reconfigure the `DataProtectionApplication` (DPA) manifest as follows.

.Procedure
. Click *Operators* → *Installed Operators* and select the OADP Operator.
. In the *Provided APIs* section, click *View more*.
. Click *Create instance* in the *DataProtectionApplication* box.
. Click *YAML View* to display the current DPA parameters.
+
.Example current DPA
[source,yaml]
----
spec:
  configuration:
    features:
      dataMover:
      enable: true
      credentialName: dm-credentials
    velero:
      defaultPlugins:
      - vsm
      - csi
      - openshift
# ...
----

. Update the DPA parameters:
* Remove the `features.dataMover` key and values from the DPA.
* Remove the VolumeSnapshotMover (VSM) plugin.
* Add the `nodeAgent` key and values.
+
.Example updated DPA
[source,yaml]
----
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    velero:
      defaultPlugins:
      - csi
      - openshift
# ...
----

. Wait for the DPA to reconcile successfully.
