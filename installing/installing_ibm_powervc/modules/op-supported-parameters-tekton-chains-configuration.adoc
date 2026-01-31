// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-chains-for-pipelines-supply-chain-security.adoc

:_mod-docs-content-type: REFERENCE
[id="supported-parameters-tekton-chains-configuration_{context}"]
= Supported parameters for {tekton-chains} configuration

Cluster administrators can use various supported parameter keys and values to configure specifications about task runs, OCI images, and storage.

[id="chains-supported-parameters-task-run_{context}"]
== Supported parameters for task run artifacts

.Chains configuration: Supported parameters for task run artifacts
[options="header"]
|===

| Key | Description | Supported values | Default value

| `artifacts.taskrun.format`
| The format for storing task run payloads.
| `in-toto`, `slsa/v1`
| `in-toto`

| `artifacts.taskrun.storage`
| The storage backend for task run signatures. You can specify multiple backends as a comma-separated list, such as `“tekton,oci”`. To disable storing task run artifacts, provide an empty string `“”`.
| `tekton`, `oci`, `gcs`, `docdb`, `grafeas`
| `tekton`

| `artifacts.taskrun.signer`
| The signature backend for signing task run payloads.
| `x509`,`kms`
| `x509`

|===

[NOTE]
====
`slsa/v1` is an alias of `in-toto` for backwards compatibility.
====

[id="chains-supported-parameters-pipeline-run_{context}"]
== Supported parameters for pipeline run artifacts

.Chains configuration: Supported parameters for pipeline run artifacts
[options="header"]
|===

| Parameter | Description | Supported values | Default value

| `artifacts.pipelinerun.format`
| The format for storing pipeline run payloads.
| `in-toto`, `slsa/v1`
| `in-toto`

| `artifacts.pipelinerun.storage`
| The storage backend for storing pipeline run signatures. You can specify multiple backends as a comma-separated list, such as `“tekton,oci”`. To disable storing pipeline run artifacts, provide an empty string `“”`.
| `tekton`, `oci`, `gcs`, `docdb`, `grafeas`
| `tekton`

| `artifacts.pipelinerun.signer`
| The signature backend for signing pipeline run payloads.
| `x509`, `kms`
| `x509`
|===

[NOTE]
====
* `slsa/v1` is an alias of `in-toto` for backwards compatibility.
* For the `grafeas` storage backend, only Container Analysis is supported. You can not configure the `grafeas` server address in the current version of {tekton-chains}.
====

[id="chains-supported-parameters-oci_{context}"]
== Supported parameters for OCI artifacts

.Chains configuration: Supported parameters for OCI artifacts
[options="header"]
|===

| Parameter | Description | Supported values | Default value

| `artifacts.oci.format`
| The format for storing OCI payloads.
| `simplesigning`
| `simplesigning`

| `artifacts.oci.storage`
| The storage backend for storing OCI signatures. You can specify multiple backends as a comma-separated list, such as `“oci,tekton”`. To disable storing OCI artifacts, provide an empty string `“”`.
| `tekton`, `oci`, `gcs`, `docdb`, `grafeas`
| `oci`

| `artifacts.oci.signer`
| The signature backend for signing OCI payloads.
| `x509`, `kms`
| `x509`

|===

[id="chains-supported-parameters-kms_{context}"]
== Supported parameters for KMS signers

.Chains configuration: Supported parameters for KMS signers
|===
| Parameter | Description | Supported values | Default value

| `signers.kms.kmsref`
| The URI reference to a KMS service to use in `kms` signers.
| Supported schemes: `gcpkms://`, `awskms://`, `azurekms://`, `hashivault://`. See link:https://docs.sigstore.dev/cosign/kms_support[KMS Support] in the Sigstore documentation for more details.
|
|===

[id="chains-supported-parameters-storage_{context}"]
== Supported parameters for storage

.Chains configuration: Supported parameters for storage
[options="header"]
|===

| Parameter | Description | Supported values | Default value

| `storage.gcs.bucket`
| The GCS bucket for storage
|
|

| `artifacts.oci.repository`
| The OCI repository for storing OCI signatures and attestation.
| If you configure one of the artifact storage backends to `oci` and do not define this key, {tekton-chains} stores the attestation alongside the stored OCI artifact itself. If you define this key, the attestation is not stored alongside the OCI artifact and is instead stored in the designated location. See the link:https://github.com/sigstore/cosign#specifying-registry[cosign documentation] for additional information.
|

| `builder.id`
| The builder ID to set for in-toto attestations
|
| `+https://tekton.dev/chains/v2+`

|===

If you enable the `docdb` storage method is for any artifacts, configure docstore storage options. For more information about the go-cloud docstore URI format, see the link:https://gocloud.dev/howto/docstore/[docstore package documentation]. {pipelines-title} supports the following docstore services:

