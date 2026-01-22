// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-crio-issues.adoc

:_mod-docs-content-type: CONCEPT
[id="about-crio_{context}"]
= About CRI-O container runtime engine

include::snippets/about-crio-snippet.adoc[]

When container runtime issues occur, verify the status of the `crio` systemd service on each node. Gather CRI-O journald unit logs from nodes that have container runtime issues.
