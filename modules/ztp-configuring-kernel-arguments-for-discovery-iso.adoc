// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc
:_mod-docs-content-type: PROCEDURE
[id="setting-managed-bare-metal-host-kernel-arguments_{context}"]
= Configuring Discovery ISO kernel arguments for installations using {ztp}

The {ztp-first} workflow uses the Discovery ISO as part of the {product-title} installation process on managed bare-metal hosts. You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO. This is useful for cluster installations with specific environmental requirements. For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation.

[NOTE]
====
In {product-title} {product-version}, you can only add kernel arguments. You can not replace or delete kernel arguments.
====

.Prerequisites

* You have installed the OpenShift CLI (oc).
* You have logged in to the hub cluster as a user with cluster-admin privileges.

.Procedure

. Create the `InfraEnv` CR and edit the `spec.kernelArguments` specification to configure kernel arguments.

.. Save the following YAML in an `InfraEnv-example.yaml` file:
+
[NOTE]
====
The `InfraEnv` CR in this example uses template syntax such as `{{ .Cluster.ClusterName }}` that is populated based on values in the `SiteConfig` CR. The `SiteConfig` CR automatically populates values for these templates during deployment. Do not edit the templates manually.
====
+
[source,yaml]
----
apiVersion: agent-install.openshift.io/v1beta1
kind: InfraEnv
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"
  name: "{{ .Cluster.ClusterName }}"
  namespace: "{{ .Cluster.ClusterName }}"
spec:
  clusterRef:
    name: "{{ .Cluster.ClusterName }}"
    namespace: "{{ .Cluster.ClusterName }}"
  kernelArguments:
    - operation: append <1>
      value: audit=0 <2>
    - operation: append
      value: trace=1
  sshAuthorizedKey: "{{ .Site.SshPublicKey }}"
  proxy: "{{ .Cluster.ProxySettings }}"
  pullSecretRef:
    name: "{{ .Site.PullSecretRef.Name }}"
  ignitionConfigOverride: "{{ .Cluster.IgnitionConfigOverride }}"
  nmStateConfigLabelSelector:
    matchLabels:
      nmstate-label: "{{ .Cluster.ClusterName }}"
  additionalNTPSources: "{{ .Cluster.AdditionalNTPSources }}"
----
<1> Specify the append operation to add a kernel argument.
<2> Specify the kernel argument you want to configure. This example configures the audit kernel argument and the trace kernel argument.

. Commit the `InfraEnv-example.yaml` CR to the same location in your Git repository that has the `SiteConfig` CR and push your changes. The following example shows a sample Git repository structure:

+
[source,text]
----
~/example-ztp/install
          └── site-install
               ├── siteconfig-example.yaml
               ├── InfraEnv-example.yaml
               ...
----

. Edit the `spec.clusters.crTemplates` specification in the `SiteConfig` CR to reference the `InfraEnv-example.yaml` CR in your Git repository:
+
[source,yaml,options="nowrap",role="white-space-pre"]
----
clusters:
  crTemplates:
    InfraEnv: "InfraEnv-example.yaml"
----
+
When you are ready to deploy your cluster by committing and pushing the `SiteConfig` CR, the build pipeline uses the custom `InfraEnv-example` CR in your Git repository to configure the infrastructure environment, including the custom kernel arguments.

.Verification
To verify that the kernel arguments are applied, after the Discovery image verifies that {product-title} is ready for installation, you can SSH to the target host before the installation process begins. At that point, you can view the kernel arguments for the Discovery ISO in the `/proc/cmdline` file.

. Begin an SSH session with the target host:
+
[source,terminal]
----
$ ssh -i /path/to/privatekey core@<host_name>
----

. View the system's kernel arguments by using the following command:
+
[source,terminal]
----
$ cat /proc/cmdline
----
