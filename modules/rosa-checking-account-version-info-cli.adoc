// Module included in the following assemblies:
//
// 

[id="rosa-checking-account-version-information_{context}"]
= Checking account and version information with the ROSA CLI

Use the following commands to check your account and version information with the {product-title} (ROSA) CLI, `rosa`.

[id="rosa-whoami_{context}"]
== whoami

Display information about your AWS and Red Hat accounts.

.Syntax
[source,terminal]
----
$ rosa whoami [arguments]
----

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|--profile
|Specifies an AWS profile (string) from your credentials file.
|===

.Example
[source,terminal]
----
$ rosa whoami
----

[id="rosa-version_{context}"]
== version

Display the version of your {product-title} (ROSA) CLI, `rosa`.

.Syntax
[source,terminal]
----
$ rosa version [arguments]
----

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|--profile
|Specifies an AWS profile (string) from your credentials file.
|===

.Example
[source,terminal]
----
$ rosa version
----
