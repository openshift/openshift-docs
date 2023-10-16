// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting.adoc
// * migrating_from_ocp_3_to_4/troubleshooting-3-4.adoc
// * migration_toolkit_for_containers/troubleshooting-mtc

[id="migration-debugging-velero-resources_{context}"]
= Debugging Velero resources with the Velero CLI tool

You can debug `Backup` and `Restore` custom resources (CRs) and retrieve logs with the Velero CLI tool.

The Velero CLI tool provides more detailed information than the OpenShift CLI tool.

[discrete]
[id="velero-command-syntax_{context}"]
== Syntax

Use the `oc exec` command to run a Velero CLI command:

[source,terminal,subs="attributes+"]
----
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  <backup_restore_cr> <command> <cr_name>
----

.Example
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  backup describe 0e44ae00-5dc3-11eb-9ca8-df7e5254778b-2d8ql
----

[discrete]
[id="velero-help-option_{context}"]
== Help option

Use the `velero --help` option to list all Velero CLI commands:

[source,terminal,subs="attributes+"]
----
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  --help
----

[discrete]
[id="velero-describe-command_{context}"]
== Describe command

Use the `velero describe` command to retrieve a summary of warnings and errors associated with a `Backup` or `Restore` CR:

[source,terminal,subs="attributes+"]
----
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  <backup_restore_cr> describe <cr_name>
----

.Example
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  backup describe 0e44ae00-5dc3-11eb-9ca8-df7e5254778b-2d8ql
----

[discrete]
[id="velero-logs-command_{context}"]
== Logs command

Use the `velero logs` command to retrieve the logs of a `Backup` or `Restore` CR:

[source,terminal,subs="attributes+"]
----
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  <backup_restore_cr> logs <cr_name>
----

.Example
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  restore logs ccc7c2d0-6017-11eb-afab-85d0007f5a19-x4lbf
----
