// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc

[id="gluster-definition_{context}"]
= GlusterFS object definition

.glusterfs-storageclass.yaml
[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: slow
provisioner: kubernetes.io/glusterfs
parameters: <1>
  resturl: http://127.0.0.1:8081 <2>
  restuser: admin <3>
  secretName: heketi-secret <4>
  secretNamespace: default <5>
  gidMin: "40000" <6>
  gidMax: "50000" <7>
  volumeoptions: group metadata-cache, nl-cache on <8>
  volumetype: replicate:3 <9>
----
<1> Listed are mandatory and a few optional parameters. Refer to
link:https://access.redhat.com/documentation/en-us/red_hat_openshift_container_storage/3.10/html-single/operations_guide/#sect_file_reg_storageclass[Registering a Storage Class] for additional parameters.
<2> link:https://github.com/heketi/heketi[heketi] (volume management REST
service for Gluster) URL that provisions GlusterFS volumes on demand. The
general format should be `{http/https}://{IPaddress}:{Port}`. This is a
mandatory parameter for the GlusterFS dynamic provisioner. If the heketi
service is exposed as a routable service in the {product-title}, it will
have a resolvable fully qualified domain name (FQDN) and heketi service URL.
<3> heketi user who has access to create volumes. This is typically `admin`.
<4> Identification of a Secret that contains a user password to use when
talking to heketi. An empty password will be used
when both `secretNamespace` and `secretName` are omitted.
The provided secret must be of type `"kubernetes.io/glusterfs"`.
<5> The namespace of mentioned `secretName`. An empty password will be used
when both `secretNamespace` and `secretName` are omitted. The provided
Secret must be of type `"kubernetes.io/glusterfs"`.
<6> Optional. The minimum value of the GID range for volumes of this
StorageClass.
<7> Optional. The maximum value of the GID range for volumes of this
StorageClass.
<8> Optional. Options for newly created volumes. It allows for
performance tuning. See
link:https://docs.gluster.org/en/v3/Administrator%20Guide/Managing%20Volumes/#tuning-volume-options[Tuning Volume Options]
for more GlusterFS volume options.
<9> Optional. The
link:https://docs.gluster.org/en/v3/Quick-Start-Guide/Architecture/[type of volume]
to use.

[NOTE]
====
When the `gidMin` and `gidMax` values are not specified, their defaults are
2000 and 2147483647 respectively. Each dynamically provisioned volume
will be given a GID in this range (`gidMin-gidMax`). This GID is released
from the pool when the respective volume is deleted. The GID pool is
per StorageClass.
If two or more storage classes have GID ranges that overlap there may be
duplicate GIDs dispatched by the provisioner.
====

When heketi authentication is used, a Secret containing the admin key must
also exist.

[source,terminal]
----
$ oc create secret generic heketi-secret --from-literal=key=<password> -n <namespace> --type=kubernetes.io/glusterfs
----

This results in the following configuration:

.heketi-secret.yaml
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: heketi-secret
  namespace: namespace
  ...
data:
  key: cGFzc3dvcmQ= <1>
type: kubernetes.io/glusterfs
----
<1> base64 encoded password

[NOTE]
====
When the PVs are dynamically provisioned, the GlusterFS plugin
automatically creates an Endpoints and a headless Service named
`gluster-dynamic-<claimname>`. When the PVC is deleted, these dynamic
resources are deleted automatically.
====
