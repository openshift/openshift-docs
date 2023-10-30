:_mod-docs-content-type: PROCEDURE
[id="creating-a-custom-helm-chart-on-openshift_{context}"]
= Creating a custom Helm chart on {product-title}

.Procedure
. Create a new project:
+
[source,terminal]
----
$ oc new-project nodejs-ex-k
----

. Download an example Node.js chart that contains {product-title} objects:
+
[source,terminal]
----
$ git clone https://github.com/redhat-developer/redhat-helm-charts
----

. Go to the directory with the sample chart:
+
[source,terminal]
----
$ cd redhat-helm-charts/alpha/nodejs-ex-k/
----

. Edit the `Chart.yaml` file  and add a description of your chart:
+
[source,yaml]
----
apiVersion: v2 <1>
name: nodejs-ex-k <2>
description: A Helm chart for OpenShift <3>
icon: https://static.redhat.com/libs/redhat/brand-assets/latest/corp/logo.svg <4>
version: 0.2.1 <5>
----
+
<1> The chart API version. It should be `v2` for Helm charts that require at least Helm 3.
<2> The name of your chart.
<3> The description of your chart.
<4> The URL to an image to be used as an icon.
<5> The Version of your chart as per the Semantic Versioning (SemVer) 2.0.0 Specification.

. Verify that the chart is formatted properly:
+
[source,terminal]
----
$ helm lint
----
+
.Example output
[source,terminal]
----
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
----

. Navigate to the previous directory level:
+
[source,terminal]
----
$ cd ..
----

. Install the chart:
+
[source,terminal]
----
$ helm install nodejs-chart nodejs-ex-k
----

. Verify that the chart has installed successfully:
+
[source,terminal]
----
$ helm list
----
+
.Example output
[source,terminal]
----
NAME NAMESPACE REVISION UPDATED STATUS CHART APP VERSION
nodejs-chart nodejs-ex-k 1 2019-12-05 15:06:51.379134163 -0500 EST deployed nodejs-0.1.0  1.16.0
----
