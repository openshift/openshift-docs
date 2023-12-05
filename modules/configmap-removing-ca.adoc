// Module included in the following assemblies:
//
// * builds/setting-up-trusted-ca

:_mod-docs-content-type: PROCEDURE
[id="configmap-removing-ca_{context}"]
= Removing certificate authorities on a {product-title} cluster

You can remove certificate authorities (CA) from your cluster with the {product-title} (ROSA) CLI, `rosa`.

.Prerequisites

* You must have cluster administrator privileges.
* You have installed the ROSA CLI (`rosa`).
* Your cluster has certificate authorities added.

.Procedure

* Use the `rosa edit` command to modify the CA trust bundle. You must pass empty strings to the `--additional-trust-bundle-file` argument to clear the trust bundle from the cluster:
+
[source,terminal]
----
$ rosa edit cluster -c <cluster_name> --additional-trust-bundle-file ""
----
+
.Example Output
+
[source,yaml]
----
I: Updated cluster <cluster_name>
----

.Verification

* You can verify that the trust bundle has been removed from the cluster by using the `rosa describe` command:
+
[source,yaml]
----
$ rosa describe cluster -c <cluster_name>
----
+
Before removal, the Additional trust bundle section appears, redacting its value for security purposes:
+
[source,yaml,subs="attributes+"]
----
Name:                       <cluster_name>
ID:                         <cluster_internal_id>
External ID:                <cluster_external_id>
OpenShift Version:          {product-version}.0
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <aws_account_id>
API URL:                    <api_url>
Console URL:                <console_url>
Region:                     us-east-1
Multi-AZ:                   false
Nodes:
 - Control plane:           3
 - Infra:                   2
 - Compute:                 2
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             <host_prefix>
Proxy:
 - HTTPProxy:               <proxy_url>
Additional trust bundle:    REDACTED
----
+
After removing the proxy, the Additional trust bundle section is removed:
+
[source,yaml,subs="attributes+"]
----
Name:                       <cluster_name>
ID:                         <cluster_internal_id>
External ID:                <cluster_external_id>
OpenShift Version:          {product-version}.0
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <aws_account_id>
API URL:                    <api_url>
Console URL:                <console_url>
Region:                     us-east-1
Multi-AZ:                   false
Nodes:
 - Control plane:           3
 - Infra:                   2
 - Compute:                 2
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             <host_prefix>
Proxy:
 - HTTPProxy:               <proxy_url>
----
