[id="adding-new-devices_{context}"]
= Adding new devices

Adding a new device is semi-automatic. The provisioner periodically checks for new mounts in configured directories. Administrators must create a new subdirectory, mount a device, and allow Pods to use the device by applying the SELinux label, for example:

----
$ chcon -R unconfined_u:object_r:svirt_sandbox_file_t:s0 /mnt/local-storage/
----

[WARNING]
====
Omitting any of these steps may result in the wrong PV being created.
====
