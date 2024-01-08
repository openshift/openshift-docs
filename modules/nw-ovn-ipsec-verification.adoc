// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/about-ipsec-ovn.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ovn-ipsec-verification_{context}"]
= Verifying that IPsec is enabled

As a cluster administrator, you can verify that IPsec is enabled.

.Verification

. To find the names of the OVN-Kubernetes data plane pods, enter the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ovn-kubernetes -l=app=ovnkube-node
----
+
.Example output
[source,terminal]
----
ovnkube-node-5xqbf                       8/8     Running   0              28m
ovnkube-node-6mwcx                       8/8     Running   0              29m
ovnkube-node-ck5fr                       8/8     Running   0              31m
ovnkube-node-fr4ld                       8/8     Running   0              26m
ovnkube-node-wgs4l                       8/8     Running   0              33m
ovnkube-node-zfvcl                       8/8     Running   0              34m
----

. Verify that IPsec is enabled on your cluster:
+
[source,terminal]
----
$ oc -n openshift-ovn-kubernetes -c nbdb rsh ovnkube-node-<XXXXX> ovn-nbctl --no-leader-only get nb_global . ipsec
----
+
--
where:

`<XXXXX>`:: Specifies the random sequence of letters for a pod from the previous step.
--
+
.Example output
[source,text]
----
true
----
