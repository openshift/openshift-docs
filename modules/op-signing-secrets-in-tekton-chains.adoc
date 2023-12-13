// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-chains-for-pipelines-supply-chain-security.adoc

:_mod-docs-content-type: CONCEPT
[id="signing-secrets-in-tekton-chains_{context}"]
= Secrets for signing data in {tekton-chains}

[role="_abstract"]
Cluster administrators can generate a key pair and use {tekton-chains} to sign artifacts using a Kubernetes secret. For {tekton-chains} to work, a private key and a password for encrypted keys must exist as part of the `signing-secrets` secret in the `openshift-pipelines` namespace.

Currently, {tekton-chains} supports the `x509` and `cosign` signature schemes.

[NOTE]
====
Use only one of the supported signature schemes.
====

To use the `x509` signing scheme with {tekton-chains}, store the `x509.pem` private key of the `ed25519` or `ecdsa` type in the `signing-secrets` Kubernetes secret.
