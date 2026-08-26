// Module included in the following assemblies:
//
// * security/nbde_tang_server_operator/nbde-tang-server-operator-configuring-managing.adoc

:_mod-docs-content-type: PROCEDURE
[id="rotating-keys-using-nbde-tang-server-operator_{context}"]
= Rotating keys using the NBDE Tang Server Operator

With the NBDE Tang Server Operator, you also can rotate your Tang server keys. The precise interval at which you should rotate them depends on your application, key sizes, and institutional policy.

.Prerequisites

* You must have `cluster-admin` privileges on an {product-title} cluster.
* You deployed a Tang server using the NBDE Tang Server Operator on your OpenShift cluster.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List the existing keys on your Tang server, for example:
+
[source,terminal]
----
$ oc -n nbde describe tangserver
----
+
.Example output
[source,terminal]
----
…
Status:
  Active Keys:
	File Name:  	QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
	Generated:  	2022-02-08 15:44:17.030090484 +0000
	sha1:       	PvYQKtrTuYsMV2AomUeHrUWkCGg
	sha256:     	QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
…	
----
. Create a YAML file for moving your active keys to hidden keys, for example, `minimal-keyretrieve-rotate-tangserver.yaml`:
+
.Example key-rotation YAML for tang-operator
[source,yaml]
----
apiVersion: daemons.redhat.com/v1alpha1
kind: TangServer
metadata:
  name: tangserver
  namespace: nbde
  finalizers:
    - finalizer.daemons.tangserver.redhat.com
spec:
  replicas: 1
  hiddenKeys:
    - sha1: "PvYQKtrTuYsMV2AomUeHrUWkCGg" <1>
----
<1> Specify the SHA-1 thumbprint of your active key to rotate it.

. Apply the YAML file:
+
[source,terminal]
----
$ oc apply -f minimal-keyretrieve-rotate-tangserver.yaml
----

.Verification

. After a certain amount of time depending on your configuration, check that the previous `activeKey` value is the new `hiddenKey` value and the `activeKey` key file is newly generated, for example:
+
[source,terminal]
----
$ oc -n nbde describe tangserver
----
+
.Example output
[source,terminal]
----
…
Spec:
  Hidden Keys:
    sha1:    PvYQKtrTuYsMV2AomUeHrUWkCGg
  Replicas:  1
Status:
  Active Keys:
    File Name:  T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY.jwk
    Generated:  2023-10-25 15:38:18.134939752 +0000
    sha1:       vVxkNCNq7gygeeA9zrHrbc3_NZ4
    sha256:     T-0wx1HusMeWx4WMOk4eK97Q5u4dY5tamdDs7_ughnY
  Hidden Keys:
    File Name:           .QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg.jwk
    Generated:           2023-10-25 15:37:29.126928965 +0000
    Hidden:              2023-10-25 15:38:13.515467436 +0000
    sha1:                PvYQKtrTuYsMV2AomUeHrUWkCGg
    sha256:              QS82aXnPKA4XpfHr3umbA0r2iTbRcpWQ0VI2Qdhi6xg
…
----
