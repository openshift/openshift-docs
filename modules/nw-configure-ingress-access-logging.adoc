// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-configure-ingress-access-logging_{context}"]
= Configuring Ingress access logging

You can configure the Ingress Controller to enable access logs. If you have clusters that do not receive much traffic, then you can log to a sidecar. If you have high traffic clusters, to avoid exceeding the capacity of the logging stack or  to integrate with a logging infrastructure outside of {product-title}, you can forward logs to a custom syslog endpoint. You can also specify the format for access logs.

Container logging is useful to enable access logs on low-traffic clusters when there is no existing Syslog logging infrastructure, or for short-term use while diagnosing problems with the Ingress Controller.

Syslog is needed for high-traffic clusters where access logs could exceed the OpenShift Logging stack's capacity, or for environments where any logging solution needs to integrate with an existing Syslog logging infrastructure. The Syslog use-cases can overlap.

.Prerequisites

* Log in as a user with `cluster-admin` privileges.

.Procedure

Configure Ingress access logging to a sidecar.

* To configure Ingress access logging, you must specify a destination using `spec.logging.access.destination`. To specify logging to a sidecar container, you must specify `Container` `spec.logging.access.destination.type`. The following example is an Ingress Controller definition that logs to a `Container` destination:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 2
  logging:
    access:
      destination:
        type: Container
----

* When you configure the Ingress Controller to log to a sidecar, the operator creates a container named `logs` inside the Ingress Controller Pod:
+
[source,terminal]
----
$ oc -n openshift-ingress logs deployment.apps/router-default -c logs
----
+
.Example output
[source,terminal]
----
2020-05-11T19:11:50.135710+00:00 router-default-57dfc6cd95-bpmk6 router-default-57dfc6cd95-bpmk6 haproxy[108]: 174.19.21.82:39654 [11/May/2020:19:11:50.133] public be_http:hello-openshift:hello-openshift/pod:hello-openshift:hello-openshift:10.128.2.12:8080 0/0/1/0/1 200 142 - - --NI 1/1/0/0/0 0/0 "GET / HTTP/1.1"
----

Configure Ingress access logging to a Syslog endpoint.

* To configure Ingress access logging, you must specify a destination using `spec.logging.access.destination`. To specify logging to a Syslog endpoint destination, you must specify `Syslog` for `spec.logging.access.destination.type`. If the destination type is `Syslog`, you must also specify a destination endpoint using `spec.logging.access.destination.syslog.endpoint` and you can specify a facility using `spec.logging.access.destination.syslog.facility`. The following example is an Ingress Controller definition that logs to a `Syslog` destination:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 2
  logging:
    access:
      destination:
        type: Syslog
        syslog:
          address: 1.2.3.4
          port: 10514
----
+
[NOTE]
====
The `syslog` destination port must be UDP.
====

Configure Ingress access logging with a specific log format.

* You can specify `spec.logging.access.httpLogFormat` to customize the log format. The following example is an Ingress Controller definition that logs to a `syslog` endpoint with IP address 1.2.3.4 and port 10514:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 2
  logging:
    access:
      destination:
        type: Syslog
        syslog:
          address: 1.2.3.4
          port: 10514
      httpLogFormat: '%ci:%cp [%t] %ft %b/%s %B %bq %HM %HU %HV'
----

Disable Ingress access logging.

* To disable Ingress access logging, leave `spec.logging` or `spec.logging.access` empty:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 2
  logging:
    access: null
----

Allow the Ingress Controller to modify the HAProxy log length when using a sidecar.

* Use `spec.logging.access.destination.syslog.maxLength` if you are using `spec.logging.access.destination.type: Syslog`.

+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 2
  logging:
    access:
      destination:
        type: Syslog
        syslog:
          address: 1.2.3.4
          maxLength: 4096
          port: 10514
----
* Use `spec.logging.access.destination.container.maxLength` if you are using `spec.logging.access.destination.type: Container`.

+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 2
  logging:
    access:
      destination:
        type: Container
        container:
          maxLength: 8192
----

