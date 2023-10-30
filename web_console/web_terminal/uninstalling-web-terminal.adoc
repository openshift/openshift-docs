:_mod-docs-content-type: ASSEMBLY
[id="uninstalling-web-terminal"]
= Uninstalling the web terminal
include::_attributes/common-attributes.adoc[]
:context: uninstalling-web-terminal

toc::[]

Uninstalling the {web-terminal-op} does not remove any of the custom resource definitions (CRDs) or managed resources that are created when the Operator is installed. For security purposes, you must manually uninstall these components. By removing these components, you save cluster resources because terminals do not idle when the Operator is uninstalled.

Uninstalling the web terminal is a two-step process:

. Uninstall the {web-terminal-op} and related custom resources (CRs) that were added when you installed the Operator.
. Uninstall the DevWorkspace Operator and its related custom resources that were added as a dependency of the {web-terminal-op}.

include::modules/removing-web-terminal-operator.adoc[leveloffset=+1]
include::modules/removing-devworkspace-operator.adoc[leveloffset=+1]