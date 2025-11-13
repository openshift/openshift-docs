// Module included in the following assemblies:
//
// * nodes/nodes-containers-remote-commands.adoc

[id="nodes-containers-remote-commands-protocol_{context}"]
= Protocol for initiating a remote command from a client

Clients initiate the execution of a remote command in a container by issuing a
request to the Kubernetes API server:

[source,terminal]
----
/proxy/nodes/<node_name>/exec/<namespace>/<pod>/<container>?command=<command>
----

In the above URL:

- `<node_name>` is the FQDN of the node.
- `<namespace>` is the project of the target pod.
- `<pod>` is the name of the target pod.
- `<container>` is the name of the target container.
- `<command>` is the desired command to be executed.

For example:

[source,terminal]
----
/proxy/nodes/node123.openshift.com/exec/myns/mypod/mycontainer?command=date
----

Additionally, the client can add parameters to the request to indicate if:

- the client should send input to the remote container's command (stdin).
- the client's terminal is a TTY.
- the remote container's command should send output from stdout to the client.
- the remote container's command should send output from stderr to the client.

After sending an `exec` request to the API server, the client upgrades the
connection to one that supports multiplexed streams; the current implementation
uses *HTTP/2*.

The client creates one stream each for stdin, stdout, and stderr. To distinguish
among the streams, the client sets the `streamType` header on the stream to one
of `stdin`, `stdout`, or `stderr`.

The client closes all streams, the upgraded connection, and the underlying
connection when it is finished with the remote command execution request.
