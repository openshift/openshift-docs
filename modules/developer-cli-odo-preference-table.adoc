// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/configuring-the-odo-cli.adoc

:_mod-docs-content-type: REFERENCE
[id="developer-cli-odo-preference-table_{context}"]
= Preference key table

The following table shows the available options for setting preference keys for the `odo` CLI:

[cols="1,3,1"]
|===
|Preference key |Description |Default value

|`UpdateNotification`
|Control whether a notification to update `odo` is shown.
|True

|`NamePrefix`
|Set a default name prefix for an `odo` resource. For example, `component` or  `storage`.
|Current directory name

|`Timeout`
|Timeout for the Kubernetes server connection check.
|1 second

|`BuildTimeout`
|Timeout for waiting for a build of the git component to complete.
|300 seconds

|`PushTimeout`
|Timeout for waiting for a component to start.
|240 seconds

|`Ephemeral`
|Controls whether `odo` should create an `emptyDir` volume to store source code.
|True

|`ConsentTelemetry`
|Controls whether `odo` can collect telemetry for the user's `odo` usage.
|False

|===
