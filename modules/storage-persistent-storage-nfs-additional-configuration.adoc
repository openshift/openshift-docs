// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-nfs.adoc

= Additional configuration and troubleshooting

Depending on what version of NFS is being used and how it is configured,
there may be additional configuration steps needed for proper export and
security mapping. The following are some that may apply:

[cols="1,2"]
|===

|NFSv4 mount incorrectly shows all files with ownership of `nobody:nobody`
a|- Could be attributed to the ID mapping settings, found in `/etc/idmapd.conf` on your NFS.
- See https://access.redhat.com/solutions/33455[this Red Hat Solution].

|Disabling ID mapping on NFSv4
a|- On both the NFS client and server, run:
+
[source,terminal]
----
# echo 'Y' > /sys/module/nfsd/parameters/nfs4_disable_idmapping
----
|===
