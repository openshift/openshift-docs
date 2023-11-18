// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/prepare-pxe-infra-agent.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-ocp-agent-retrieve_{context}"]
= Downloading the Agent-based Installer

Use this procedure to download the Agent-based Installer and the CLI needed for your installation.

.Procedure

. Log in to the {product-title} web console using your login credentials.

. Navigate to link:https://console.redhat.com/openshift/create/datacenter[Datacenter].

. Click *Run Agent-based Installer locally*.

. Select the operating system and architecture for the *OpenShift Installer* and *Command line interface*.

. Click *Download Installer* to download and extract the install program.

. You can either download or copy the pull secret by clicking on *Download pull secret* or *Copy pull secret*.

. Click *Download command-line tools* and place the `openshift-install` binary in a directory that is on your `PATH`.
