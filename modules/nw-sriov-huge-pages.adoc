// Module included in the following assemblies:
//
// * networking/hardware_networks/about-sriov.adoc

[id="nw-sriov-hugepages_{context}"]
= Huge pages resource injection for Downward API

When a pod specification includes a resource request or limit for huge pages, the Network Resources Injector automatically adds Downward API fields to the pod specification to provide the huge pages information to the container.

The Network Resources Injector adds a volume that is named `podnetinfo` and is mounted at `/etc/podnetinfo` for each container in the pod. The volume uses the Downward API and includes a file for huge pages requests and limits. The file naming convention is as follows:

* `/etc/podnetinfo/hugepages_1G_request_<container-name>`
* `/etc/podnetinfo/hugepages_1G_limit_<container-name>`
* `/etc/podnetinfo/hugepages_2M_request_<container-name>`
* `/etc/podnetinfo/hugepages_2M_limit_<container-name>`

The paths specified in the previous list are compatible with the `app-netutil` library. By default, the library is configured to search for resource information in the `/etc/podnetinfo` directory. If you choose to specify the Downward API path items yourself manually, the `app-netutil` library searches for the following paths in addition to the paths in the previous list.

* `/etc/podnetinfo/hugepages_request`
* `/etc/podnetinfo/hugepages_limit`
* `/etc/podnetinfo/hugepages_1G_request`
* `/etc/podnetinfo/hugepages_1G_limit`
* `/etc/podnetinfo/hugepages_2M_request`
* `/etc/podnetinfo/hugepages_2M_limit`

As with the paths that the Network Resources Injector can create, the paths in the preceding list can optionally end with a `_<container-name>` suffix.
