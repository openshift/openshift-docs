:_mod-docs-content-type: ASSEMBLY
[id="microshift-kubeconfig"]
= Cluster access with kubeconfig
include::_attributes/attributes-microshift.adoc[]
:context: microshift-kubeconfig

toc::[]

Learn about how `kubeconfig` files are used with {microshift-short} deployments. CLI tools use `kubeconfig` files to communicate with the API server of a cluster. These files provide cluster details, IP addresses, and other information needed for authentication.

include::modules/microshift-kubeconfig-overview.adoc[leveloffset=+1]

include::modules/microshift-kubeconfig-local-access.adoc[leveloffset=+1]

include::modules/microshift-accessing-cluster-locally.adoc[leveloffset=+2]

include::modules/microshift-kubeconfig-remote-con.adoc[leveloffset=+1]

include::modules/microshift-kubeconfig-generating-remote-kcfiles.adoc[leveloffset=+1]

include::modules/microshift-accessing-cluster-open-firewall.adoc[leveloffset=+2]

include::modules/microshift-accessing-cluster-remotely.adoc[leveloffset=+2]