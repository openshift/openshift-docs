// Module included in the following assemblies:
//
// * storage/generic-ephemeral-vols.adoc
// * microshift_storage/generic-ephemeral-volumes-microshift.adoc

:_mod-docs-content-type: CONCEPT
[id="generic-ephemeral-vols-pvc-naming_{context}"]
= Persistent volume claim naming

Automatically created persistent volume claims (PVCs) are named by a combination of the pod name and the volume name, with a hyphen (-) in the middle. This naming convention also introduces a potential conflict between different pods, and between pods and manually created PVCs.

For example, `pod-a` with volume `scratch` and `pod` with volume `a-scratch` both end up with the same PVC name, `pod-a-scratch`.

Such conflicts are detected, and a PVC is only used for an ephemeral volume if it was created for the pod. This check is based on the ownership relationship. An existing PVC is not overwritten or modified, but this does not resolve the conflict. Without the right PVC, a pod cannot start.

[IMPORTANT]
====
Be careful when naming pods and volumes inside the same namespace so that naming conflicts do not occur.
====