* `firestore`
* `dynamodb`

.Chains configuration: Supported parameters for `docstore` storage
[options="header"]
|===

| Parameter | Description | Supported values | Default value


| `storage.docdb.url`
| The go-cloud URI reference to a `docstore` collection. Used if the `docdb` storage method is enabled for any artifacts.
| `firestore://projects/[PROJECT]/databases/(default)/documents/[COLLECTION]?name_field=name`
|

|===

If you enable the `grafeas` storage method for any artifacts, configure Grafeas storage options. For more information about Grafeas notes and occurrences, see link:https://github.com/grafeas/grafeas/blob/master/docs/grafeas_concepts.md[Grafeas concepts].

To create occurrences, {pipelines-title} must first create notes that are used to link occurrences. {pipelines-title} creates two types of occurrences: `ATTESTATION` Occurrence and `BUILD` Occurrence.

{pipelines-title} uses the configurable `noteid` as the prefix of the note name. It appends the suffix `-simplesigning` for the `ATTESTATION` note and the suffix `-intoto` for the `BUILD` note. If the `noteid` field is not configured, {pipelines-title} uses `tekton-<NAMESPACE>` as the prefix.

.Chains configuration: Supported parameters for Grafeas storage
[options="header"]
|===

| Parameter | Description | Supported values | Default value

| `storage.grafeas.projectid`
| The {product-title} project in which the Grafeas server for storing occurrences is located.
|
|

| `storage.grafeas.noteid`
| Optional: the prefix to use for the name of all created notes.
| A string without spaces.
|

| `storage.grafeas.notehint`
| Optional: the https://github.com/grafeas/grafeas/blob/cd23d4dc1bef740d6d6d90d5007db5c9a2431c41/proto/v1/attestation.proto#L49[`human_readable_name`] field for the Grafeas `ATTESTATION` note.
|
|`This attestation note was generated by Tekton Chains`
|===

Optionally, you can enable additional uploads of binary transparency attestations.

.Chains configuration: Supported parameters for transparency attestation storage
[options="header"]
|===

| Parameter | Description | Supported values | Default value

| `transparency.enabled`
| Enable or disable automatic binary transparency uploads.
| `true`, `false`, `manual`
| `false`

| `transparency.url`
| The URL for uploading binary transparency attestations, if enabled.
|
| `+https://rekor.sigstore.dev+`
|===

NOTE: If you set `transparency.enabled` to `manual`, only task runs and pipeline runs with the following annotation are uploaded to the transparency log:

[source,yaml]
----
chains.tekton.dev/transparency-upload: "true"
----

If you configure the `x509` signature backend, you can optionally enable keyless signing with Fulcio.

.Chains configuration: Supported parameters for `x509` keyless signing with Fulcio
[options="header"]
|===

| Parameter | Description | Supported values | Default value

| `signers.x509.fulcio.enabled`
| Enable or disable requesting automatic certificates from Fulcio.
| `true`, `false`
| `false`

| `signers.x509.fulcio.address`
| The Fulcio address for requesting certificates, if enabled.
|
| `+https://v1.fulcio.sigstore.dev+`

| `signers.x509.fulcio.issuer`
| The expected OIDC issuer.
|
| `+https://oauth2.sigstore.dev/auth+`

| `signers.x509.fulcio.provider`
| The provider from which to request the ID Token.
| `google`, `spiffe`, `github`, `filesystem`
| {pipelines-title} attempts to use every provider

| `signers.x509.identity.token.file`
| Path to the file containing the ID Token.
|
|

| `signers.x509.tuf.mirror.url`
| The URL for the TUF server. `$TUF_URL/root.json` must be present.
|
| `+https://sigstore-tuf-root.storage.googleapis.com+`
|===

If you configure the `kms` signature backend, set the KMS configuration, including OIDC and Spire, as necessary.

.Chains configuration: Supported parameters for KMS signing
[options="header"]
|===

| Parameter | Description | Supported values | Default value

| `signers.kms.auth.address`
| URI of the KMS server (the value of `VAULT_ADDR`).

| `signers.kms.auth.token`
| Authentication token for the KMS server (the value of `VAULT_TOKEN`).

| `signers.kms.auth.oidc.path`
| The path for OIDC authentication (for example, `jwt` for Vault).

| `signers.kms.auth.oidc.role`
| The role for OIDC authentication.

| `signers.kms.auth.spire.sock`
| The URI of the Spire socket for the KMS token (for example, `unix:///tmp/spire-agent/public/api.sock`).

| `signers.kms.auth.spire.audience`
| The audience for requesting a SVID from Spire.
|===
