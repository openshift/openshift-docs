// Module included in the following assemblies:
//
// * registry/configuring-registry-operator.adoc
// * openshift_images/image-configuration.adoc
// * post_installation_configuration/preparing-for-users.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-configuration-cas_{context}"]
= Configuring additional trust stores for image registry access

The `image.config.openshift.io/cluster` custom resource can contain a reference to a config map that contains additional certificate authorities to be trusted during image registry access.

.Prerequisites
* The certificate authorities (CA) must be PEM-encoded.

.Procedure

You can create a config map in the `openshift-config` namespace and use its name in `AdditionalTrustedCA` in the `image.config.openshift.io` custom resource to provide additional CAs that should be trusted when contacting external registries.

The config map key is the hostname of a registry with the port for which this CA is to be trusted, and the PEM certificate content is the value, for each additional registry CA to trust.

.Image registry CA config map example
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-registry-ca
data:
  registry.example.com: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
  registry-with-port.example.com..5000: | <1>
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
----
<1>  If the registry has the port, such as `registry-with-port.example.com:5000`, `:` should be replaced with `..`.

You can configure additional CAs with the following procedure.

* To configure an additional CA:
+
[source,terminal]
----
$ oc create configmap registry-config --from-file=<external_registry_address>=ca.crt -n openshift-config
----
+
[source,terminal]
----
$ oc edit image.config.openshift.io cluster
----
+
[source,yaml]
----
spec:
  additionalTrustedCA:
    name: registry-config
----
