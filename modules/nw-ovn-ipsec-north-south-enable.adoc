// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-ipsec-ovn.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ovn-ipsec-north-south-enable_{context}"]
= Enabling IPsec encryption for external IPsec endpoints

// This procedure requests installing Butane to prepare the machine config

As a cluster administrator, you can enable IPsec encryption between the cluster and external IPsec endpoints. Because this procedure uses Butane to create machine configs, you must have the `butane` command installed.

[NOTE]
====
After you apply the machine config, the Machine Config Operator reboots affected nodes in your cluster to rollout the new machine config.
====

.Prerequisites

* Install the {oc-first}.
* You are logged in to the cluster as a user with `cluster-admin` privileges.
* You have reduced the size of your cluster MTU by `46` bytes to allow for the overhead of the IPsec ESP header.
* You have installed the `butane` utility.
* You have an existing PKCS#12 certificate for the IPsec endpoint and a CA cert in PEM format.

.Procedure

As a cluster administrator, you can enable IPsec support for external IPsec endpoints.

. Create an IPsec configuration file named `ipsec-endpoint-config.conf`. The configuration is consumed in the next step. For more information, see link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/securing_networks/configuring-a-vpn-with-ipsec_securing-networks#configuring-a-vpn-with-ipsec_securing-networks[Libreswan as an IPsec VPN implementation].

. Provide the following certificate files to add to the Network Security Services (NSS) database on each host. These files are imported as part of the Butane configuration in subsequent steps.
+
--
* `left_server.p12`: The certificate bundle for the IPsec endpoints
* `ca.pem`: The certificate authority that you signed your certificates with
--

. Create a machine config to apply the IPsec configuration to your cluster by using the following two steps:

.. To add the IPsec configuration, create Butane config files for the control plane and worker nodes with the following contents:
+
[source,terminal,subs="attributes+"]
----
$ for role in master worker; do
  cat >> "99-ipsec-$\{role}-endpoint-config.bu" <<-EOF
  variant: openshift
  version: {product-version}.0
  metadata:
    name: 99-$\{role}-import-certs-enable-svc-os-ext
    labels:
      machineconfiguration.openshift.io/role: $role
  openshift:
    extensions:
      - ipsec
  systemd:
    units:
    - name: ipsec-import.service
      enabled: true
      contents: |
        [Unit]
        Description=Import external certs into ipsec NSS
        Before=ipsec.service

        [Service]
        Type=oneshot
        ExecStart=/usr/local/bin/ipsec-addcert.sh
        RemainAfterExit=false
        StandardOutput=journal

        [Install]
        WantedBy=multi-user.target
    - name: ipsecenabler.service
      enabled: true
      contents: |
        [Service]
        Type=oneshot
        ExecStart=systemctl enable --now ipsec.service

        [Install]
        WantedBy=multi-user.target
  storage:
    files:
    - path: /etc/pki/certs/ca.pem
      mode: 0400
      overwrite: true
      contents:
        local: ca.pem
    - path: /etc/pki/certs/left_server.p12
      mode: 0400
      overwrite: true
      contents:
        local: left_server.p12
    - path: /usr/local/bin/ipsec-addcert.sh
      mode: 0740
      overwrite: true
      contents:
        inline: |
          #!/bin/bash -e
          echo "importing cert to NSS"
          certutil -A -n "CA" -t "CT,C,C" -d /var/lib/ipsec/nss/ -i /etc/pki/certs/ca.pem
          pk12util -W "" -i /etc/pki/certs/left_server.p12 -d /var/lib/ipsec/nss/
          certutil -M -n "left_server" -t "u,u,u" -d /var/lib/ipsec/nss/
EOF
done
----

.. To transform the Butane files that you created in the previous step into machine configs, enter the following command:
+
[source,terminal]
----
$ for role in master worker; do
  butane 99-ipsec-${role}-endpoint-config.bu -o ./99-ipsec-$role-endpoint-config.yaml
done
----

. To apply the machine configs to your cluster, enter the following command:
+
[source,terminal]
----
$ for role in master worker; do
  oc apply -f 99-ipsec-${role}-endpoint-config.yaml
done
----
+
[IMPORTANT]
====
As the Machine Config Operator (MCO) updates machines in each machine config pool, it reboots each node one by one. You must wait until all the nodes are updated before external IPsec connectivity is available.
====

. Check the machine config pool status by entering the following command:
+
[source,terminal]
----
$ oc get mcp
----
+
A successfully updated node has the following status: `UPDATED=true`, `UPDATING=false`, `DEGRADED=false`.
+
[NOTE]
====
By default, the MCO updates one machine per pool at a time, causing the total time the migration takes to increase with the size of the cluster.
====
