// Module included in the following assemblies:
//
// * virt/support/virt-monitoring-vm-health.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-readiness-liveness-probes_{context}"]

= About readiness and liveness probes

Use readiness and liveness probes to detect and handle unhealthy virtual machines (VMs). You can include one or more probes in the specification of the VM to ensure that traffic does not reach a VM that is not ready for it and that a new VM is created when a VM becomes unresponsive.

A _readiness probe_ determines whether a VM is ready to accept service requests. If the probe fails, the VM is removed from the list of available endpoints until the VM is ready.

A _liveness probe_ determines whether a VM is responsive. If the probe fails, the VM is deleted and a new VM is created to restore responsiveness.

You can configure readiness and liveness probes by setting the `spec.readinessProbe` and the `spec.livenessProbe` fields of the `VirtualMachine` object. These fields support the following tests:

HTTP GET:: The probe determines the health of the VM by using a web hook. The test is successful if the HTTP response code is between 200 and 399. You can use an HTTP GET test with applications that return HTTP status codes when they are completely initialized.

TCP socket:: The probe attempts to open a socket to the VM. The VM is only considered healthy if the probe can establish a connection. You can use a TCP socket test with applications that do not start listening until initialization is complete.

Guest agent ping:: The probe uses the `guest-ping` command to determine if the QEMU guest agent is running on the virtual machine.
