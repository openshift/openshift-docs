:_mod-docs-content-type: ASSEMBLY
[id="cert-manager-customizing-api-fields"]
= Customizing cert-manager Operator API fields
include::_attributes/common-attributes.adoc[]
:context: cert-manager-customizing-api-fields

toc::[]

You can customize the {cert-manager-operator} API fields by overriding environment variables and arguments.

[WARNING]
====
To override unsupported arguments, you can add `spec.unsupportedConfigOverrides` section in the `CertManager` resource, but using `spec.unsupportedConfigOverrides` is unsupported.
====

include::modules/cert-manager-override-environment-variables.adoc[leveloffset=+1]

include::modules/cert-manager-override-arguments.adoc[leveloffset=+1]

include::modules/cert-manager-override-flag-controller.adoc[leveloffset=+1]

include::modules/cert-manager-configure-cpu-memory.adoc[leveloffset=+1]
