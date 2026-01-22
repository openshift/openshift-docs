:_mod-docs-content-type: REFERENCE
[id="install-osp-external-lb-config_{context}"]
= Installation configuration for a cluster on OpenStack with a user-managed load balancer

The following example `install-config.yaml` file demonstrates how to configure a cluster that uses an external, user-managed load balancer rather than the default internal load balancer.

[source,yaml]
----
apiVersion: v1
baseDomain: mydomain.test
compute:
- name: worker
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
controlPlane:
  name: master
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
metadata:
  name: mycluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 192.168.10.0/24
platform:
  openstack:
    cloud: mycloud
    machinesSubnet: 8586bf1a-cc3c-4d40-bdf6-c243decc603a <1>
    apiVIPs:
    - 192.168.10.5
    ingressVIPs:
    - 192.168.10.7
    loadBalancer:
      type: UserManaged <2>

----
<1> Regardless of which load balancer you use, the load balancer is deployed to this subnet.
<2> The `UserManaged` value indicates that you are using an user-managed load balancer.