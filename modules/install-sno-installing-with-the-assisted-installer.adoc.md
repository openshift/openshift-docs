# Installing single-node Openshift with the Assisted Installer

Use the Assisted Installer to install the single-node cluster.

1. Attach the {op-system} discovery ISO to the target host.
2. Configure the boot drive order in the server BIOS settings to boot from the attached discovery ISO and then reboot the server.
3. On the administration host, return to the browser. Wait for the host to appear in the list of discovered hosts. If necessary, reload the [**Assisted Clusters**](https://console.redhat.com/openshift/assisted-installer/clusters) page and select the cluster name.
4. Complete the install wizard steps. Add networking details, including a subnet from the available subnets. Add the SSH public key if necessary.
5. Monitor the installation’s progress. Watch the cluster events. After the installation process finishes writing the operating system image to the server’s hard disk, the server restarts.
6. Remove the discovery ISO, and reset the server to boot from the installation drive.

   The server restarts several times automatically, deploying the control plane.
