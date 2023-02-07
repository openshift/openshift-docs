// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-government-region.adoc

[id="installation-azure-about-government-region_{context}"]
= Azure government regions

{product-title} supports deploying a cluster to
link:https://docs.microsoft.com/en-us/azure/azure-government/documentation-government-welcome[Microsoft Azure Government (MAG)]
regions. MAG is specifically designed for US government agencies at the federal,
state, and local level, as well as contractors, educational institutions, and
other US customers that must run sensitive workloads on Azure. MAG is composed
of government-only data center regions, all granted an
link:https://docs.microsoft.com/en-us/microsoft-365/compliance/offering-dod-disa-l2-l4-l5?view=o365-worldwide#dod-impact-level-5-provisional-authorization[Impact Level 5 Provisional Authorization].

Installing to a MAG region requires manually configuring the Azure Government
dedicated cloud instance and region in the `install-config.yaml` file. You must
also update your service principal to reference the appropriate government
environment.

[NOTE]
====
The Azure government region cannot be selected using the guided terminal prompts
from the installation program. You must define the region manually in the
`install-config.yaml` file. Remember to also set the dedicated cloud instance,
like `AzureUSGovernmentCloud`, based on the region specified. 
====
