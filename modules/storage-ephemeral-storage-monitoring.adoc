// Module included in the following assemblies:
//
// storage/understanding-persistent-storage.adoc[leveloffset=+1]
//* microshift_storage/understanding-ephemeral-storage-microshift.adoc


[id=storage-ephemeral-storage-monitoring_{context}]
= Monitoring ephemeral storage

You can use `/bin/df` as a tool to monitor ephemeral storage usage on the volume where ephemeral container data is located, which is `/var/lib/kubelet` and `/var/lib/containers`. The available space for only `/var/lib/kubelet` is shown when you use the `df` command if `/var/lib/containers` is placed on a separate disk by the cluster administrator.

To show the human-readable values of used and available space in `/var/lib`, enter the following command:

[source,terminal]
----
$ df -h /var/lib
----

The output shows the ephemeral storage usage in `/var/lib`:

.Example output
[source,terminal]
----
Filesystem  Size  Used Avail Use% Mounted on
/dev/disk/by-partuuid/4cd1448a-01    69G   32G   34G  49% /
----
