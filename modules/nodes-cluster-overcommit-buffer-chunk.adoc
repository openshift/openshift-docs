// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc
// * cluster-logging-collector.adoc


[id="understandin-fluentd-buffering_{context}"]
= Understanding Buffer Chunk Limiting for Fluentd

If the Fluentd logger is unable to keep up with a high number of logs, it will need
to switch to file buffering to reduce memory usage and prevent data loss.

Fluentd file buffering stores records in _chunks_. Chunks are stored in _buffers_.

[NOTE]
====
To modify the `FILE_BUFFER_LIMIT` or `BUFFER_SIZE_LIMIT` parameters
in the Fluentd daemonset as described below, you must set OpenShift Logging to the unmanaged state.
Operators in an unmanaged state are unsupported and the cluster administrator assumes full control of the individual component configurations and upgrades.
====

The Fluentd `buffer_chunk_limit` is determined by the environment variable
`BUFFER_SIZE_LIMIT`, which has the default value `8m`. The file buffer size per
output is determined by the environment variable `FILE_BUFFER_LIMIT`, which has
the default value `256Mi`. The permanent volume size must be larger than
`FILE_BUFFER_LIMIT` multiplied by the output.

On the Fluentd pods, permanent volume */var/lib/fluentd* should be
prepared by the PVC or hostmount, for example. That area is then used for the
file buffers.

The `buffer_type` and `buffer_path` are configured in the Fluentd configuration files as
follows:

[source,terminal]
----
$ egrep "buffer_type|buffer_path" *.conf
----

.Example output
[source,text]
----
output-es-config.conf:
  buffer_type file
  buffer_path `/var/lib/fluentd/buffer-output-es-config`
output-es-ops-config.conf:
  buffer_type file
  buffer_path `/var/lib/fluentd/buffer-output-es-ops-config`
----

The Fluentd `buffer_queue_limit` is the value of the variable `BUFFER_QUEUE_LIMIT`. This value is `32` by default.

The environment variable `BUFFER_QUEUE_LIMIT` is calculated as `(FILE_BUFFER_LIMIT / (number_of_outputs * BUFFER_SIZE_LIMIT))`.

If the `BUFFER_QUEUE_LIMIT` variable has the default set of values:

* `FILE_BUFFER_LIMIT = 256Mi`
* `number_of_outputs = 1`
* `BUFFER_SIZE_LIMIT = 8Mi`

The value of `buffer_queue_limit` will be `32`. To change the `buffer_queue_limit`, you must change the value of `FILE_BUFFER_LIMIT`.

In this formula, `number_of_outputs` is `1` if all the logs are sent to a single resource, and it is incremented by `1` for each additional resource. For example, the value of `number_of_outputs` is:

 * `1` - if all logs are sent to a single Elasticsearch pod
 * `2` - if application logs are sent to an Elasticsearch pod and ops logs are sent to
another Elasticsearch pod
 * `4` - if application logs are sent to an Elasticsearch pod, ops logs are sent to
another Elasticsearch pod, and both of them are forwarded to other Fluentd instances
