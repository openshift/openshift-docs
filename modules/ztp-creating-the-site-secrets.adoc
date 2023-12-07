// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

:_mod-docs-content-type: PROCEDURE
[id="ztp-creating-the-site-secrets_{context}"]
= Creating the managed bare-metal host secrets

Add the required `Secret` custom resources (CRs) for the managed bare-metal host to the hub cluster. You need a secret for the {ztp-first} pipeline to access the Baseboard Management Controller (BMC) and a secret for the assisted installer service to pull cluster installation images from the registry.

[NOTE]
====
The secrets are referenced from the `SiteConfig` CR by name. The namespace
must match the `SiteConfig` namespace.
====

.Procedure

. Create a YAML secret file containing credentials for the host Baseboard Management Controller (BMC) and a pull secret required for installing OpenShift and all add-on cluster Operators:

.. Save the following YAML as the file `example-sno-secret.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: example-sno-bmc-secret
  namespace: example-sno <1>
data: <2>
  password: <base64_password>
  username: <base64_username>
type: Opaque
---
apiVersion: v1
kind: Secret
metadata:
  name: pull-secret
  namespace: example-sno  <3>
data:
  .dockerconfigjson: <pull_secret> <4>
type: kubernetes.io/dockerconfigjson
----
<1> Must match the namespace configured in the related `SiteConfig` CR
<2> Base64-encoded values for `password` and `username`
<3> Must match the namespace configured in the related `SiteConfig` CR
<4> Base64-encoded pull secret

. Add the relative path to `example-sno-secret.yaml` to the `kustomization.yaml` file that you use to install the cluster.
