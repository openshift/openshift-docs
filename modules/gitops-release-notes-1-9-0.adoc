// Module included in the following assembly:
//
// * gitops/gitops-release-notes.adoc
:_mod-docs-content-type: REFERENCE
[id="gitops-release-notes-1-9-0_{context}"]
= Release notes for {gitops-title} 1.9.0

{gitops-title} 1.9.0 is now available on {product-title} 4.12 and 4.13.

[id="errata-updates-1-9-0_{context}"]
== Errata updates

=== RHSA-2023:3557 - {gitops-title} 1.9.0 security update advisory

Issued: 2023-06-09

The list of security fixes that are included in this release is documented in the following advisory:

* link:https://access.redhat.com/errata/RHSA-2023:3557[RHSA-2023:3557]

If you have installed the {gitops-title} Operator, run the following command to view the container images in this release:

[source,terminal]
----
$ oc describe deployment gitops-operator-controller-manager -n openshift-operators
----

[id="new-features-1-9-0_{context}"]
== New features

The current release adds the following improvements:

* With this update, you can use a custom `must-gather` tool to collect diagnostic information for project-level resources, cluster-level resources, and {gitops-title} components. This tool provides the debugging information about the cluster associated with {gitops-title}, which you can share with the Red Hat Support team for analysis. link:https://issues.redhat.com/browse/GITOPS-2797[GITOPS-2797]
+
[IMPORTANT]
====
The custom `must-gather` tool is a Technology Preview feature.
====

* With this update, you can add support to progressive delivery using Argo Rollouts. Currently, the supported traffic manager is only {SMProductName}. link:https://issues.redhat.com/browse/GITOPS-959[GITOPS-959]
+
[IMPORTANT]
====
Argo Rollouts is a Technology Preview feature.
====

[role="_additional-resources"]
.Additional resources
* link:https://argo-rollouts-manager.readthedocs.io/en/latest/crd_reference/[Using Argo Rollouts]

[id="deprecated-features-1-9-0_{context}"]
== Deprecated and removed features

* In {gitops-title} 1.7.0,  the `.spec.resourceCustomizations` parameter was deprecated. The deprecated `.spec.resourceCustomizations` parameter is planned to be removed in the upcoming {gitops-title} GA v1.10.0 release. You can use the new formats `spec.ResourceHealthChecks`, `spec.ResourceIgnoreDifferences`, and `spec.ResourceActions` instead. link:https://issues.redhat.com/browse/GITOPS-2890[GITOPS-2890]

* With this update, the support for the following deprecated `sso` and `dex` fields extends until the upcoming {gitops-title} GA v1.10.0 release:
+
** The `.spec.sso.image`, `.spec.sso.version`, `.spec.sso.resources`, and `.spec.sso.verifyTLS` fields.
** The `.spec.dex` parameter along with `DISABLE_DEX`.
+
The deprecated previous `sso` and `dex` fields were earlier scheduled for removal in the {gitops-title} v1.9.0 release but are now planned to be removed in the upcoming {gitops-title} GA v1.10.0 release.
link:https://issues.redhat.com/browse/GITOPS-2904[GITOPS-2904]

[id="fixed-issues-1-9-0_{context}"]
== Fixed issues
The following issues have been resolved in the current release:

* Before this update, when the `argocd-server-tls` secret was updated with a new certificate Argo CD was not always picking up this secret. As a result, the old expired certificate was presented. This update fixes the issue with a new `GetCertificate` function and ensures that the latest version of certificates is in use. When adding new certificates, now Argo CD picks them up automatically without the user having to restart the `argocd-server` pod. link:https://issues.redhat.com/browse/GITOPS-2375[GITOPS-2375]

* Before this update, when enforcing GPG signature verification against a `targetRevision` integer pointing to a signed Git tag, users got a `Target revision in Git is not signed` error. This update fixes the issue and lets users enforce GPG signature verification against signed Git tags. link:https://issues.redhat.com/browse/GITOPS-2418[GITOPS-2418]

* Before this update, users could not connect to Microsoft Team Foundation Server (TFS) type Git repositories through Argo CD deployed by the Operator. This update fixes the issue by updating the Git version to
2.39.3 in the Operator. link:https://issues.redhat.com/browse/GITOPS-2768[GITOPS-2768]

* Before this update, when the Operator was deployed and running with the High availability (HA) feature enabled, setting resource limits under the `.spec.ha.resources` field did not affect Redis HA pods. This update fixes the reconciliation by adding checks in the Redis reconciliation code. These checks ensure whether the `spec.ha.resources` field in the Argo CD custom resource (CR) is updated. When the Argo CD CR is updated with new CPU and memory requests or limit values for HA, now these changes are applied to the Redis HA pods. link:https://issues.redhat.com/browse/GITOPS-2404[GITOPS-2404]

* Before this update, if a namespace-scoped Argo CD instance was managing multiple namespaces by using the `managed-by` label and one of those managed namespaces was in a *Terminating* state, the Argo CD instance could not deploy resources to all other managed namespaces. This update fixes the issue by enabling the Operator to remove the `managed-by` label from any previously managed now terminating namespace. Now, a terminating namespace managed by a namespace-scoped Argo CD instance does not block the deployment of resources to other managed namespaces. link:https://issues.redhat.com/browse/GITOPS-2627[GITOPS-2627]

[id="known-issues-1-10_{context}"]
== Known issues
* Currently, the Argo CD does not read the Transport Layer Security (TLS) certificates from the path specified in the `argocd-tls-certs-cm` config map resulting in the `x509: certificate signed by unknown authority` error.
+
Workaround: Perform the following steps:

. Add the `SSL_CERT_DIR` environment variable:
+
.Example Argo CD custom resource

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: repo
spec:
   ...
  repo:
    env:
      - name: SSL_CERT_DIR
        value: /tmp/sslcertdir
    volumeMounts:
      - name: ssl
        mountPath: /tmp/sslcertdir
    volumes:
      - name: ssl
        configMap:
          name: user-ca-bundle
   ...
----

. Create an empty config map in the namespace where the subscription for your Operator exists and include the following label:
+
.Example config map

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-ca-bundle <1>
  labels:
    config.openshift.io/inject-trusted-cabundle: "true" <2>
----
<1> Name of the config map.
<2> Requests the Cluster Network Operator to inject the merged bundle.
+
After creating this config map, the `user-ca-bundle` content from the `openshift-config` namespace automatically gets injected into this config map, even merged with the system ca-bundle. link:https://issues.redhat.com/browse/GITOPS-1482[GITOPS-1482]
