// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/understanding-odo.adoc

:_mod-docs-content-type: CONCEPT
[id="odo-telemetry_{context}"]

= Telemetry in odo

`odo` collects information about how it is being used, including metrics on the operating system, RAM, CPU, number of cores, `odo` version, errors, success/failures, and how long `odo` commands take to complete.

You can modify your telemetry consent by using the `odo preference` command:

* `odo preference set ConsentTelemetry true` consents to telemetry.
* `odo preference unset ConsentTelemetry` disables telemetry.
* `odo preference view` shows the current preferences.