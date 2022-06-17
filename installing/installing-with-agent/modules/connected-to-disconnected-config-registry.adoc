// Module included in the following assemblies:
//
// * post_installation_configuration/connected-to-disconnected.adoc

[id="connected-to-disconnected-config-registry_{context}"]
= Configuring the cluster for the mirror registry

After creating and mirroring the images to the mirror registry, you must modify your cluster so that pods can pull images from the mirror registry.
 
You must: 

* Add the mirror registry credentials to the global pull secret.
* Add the mirror registry server certificate to the cluster.
* Create an `ImageContentSourcePolicy` custom resource (ICSP), which associates the mirror registry with the source registry.



. Add mirror registry credential to the cluster global pull-secret:
+
[source,terminal]
----
$ oc set data secret/pull-secret -n openshift-config --from-file=.dockerconfigjson=<pull_secret_location> <1>
----
<1> Provide the path to the new pull secret file.
+
For example:
+
[source,terminal]
----
$ oc set data secret/pull-secret -n openshift-config --from-file=.dockerconfigjson=.mirrorsecretconfigjson
----

. Add the CA-signed mirror registry server certificate to the nodes in the cluster:

.. Create a config map that includes the server certificate for the mirror registry
+
[source,terminal]
----
$ oc create configmap <config_map_name> --from-file=<mirror_address_host>..<port>=$path/ca.crt -n openshift-config
----
+
For example:
+
[source,terminal]
----
S oc create configmap registry-config --from-file=mirror.registry.com..443=/root/certs/ca-chain.cert.pem -n openshift-config
----

.. Use the config map to update the `image.config.openshift.io/cluster` custom resource (CR). {product-title} applies the changes to this CR to all nodes in the cluster:
+
[source,terminal]
----
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"<config_map_name>"}}}' --type=merge
----
+
For example:
+
[source,terminal]
----
$ oc patch image.config.openshift.io/cluster --patch '{"spec":{"additionalTrustedCA":{"name":"registry-config"}}}' --type=merge
----

. Create an ICSP to redirect container pull requests from the online registries to the mirror registry:

.. Create the `ImageContentSourcePolicy` custom resource:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1alpha1
kind: ImageContentSourcePolicy
metadata:
  name: mirror-ocp
spec:
  repositoryDigestMirrors:
  - mirrors:
    - mirror.registry.com:443/ocp/release <1>
    source: quay.io/openshift-release-dev/ocp-release <2>
  - mirrors:
    - mirror.registry.com:443/ocp/release
    source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
----
<1> Specifies the name of the mirror image registry and repository.
<2> Specifies the online registry and repository containing the content that is mirrored.

.. Create the ICSP object:
+
[source,terminal]
----
$ oc create -f registryrepomirror.yaml
----
+
.Example output
[source,terminal]
----
imagecontentsourcepolicy.operator.openshift.io/mirror-ocp created
----
+
{product-title} applies the changes to this CR to all nodes in the cluster.

. Verify that the credentials, CA, and ICSP for mirror registry were added:

.. Log into a node: 
+
[source,terminal]
----
$ oc debug node/<node_name>
----

.. Set `/host` as the root directory within the debug shell:
+
[source,terminal]
----
sh-4.4# chroot /host
----

.. Check the `config.json` file for the credentials:
+
[source,terminal]
----
sh-4.4# cat /var/lib/kubelet/config.json
----
+
.Example output
[source,terminal]
----
{"auths":{"brew.registry.redhat.io":{"xx=="},"brewregistry.stage.redhat.io":{"auth":"xxx=="},"mirror.registry.com:443":{"auth":"xx="}}} <1>
----
<1> Ensure that the mirror registry and credentials are present.

.. Change to the `certs.d` directory
+
[source,terminal]
----
sh-4.4# cd /etc/docker/certs.d/
----

.. List the certificates in the `certs.d` directory:
+
[source,terminal]
----
sh-4.4# ls
----
+
.Example output
----
image-registry.openshift-image-registry.svc.cluster.local:5000
image-registry.openshift-image-registry.svc:5000
mirror.registry.com:443 <1>
----
<1> Ensure that the mirror registry is in the list.

.. Check that the ICSP added the mirror registry to the `registries.conf` file:
+
[source,terminal]
----
sh-4.4# cat /etc/containers/registries.conf
----
+
.Example output
+
[source,terminal]
----
unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

[[registry]]
  prefix = ""
  location = "quay.io/openshift-release-dev/ocp-release"
  mirror-by-digest-only = true

  [[registry.mirror]]
    location = "mirror.registry.com:443/ocp/release"

[[registry]]
  prefix = ""
  location = "quay.io/openshift-release-dev/ocp-v4.0-art-dev"
  mirror-by-digest-only = true

  [[registry.mirror]]
    location = "mirror.registry.com:443/ocp/release"
----
+
The `registry.mirror` parameters indicate that the mirror registry is searched before the original registry. 

.. Exit the node.
+
[source,terminal]
----
sh-4.4# exit
----

