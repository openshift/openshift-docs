// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ovn-kubernetes-alerts-cli_{context}"]
= Viewing OVN-Kubernetes alerts in the CLI

You can get information about alerts and their governing alerting rules and silences from the command line.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.
* The OpenShift CLI (`oc`) installed.
* You have installed `jq`.

.Procedure

. View active or firing alerts by running the following commands.

.. Set the alert manager route environment variable by running the following command:
+
[source,terminal]
----
$ ALERT_MANAGER=$(oc get route alertmanager-main -n openshift-monitoring \
-o jsonpath='{@.spec.host}')
----

.. Issue a `curl` request to the alert manager route API by running the following command, replacing `$ALERT_MANAGER` with the URL of your `Alertmanager` instance:
+
[source,terminal]
----
$ curl -s -k -H "Authorization: Bearer $(oc create token prometheus-k8s -n openshift-monitoring)" https://$ALERT_MANAGER/api/v1/alerts | jq '.data[] | "\(.labels.severity) \(.labels.alertname) \(.labels.pod) \(.labels.container) \(.labels.endpoint) \(.labels.instance)"'
----

. View alerting rules by running the following command:
+
[source,terminal]
----
$ oc -n openshift-monitoring exec -c prometheus prometheus-k8s-0 -- curl -s 'http://localhost:9090/api/v1/rules' | jq '.data.groups[].rules[] | select(((.name|contains("ovn")) or (.name|contains("OVN")) or (.name|contains("Ovn")) or (.name|contains("North")) or (.name|contains("South"))) and .type=="alerting")'
----