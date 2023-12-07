// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-chains-for-pipelines-supply-chain-security.adoc

:_mod-docs-content-type: PROCEDURE

[id="chains-signing-secrets-cosign_{context}"]
= Signing using cosign

You can use the `cosign` signing scheme with {tekton-chains} using the `cosign` tool.

.Prerequisites

* You installed the link:https://docs.sigstore.dev/cosign/installation/[cosign] tool.

.Procedure

. Generate the `cosign.key` and `cosign.pub` key pairs by running the following command:
+
[source,terminal]
----
$ cosign generate-key-pair k8s://openshift-pipelines/signing-secrets
----
+
Cosign prompts you for a password and then creates a Kubernetes secret.

. Store the encrypted `cosign.key` private key and the `cosign.password` decryption password in the `signing-secrets` Kubernetes secret. Ensure that the private key is stored as an encrypted PEM file of the `ENCRYPTED COSIGN PRIVATE KEY` type.
