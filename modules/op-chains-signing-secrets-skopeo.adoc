// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-chains-for-pipelines-supply-chain-security.adoc

:_mod-docs-content-type: PROCEDURE

[id="chains-signing-secrets-skopeo_{context}"]
= Signing using skopeo

You can generate keys using the `skopeo` tool and use them in the `cosign` signing scheme with {tekton-chains}.

.Prerequisites

* You installed the link:https://github.com/containers/skopeo[skopeo] tool.

.Procedure

. Generate a public/private key pair by running the following command:
+
[source,terminal]
----
$ skopeo generate-sigstore-key --output-prefix <mykey> # <1>
----
<1> Replace `<mykey>` with a key name of your choice.
+
Skopeo prompts you for a passphrase for the private key and then creates the key files named `<mykey>.private` and `<mykey>.pub`.

. Encode the `<mykey>.pub` file using the `base64` tool by running the following command:
+
[source,terminal]
----
$ base64 -w 0 <mykey>.pub > b64.pub
----

. Encode the `<mykey>.private` file using the `base64` tool by running the following command:
+
[source,terminal]
----
$ base64 -w 0 <mykey>.private > b64.private
----

. Encode the passhprase using the `base64` tool by running the following command:
+
[source,terminal]
----
$ echo -n '<passphrase>' | base64 -w 0 > b64.passphrase # <1>
----
<1> Replace `<passphrase>` with the passphrase that you used for the key pair.

. Create the `signing-secrets` secret in the `openshift-pipelines` namespace by running the following command:
+
[source,terminal]
----
$ oc create secret generic signing-secrets -n openshift-pipelines
----
+
. Edit the `signing-secrets` secret by running the following command:
+
----
$ oc edit secret -n openshift-pipelines signing-secrets
----
+
Add the encoded keys in the data of the secret in the following way:
+
[source,yaml]
----
apiVersion: v1
data:
  cosign.key: <Encoded <mykey>.private> # <1>
  cosign.password: <Encoded passphrase> # <2>
  cosign.pub: <Encoded <mykey>.pub> # <3>
immutable: true
kind: Secret
metadata:
  name: signing-secrets
# ...
type: Opaque
----
<1> Replace `<Encoded <mykey>.private>` with the content of the `b64.private` file.
<2> Replace `<Encoded passphrase>` with the content of the `b64.passphrase` file.
<3> Replace `<Encoded <mykey>.pub>` with the content of the `b64.pub` file.
