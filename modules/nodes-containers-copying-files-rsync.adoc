// Module included in the following assemblies:
//
// * nodes/nodes-containers-copying-files.adoc

[id="nodes-containers-copying-files-rsync_{context}"]
= Using advanced Rsync features

The `oc rsync` command exposes fewer command line options than standard `rsync`.
In the case that you want to use a standard `rsync` command line option that is
not available in `oc rsync`, for example the `--exclude-from=FILE` option, it
might be possible to use standard `rsync` 's `--rsh` (`-e`) option or `RSYNC_RSH`
environment variable as a workaround, as follows:

[source,terminal]
----
$ rsync --rsh='oc rsh' --exclude-from=<file_name> <local-dir> <pod-name>:/<remote-dir>
----

or:

Export the `RSYNC_RSH` variable:

[source,terminal]
----
$ export RSYNC_RSH='oc rsh'
----

Then, run the rsync command:

[source,terminal]
----
$ rsync --exclude-from=<file_name> <local-dir> <pod-name>:/<remote-dir>
----

Both of the above examples configure standard `rsync` to use `oc rsh` as its
remote shell program to enable it to connect to the remote pod, and are an
alternative to running `oc rsync`.
