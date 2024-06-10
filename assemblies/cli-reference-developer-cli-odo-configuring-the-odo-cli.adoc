////
:_mod-docs-content-type: ASSEMBLY
[id='configuring-the-odo-cli']
= Configuring the odo CLI
include::_attributes/common-attributes.adoc[]
:context: configuring-the-odo-cli

toc::[]

// Comment out per https://issues.redhat.com/browse/RHDEVDOCS-3594
// include::modules/developer-cli-odo-using-command-completion.adoc[leveloffset=+1]

You can find the global settings for `odo` in the `preference.yaml` file which is located by default in your `$HOME/.odo` directory.

You can set a different location for the `preference.yaml` file by exporting the `GLOBALODOCONFIG` variable.

// view config
include::modules/developer-cli-odo-view-config.adoc[leveloffset=+1]
// set key
include::modules/developer-cli-odo-set-config.adoc[leveloffset=+1]
// unset key
include::modules/developer-cli-odo-unset-config.adoc[leveloffset=+1]
// preference ref table
include::modules/developer-cli-odo-preference-table.adoc[leveloffset=+1]

include::modules/developer-cli-odo-ignoring-files-or-patterns.adoc[leveloffset=+1]
////