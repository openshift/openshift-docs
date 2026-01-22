// Module included in the following assemblies:
//
// * nodes/nodes-containers-copying-files.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-containers-copying-files-about_{context}"]
= Understanding how to copy files

The `oc rsync` command, or remote sync, is a useful tool for copying database archives to and from your pods for backup and restore purposes.
You can also use `oc rsync` to copy source code changes into a running pod for development debugging, when the running pod supports hot reload of source files.

[source,terminal]
----
$ oc rsync <source> <destination> [-c <container>]
----

== Requirements

Specifying the Copy Source::
The source argument of the `oc rsync` command must point to either a local
directory or a pod directory. Individual files are not supported.
+
When specifying a pod directory the directory name must be prefixed with the pod
name:
+
[source,terminal]
----
<pod name>:<dir>
----
+
If the directory name ends in a path separator (`/`), only the contents of the directory are copied to the destination. Otherwise, the
directory and its contents are copied to the destination.

Specifying the Copy Destination::
The destination argument of the `oc rsync` command must point to a directory. If
the directory does not exist, but `rsync` is used for copy, the directory is
created for you.

Deleting Files at the Destination::
The `--delete` flag may be used to delete any files in the remote directory that
are not in the local directory.

Continuous Syncing on File Change::
Using the `--watch` option causes the command to monitor the source path for any
file system changes, and synchronizes changes when they occur. With this
argument, the command runs forever.
+
Synchronization occurs after short quiet periods to ensure a
rapidly changing file system does not result in continuous synchronization
calls.
+
When using the `--watch` option, the behavior is effectively the same as
manually invoking `oc rsync` repeatedly, including any arguments normally passed
to `oc rsync`. Therefore, you can control the behavior via the same flags used
with manual invocations of `oc rsync`, such as `--delete`.
