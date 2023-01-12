// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-kuryr.adoc

[id="installation-osp-config-yaml_{context}"]
= Sample customized `install-config.yaml` file for {rh-openstack}

This sample `install-config.yaml` demonstrates all of the possible {rh-openstack-first}
customization options.

[IMPORTANT]
This sample file is provided for reference only. You must obtain your
`install-config.yaml` file by using the installation program.

[source,yaml]
----
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  platform: {}
  replicas: 3
compute:
- name: worker
  platform:
    openstack:
      type: ml.large
  replicas: 3
metadata:
  name: example
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
  networkType: OVNKubernetes
platform:
  openstack:
    cloud: mycloud
    externalNetwork: external
    computeFlavor: m1.xlarge
    apiFloatingIP: 128.0.0.1
ifndef::openshift-origin[]
fips: false
endif::openshift-origin[]
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----
