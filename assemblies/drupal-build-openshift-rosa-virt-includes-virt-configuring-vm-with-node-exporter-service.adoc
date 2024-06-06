// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-custom-metrics-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-vm-with-node-exporter-service_{context}"]
= Configuring a virtual machine with the node exporter service

Download the `node-exporter` file on to the virtual machine. Then, create a `systemd` service that runs the node-exporter service when the virtual machine boots.

.Prerequisites
* The pods for the component are running in the `openshift-user-workload-monitoring` project.
* Grant the `monitoring-edit` role to users who need to monitor this user-defined project.

.Procedure

. Log on to the virtual machine.

. Download the `node-exporter` file on to the virtual machine by using the directory path that applies to the version of `node-exporter` file.
+
[source,terminal]
----
$ wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz
----

. Extract the executable and place it in the `/usr/bin` directory.
+
[source,terminal]
----
$ sudo tar xvf node_exporter-1.3.1.linux-amd64.tar.gz \
    --directory /usr/bin --strip 1 "*/node_exporter"
----

. Create a `node_exporter.service` file in this directory path: `/etc/systemd/system`. This `systemd` service file runs the node-exporter service when the virtual machine reboots.
+
[source,terminal]
----
[Unit]
Description=Prometheus Metrics Exporter
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/usr/bin/node_exporter

[Install]
WantedBy=multi-user.target
----

. Enable and start the `systemd` service.
+
[source,terminal]
----
$ sudo systemctl enable node_exporter.service
$ sudo systemctl start node_exporter.service
----

.Verification
* Verify that the node-exporter agent is reporting metrics from the virtual machine.
+
[source,terminal]
----
$ curl http://localhost:9100/metrics
----
+
.Example output
[source,terminal]
----
go_gc_duration_seconds{quantile="0"} 1.5244e-05
go_gc_duration_seconds{quantile="0.25"} 3.0449e-05
go_gc_duration_seconds{quantile="0.5"} 3.7913e-05
----
