// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc

:_mod-docs-content-type: REFERENCE
[id="GitOps-compatibility-support-matrix_{context}"]
= Compatibility and support matrix

Some features in this release are currently in link:https://access.redhat.com/support/offerings/techpreview[Technology Preview]. These experimental features are not intended for production use.

In the table, features are marked with the following statuses:

* *TP*: _Technology Preview_
* *GA*: _General Availability_
* *NA*: _Not Applicable_

[IMPORTANT]
====
In {product-title} 4.13, the `stable` channel has been removed. Before upgrading to {product-title} 4.13, if you are already on the `stable` channel, choose the appropriate channel and switch to it.
====

|===
|*OpenShift GitOps* 7+|*Component Versions*|*OpenShift Versions*

|*Version* |*`kam`*    |*Helm*  |*Kustomize* |*Argo CD*|*ApplicationSet* |*Dex*     |*RH SSO* |
|1.9.0    |0.0.49 TP |3.11.2 GA|5.0.1 GA   |2.7.2 GA |NA     |2.35.1 GA |7.5.1 GA |4.12-4.13
|1.8.0    |0.0.47 TP |3.10.0 GA|4.5.7 GA   |2.6.3 GA |NA     |2.35.1 GA |7.5.1 GA |4.10-4.13
|1.7.0    |0.0.46 TP |3.10.0 GA|4.5.7 GA   |2.5.4 GA |NA     |2.35.1 GA |7.5.1 GA |4.10-4.12
|1.6.0    |0.0.46 TP |3.8.1 GA|4.4.1 GA   |2.4.5 GA |GA and included in ArgoCD component    |2.30.3 GA |7.5.1 GA |4.8-4.11
|1.5.0    |0.0.42 TP|3.8.0 GA|4.4.1 GA   |2.3.3 GA |0.4.1 TP       |2.30.3 GA |7.5.1 GA |4.8-4.11
|1.4.0    |0.0.41 TP|3.7.1 GA|4.2.0 GA   |2.2.2 GA |0.2.0 TP       |2.30.0 GA |7.4.0 GA |4.7-4.10
|1.3.0    |0.0.40 TP|3.6.0 GA|4.2.0 GA   |2.1.2 GA |0.2.0 TP       |2.28.0 GA |7.4.0 GA |4.7-4.9, 4.6 with limited GA support
|1.2.0    |0.0.38 TP |3.5.0 GA |3.9.4 GA  |2.0.5 GA |0.1.0 TP      |NA |7.4.0 GA|4.8
|1.1.0    |0.0.32 TP |3.5.0 GA |3.9.4 GA  |2.0.0 GA |NA            |NA |NA |4.7
|===

* `kam` is the {gitops-title} Application Manager command-line interface (CLI).
* RH SSO is an abbreviation for Red Hat SSO.

// Writer, to update this support matrix, refer to https://spaces.redhat.com/display/GITOPS/GitOps+Component+Matrix

[id="GitOps-technology-preview_{context}"]
== Technology Preview features

The features mentioned in the following table are currently in Technology Preview (TP). These experimental features are not intended for production use.

.Technology Preview tracker
[cols="4,1,1",options="header"]
|====
|Feature |TP in {gitops-title} versions|GA in {gitops-title} versions

|The custom `must-gather` tool
|1.9.0
|NA

|Argo Rollouts
|1.9.0
|NA

|ApplicationSet Progressive Rollout Strategy
|1.8.0
|NA

|Multiple sources for an application
|1.8.0
|NA

|Argo CD applications in non-control plane namespaces
|1.7.0
|NA

|Argo CD Notifications controller
|1.6.0
|NA

|The {gitops-title} *Environments* page in the *Developer* perspective of the {product-title} web console 
|1.1.0
|NA
|====
