// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-security.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-cert-manage-add-cert-key_{context}"]
== Adding an existing certificate and key

To use an existing signing (CA) certificate and key, you must create a chain of trust file that includes the CA certificate, key, and root certificate. You must use the following exact file names for each of the corresponding certificates. The CA certificate is named `ca-cert.pem`, the key is `ca-key.pem`, and the root certificate, which signs `ca-cert.pem`, is named `root-cert.pem`. If your workload uses intermediate certificates, you must specify them in a `cert-chain.pem` file.

. Save the example certificates from the link:https://github.com/maistra/istio/tree/maistra-{MaistraVersion}/samples/certs[Maistra repository] locally and replace `<path>` with the path to your certificates.

. Create a secret named `cacert` that includes the input files `ca-cert.pem`, `ca-key.pem`, `root-cert.pem` and `cert-chain.pem`.
+
[source,terminal]
----
$ oc create secret generic cacerts -n istio-system --from-file=<path>/ca-cert.pem \
    --from-file=<path>/ca-key.pem --from-file=<path>/root-cert.pem \
    --from-file=<path>/cert-chain.pem
----
+
. In the `ServiceMeshControlPlane` resource set `spec.security.dataPlane.mtls true` to `true` and configure the `certificateAuthority` field as shown in the following example. The default `rootCADir` is `/etc/cacerts`. You do not need to set the `privateKey` if the key and certs are mounted in the default location.  {SMProductShortName} reads the certificates and key from the secret-mount files.
+
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
spec:
  security:
    dataPlane:
      mtls: true
    certificateAuthority:
      type: Istiod
      istiod:
        type: PrivateKey
        privateKey:
          rootCADir: /etc/cacerts
----

. After creating/changing/deleting the `cacert` secret, the {SMProductShortName} control plane `istiod` and `gateway` pods must be restarted so the changes go into effect. Use the following command to restart the pods:
+
[source,terminal]
----
$ oc -n istio-system delete pods -l 'app in (istiod,istio-ingressgateway, istio-egressgateway)'
----
+
The Operator will automatically recreate the pods after they have been deleted.

. Restart the bookinfo application pods so that the sidecar proxies pick up the secret changes. Use the following command to restart the pods:
+
[source,terminal]
----
$ oc -n bookinfo delete pods --all
----
+
You should see output similar to the following:
+

[source,terminal]
----
pod "details-v1-6cd699df8c-j54nh" deleted
pod "productpage-v1-5ddcb4b84f-mtmf2" deleted
pod "ratings-v1-bdbcc68bc-kmng4" deleted
pod "reviews-v1-754ddd7b6f-lqhsv" deleted
pod "reviews-v2-675679877f-q67r2" deleted
pod "reviews-v3-79d7549c7-c2gjs" deleted
----

. Verify that the pods were created and are ready with the following command:
+

[source,terminal]
----
$ oc get pods -n bookinfo
----
