// Module included in the following assemblies:
//
// -service_mesh/v1x/ossm-architecture.adoc

[id="ossm-architecture-1x_{context}"]
= {SMProductName} Architecture

{SMProductName} is logically split into a data plane and a control plane:

The *data plane* is a set of intelligent proxies deployed as sidecars. These proxies intercept and control all inbound and outbound network communication between microservices in the service mesh. Sidecar proxies also communicate with Mixer, the general-purpose policy and telemetry hub.

* *Envoy proxy* intercepts all inbound and outbound traffic for all services in the service mesh. Envoy is deployed as a sidecar to the relevant service in the same pod.

The *control plane* manages and configures proxies to route traffic, and configures Mixers to enforce policies and collect telemetry.

* *Mixer* enforces access control and usage policies (such as authorization, rate limits, quotas, authentication, and request tracing) and collects telemetry data from the Envoy proxy and other services.
* *Pilot* configures the proxies at runtime. Pilot provides service discovery for the Envoy sidecars, traffic management capabilities for intelligent routing (for example, A/B tests or canary deployments), and resiliency (timeouts, retries, and circuit breakers).
* *Citadel* issues and rotates certificates. Citadel provides strong service-to-service and end-user authentication with built-in identity and credential management. You can use Citadel to upgrade unencrypted traffic in the service mesh. Operators can enforce policies based on service identity rather than on network controls using Citadel.
* *Galley* ingests the service mesh configuration, then validates, processes, and distributes the configuration. Galley protects the other service mesh components from obtaining user configuration details from {product-title}.

{SMProductName} also uses the *istio-operator* to manage the installation of the control plane. An _Operator_ is a piece of software that enables you to implement and automate common activities in your {product-title} cluster. It acts as a controller, allowing you to set or change the desired state of objects in your cluster.
