# Modules in the nav map but not the topic map — unique to enterprise-5.0

Same comparison as `nav_modules_not_in_topic_map.md` (main), run against
`upstream/enterprise-5.0`, then filtered to drop every module that is already
a finding on main. What remains is specific to this branch.

## Method

* Topic map: 1778 `File:` entries (1764 unique) -> 1764 assemblies -> 6792 distinct modules.
* Nav map: 24 category maps -> 900 wired job maps -> 4358 distinct modules (971 job map files exist under `maps/ocp-jobs/`).
* Raw difference (nav minus topic map): 734 modules.
* Excluded as JTBD-era (adding commit is one of this branch's 35 commits touching `maps/ocp/` or `maps/ocp-jobs/`): 452.
* Findings on this branch: **282**
* Of those, already findings on main (dropped): **40**
* **Unique to enterprise-5.0: 242**

For reference: 0 of main's 40 findings do not appear on this branch at all.

## Summary

* **242** — Assembly's topic-map entry is commented out (`topic-map-entry-commented-out`)

## Assembly's topic-map entry is commented out (242)

The assembly still exists on disk and still includes these modules, but its `File:` entry in `_topic_maps/_topic_map.yml` is commented out on this branch. Content deliberately pulled from the published docs without being deleted — and the nav map is republishing it.

242 modules across 47 assemblies. Full detail is in the CSV.

### hosted_control_planes/hcp-authentication-authorization.adoc

4 modules; nav categories: secure

* `modules/hcp-cco-aws-sts.adoc` — authentication-and-authorization-for-hosted-control-planes
* `modules/hcp-cco-verify-aws-sts.adoc` — authentication-and-authorization-for-hosted-control-planes
* `modules/hcp-configuring-oauth-console.adoc` — authentication-and-authorization-for-hosted-control-planes
* `modules/hcp-configuring-oauth.adoc` — authentication-and-authorization-for-hosted-control-planes

### hosted_control_planes/hcp-certificates.adoc

5 modules; nav categories: secure

* `modules/hcp-custom-cert.adoc` — configure-certificates-for-hosted-control-planes
* `modules/hcp-kube-api-server-cert.adoc` — configure-certificates-for-hosted-control-planes
* `modules/hcp-oauth-server-cert-about.adoc` — configure-certificates-for-hosted-control-planes
* `modules/hcp-oauth-server-cert.adoc` — configure-certificates-for-hosted-control-planes
* `modules/hcp-ts-custom-dns.adoc` — configure-certificates-for-hosted-control-planes

### hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

20 modules; nav categories: install

* `modules/hc-create-aws-multi-zones.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-access-hc-aws.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-access-priv-mgmt-aws.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-create-dns-hosted-zone.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-create-public-zone.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-create-role-sts-creds.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-create-secret-s3.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-deploy-hc.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-enable-ext-dns.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-enable-private-link.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-hc-ext-dns.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-prepare.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-prereqs.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-aws-set-up-ext-dns.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-create-hc-arm64-aws.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-create-hc-aws.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-create-hc-multi-zone-aws-creds.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-create-np-arm64-aws.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-create-private-hc-aws.adoc` — deploying-hosted-control-planes-on-aws
* `modules/hcp-enable-arm-amd.adoc` — deploying-hosted-control-planes-on-aws

### hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-bm.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-ibm-power.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-ibmz.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-non-bm.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-virt.adoc

3 modules; nav categories: install

* `modules/hcp-cluster-capabilities-proc.adoc` — deploying-hosted-control-planes-on-aws;deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform;deploying-hosted-control-planes-on-ibm-power;deploying-hosted-control-planes-on-ibm-z;deploying-hosted-control-planes-on-non-bare-metal-agent-machines;deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-cluster-capabilities-ref.adoc` — deploying-hosted-control-planes-on-aws;deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform;deploying-hosted-control-planes-on-ibm-power;deploying-hosted-control-planes-on-ibm-z;deploying-hosted-control-planes-on-non-bare-metal-agent-machines;deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-cluster-capabilities.adoc` — deploying-hosted-control-planes-on-aws;deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform;deploying-hosted-control-planes-on-ibm-power;deploying-hosted-control-planes-on-ibm-z;deploying-hosted-control-planes-on-non-bare-metal-agent-machines;deploying-hosted-control-planes-on-openshift-virtualization

### hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-bm.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-ibm-power.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-ibmz.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-non-bm.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-virt.adoc

1 modules; nav categories: install

* `modules/hcp-custom-dns.adoc` — deploying-hosted-control-planes-on-aws;deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform;deploying-hosted-control-planes-on-ibm-power;deploying-hosted-control-planes-on-ibm-z;deploying-hosted-control-planes-on-non-bare-metal-agent-machines;deploying-hosted-control-planes-on-openshift-virtualization

### hosted_control_planes/hcp-deploy/hcp-deploy-bm.adoc

11 modules; nav categories: install

* `modules/hcp-bm-add-nodes-to-inventory.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-create-infra-console.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-hc-console.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-hc-create.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-hc-mirror.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-infra-reqs.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-infraenv.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-overview.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-prepare.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-prereqs.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform
* `modules/hcp-bm-verify.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform

### hosted_control_planes/hcp-deploy/hcp-deploy-bm.adoc + hosted_control_planes/hcp-deploy/hcp-deploy-ibm-power.adoc

1 modules; nav categories: install

* `modules/hcp-bm-hc.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform;deploying-hosted-control-planes-on-ibm-power

### hosted_control_planes/hcp-deploy/hcp-deploy-bm.adoc + hosted_control_planes/hcp-disconnected/hcp-deploy-dc-bm.adoc

1 modules; nav categories: install

* `modules/hcp-bm-dns.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment;deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform

### hosted_control_planes/hcp-deploy/hcp-deploy-bm.adoc + hosted_control_planes/hcp-networking.adoc

1 modules; nav categories: configure, install

* `modules/hcp-bm-firewall-port-svc-reqs.adoc` — deploying-hosted-control-planes-on-bare-metal-with-the-agent-platform;networks-for-hosted-control-planes

### hosted_control_planes/hcp-deploy/hcp-deploy-ibm-power.adoc

11 modules; nav categories: install, troubleshoot

* `modules/hcp-adding-agents.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-create-heterogeneous-nodepools.adoc` — deploying-hosted-control-planes-on-ibm-power;troubleshoot-node-performance-issues-collect-node-profiling-data
* `modules/hcp-create-infraenv.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-ibm-power-create-heterogeneous-nodepools-agent-hc-con.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-ibm-power-create-heterogeneous-nodepools-agent-hc.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-ibm-power-dns.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-ibm-power-heterogeneous-nodepools-agent-hc-dns.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-ibm-power-heterogeneous-nodepools-create-agent-cluster.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-ibm-power-infra-reqs.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-ibm-power-prereqs.adoc` — deploying-hosted-control-planes-on-ibm-power
* `modules/hcp-scale-the-nodepool.adoc` — deploying-hosted-control-planes-on-ibm-power

### hosted_control_planes/hcp-deploy/hcp-deploy-ibmz.adoc

9 modules; nav categories: install

* `modules/hcp-ibm-z-dns.adoc` — deploying-hosted-control-planes-on-ibm-z
* `modules/hcp-ibm-z-infra-reqs.adoc` — deploying-hosted-control-planes-on-ibm-z
* `modules/hcp-ibm-z-infraenv.adoc` — deploying-hosted-control-planes-on-ibm-z
* `modules/hcp-ibm-z-kvm-agents.adoc` — deploying-hosted-control-planes-on-ibm-z
* `modules/hcp-ibm-z-lpar-agents.adoc` — deploying-hosted-control-planes-on-ibm-z
* `modules/hcp-ibm-z-prereqs.adoc` — deploying-hosted-control-planes-on-ibm-z
* `modules/hcp-ibm-z-scale-np.adoc` — deploying-hosted-control-planes-on-ibm-z
* `modules/hcp-ibm-z-zvm-agents.adoc` — deploying-hosted-control-planes-on-ibm-z
* `modules/hcp-ibmz-create-hc.adoc` — deploying-hosted-control-planes-on-ibm-z

### hosted_control_planes/hcp-deploy/hcp-deploy-non-bm.adoc

8 modules; nav categories: install

* `modules/hcp-non-bm-dns.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines
* `modules/hcp-non-bm-hc-console.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines
* `modules/hcp-non-bm-hc-mirror.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines
* `modules/hcp-non-bm-hc.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines
* `modules/hcp-non-bm-infra-reqs.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines
* `modules/hcp-non-bm-prepare.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines
* `modules/hcp-non-bm-prereqs.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines
* `modules/hcp-non-bm-verify.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines

### hosted_control_planes/hcp-deploy/hcp-deploy-non-bm.adoc + hosted_control_planes/hcp-networking.adoc

1 modules; nav categories: configure, install

* `modules/hcp-non-bm-firewall-port-svc-reqs.adoc` — deploying-hosted-control-planes-on-non-bare-metal-agent-machines;networks-for-hosted-control-planes

### hosted_control_planes/hcp-deploy/hcp-deploy-openstack.adoc

6 modules; nav categories: install, troubleshoot

* `modules/hcp-deploy-openstack-create.adoc` — deploying-hosted-control-planes-on-openstack
* `modules/hcp-deploy-openstack-parameters.adoc` — deploying-hosted-control-planes-on-openstack
* `modules/hosted-clusters-openstack-create-floating-ip.adoc` — deploying-hosted-control-planes-on-openstack
* `modules/hosted-clusters-openstack-prepare-etcd.adoc` — deploying-hosted-control-planes-on-openstack;move-etcd-to-a-different-disk
* `modules/hosted-clusters-openstack-prerequisites.adoc` — deploying-hosted-control-planes-on-openstack
* `modules/hosted-clusters-openstack-upload-rhcos.adoc` — deploying-hosted-control-planes-on-openstack

### hosted_control_planes/hcp-deploy/hcp-deploy-virt.adoc

14 modules; nav categories: install

* `modules/hcp-metallb.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-add-networks.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-add-node.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-addl-config.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-addl-network.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-create-hc-console.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-create-hc-ext-infra.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-create-hc.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-guaranteed-cpus.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-ingress-dns-custom.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-live-migration.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-scale-nodepool.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-sched-vms.adoc` — deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-verify-hc.adoc` — deploying-hosted-control-planes-on-openshift-virtualization

### hosted_control_planes/hcp-deploy/hcp-deploy-virt.adoc + hosted_control_planes/hcp-disconnected/hcp-deploy-dc-virt.adoc

6 modules; nav categories: install

* `modules/hcp-virt-create-hc-cli.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment;deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-hc-base-domain.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment;deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-ingress-dns.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment;deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-load-balancer.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment;deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-prereqs.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment;deploying-hosted-control-planes-on-openshift-virtualization
* `modules/hcp-virt-wildcard-dns.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment;deploying-hosted-control-planes-on-openshift-virtualization

### hosted_control_planes/hcp-deploy/hcp-deploy-virt.adoc + hosted_control_planes/hcp-networking.adoc

1 modules; nav categories: configure, install

* `modules/hcp-virt-firewall-port.adoc` — deploying-hosted-control-planes-on-openshift-virtualization;networks-for-hosted-control-planes

### hosted_control_planes/hcp-destroy/hcp-destroy-bm.adoc

2 modules; nav categories: administer

* `modules/destroy-hc-bm-cli.adoc` — delete-a-hosted-cluster
* `modules/destroy-hc-bm-console.adoc` — delete-a-hosted-cluster

### hosted_control_planes/hcp-destroy/hcp-destroy-ibm-power.adoc

1 modules; nav categories: administer

* `modules/destroy-hc-ibm-power-cli.adoc` — delete-a-hosted-cluster

### hosted_control_planes/hcp-destroy/hcp-destroy-non-bm.adoc

1 modules; nav categories: administer

* `modules/destroy-hc-non-bm-cli.adoc` — delete-a-hosted-cluster

### hosted_control_planes/hcp-disconnected/disconnected-install-ibmz-hcp.adoc

4 modules; nav categories: install

* `modules/hcp-ibm-z-adding-credentials-registry.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-ibm-z-adding-reg-ca-hostedcluster.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-ibm-z-dc-prereqs.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-ibm-z-update-reg-ca.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment

### hosted_control_planes/hcp-disconnected/hcp-deploy-dc-bm.adoc

13 modules; nav categories: install

* `modules/hcp-agentserviceconfig.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-bm-hosts.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-bm-arch.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-bm-hosted.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-bm-reqs.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-extract.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-infraenv.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-mgmt-cluster.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-registry.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-scale-np.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-web-server.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-hc-objects.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-nodepool-hc.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment

### hosted_control_planes/hcp-disconnected/hcp-deploy-dc-bm.adoc + hosted_control_planes/hcp-disconnected/hcp-deploy-dc-virt.adoc

4 modules; nav categories: install

* `modules/hcp-dc-apply-objects.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-image-mirror.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-tls-hosted.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-tls-mgmt.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment

### hosted_control_planes/hcp-disconnected/hcp-deploy-dc-virt.adoc

7 modules; nav categories: install

* `modules/hcp-dc-finish.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-mce-virt.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-tls-virt.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-virt-hosted.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-dc-virt-ingress-dns-custom.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-monitor-cp.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment
* `modules/hcp-monitor-dp.adoc` — deploying-hosted-control-planes-in-a-disconnected-environment

### hosted_control_planes/hcp-import.adoc

2 modules; nav categories: administer

* `modules/hcp-import-manual-aws.adoc` — manually-import-a-hosted-cluster
* `modules/hcp-import-manual.adoc` — manually-import-a-hosted-cluster

### hosted_control_planes/hcp-machine-config.adoc

12 modules; nav categories: optimize

* `modules/balance-ignored-labels-autoscaler-hcp.adoc` — machine-configuration-for-hosted-control-planes
* `modules/configuring-node-pools-for-hcp.adoc` — machine-configuration-for-hosted-control-planes
* `modules/hcp-autoscaling-nodepool-reference.adoc` — machine-configuration-for-hosted-control-planes
* `modules/hcp-autoscaling-to-from-zero-configure.adoc` — machine-configuration-for-hosted-control-planes
* `modules/hcp-autoscaling-to-from-zero.adoc` — machine-configuration-for-hosted-control-planes
* `modules/hcp-configure-ntp.adoc` — machine-configuration-for-hosted-control-planes
* `modules/hcp-kubeconf-nodepool.adoc` — machine-configuration-for-hosted-control-planes
* `modules/hcp-nodepool-api-reference.adoc` — machine-configuration-for-hosted-control-planes
* `modules/priority-expander-autoscaler-hcp.adoc` — machine-configuration-for-hosted-control-planes
* `modules/scale-down-data-plane.adoc` — machine-configuration-for-hosted-control-planes
* `modules/scale-up-autoscaler-hcp.adoc` — machine-configuration-for-hosted-control-planes
* `modules/scale-up-down-autoscaler-hcp.adoc` — machine-configuration-for-hosted-control-planes

### hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

1 modules; nav categories: troubleshoot

* `modules/hcp-aws-config-sqs-eventbridge.adoc` — view-cluster-events

### hosted_control_planes/hcp-manage/hcp-manage-bm.adoc + hosted_control_planes/hcp-manage/hcp-manage-non-bm.adoc

4 modules; nav categories: administer, troubleshoot

* `modules/hcp-bm-add-np.adoc` — scale-workloads-in-a-hosted-cluster
* `modules/hcp-bm-autoscale-disable.adoc` — scale-workloads-in-a-hosted-cluster
* `modules/hcp-bm-machine-health.adoc` — troubleshoot-machine-management
* `modules/hcp-bm-scale-np.adoc` — scale-workloads-in-a-hosted-cluster

### hosted_control_planes/hcp-manage/hcp-manage-bm.adoc + hosted_control_planes/hcp-manage/hcp-manage-non-bm.adoc + hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

1 modules; nav categories: administer

* `modules/hcp-bm-autoscale.adoc` — scale-workloads-in-a-hosted-cluster

### hosted_control_planes/hcp-manage/hcp-manage-bm.adoc + hosted_control_planes/hcp-manage/hcp-manage-non-bm.adoc + hosted_control_planes/hcp-networking.adoc

1 modules; nav categories: configure

* `modules/hcp-bm-ingress.adoc` — networks-for-hosted-control-planes

### hosted_control_planes/hcp-manage/hcp-manage-ibm-power.adoc

1 modules; nav categories: administer

* `modules/hcp-ibm-power-scale-np.adoc` — scale-workloads-in-a-hosted-cluster

### hosted_control_planes/hcp-manage/hcp-manage-openstack.adoc

3 modules; nav categories: optimize

* `modules/hosted-clusters-openstack-performance-enabling.adoc` — optimize-infrastructure-for-specific-platforms
* `modules/hosted-clusters-openstack-performance-tuning.adoc` — optimize-infrastructure-for-specific-platforms
* `modules/hosted-clusters-openstack-performance.adoc` — optimize-infrastructure-for-specific-platforms

### hosted_control_planes/hcp-manage/hcp-manage-virt.adoc

1 modules; nav categories: troubleshoot

* `modules/hcp-virt-etcd-storage.adoc` — move-etcd-to-a-different-disk

### hosted_control_planes/hcp-networking.adoc

14 modules; nav categories: configure, plan, troubleshoot

* `modules/hcp-custom-ovn-subnets.adoc` — networks-for-hosted-control-planes
* `modules/hcp-egress-reqs.adoc` — networking-guidance-for-hosted-control-planes;networks-for-hosted-control-planes
* `modules/hcp-ingress-egress-example.adoc` — networks-for-hosted-control-planes
* `modules/hcp-ingress-egress-reqs.adoc` — networking-guidance-for-hosted-control-planes;networks-for-hosted-control-planes
* `modules/hcp-ingress-reqs.adoc` — networking-guidance-for-hosted-control-planes;networks-for-hosted-control-planes
* `modules/hcp-isolation-overview.adoc` — networking-guidance-for-hosted-control-planes;networks-for-hosted-control-planes
* `modules/hcp-networking-firewall.adoc` — networking-guidance-for-hosted-control-planes;networks-for-hosted-control-planes
* `modules/hcp-networking-overview.adoc` — incident-investigation-75-reconstruct-timeline-of-network-events;networking-guidance-for-hosted-control-planes;networks-for-hosted-control-planes
* `modules/hcp-proxy-addl-network.adoc` — networks-for-hosted-control-planes
* `modules/hcp-proxy-api.adoc` — networks-for-hosted-control-planes
* `modules/hcp-proxy-cp-workloads.adoc` — networks-for-hosted-control-planes
* `modules/hcp-proxy-ignition.adoc` — networks-for-hosted-control-planes
* `modules/hcp-proxy-mgmt-cluster.adoc` — networks-for-hosted-control-planes
* `modules/hcp-proxy-overview.adoc` — networking-guidance-for-hosted-control-planes;networks-for-hosted-control-planes

### hosted_control_planes/hcp-networking.adoc + hosted_control_planes/hcp-prepare/hcp-distribute-workloads.adoc

1 modules; nav categories: configure, plan

* `modules/hcp-isolation.adoc` — distribute-hosted-cluster-workloads;networks-for-hosted-control-planes

### hosted_control_planes/hcp-observability.adoc

15 modules; nav categories: observe

* `modules/hcp-cluster-ids-example.adoc` — enable-monitoring-dashboards-in-a-hosted-cluster
* `modules/hcp-cluster-ids.adoc` — enable-monitoring-dashboards-in-a-hosted-cluster
* `modules/hcp-connect-control-plane.adoc` — connectivity-monitoring-from-the-control-plane-to-the-data-plane
* `modules/hcp-connect-data-plane.adoc` — connectivity-monitoring-from-the-control-plane-to-the-data-plane
* `modules/hcp-connectivity-metrics.adoc` — connectivity-monitoring-from-the-control-plane-to-the-data-plane
* `modules/hcp-cp-metrics-dashboards.adoc` — monitor-hosted-control-planes
* `modules/hcp-cp-metrics-forwarding-configure.adoc` — monitor-hosted-control-planes
* `modules/hcp-cp-metrics-forwarding-migrate.adoc` — monitor-hosted-control-planes
* `modules/hcp-cp-metrics-overview.adoc` — monitor-hosted-control-planes
* `modules/hcp-cp-query-metrics-console.adoc` — monitor-hosted-control-planes
* `modules/hcp-cp-query-metrics.adoc` — monitor-hosted-control-planes
* `modules/hcp-customize-dashboards.adoc` — enable-monitoring-dashboards-in-a-hosted-cluster
* `modules/hcp-metrics-sets-ref.adoc` — configure-metrics-sets-for-hosted-control-planes
* `modules/hosted-control-planes-metrics-sets.adoc` — configure-metrics-sets-for-hosted-control-planes
* `modules/hosted-control-planes-monitoring-dashboard.adoc` — enable-monitoring-dashboards-in-a-hosted-cluster

### hosted_control_planes/hcp-prepare/hcp-distribute-workloads.adoc

4 modules; nav categories: plan

* `modules/hcp-labels-taints.adoc` — distribute-hosted-cluster-workloads
* `modules/hcp-node-labeling.adoc` — distribute-hosted-cluster-workloads
* `modules/hcp-priority-classes.adoc` — distribute-hosted-cluster-workloads
* `modules/hcp-virt-taints-tolerations.adoc` — distribute-hosted-cluster-workloads

### hosted_control_planes/hcp-prepare/hcp-enable-disable.adoc

4 modules; nav categories: administer

* `modules/hcp-disable-feature.adoc` — enable-or-disable-the-hosted-control-planes-feature
* `modules/hcp-enable-manual-addon.adoc` — enable-or-disable-the-hosted-control-planes-feature
* `modules/hcp-enable-manual.adoc` — enable-or-disable-the-hosted-control-planes-feature
* `modules/hcp-uninstall-operator.adoc` — enable-or-disable-the-hosted-control-planes-feature

### hosted_control_planes/hcp-prepare/hcp-requirements.adoc

2 modules; nav categories: install, plan

* `modules/hcp-fips.adoc` — install-hosted-control-planes;requirements-for-hosted-control-planes
* `modules/hcp-support-matrix.adoc` — install-hosted-control-planes;requirements-for-hosted-control-planes

### hosted_control_planes/hcp-prepare/hcp-sizing-guidance.adoc

5 modules; nav categories: plan

* `modules/hcp-load-based-limit.adoc` — size-guidance-for-hosted-control-planes
* `modules/hcp-pod-limits.adoc` — size-guidance-for-hosted-control-planes
* `modules/hcp-resource-limit.adoc` — size-guidance-for-hosted-control-planes
* `modules/hcp-shared-infra.adoc` — size-guidance-for-hosted-control-planes
* `modules/hcp-sizing-calculation.adoc` — size-guidance-for-hosted-control-planes

### hosted_control_planes/hcp-troubleshooting.adoc

14 modules; nav categories: troubleshoot

* `modules/hcp-must-gather-cli.adoc` — troubleshoot-hosted-clusters-by-platform
* `modules/hcp-must-gather-console.adoc` — troubleshoot-hosted-clusters-by-platform
* `modules/hcp-must-gather-day-2.adoc` — investigate-an-active-cluster-issue-collect-comprehensive-data-for-vendor-support;troubleshoot-hosted-clusters-by-platform
* `modules/hcp-ts-bm-nodes-not-added.adoc` — troubleshoot-hosted-clusters-by-platform-troubleshoot-hosted-clusters-on-bare-metal
* `modules/hcp-ts-bm.adoc` — troubleshoot-hosted-clusters-by-platform-troubleshoot-hosted-clusters-on-bare-metal
* `modules/hcp-ts-hc-stuck.adoc` — troubleshoot-hosted-clusters-by-platform
* `modules/hcp-ts-no-nodes-reg.adoc` — troubleshoot-hosted-clusters-by-platform
* `modules/hcp-ts-nodes-stuck.adoc` — troubleshoot-hosted-clusters-by-platform
* `modules/hcp-ts-ocp-virt.adoc` — troubleshoot-hosted-clusters-by-platform-troubleshoot-hosted-clusters-on-openshift-virtualization
* `modules/hcp-ts-rhcos.adoc` — troubleshoot-hosted-clusters-by-platform-troubleshoot-hosted-clusters-on-bare-metal
* `modules/hcp-ts-vm-nodes.adoc` — troubleshoot-hosted-clusters-by-platform-troubleshoot-hosted-clusters-on-openshift-virtualization
* `modules/hosted-control-planes-pause-reconciliation.adoc` — restart-hosted-control-plane-components-and-pause-reconciliation
* `modules/hosted-control-planes-troubleshooting.adoc` — troubleshoot-hosted-clusters-by-platform
* `modules/hosted-restart-hcp-components.adoc` — restart-hosted-control-plane-components-and-pause-reconciliation

### hosted_control_planes/hcp-updating.adoc

9 modules; nav categories: troubleshoot, upgrade

* `modules/hcp-get-ocp-channel.adoc` — upgrade-hosted-control-planes
* `modules/hcp-get-upgrade-versions.adoc` — upgrade-hosted-control-planes
* `modules/hcp-np-version-skew.adoc` — upgrade-hosted-control-planes-hosted-cluster-and-node-pool-version-skew-policy
* `modules/hcp-update-node-pools.adoc` — upgrade-hosted-control-planes-updating-node-pools-and-control-planes
* `modules/hcp-update-ocp-hc.adoc` — upgrade-hosted-control-planes-updating-the-ocp-version-in-a-hosted-cluster
* `modules/hcp-update-using-mce-console.adoc` — upgrade-hosted-control-planes-updating-the-ocp-version-in-a-hosted-cluster
* `modules/hcp-updates-hosted-cluster.adoc` — troubleshoot-common-update-failures;upgrade-hosted-control-planes-updating-node-pools-and-control-planes
* `modules/hcp-updates-node-pools.adoc` — troubleshoot-common-update-failures;upgrade-hosted-control-planes-updating-node-pools-and-control-planes
* `modules/hcp-updating-requirements.adoc` — upgrade-hosted-control-planes-requirements-to-upgrade-hosted-control-planes

### hosted_control_planes/hcp-using-feature-gates.adoc

1 modules; nav categories: configure

* `modules/hcp-enable-feature-sets.adoc` — use-feature-gates-in-a-hosted-cluster

### hosted_control_planes/hcp_high_availability/hcp-backup-etcd-snapshot.adoc

4 modules; nav categories: troubleshoot

* `modules/hcp-backup-etcd-snapshot-about.adoc` — etcd-best-practices-back-up-etcd-data;etcd-best-practices-create-recurring-automatic-etcd-backup
* `modules/hcp-backup-etcd-snapshot-backup.adoc` — etcd-best-practices-create-recurring-automatic-etcd-backup
* `modules/hcp-backup-etcd-snapshot-config.adoc` — etcd-best-practices-back-up-etcd-data;etcd-best-practices-create-recurring-automatic-etcd-backup
* `modules/hcp-backup-etcd-snapshot-restore.adoc` — backup-and-restore-etcd-data;control-plane-disaster-recovery;encrypt-etcd-restore-to-a-previous-cluster-state;encrypt-etcd-test-restore-procedures;etcd-best-practices-restore-etcd-data;high-availability-and-disaster-recovery-for-hosted-control-planes

### hosted_control_planes/hcp_high_availability/hcp-backup-restore-aws.adoc

1 modules; nav categories: troubleshoot

* `modules/restoring-etcd-snapshot-hosted-cluster.adoc` — etcd-best-practices-back-up-etcd-data

### hosted_control_planes/hcp_high_availability/hcp-backup-restore-on-premise.adoc

1 modules; nav categories: troubleshoot

* `modules/hosted-cluster-etcd-backup-restore-on-premise.adoc` — backup-and-restore-etcd-data;encrypt-etcd-test-restore-procedures;high-availability-and-disaster-recovery-for-hosted-control-planes

### hosted_control_planes/index.adoc

6 modules; nav categories: discover, install

* `modules/hcp-acm-discover.adoc` — install-hosted-control-planes
* `modules/hcp-mce-acm-relationship-intro.adoc` — install-hosted-control-planes
* `modules/hcp-ocp-differences.adoc` — install-hosted-control-planes
* `modules/hosted-control-planes-concepts-personas.adoc` — install-hosted-control-planes
* `modules/hosted-control-planes-overview.adoc` — compare-architectural-deployment-models;compare-openshift-deployment-models;install-hosted-control-planes
* `modules/hosted-control-planes-version-support.adoc` — install-hosted-control-planes

