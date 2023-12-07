//Module included in the following assemblies:
//
//* microshift_running_apps/microshift-greenboot-workload-scripts.adoc

:_mod-docs-content-type: CONCEPT
[id="microshift-greenboot-how-workload-health-check-scripts-work_{context}"]
= How workload health check scripts work

The workload or application health check script described in this tutorial uses the {microshift-short} health check functions that are available in the `/usr/share/microshift/functions/greenboot.sh` file. This enables you to reuse procedures already implemented for the {microshift-short} core services.

The script starts by running checks that the basic functions of the workload are operating as expected. To run the script successfully:

* Execute the script from a root user account.
* Enable the {microshift-short} service.

The health check performs the following actions:

* Gets a wait timeout of the current boot cycle for the `wait_for` function.
* Calls the `namespace_images_downloaded` function to wait until pod images are available.
* Calls the `namespace_pods_ready` function to wait until pods are ready.
* Calls the `namespace_pods_not_restarting` function to verify pods are not restarting.

[NOTE]
====
Restarting pods can indicate a crash loop.
====