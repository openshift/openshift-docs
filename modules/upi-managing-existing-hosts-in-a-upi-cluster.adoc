// Module included in the following assemblies:
//
// * installing/installing_bare_metal/scaling-a-user-provisioned-cluster-with-the-bare-metal-operator.adoc
:_mod-docs-content-type: PROCEDURE
[id="upi-managing-existing-hosts-in-a-upi-cluster_{context}"]
= Optional: Managing existing hosts in a user-provisioned cluster by using the BMO

Optionally, you can use the Bare Metal Operator (BMO) to manage existing bare-metal controller hosts in a user-provisioned cluster by creating a `BareMetalHost` object for the existing host.
It is not a requirement to manage existing user-provisioned hosts; however, you can enroll them as externally-provisioned hosts for inventory purposes.

[IMPORTANT]
====
To manage existing hosts by using the BMO, you must set the `spec.externallyProvisioned` specification in the `BareMetalHost` custom resource to `true` to prevent the BMO from re-provisioning the host.
====

.Prerequisites

* You created a user-provisioned bare-metal cluster.
* You have baseboard management controller (BMC) access to the hosts.
* You deployed a provisioning service in the cluster by creating a `Provisioning` CR.

.Procedure

. Create the `Secret` CR and the `BareMetalHost` CR.

.. Save the following YAML in the `controller.yaml` file:
+
[source,yaml]
----
---
apiVersion: v1
kind: Secret
metadata:
  name: controller1-bmc
  namespace: openshift-machine-api
type: Opaque
data:
  username: <base64_of_uid>
  password: <base64_of_pwd>
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: controller1
  namespace: openshift-machine-api
spec:
  bmc:
    address: <protocol>://<bmc_url> <1>
    credentialsName: "controller1-bmc"
  bootMACAddress: <nic1_mac_address>
  customDeploy:
    method: install_coreos
  externallyProvisioned: true <2>
  online: true
  userData:
    name: controller-user-data-managed
    namespace: openshift-machine-api
----
<1> You can only use bare-metal host drivers that support virtual media networking booting, for example `redfish-virtualmedia` and `idrac-virtualmedia`.
<2> You must set the value to true to prevent the BMO from re-provisioning the bare-metal controller host.

. Create the bare-metal host object by running the following command:
+
[source,terminal]
----
$ oc create -f controller.yaml
----
+
.Example output
[source,terminal]
----
secret/controller1-bmc created
baremetalhost.metal3.io/controller1 created
----

.Verification

* Verify that the BMO created the bare-metal host object by running the following command:
+
[source,terminal]
----
$ oc get bmh -A
----
+
.Example output
[source,terminal]
----
NAMESPACE               NAME          STATE                    CONSUMER   ONLINE   ERROR   AGE
openshift-machine-api   controller1   externally provisioned              true             13s
----

