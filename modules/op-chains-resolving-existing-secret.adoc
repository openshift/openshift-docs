// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-chains-for-pipelines-supply-chain-security.adoc

:_mod-docs-content-type: PROCEDURE

[id="chains-resolving-existing-secret_{context}"]
= Resolving the "secret already exists" error

If the `signing-secret` secret is already populated, the command to create this secret might output the following error message:

[source,terminal]
----
Error from server (AlreadyExists): secrets "signing-secrets" already exists
----

You can resolve this error by deleting the secret.

.Procedure

. Delete the `signing-secret` secret by running the following command:
+
[source,terminal]
----
$ oc delete secret signing-secrets -n openshift-pipelines
----

. Re-create the key pairs and store them in the secret using your preferred signing scheme.
