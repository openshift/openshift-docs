# Generating the installation ISO with coreos-installer

Installing OpenShift Container Platform on a single node requires an installation ISO, which you can generate with the following procedure.

* Install `podman`.

1. Set the OpenShift Container Platform version:

   ```terminal
   $ OCP_VERSION=<ocp_version> ①
   ```

   1. Replace `<ocp_version>` with the current version, for example, `latest-{product-version}`
2. Set the host architecture:

   ```terminal
   $ ARCH=<architecture> ①
   ```
   1. Replace `<architecture>` with the target host architecture, for example, `aarch64` or `x86_64`.
3. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands:

   ```terminal
   $ curl -k https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$OCP_VERSION/openshift-client-linux.tar.gz -o oc.tar.gz
   ```

   ```terminal
   $ tar zxf oc.tar.gz
   ```

   ```terminal
   $ chmod +x oc
   ```
4. Download the OpenShift Container Platform installer and make it available for use by entering the following commands:

   ```terminal
   $ curl -k https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$OCP_VERSION/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
   ```

   ```terminal
   $ tar zxvf openshift-install-linux.tar.gz
   ```

   ```terminal
   $ chmod +x openshift-install
   ```
5. Retrieve the {op-system} ISO URL by running the following command:

   ```terminal
   $ ISO_URL=$(./openshift-install coreos print-stream-json | grep location | grep $ARCH | grep iso | cut -d\" -f4)
   ```
6. Download the {op-system} ISO:

   ```terminal
   $ curl -L $ISO_URL -o rhcos-live.iso
   ```
7. Prepare the `install-config.yaml` file:

   ```yaml
   apiVersion: v1
   baseDomain: <domain> ①
   compute:
   - name: worker
     replicas: 0 ②
   controlPlane:
     name: master
     replicas: 1 ③
   metadata:
     name: <name> ④
   networking: ⑤
     clusterNetwork:
     - cidr: 10.128.0.0/14
       hostPrefix: 23
     machineNetwork:
     - cidr: 10.0.0.0/16 ⑥
     networkType: OVNKubernetes
     serviceNetwork:
     - 172.30.0.0/16
   platform:
     none: {}
   bootstrapInPlace:
     installationDisk: /dev/disk/by-id/<disk_id> ⑦
   pullSecret: '<pull_secret>' ⑧
   sshKey: |
     <ssh_key> ⑨
   ```
   1. Add the cluster domain name.
   2. Set the `compute` replicas to `0`. This makes the control plane node schedulable.
   3. Set the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node.
   4. Set the `metadata` name to the cluster name.
   5. Set the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters.
   6. Set the `cidr` value to match the subnet of the single-node Openshift cluster.
   7. Set the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`.
   8. Copy the {cluster-manager-url-pull} and add the contents to this configuration setting.
   9. Add the public SSH key from the administration host so that you can log in to the cluster after installation.
8. Generate OpenShift Container Platform assets by running the following commands:

   ```terminal
   $ mkdir ocp
   ```

   ```terminal
   $ cp install-config.yaml ocp
   ```

   ```terminal
   $ ./openshift-install --dir=ocp create single-node-ignition-config
   ```
9. Embed the ignition data into the {op-system} ISO by running the following commands:

   ```terminal
   $ alias coreos-installer='podman run --privileged --pull always --rm \
           -v /dev:/dev -v /run/udev:/run/udev -v $PWD:/data \
           -w /data quay.io/coreos/coreos-installer:release'
   ```

   ```terminal
   $ coreos-installer iso ignition embed -fi ocp/bootstrap-in-place-for-live-iso.ign rhcos-live.iso
   ```
