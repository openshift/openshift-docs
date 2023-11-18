// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

:_mod-docs-content-type: PROCEDURE
[id="secrets-store-sync-secrets_{context}"]
= Enabling synchronization of mounted content as Kubernetes secrets

You can enable synchronization to create Kubernetes secrets from the content on a mounted volume. An example where you might want to enable synchronization is to use an environment variable in your deployment to reference the Kubernetes secret.

[WARNING]
====
Do not enable synchronization if you do not want to store your secrets on your {product-title} cluster and in etcd. Enable this functionality only if you require it, such as when you want to use environment variables to refer to the secret.
====

If you enable synchronization, the secrets from the mounted volume are synchronized as Kubernetes secrets after you start a pod that mounts the secrets.

The synchronized Kubernetes secret is deleted when all pods that mounted the content are deleted.

.Prerequisites

* You have installed the {secrets-store-operator}.
* You have installed a secrets store provider.
* You have created the secret provider class.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the `SecretProviderClass` resource by running the following command:
+
[source,terminal]
----
$ oc edit secretproviderclass my-azure-provider <1>
----
<1> Replace `my-azure-provider` with the name of your secret provider class.

. Add the `secretsObjects` section with the configuration for the synchronized Kubernetes secrets:
+
[source,yaml]
----
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: my-azure-provider
  namespace: my-namespace
spec:
  provider: azure
  secretObjects:                                   <1>
    - secretName: tlssecret                        <2>
      type: kubernetes.io/tls                      <3>
      labels:
        environment: "test"
      data:
        - objectName: tlskey                       <4>
          key: tls.key                             <5>
        - objectName: tlscrt
          key: tls.crt
  parameters:
    usePodIdentity: "false"
    keyvaultName: "kvname"
    objects:  |
      array:
        - |
          objectName: tlskey
          objectType: secret
        - |
          objectName: tlscrt
          objectType: secret
    tenantId: "tid"
----
<1> Specify the configuration for synchronized Kubernetes secrets.
<2> Specify the name of the Kubernetes `Secret` object to create.
<3> Specify the type of Kubernetes `Secret` object to create. For example, `Opaque` or `kubernetes.io/tls`.
<4> Specify the object name or alias of the mounted content to synchronize.
<5> Specify the data field from the specified `objectName` to populate the Kubernetes secret with.

. Save the file to apply the changes.
