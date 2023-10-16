// Module included in the following assemblies:
//
// * operators/understanding/olm-what-operators-are.adoc

[id="olm-why-use-operators_{context}"]
= Why use Operators?

Operators provide:

--
- Repeatability of installation and upgrade.
- Constant health checks of every system component.
- Over-the-air (OTA) updates for OpenShift components and ISV content.
- A place to encapsulate knowledge from field engineers and spread it to all users, not just one or two.
--

Why deploy on Kubernetes?::
Kubernetes (and by extension, {product-title}) contains all of the primitives needed to build complex distributed systems – secret handling, load balancing, service discovery, autoscaling – that work across on-premises and cloud providers.

Why manage your app with Kubernetes APIs and `kubectl` tooling?::
These APIs are feature rich, have clients for all platforms and plug into the cluster's access control/auditing. An Operator uses the Kubernetes extension mechanism, custom resource definitions (CRDs), so your custom object, link:https://marketplace.redhat.com/en-us/products/mongodb-enterprise-advanced-from-ibm[for example `MongoDB`], looks and acts just like the built-in, native Kubernetes objects.

How do Operators compare with service brokers?::
A service broker is a step towards programmatic discovery and deployment of an app. However, because it is not a long running process, it cannot execute Day 2 operations like upgrade, failover, or scaling. Customizations and parameterization of tunables are provided at install time, versus an Operator that is constantly watching the current state of your cluster. Off-cluster services are a good match for a service broker, although Operators exist for these as well.
