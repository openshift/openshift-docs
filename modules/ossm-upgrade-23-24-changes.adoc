// Module included in the following assemblies:
// * service_mesh/v2x/upgrading-ossm.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-upgrade-23-24-changes_{context}"]
= Upgrade changes from version 2.3 to version 2.4

Upgrading the {SMProductShortName} control plane from version 2.3 to 2.4 introduces the following behavioral changes:

* Support for Istio OpenShift Routing (IOR) has been deprecated. IOR functionality is still enabled, but it will be removed in a future release.

* The following cipher suites are no longer supported, and were removed from the list of ciphers used in client and server side TLS negotiations.

** ECDHE-ECDSA-AES128-SHA
** ECDHE-RSA-AES128-SHA
** AES128-GCM-SHA256
** AES128-SHA
** ECDHE-ECDSA-AES256-SHA
** ECDHE-RSA-AES256-SHA
** AES256-GCM-SHA384
** AES256-SHA
+
Applications that require access to services that use one of these cipher suites will fail to connect when the proxy initiates a TLS connection.
