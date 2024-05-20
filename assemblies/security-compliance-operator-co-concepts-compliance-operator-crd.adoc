:_mod-docs-content-type: ASSEMBLY
[id="custom-resource-definitions"]
= Understanding the Custom Resource Definitions
include::_attributes/common-attributes.adoc[]
:context: compliance-crd

toc::[]

The Compliance Operator in the {product-title} provides you with several Custom Resource Definitions (CRDs) to accomplish the compliance scans. To run a compliance scan, it leverages the predefined security policies, which are derived from the link:https://github.com/ComplianceAsCode/content[ComplianceAsCode] community project. The Compliance Operator converts these security policies into CRDs, which you can use to run compliance scans and get remediations for the issues found.

include::modules/compliance-crd-workflow.adoc[leveloffset=+1]

[id="defining-compliance-scan-requirements_{context}"]
== Defining the compliance scan requirements
By default, the Compliance Operator CRDs include `ProfileBundle` and `Profile` objects, in which you can define and set the rules for your compliance scan requirements. You can also customize the default profiles by using a `TailoredProfile` object.

include::modules/compliance-crd-profile-bundle.adoc[leveloffset=+2]

include::modules/compliance-crd-profile.adoc[leveloffset=+2]

include::modules/compliance-crd-rule.adoc[leveloffset=+2]

include::modules/compliance-crd-tailored-profile.adoc[leveloffset=+2]

[id="configure-compliance-scan-settings_{context}"]
== Configuring the compliance scan settings
After you have defined the requirements of the compliance scan, you can configure it by specifying the type of the scan, occurrence of the scan, and location of the scan. To do so, Compliance Operator provides you with a `ScanSetting` object.

include::modules/compliance-crd-scan-setting.adoc[leveloffset=+2]

[id="process-compliance-requirements-with-compliance-settings_{context}"]
== Processing the compliance scan requirements with compliance scans settings
When you have defined the compliance scan requirements and configured the settings to run the scans, then the Compliance Operator processes it using the `ScanSettingBinding` object.

include::modules/compliance-crd-scan-setting-binding.adoc[leveloffset=+2]

[id="track-compliance-scans_{context}"]
== Tracking the compliance scans
After the creation of compliance suite, you can monitor the status of the deployed scans using the `ComplianceSuite` object.

include::modules/compliance-crd-compliance-suite.adoc[leveloffset=+2]

include::modules/compliance-crd-advanced-compliance-scan.adoc[leveloffset=+2]

[id="view-compliance-results_{context}"]
== Viewing the compliance results
When the compliance suite reaches the `DONE` phase, you can view the scan results and possible remediations.

include::modules/compliance-crd-compliance-check-result.adoc[leveloffset=+2]

include::modules/compliance-crd-compliance-remediation.adoc[leveloffset=+2]
