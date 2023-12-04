:_mod-docs-content-type: ASSEMBLY
[id="security-deploy"]
= Deploying containers
include::_attributes/common-attributes.adoc[]
:context: security-deploy

toc::[]

You can use a variety of techniques to make sure that the containers you
deploy hold the latest production-quality content and that they have not
been tampered with. These techniques include setting up build triggers to
incorporate the latest code and using signatures to ensure that the container
comes from a trusted source and has not been modified.

// Controlling container deployments with triggers
include::modules/security-deploy-trigger.adoc[leveloffset=+1]

// Controlling what image sources can be deployed
include::modules/security-deploy-image-sources.adoc[leveloffset=+1]

// Signature transports
include::modules/security-deploy-signature.adoc[leveloffset=+1]

// Secrets and ConfigMaps
include::modules/security-deploy-secrets.adoc[leveloffset=+1]

// Continuous deployment tooling
include::modules/security-deploy-continuous.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../cicd/builds/creating-build-inputs.adoc#builds-input-secrets-configmaps_creating-build-inputs[Input secrets and config maps]
