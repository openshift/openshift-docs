// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-pipelines-as-code-cli_{context}"]
= Installing {pac} CLI

[role="_abstract"]
Cluster administrators can use the `tkn pac` and `opc` CLI tools on local machines or as containers for testing. The `tkn pac` and `opc` CLI tools are installed automatically when you install the `tkn` CLI for {pipelines-title}.

You can install the `tkn pac` and `opc` version `1.11.0` binaries for the supported platforms:

* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.11.0/tkn-linux-amd64.tar.gz[Linux (x86_64, amd64)]
* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.11.0/tkn-linux-s390x.tar.gz[Linux on {ibm-z-name} and {ibm-linuxone-name} (s390x)]
* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.11.0/tkn-linux-ppc64le.tar.gz[Linux on {ibm-power-name} (ppc64le)]
* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.11.0/tkn-macos-amd64.tar.gz[macOS]
* link:https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.11.0/tkn-windows-amd64.zip[Windows]

// In addition, you can install `tkn pac` using the following methods:

// [CAUTION]
// ====
// The `tkn pac` CLI tool available using these methods is _not updated regularly_.
// ====

// * Install on Linux or Mac OS using the `brew` package manager:
// +
// [source,terminal]
// ----
// $ brew install openshift-pipelines/pipelines-as-code/tektoncd-pac
// ----
// +
// You can upgrade the package by running the following command:
// +
// [source,terminal]
// ----
// $ brew upgrade openshift-pipelines/pipelines-as-code/tektoncd-pac
// ----

// * Install as a container using `podman`:
// +
// [source,terminal]
// ----
// $ podman run -e KUBECONFIG=/tmp/kube/config -v ${HOME}/.kube:/tmp/kube \
//      -it quay.io/openshift-pipeline/pipelines-as-code tkn pac help
// ----
// +
// You can also use `docker` as a substitute for `podman`.

// * Install from the GitHub repository using `go`:
// +
// [source,terminal]
// ----
// $ go install github.com/openshift-pipelines/pipelines-as-code/cmd/tkn-pac
// ----