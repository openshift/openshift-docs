// Module included in the following assemblies:
//
// * installing/installing_openstack/installing-openstack-user.adoc

:_mod-docs-content-type: PROCEDURE
[id="installation-osp-verifying-installation_{context}"]
= Verifying a successful installation

Verify that the {product-title} installation is complete.

.Prerequisites

* You have the installation program (`openshift-install`)


.Procedure

* On a command line, enter:
+
[source,terminal]
----
$ openshift-install --log-level debug wait-for install-complete
----

The program outputs the console URL, as well as the administrator's login information.
