// Module included in the following assemblies:
//
// * architecture/architecture_rhcos.adoc

[id="ignition-config-viewing_{context}"]
= Viewing Ignition configuration files

To see the Ignition config file used to deploy the bootstrap machine, run the
following command:

[source,terminal]
----
$ openshift-install create ignition-configs --dir $HOME/testconfig
----

After you answer a few questions, the `bootstrap.ign`, `master.ign`, and
`worker.ign` files appear in the directory you entered.

To see the contents of the `bootstrap.ign` file, pipe it through the `jq` filter.
Here's a snippet from that file:

[source,terminal]
----
$ cat $HOME/testconfig/bootstrap.ign | jq
{
  "ignition": {
    "version": "3.2.0"
  },
  "passwd": {
    "users": [
      {
        "name": "core",
        "sshAuthorizedKeys": [
          "ssh-rsa AAAAB3NzaC1yc...."
        ]
      }
    ]
  },
  "storage": {
    "files": [
      {
        "overwrite": false,
        "path": "/etc/motd",
        "user": {
          "name": "root"
        },
        "append": [
          {
            "source": "data:text/plain;charset=utf-8;base64,VGhpcyBpcyB0aGUgYm9vdHN0cmFwIG5vZGU7IGl0IHdpbGwgYmUgZGVzdHJveWVkIHdoZW4gdGhlIG1hc3RlciBpcyBmdWxseSB1cC4KClRoZSBwcmltYXJ5IHNlcnZpY2VzIGFyZSByZWxlYXNlLWltYWdlLnNlcnZpY2UgZm9sbG93ZWQgYnkgYm9vdGt1YmUuc2VydmljZS4gVG8gd2F0Y2ggdGhlaXIgc3RhdHVzLCBydW4gZS5nLgoKICBqb3VybmFsY3RsIC1iIC1mIC11IHJlbGVhc2UtaW1hZ2Uuc2VydmljZSAtdSBib290a3ViZS5zZXJ2aWNlCg=="
          }
        ],
        "mode": 420
      },
...
----

To decode the contents of a file listed in the `bootstrap.ign` file, pipe the
base64-encoded data string representing the contents of that file to the `base64
-d` command. Here's an example using the contents of the `/etc/motd` file added to
the bootstrap machine from the output shown above:

[source,terminal]
----
$ echo VGhpcyBpcyB0aGUgYm9vdHN0cmFwIG5vZGU7IGl0IHdpbGwgYmUgZGVzdHJveWVkIHdoZW4gdGhlIG1hc3RlciBpcyBmdWxseSB1cC4KClRoZSBwcmltYXJ5IHNlcnZpY2VzIGFyZSByZWxlYXNlLWltYWdlLnNlcnZpY2UgZm9sbG93ZWQgYnkgYm9vdGt1YmUuc2VydmljZS4gVG8gd2F0Y2ggdGhlaXIgc3RhdHVzLCBydW4gZS5nLgoKICBqb3VybmFsY3RsIC1iIC1mIC11IHJlbGVhc2UtaW1hZ2Uuc2VydmljZSAtdSBib290a3ViZS5zZXJ2aWNlCg== | base64 --decode
----

.Example output
[source,terminal]
----
This is the bootstrap node; it will be destroyed when the master is fully up.

The primary services are release-image.service followed by bootkube.service. To watch their status, run e.g.

  journalctl -b -f -u release-image.service -u bootkube.service
----

Repeat those commands on the `master.ign` and `worker.ign` files to see the source
of Ignition config files for each of those machine types.  You should see a line
like the following for the `worker.ign`, identifying how it gets its Ignition
config from the bootstrap machine:

[source,terminal]
----
"source": "https://api.myign.develcluster.example.com:22623/config/worker",
----

Here are a few things you can learn from the `bootstrap.ign` file: +

* Format: The format of the file is defined in the
https://coreos.github.io/ignition/configuration-v3_2/[Ignition config spec].
Files of the same format are used later by the MCO to merge changes into a
machine's configuration.
* Contents: Because the bootstrap machine serves the Ignition configs for other
machines, both master and worker machine Ignition config information is stored in the
`bootstrap.ign`, along with the bootstrap machine's configuration.
* Size: The file is more than 1300 lines long, with path to various types of resources.
* The content of each file that will be copied to the machine is actually encoded
into data URLs, which tends to make the content a bit clumsy to read. (Use the
  `jq` and `base64` commands shown previously to make the content more readable.)
* Configuration: The different sections of the Ignition config file are generally
 meant to contain files that are just dropped into a machine's file system, rather
 than commands to modify existing files. For example, instead of having a section
 on NFS that configures that service, you would just add an NFS configuration
 file, which would then be started by the init process when the system comes up.
* users: A user named `core` is created, with your SSH key assigned to that user.
This allows you to log in to the cluster with that user name and your
credentials.
* storage: The storage section identifies files that are added to each machine. A
few notable files include `/root/.docker/config.json` (which provides credentials
  your cluster needs to pull from container image registries) and a bunch of
  manifest files in `/opt/openshift/manifests` that are used to configure your cluster.
* systemd: The `systemd` section holds content used to create `systemd` unit files.
Those files are used to start up services at boot time, as well as manage those
services on running systems.
* Primitives: Ignition also exposes low-level primitives that other tools can
build on.
