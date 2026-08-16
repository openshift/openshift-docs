// Module included in the following assemblies:
//
// * networking/using-sctp.adoc

:image: registry.access.redhat.com/ubi9/ubi

ifdef::openshift-origin[]
:image: fedora:31
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="nw-sctp-verifying_{context}"]
= Verifying Stream Control Transmission Protocol (SCTP) is enabled

You can verify that SCTP is working on a cluster by creating a pod with an application that listens for SCTP traffic, associating it with a service, and then connecting to the exposed service.

.Prerequisites

* Access to the internet from the cluster to install the `nc` package.
* Install the OpenShift CLI (`oc`).
* Access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Create a pod starts an SCTP listener:

.. Create a file named `sctp-server.yaml` that defines a pod with the following YAML:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Pod
metadata:
  name: sctpserver
  labels:
    app: sctpserver
spec:
  containers:
    - name: sctpserver
      image: {image}
      command: ["/bin/sh", "-c"]
      args:
        ["dnf install -y nc && sleep inf"]
      ports:
        - containerPort: 30102
          name: sctpserver
          protocol: SCTP
----

.. Create the pod by entering the following command:
+
[source,terminal]
----
$ oc create -f sctp-server.yaml
----

. Create a service for the SCTP listener pod.

.. Create a file named `sctp-service.yaml` that defines a service with the following YAML:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: sctpservice
  labels:
    app: sctpserver
spec:
  type: NodePort
  selector:
    app: sctpserver
  ports:
    - name: sctpserver
      protocol: SCTP
      port: 30102
      targetPort: 30102
----

.. To create the service, enter the following command:
+
[source,terminal]
----
$ oc create -f sctp-service.yaml
----

. Create a pod for the SCTP client.

.. Create a file named `sctp-client.yaml` with the following YAML:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Pod
metadata:
  name: sctpclient
  labels:
    app: sctpclient
spec:
  containers:
    - name: sctpclient
      image: {image}
      command: ["/bin/sh", "-c"]
      args:
        ["dnf install -y nc && sleep inf"]
----

.. To create the `Pod` object, enter the following command:
+
[source,terminal]
----
$ oc apply -f sctp-client.yaml
----

. Run an SCTP listener on the server.

.. To connect to the server pod, enter the following command:
+
[source,terminal]
----
$ oc rsh sctpserver
----

.. To start the SCTP listener, enter the following command:
+
[source,terminal]
----
$ nc -l 30102 --sctp
----

. Connect to the SCTP listener on the server.

.. Open a new terminal window or tab in your terminal program.

.. Obtain the IP address of the `sctpservice` service. Enter the following command:
+
[source,terminal]
----
$ oc get services sctpservice -o go-template='{{.spec.clusterIP}}{{"\n"}}'
----

.. To connect to the client pod, enter the following command:
+
[source,terminal]
----
$ oc rsh sctpclient
----

.. To start the SCTP client, enter the following command. Replace `<cluster_IP>` with the cluster IP address of the `sctpservice` service.
+
[source,terminal]
----
# nc <cluster_IP> 30102 --sctp
----
