// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-nfs.adoc

= Export settings

To enable arbitrary container users to read and write the volume,
each exported volume on the NFS server should conform to the following
conditions:

* Every export must be exported using the following format:
+
[source,terminal]
----
/<example_fs> *(rw,root_squash)
----

* The firewall must be configured to allow traffic to the mount point.
** For NFSv4, configure the default port `2049` (*nfs*).
+
.NFSv4
[source,terminal]
----
# iptables -I INPUT 1 -p tcp --dport 2049 -j ACCEPT
----

** For NFSv3, there are three ports to configure:
`2049` (*nfs*), `20048` (*mountd*), and `111` (*portmapper*).
+
.NFSv3
[source,terminal]
----
# iptables -I INPUT 1 -p tcp --dport 2049 -j ACCEPT
----
+
[source,terminal]
----
# iptables -I INPUT 1 -p tcp --dport 20048 -j ACCEPT
----
+
[source,terminal]
----
# iptables -I INPUT 1 -p tcp --dport 111 -j ACCEPT
----

* The NFS export and directory must be set up so that they are accessible
by the target pods. Either set the export to be owned by the container's
primary UID, or supply the pod group access using `supplementalGroups`,
as shown in the group IDs above.
