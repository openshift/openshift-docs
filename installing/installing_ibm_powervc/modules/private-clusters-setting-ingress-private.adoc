// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc

:_mod-docs-content-type: PROCEDURE
[id="private-clusters-setting-ingress-private_{context}"]
= Setting the Ingress Controller to private

After you deploy a cluster, you can modify its Ingress Controller to use only a private zone.

.Procedure

. Modify the default Ingress Controller to use only an internal endpoint:
+
[source,terminal]
----
$ oc replace --force --wait --filename - <<EOF
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: default
spec:
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal
EOF
----
+
.Example output
[source,terminal]
----
ingresscontroller.operator.openshift.io "default" deleted
ingresscontroller.operator.openshift.io/default replaced
----
+
The public DNS entry is removed, and the private zone entry is updated.
