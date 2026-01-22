// Module included in the following assemblies:
//
// * security/oc_compliance_plug_in/co-scans/oc-compliance-plug-in-using.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-oc-compliance_{context}"]
= Installing the oc-compliance plugin

.Procedure

. Extract the `oc-compliance` image to get the `oc-compliance` binary:
+
[source,terminal]
----
$ podman run --rm -v ~/.local/bin:/mnt/out:Z registry.redhat.io/compliance/oc-compliance-rhel8:stable /bin/cp /usr/bin/oc-compliance /mnt/out/
----
+
.Example output
+
[source,terminal]
----
W0611 20:35:46.486903   11354 manifest.go:440] Chose linux/amd64 manifest from the manifest list.
----
+
You can now run `oc-compliance`.
