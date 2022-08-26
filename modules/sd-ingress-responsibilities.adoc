// Module included in the following assemblies:
// * understanding-networking.adoc

[id="sd-ingress-responsibility-matrix_{context}"]
= {product-title} Ingress Operator configurations

The following table details the components of the Ingress Operator and if Red Hat Site Reliability Engineers (SRE) maintains this component on {product-title} clusters.

.Ingress Operator Responsibility Chart

[cols="3,2a,2a",options="header"]
|===

|Ingress component
|Managed by
|Default configuration?

|Scaling Ingress Controller | SRE | Yes

|Ingress Operator thread count | SRE | Yes

|Ingress Controller access logging | SRE | Yes

|Ingress Controller sharding | SRE | Yes

|Ingress Controller route admission policy | SRE | Yes

|Ingress Controller wildcard routes | SRE | Yes

|Ingress Controller X-Forwarded headers | SRE | Yes

|Ingress Controller route compression | SRE | Yes

|===
