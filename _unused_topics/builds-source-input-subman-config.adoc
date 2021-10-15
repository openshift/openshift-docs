// Module included in the following assemblies:
//
//* builds/running-entitled-builds.adoc

[id="builds-source-input-subman-config_{context}"]
= Adding Subscription Manager configurations to builds

Builds that use the Subscription Manager to install content must provide appropriate configuration files and certificate authorities for subscribed repositories.

.Prerequisites

You must have access to the Subscription Manager's configuration and certificate authority files.

.Procedure

. Create a `ConfigMap` for the Subscription Manager configuration:
+
[source,terminal]
----
$ oc create configmap rhsm-conf --from-file /path/to/rhsm/rhsm.conf
----

. Create a `ConfigMap` for the certificate authority:
+
[source,terminal]
----
$ oc create configmap rhsm-ca --from-file /path/to/rhsm/ca/redhat-uep.pem
----

. Add the Subscription Manager configuration and certificate authority to the
`BuildConfig`:
+
[source,yaml]
----
source:
    configMaps:
    - configMap:
        name: rhsm-conf
      destinationDir: rhsm-conf
    - configMap:
        name: rhsm-ca
      destinationDir: rhsm-ca
----
