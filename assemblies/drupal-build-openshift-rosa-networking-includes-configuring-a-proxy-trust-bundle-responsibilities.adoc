// Module included in the following assemblies:
//
// * networking/configuring-cluster-wide-proxy.adoc

:_mod-docs-content-type: CONCEPT
[id="configuring-a-proxy-trust-bundle-responsibilities_{context}"]
= Responsibilities for additional trust bundles

If you supply an additional trust bundle, you are responsible for the following requirements:

* Ensuring that the contents of the additional trust bundle are valid
* Ensuring that the certificates, including intermediary certificates, contained in the additional trust bundle have not expired
* Tracking the expiry and performing any necessary renewals for certificates contained in the additional trust bundle
* Updating the cluster configuration with the updated additional trust bundle
