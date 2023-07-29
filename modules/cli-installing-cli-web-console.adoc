ifeval::["{context}" == "updating-restricted-network-cluster"]
:restricted:
endif::[]

[id="cli-installing-cli-web-console_{context}"]
= Installing the OpenShift CLI by using the web console

You can install the {oc-first} to interact with {product-title} 
ifdef::openshift-rosa[]
(ROSA)
endif::openshift-rosa[]
ifdef::openshift-dedicated[]
clusters
endif::openshift-dedicated[]
from a web console. You can install `oc` on Linux, Windows, or macOS.

[IMPORTANT]
====
If you installed an earlier version of `oc`, you cannot use it to complete all
of the commands in 
ifndef::openshift-rosa[]
{product-title} {product-version}.
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA.
endif::openshift-rosa[]
Download and
install the new version of `oc`.
ifdef::restricted[]
If you are upgrading a cluster in a restricted network, install the `oc` version that you plan to upgrade to.
endif::restricted[]
====

ifeval::["{context}" == "updating-restricted-network-cluster"]
:!restricted:
endif::[]
