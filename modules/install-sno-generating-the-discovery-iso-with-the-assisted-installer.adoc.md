# Generating the discovery ISO with the Assisted Installer

Installing {product-title} on a single node requires a discovery ISO, which the Assisted Installer can generate.

1. On the administration host, open a browser and navigate to [{cluster-manager-first}](https://console.redhat.com/openshift/assisted-installer/clusters).
2. Click **Create Cluster** to create a new cluster.
3. In the **Cluster name** field, enter a name for the cluster.
4. In the **Base domain** field, enter a base domain. For example:

   ```
   example.com
   ```

   All DNS records must be subdomains of this base domain and include the cluster name, for example:

   ```
   <cluster-name>.example.com
   ```

   <dl><dt><strong>📌 NOTE</strong></dt><dd>

   You cannot change the base domain or cluster name after cluster installation.
   </dd></dl>
5. Select **Install single node OpenShift (SNO)** and complete the rest of the wizard steps. Download the discovery ISO.
6. Make a note of the discovery ISO URL for installing with virtual media.

=====
If you enable {VirtProductName} during this process, you must have a second local storage device of at least 50GiB for your virtual machines.
=====
