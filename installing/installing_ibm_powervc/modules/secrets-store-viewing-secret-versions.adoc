// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets-store.adoc

:_mod-docs-content-type: PROCEDURE
[id="secrets-store-viewing-secret-versions_{context}"]
= Viewing the status of secrets in the pod volume mount

You can view detailed information, including the versions, of the secrets in the pod volume mount.

The {secrets-store-operator} creates a `SecretProviderClassPodStatus` resource in the same namespace as the pod. You can review this resource to see detailed information, including versions, about the secrets in the pod volume mount.

.Prerequisites

* You have installed the {secrets-store-operator}.
* You have installed a secrets store provider.
* You have created the secret provider class.
* You have deployed a pod that mounts a volume from the {secrets-store-operator}.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

* View detailed information about the secrets in a pod volume mount by running the following command:
+
[source,terminal]
----
$ oc get secretproviderclasspodstatus <secret_provider_class_pod_status_name> -o yaml <1>
----
<1> The name of the secret provider class pod status object is in the format of `<pod_name>-<namespace>-<secret_provider_class_name>`.
+
.Example output
[source,terminal]
----
...
status:
  mounted: true
  objects:
  - id: secret/tlscrt
    version: f352293b97da4fa18d96a9528534cb33
  - id: secret/tlskey
    version: 02534bc3d5df481cb138f8b2a13951ef
  podName: busybox-<hash>
  secretProviderClassName: my-azure-provider
  targetPath: /var/lib/kubelet/pods/f0d49c1e-c87a-4beb-888f-37798456a3e7/volumes/kubernetes.io~csi/secrets-store-inline/mount
----
