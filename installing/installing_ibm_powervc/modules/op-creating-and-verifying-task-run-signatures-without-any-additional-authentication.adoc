// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-chains-for-pipelines-supply-chain-security.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-and-verifying-task-run-signatures-without-any-additional-authentication_{context}"]
= Creating and verifying task run signatures without any additional authentication

[role="_abstract"]
To verify signatures of task runs using {tekton-chains} with any additional authentication, perform the following tasks:

* Create an encrypted x509 key pair and save it as a Kubernetes secret.
* Configure the {tekton-chains} backend storage.
* Create a task run, sign it, and store the signature and the payload as annotations on the task run itself.
* Retrieve the signature and payload from the signed task run.
* Verify the signature of the task run.

.Prerequisites
Ensure that the following components are installed on the cluster:

* {pipelines-title} Operator
* {tekton-chains}
* link:https://docs.sigstore.dev/cosign/installation/[Cosign]

.Procedure

. Create an encrypted x509 key pair and save it as a Kubernetes secret. For more information about creating a key pair and saving it as a secret, see "Signing secrets in {tekton-chains}".
. In the {tekton-chains} configuration, disable the OCI storage, and set the task run storage and format to `tekton`. In the `TektonConfig` custom resource set the following values:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
# ...
    chain:
      artifacts.oci.storage: ""
      artifacts.taskrun.format: tekton
      artifacts.taskrun.storage: tekton
# ...
----
+
For more information about configuring {tekton-chains} using the `TektonConfig` custom resource, see "Configuring {tekton-chains}".
. To restart the {tekton-chains} controller to ensure that the modified configuration is applied, enter the following command:
+
[source.terminal]
----
$ oc delete po -n openshift-pipelines -l app=tekton-chains-controller
----

. Create a task run by entering the following command:
+
[source,terminal]
----
$ oc create -f https://raw.githubusercontent.com/tektoncd/chains/main/examples/taskruns/task-output-image.yaml <1>
----
<1> Replace the example URI with the URI or file path pointing to your task run.
+
.Example output
[source,terminal]
----
taskrun.tekton.dev/build-push-run-output-image-qbjvh created
----

. Check the status of the steps by entering the following command. Wait until the process finishes.
+
[source,terminal]
----
$ tkn tr describe --last
----
+
.Example output
[source,terminal]
----
[...truncated output...]
NAME                            STATUS
∙ create-dir-builtimage-9467f   Completed
∙ git-source-sourcerepo-p2sk8   Completed
∙ build-and-push                Completed
∙ echo                          Completed
∙ image-digest-exporter-xlkn7   Completed
----

. To retrieve the signature from the object stored as `base64` encoded annotations, enter the following commands:
+
[source,terminal]
----
$ tkn tr describe --last -o jsonpath="{.metadata.annotations.chains\.tekton\.dev/signature-taskrun-$TASKRUN_UID}" | base64 -d > sig
----
+
[source,terminal]
----
$ export TASKRUN_UID=$(tkn tr describe --last -o  jsonpath='{.metadata.uid}')
----

. To verify the signature using the public key that you created, enter the following command:
[source,terminal]
----
$ cosign verify-blob-attestation --insecure-ignore-tlog --key path/to/cosign.pub --signature sig --type slsaprovenance --check-claims=false /dev/null <1>
----
<1> Replace `path/to/cosign.pub` with the path name of the public key file.
+
.Example output
[source,terminal]
----
Verified OK
----
