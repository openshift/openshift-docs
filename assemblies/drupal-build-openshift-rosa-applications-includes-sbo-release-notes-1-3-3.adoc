// Module included in the following assembly:
//
// * applications/connecting_applications_to_services/sbo-release-notes.adoc

:_mod-docs-content-type: REFERENCE
[id="sbo-release-notes-1-3-3_{context}"]
= Release notes for {servicebinding-title} 1.3.3

{servicebinding-title} 1.3.3 is now available on {product-title} 4.9, 4.10, 4.11 and 4.12.

[id="fixed-issues-1-3-3_{context}"]
== Fixed issues
* Before this update, a security vulnerability `CVE-2022-41717` was noted for {servicebinding-title}. This update fixes the `CVE-2022-41717` error and updates the `golang.org/x/net` package from v0.0.0-20220906165146-f3363e06e74c to v0.4.0. link:https://issues.redhat.com/browse/APPSVC-1256[APPSVC-1256]

* Before this update, Provisioned Services were only detected if the respective resource had the "servicebinding.io/provisioned-service: true" annotation set while other Provisioned Services were missed. With this update, the detection mechanism identifies all Provisioned Services correctly based on the "status.binding.name" attribute. link:https://issues.redhat.com/browse/APPSVC-1204[APPSVC-1204]
