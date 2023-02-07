// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/odo-architecture.adoc

[id="openshift-cluster-objects_{context}"]
= OpenShift cluster objects

== Init Containers
Init containers are specialized containers that run before the application container starts and configure the necessary environment for the application containers to run. Init containers can have files that application images do not have, for example setup scripts. Init containers always run to completion and the application container does not start if any of the init containers fails.

The pod created by {odo-title} executes two Init Containers:

* The `copy-supervisord` Init container.
* The `copy-files-to-volume` Init container.

=== `copy-supervisord`

The `copy-supervisord` Init container copies necessary files onto an `emptyDir` volume. The main application container utilizes these files from the `emptyDir` volume.

.Files that are copied onto the `emptyDir` volume:
* Binaries:
** `go-init` is a minimal init system. It runs as the first process (PID 1) inside the application container. go-init starts the `SupervisorD` daemon which runs the developer code. go-init is required to handle orphaned processes.
** `SupervisorD` is a process control system. It watches over configured processes and ensures that they are running. It also restarts services when necessary. For {odo-title}, `SupervisorD` executes and monitors the developer code.

* Configuration files:
** `supervisor.conf` is the configuration file necessary for the SupervisorD daemon to start.
* Scripts:
** `assemble-and-restart` is an OpenShift S2I concept to build and deploy user-source code. The assemble-and-restart script first assembles the user source code inside the application container and then restarts SupervisorD for user changes to take effect.
** `Run` is an OpenShift S2I concept of executing the assembled source code. The `run` script executes the assembled code created by the `assemble-and-restart` script.
** `s2i-setup` is a script that creates files and directories which are necessary for the `assemble-and-restart` and run scripts to execute successfully. The script is executed whenever the application container starts.

* Directories:
** `language-scripts`: OpenShift S2I allows custom `assemble` and `run` scripts. A few language specific custom scripts are present in the `language-scripts` directory. The custom scripts provide additional configuration to make {odo-title} debug work.

The `emptyDir` volume is mounted at the `/opt/odo` mount point for both the Init container and the application container.

=== `copy-files-to-volume`
The `copy-files-to-volume` Init container copies files that are in `/opt/app-root` in the S2I builder image onto the persistent volume. The volume is then mounted at the same location (`/opt/app-root`) in an application container.

Without the persistent volume on `/opt/app-root` the data in this directory is lost when the persistent volume claim is mounted at the same location.

The PVC is mounted at the `/mnt` mount point inside the Init container.

== Application container
Application container is the main container inside of which the user-source code executes.

Application container is mounted with two volumes:

* `emptyDir` volume mounted at `/opt/odo`
* The persistent volume mounted at `/opt/app-root`

`go-init` is executed as the first process inside the application container. The `go-init` process then starts the `SupervisorD` daemon.

`SupervisorD` executes and monitors the user assembled source code. If the user process crashes, `SupervisorD` restarts it.

== Persistent volumes and persistent volume claims
A persistent volume claim (PVC) is a volume type in Kubernetes which provisions a persistent volume. The life of a persistent volume is independent of a pod lifecycle. The data on the persistent volume persists across pod restarts.

The `copy-files-to-volume` Init container copies necessary files onto the persistent volume. The main application container utilizes these files at runtime for execution.

The naming convention of the persistent volume is <component_name>-s2idata.

[options="header"]
|===
| Container | PVC mounted at
| `copy-files-to-volume`
| `/mnt`

| Application container
| `/opt/app-root`
|===

== emptyDir volume
An `emptyDir` volume is created when a pod is assigned to a node, and exists as long as that pod is running on the node. If the container is restarted or moved, the content of the `emptyDir` is removed, Init container restores the data back to the `emptyDir`. `emptyDir` is initially empty.

The `copy-supervisord` Init container copies necessary files onto the `emptyDir` volume. These files are then utilized by the main application container at runtime for execution.

[options="header"]
|===
| Container | `emptyDir volume` mounted at
| `copy-supervisord`
| `/opt/odo`

| Application container
| `/opt/odo`
|===

== Service
A service is a Kubernetes concept of abstracting the way of communicating with a set of pods.

{odo-title} creates a service for every application pod to make it accessible for communication.
