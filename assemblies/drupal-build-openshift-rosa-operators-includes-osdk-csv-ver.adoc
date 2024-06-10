// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-csv-ver_{context}"]
= Version management

The `--version` flag for the `generate bundle` subcommand supplies a semantic version for your bundle when creating one for the first time and when upgrading an existing one.

By setting the `VERSION` variable in your `Makefile`, the `--version` flag is automatically invoked using that value when the `generate bundle` subcommand is run by the `make bundle` command. The CSV version is the same as the Operator version, and a new CSV is generated when upgrading Operator versions.
