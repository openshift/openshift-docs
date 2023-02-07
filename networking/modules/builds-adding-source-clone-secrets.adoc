// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-adding-source-clone-secrets_{context}"]
= Source Clone Secrets

Builder pods require access to any Git repositories defined as source for a build. Source clone secrets are used to provide the builder pod with access it would not normally have access to, such as private repositories or repositories with self-signed or untrusted SSL certificates.

The following source clone secret configurations are supported:

* .gitconfig File
* Basic Authentication
* SSH Key Authentication
* Trusted Certificate Authorities

[NOTE]
====
You can also use combinations of these configurations to meet your specific needs.
====
