// Module included in the following assemblies:
//
// * installing/disconnected_install/installing-mirroring-installation-images.adoc
// * installing/disconnected_install/installing-mirroring-disconnected.adoc
// * openshift_images/samples-operator-alt-registry.adoc
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-clusters-at-scale.adoc
// * updating/updating_a_cluster/updating_disconnected_cluster/mirroring-image-repository.adoc

ifeval::["{context}" == "mirroring-ocp-image-repository"]
:restricted:
:update-oc-mirror:
endif::[]

ifeval::["{context}" == "installing-mirroring-installation-images"]
:restricted:
endif::[]

ifeval::["{context}" == "installing-mirroring-disconnected"]
:restricted:
:oc-mirror:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="installation-adding-registry-pull-secret_{context}"]
= Configuring credentials that allow images to be mirrored

Create a container image registry credentials file that allows mirroring
images from Red Hat to your mirror.

ifdef::restricted[]
[WARNING]
====
Do not use this image registry credentials file as the pull secret when you install a cluster. If you provide this file when you install cluster, all of the machines in the cluster will have write access to your mirror registry.
====
endif::restricted[]

ifdef::restricted[]
[WARNING]
====
This process requires that you have write access to a container image registry on the mirror registry and adds the credentials to a registry pull secret.
====

endif::restricted[]

.Prerequisites
ifndef::openshift-rosa,openshift-dedicated[]
* You configured a mirror registry to use in your disconnected environment.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You configured a mirror registry to use.
endif::openshift-rosa,openshift-dedicated[]
ifdef::restricted[]
* You identified an image repository location on your mirror registry to mirror images into.
* You provisioned a mirror registry account that allows images to be uploaded to that image repository.
endif::restricted[]

.Procedure

Complete the following steps on the installation host:

ifndef::openshift-origin[]
. Download your `registry.redhat.io` {cluster-manager-url-pull}.

. Make a copy of your pull secret in JSON format:
+
[source,terminal]
----
$ cat ./pull-secret | jq . > <path>/<pull_secret_file_in_json> <1>
----
<1> Specify the path to the folder to store the pull secret in and a name for the JSON file that you create.
+
The contents of the file resemble the following example:
+
[source,json]
----
{
  "auths": {
    "cloud.openshift.com": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "quay.io": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "registry.connect.redhat.com": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    },
    "registry.redhat.io": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    }
  }
}
----
// An additional step for following this procedure when using oc-mirror as part of the disconnected install process.
ifdef::oc-mirror[]
. Save the file either as `~/.docker/config.json` or `$XDG_RUNTIME_DIR/containers/auth.json`.
endif::[]
// Similar to the additional step above, except it is framed as optional because it is included in a disconnected update page (where users may or may not use oc-mirror for their process)
ifdef::update-oc-mirror[]
. Optional: If using the oc-mirror plugin, save the file either as `~/.docker/config.json` or `$XDG_RUNTIME_DIR/containers/auth.json`.
endif::[]
endif::[]

. Generate the base64-encoded user name and password or token for your mirror registry:
+
[source,terminal]
----
$ echo -n '<user_name>:<password>' | base64 -w0 <1>
BGVtbYk3ZHAtqXs=
----
<1> For `<user_name>` and `<password>`, specify the user name and password that you configured for your registry.

ifndef::openshift-origin[]
. Edit the JSON
endif::[]
ifdef::openshift-origin[]
. Create a `.json`
endif::[]
file and add a section that describes your registry to it:
+
[source,json]
----
ifndef::openshift-origin[]
  "auths": {
    "<mirror_registry>": { <1>
      "auth": "<credentials>", <2>
      "email": "you@example.com"
    }
  },
endif::[]
ifdef::openshift-origin[]
{
  "auths": {
    "<mirror_registry>": { <1>
      "auth": "<credentials>", <2>
      "email": "you@example.com"
    }
  }
}
endif::[]
----
<1> For `<mirror_registry>`, specify the registry domain name, and optionally the
port, that your mirror registry uses to serve content. For example,
`registry.example.com` or `registry.example.com:8443`
<2> For `<credentials>`, specify the base64-encoded user name and password for
the mirror registry.
+
ifndef::openshift-origin[]
The file resembles the following example:
+
[source,json]
----
{
  "auths": {
    "registry.example.com": {
      "auth": "BGVtbYk3ZHAtqXs=",
      "email": "you@example.com"
    },
    "cloud.openshift.com": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "quay.io": {
      "auth": "b3BlbnNo...",
      "email": "you@example.com"
    },
    "registry.connect.redhat.com": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    },
    "registry.redhat.io": {
      "auth": "NTE3Njg5Nj...",
      "email": "you@example.com"
    }
  }
}
----
endif::[]

////
This is not currently working as intended.
. Log in to your registry by using the following command:
+
[source,terminal]
----
$ oc registry login --to ./pull-secret.json --registry "<registry_host_and_port>" --auth-basic=<username>:<password>
----
+
Provide both the registry details and a valid user name and password for the registry.
////

ifeval::["{context}" == "installing-mirroring-installation-images"]
:!restricted:
endif::[]

ifeval::["{context}" == "mirroring-ocp-image-repository"]
:!restricted:
:!update-oc-mirror:
endif::[]

ifeval::["{context}" == "installing-mirroring-disconnected"]
:!restricted:
:!oc-mirror:
endif::[]
