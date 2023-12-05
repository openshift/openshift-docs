// Module included in the following assemblies:
//
// * virt/about_virt/virt-security-policies.adoc

[id="virt-automatic-certificates-renewal_{context}"]
= TLS certificates

TLS certificates for {VirtProductName} components are renewed and rotated automatically. You are not required to refresh them manually.

.Automatic renewal schedules

TLS certificates are automatically deleted and replaced according to the following schedule:

* KubeVirt certificates are renewed daily.

* Containerized Data Importer controller (CDI)
 certificates are renewed every 15 days.

* MAC pool certificates are renewed every year.

Automatic TLS certificate rotation does not disrupt any operations. For example, the following operations continue to function without any disruption:

* Migrations

* Image uploads

* VNC and console connections
