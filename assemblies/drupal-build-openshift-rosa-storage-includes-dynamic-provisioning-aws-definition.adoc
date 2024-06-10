// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc
// * post_installation_configuration/storage-configuration.adoc

[id="aws-definition_{context}"]
= AWS Elastic Block Store (EBS) object definition

.aws-ebs-storageclass.yaml
[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: <storage-class-name> <1>
provisioner: kubernetes.io/aws-ebs
parameters:
  type: io1 <2>
  iopsPerGB: "10" <3>
  encrypted: "true" <4>
  kmsKeyId: keyvalue <5>
  fsType: ext4 <6>
----
<1> (required) Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes.
<2> (required) Select from `io1`, `gp3`, `sc1`, `st1`. The default is `gp3`.
See the
link:http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html[AWS documentation]
for valid Amazon Resource Name (ARN) values.
<3> Optional: Only for *io1* volumes. I/O operations per second per GiB.
The AWS volume plugin multiplies this with the size of the requested
volume to compute IOPS of the volume. The value cap is 20,000 IOPS, which
is the maximum supported by AWS. See the
link:http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html[AWS documentation]
for further details.
<4> Optional: Denotes whether to encrypt the EBS volume. Valid values
are `true` or `false`.
<5> Optional: The full ARN of the key to use when encrypting the volume.
If none is supplied, but `encypted` is set to `true`, then AWS generates a
key. See the
link:http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html[AWS documentation]
for a valid ARN value.
<6> Optional: File system that is created on dynamically provisioned
volumes. This value is copied to the `fsType` field of dynamically
provisioned persistent volumes and the file system is created when the
volume is mounted for the first time. The default value is `ext4`.
