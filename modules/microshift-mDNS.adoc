// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

:_mod-docs-content-type: CONCEPT
[id="microshift-mDNS_{context}"]
= The multicast DNS protocol

You can use the multicast DNS protocol (mDNS) to allow name resolution and service discovery within a Local Area Network (LAN) using multicast exposed on the `5353/UDP` port.

{microshift-short} includes an embedded mDNS server for deployment scenarios in which the authoritative DNS server cannot be reconfigured to point clients to services on {microshift-short}. The embedded DNS server allows `.local` domains exposed by {microshift-short} to be discovered by other elements on the LAN.
