# Monitoring the cluster installation using openshift-install

Use `openshift-install` to monitor the progress of the single-node cluster installation.

1. Attach the modified {op-system} installation ISO to the target host.
2. Configure the boot drive order in the server BIOS settings to boot from the attached discovery ISO and then reboot the server.
3. On the administration host, monitor the installation by running the following command:

   ```terminal
   $ ./openshift-install --dir=ocp wait-for install-complete
   ```

   The server restarts several times while deploying the control plane.

* After the installation is complete, check the environment by running the following command:

  ```terminal
  $ export KUBECONFIG=ocp/auth/kubeconfig
  ```

  ```terminal
  $ oc get nodes
  ```

  **Example output**

  ```terminal
  NAME                         STATUS   ROLES           AGE     VERSION
  control-plane.example.com    Ready    master,worker   10m     v1.27.3
  ```
