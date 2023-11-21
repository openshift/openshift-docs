// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

:_mod-docs-content-type: CONCEPT
[id="microshift-http-proxy_{context}"]
= Deploying {microshift-short} behind an HTTP(S) proxy

Deploy a {microshift-short} cluster behind an HTTP(S) proxy when you want to add basic anonymity and security measures to your pods.

You must configure the host operating system to use the proxy service with all components initiating HTTP(S) requests when deploying {microshift-short} behind a proxy.

All the user-specific workloads or pods with egress traffic, such as accessing cloud services, must be configured to use the proxy. There is no built-in transparent proxying of egress traffic in {microshift-short}.
