// Module included in the following assemblies:
//
// * installing/install_config/installing-restricted-networks-preparations.adoc
// * openshift_images/samples-operator-alt-registry.adoc

[id="installation-local-registry-pull-secret_{context}"]
= Creating a pull secret for your mirror registry

In a restricted network, you create a pull secret that contains only
the information for your registry.

.Prerequisites

* You configured a mirror registry to use in your restricted network and have its domain name and port as well as credentials for it.

.Procedure

. On the mirror host, generate the pull secret for your registry:
+
----
$ podman login --authfile ~/pullsecret_config.json <local_registry_host_name>:<local_registry_host_port> <1>
----
<1> For `<local_registry_host_name>`, specify the registry domain name
for your mirror registry, such as `registry.example.com`. For
`<local_registry_host_port>`, specify the port that your mirror registry uses to
serve content.
+
Provide your credentials for the mirror registry at the prompts.

. View the pull secret that you created:
+
----
# cat ~/pullsecret_config.json

{ "auths": { "<local_registry_host_name>:<local_registry_host_port>": { "auth": "ZHVtbXk6ZHVtbXk=" } } }
----
