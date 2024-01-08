// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

:_mod-docs-content-type: CONCEPT
[id="secrets-store-auto-rotation_{context}"]
= Automatic rotation

The {secrets-store-driver} periodically rotates the content in the mounted volume with the content from the external secrets store. If a secret is updated in the external secrets store, the secret will be updated in the mounted volume. The {secrets-store-operator} polls for updates every 2 minutes.

If you enabled synchronization of mounted content as Kubernetes secrets, the Kubernetes secrets are also rotated.

Applications consuming the secret data must watch for updates to the secrets.
