// Module included in the following assemblies:
//
// * security/certificates/updating-ca-bundle.adoc

:_mod-docs-content-type: PROCEDURE
[id="ca-bundle-replacing_{context}"]
= Replacing the CA Bundle certificate

.Procedure

. Create a config map that includes the root CA certificate used to sign the wildcard certificate:
+
[source,terminal]
----
$ oc create configmap custom-ca \
     --from-file=ca-bundle.crt=</path/to/example-ca.crt> \//<1>
     -n openshift-config
----
<1> `</path/to/example-ca.crt>` is the path to the CA certificate bundle on your local file system.

. Update the cluster-wide proxy configuration with the newly created config map:
+
[source,terminal]
----
$ oc patch proxy/cluster \
     --type=merge \
     --patch='{"spec":{"trustedCA":{"name":"custom-ca"}}}'
----
