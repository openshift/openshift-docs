// Module included in the following assemblies:
//
// * storage/generic-ephemeral-vols.adoc
//* microshift_storage/generic-ephemeral-volumes-microshift.adoc

:_mod-docs-content-type: CONCEPT
[id="generic-ephemeral-security_{context}"]
= Security

You can enable the generic ephemeral volume feature to allows users who can create pods to also create persistent volume claims (PVCs) indirectly. This feature works even if these users do not have permission to create PVCs directly. Cluster administrators must be aware of this. If this does not fit your security model, use an admission webhook that rejects objects such as pods that have a generic ephemeral volume.

The normal namespace quota for PVCs still applies, so even if users are allowed to use this new mechanism, they cannot use it to circumvent other policies.
