:_mod-docs-content-type: ASSEMBLY
[id="virt-using-the-cli-tools"]
= Using the virtctl and libguestfs CLI tools
include::_attributes/common-attributes.adoc[]
:context: virt-using-the-cli-tools
:toclevels: 3

toc::[]

You can manage {VirtProductName} resources by using the `virtctl` command line tool.

You can access and modify virtual machine (VM) disk images by using the link:https://libguestfs.org[`libguestfs`] command line tool. You deploy `libguestfs` by using the `virtctl libguestfs` command.

[id="installing-virtctl_virt-using-the-cli-tools"]
== Installing virtctl

To install `virtctl` on {op-system-base-full} 9 or later, Linux, Windows, and MacOS operating systems, you can download and install the `virtctl` binary file.

To install `virtctl` on {op-system-base} 8, you can enable the {VirtProductName} repository and then install the `kubevirt-virtctl` RPM package.

include::modules/virt-installing-virtctl-binary.adoc[leveloffset=+2]

include::modules/virt-installing-virtctl-rhel8-rpm.adoc[leveloffset=+2]

include::modules/virt-virtctl-commands.adoc[leveloffset=+1]

include::modules/virt-deploying-libguestfs-with-virtctl.adoc[leveloffset=+1]

include::modules/virt-about-libguestfs-tools-virtctl-guestfs.adoc[leveloffset=+2]

