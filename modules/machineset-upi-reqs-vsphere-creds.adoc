// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc

:_mod-docs-content-type: PROCEDURE
[id="machineset-upi-reqs-vsphere-creds_{context}"]
= Satisfying vSphere credentials requirements

To use compute machine sets, the Machine API must be able to interact with vCenter. Credentials that authorize the Machine API components to interact with vCenter must exist in a secret in the `openshift-machine-api` namespace.

.Procedure

. To determine whether the required credentials exist, run the following command:
+
[source,terminal]
----
$ oc get secret \
  -n openshift-machine-api vsphere-cloud-credentials \
  -o go-template='{{range $k,$v := .data}}{{printf "%s: " $k}}{{if not $v}}{{$v}}{{else}}{{$v | base64decode}}{{end}}{{"\n"}}{{end}}'
----
+
.Sample output
[source,terminal]
----
<vcenter-server>.password=<openshift-user-password>
<vcenter-server>.username=<openshift-user>
----
+
where `<vcenter-server>` is the IP address or fully qualified domain name (FQDN) of the vCenter server and `<openshift-user>` and `<openshift-user-password>` are the {product-title} administrator credentials to use.

. If the secret does not exist, create it by running the following command:
+
[source,terminal]
----
$ oc create secret generic vsphere-cloud-credentials \
  -n openshift-machine-api \
  --from-literal=<vcenter-server>.username=<openshift-user> --from-literal=<vcenter-server>.password=<openshift-user-password>
----