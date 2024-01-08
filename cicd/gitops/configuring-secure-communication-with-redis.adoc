:_mod-docs-content-type: ASSEMBLY
[id="configuring-secure-communication-with-redis"]
= Configuring secure communication with Redis
include::_attributes/common-attributes.adoc[]
:context: configuring-secure-communication-with-redis

toc::[]

Using the Transport Layer Security (TLS) encryption with {gitops-title}, you can secure the communication between the Argo CD components and Redis cache and protect the possibly sensitive data in transit.

You can secure communication with Redis by using one of the following configurations:

* Enable the `autotls` setting to issue an appropriate certificate for TLS encryption.
* Manually configure the TLS encryption by creating the `argocd-operator-redis-tls` secret with a key and certificate pair.

Both configurations are possible with or without the High Availability (HA) enabled.

.Prerequisites
* You have access to the cluster with `cluster-admin` privileges.
* You have access to the {product-title} web console.
* {gitops-title} Operator is installed on your cluster.

include::modules/gitops-configuring-tls-for-redis-with-autotls-enabled.adoc[leveloffset=+1]

include::modules/gitops-configuring-tls-for-redis-with-autotls-disabled.adoc[leveloffset=+1]


