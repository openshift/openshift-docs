// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-installer.adoc
// * installing/installing_openstack/installing-openstack-installer-custom.adoc
// * installing/installing_openstack/installing-openstack-installer-kuryr.adoc
// * installing/installing_openstack/installing-openstack-user.adoc
// * installing/installing_openstack/installing-openstack-user-kuryr.adoc

ifeval::["{context}" == "installing-openstack-installer-custom"]
:osp-ipi:
endif::[]
ifeval::["{context}" == "installing-openstack-installer-kuryr"]
:osp-kuryr:
:osp-ipi:
endif::[]
ifeval::["{context}" == "installing-openstack-user"]
:osp-upi:
endif::[]
ifeval::["{context}" == "installing-openstack-user-kuryr"]
:osp-kuryr:
:osp-upi:
endif::[]
ifeval::["{context}" == "installing-openstack-user-sr-iov"]
:osp-upi:
endif::[]
ifeval::["{context}" == "installing-openstack-user-sr-iov-kuryr"]
:osp-upi:
:osp-kuryr:
endif::[]
ifeval::["{context}" == "installing-openstack-installer-restricted"]
:osp-ipi:
:osp-restricted:
endif::[]

[id="installation-osp-accessing-api-no-floating_{context}"]
= Completing installation without floating IP addresses

You can install {product-title} on {rh-openstack-first} without providing floating IP addresses.

In the
ifdef::osp-ipi[`install-config.yaml`]
ifdef::osp-upi[`inventory.yaml`]
file, do not define the following
ifdef::osp-ipi[parameters:]
ifdef::osp-upi[variables:]

ifdef::osp-ipi[]
* `platform.openstack.ingressFloatingIP`
* `platform.openstack.apiFloatingIP`

If you cannot provide an external network, you can also leave `platform.openstack.externalNetwork` blank. If you do not provide a value for `platform.openstack.externalNetwork`, a router is not created for you, and, without additional action, the installer will fail to retrieve an image from Glance. You must configure external connectivity on your own.
endif::osp-ipi[]

ifdef::osp-upi[]
* `os_api_fip`
* `os_bootstrap_fip`
* `os_ingress_fip`

If you cannot provide an external network, you can also leave `os_external_network` blank. If you do not provide a value for `os_external_network`, a router is not created for you, and, without additional action, the installer will fail to retrieve an image from Glance. Later in the installation process, when you create network resources, you must configure external connectivity on your own.
endif::osp-upi[]

If you run the installer
ifdef::osp-upi[with the `wait-for` command]
from a system that cannot reach the cluster API due to a lack of floating IP addresses or name resolution, installation fails. To prevent installation failure in these cases, you can use a proxy network or run the installer from a system that is on the same network as your machines.

[NOTE]
====
You can enable name resolution by creating DNS records for the API and Ingress ports. For example:

[source,dns]
----
api.<cluster_name>.<base_domain>.  IN  A  <api_port_IP>
*.apps.<cluster_name>.<base_domain>. IN  A <ingress_port_IP>
----

If you do not control the DNS server, you can add the record to your `/etc/hosts` file. This action makes the API accessible to only you, which is not suitable for production deployment but does allow installation for development and testing.
====

ifeval::["{context}" == "installing-openstack-installer-custom"]
:!osp-ipi:
endif::[]
ifeval::["{context}" == "installing-openstack-installer-kuryr"]
:!osp-kuryr:
:!osp-ipi:
endif::[]
ifeval::["{context}" == "installing-openstack-user"]
:!osp-upi:
endif::[]
ifeval::["{context}" == "installing-openstack-user-kuryr"]
:!osp-kuryr:
:!osp-upi:
endif::[]
ifeval::["{context}" == "installing-openstack-user-sr-iov"]
:!osp-upi:
endif::[]
ifeval::["{context}" == "installing-openstack-user-sr-iov-kuryr"]
:!osp-upi:
:!osp-kuryr:
endif::[]
ifeval::["{context}" == "installing-openstack-installer-restricted"]
:!osp-ipi:
:!osp-restricted:
endif::[]
