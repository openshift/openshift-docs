:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="distributed-tracing-rn-2-9-2"]
= Release notes for {DTProductName} 2.9.2
:context: distributed-tracing-rn-2-9-2

toc::[]

include::modules/distr-tracing-product-overview.adoc[leveloffset=+1]

[id="component-versions_distributed-tracing-rn-2-9-2"]
== Component versions in the {DTProductName} 2.9.2

[options="header"]
|===
|Operator |Component |Version
|{JaegerName}
|Jaeger
|1.47.0

|{OTELName}
|OpenTelemetry
|0.81.0

|{TempoName}
|Tempo
|2.1.1
|===

== CVEs

This release fixes link:https://bugzilla.redhat.com/show_bug.cgi?id=2246470[CVE-2023-46234].

[id="jaeger-release-notes_distributed-tracing-rn-2-9-2"]
== {JaegerName}

[id="known-issues_jaeger-release-notes_distributed-tracing-rn-2-9-2"]
=== Known issues

* Apache Spark is not supported.
ifndef::openshift-rosa[]

* The streaming deployment via AMQ/Kafka is unsupported on IBM Z and IBM Power Systems.
endif::openshift-rosa[]

[id="tempo-release-notes_distributed-tracing-rn-2-9-2"]
== {TempoName}

:FeatureName: The {TempoName}
include::snippets/technology-preview.adoc[leveloffset=+1]

[id="known-issues_tempo-release-notes_distributed-tracing-rn-2-9-2"]
=== Known issues

* Currently, the custom TLS CA option is not implemented for connecting to object storage. (link:https://issues.redhat.com/browse/TRACING-3462[TRACING-3462])

* Currently, when used with the {TempoOperator}, the Jaeger UI only displays services that have sent traces in the last 15 minutes. For services that did not send traces in the last 15 minutes, traces are still stored but not displayed in the Jaeger UI. (link:https://issues.redhat.com/browse/TRACING-3139[TRACING-3139])

* Currently, the {TempoShortName} fails on the IBM Z (`s390x`) architecture. (link:https://issues.redhat.com/browse/TRACING-3545[TRACING-3545])

* Currently, the Tempo query frontend service must not use internal mTLS when Gateway is not deployed. This issue does not affect the Jaeger Query API. The workaround is to disable mTLS. (link:https://issues.redhat.com/browse/TRACING-3510[TRACING-3510])
+
.Workaround
+
Disable mTLS as follows:
+
. Open the {TempoOperator} ConfigMap for editing by running the following command:
+
[source,terminal]
----
$ oc edit configmap tempo-operator-manager-config -n openshift-tempo-operator <1>
----
<1> The project where the {TempoOperator} is installed.

. Disable the mTLS in the operator configuration by updating the YAML file:
+
[source,yaml]
----
data:
  controller_manager_config.yaml: |
    featureGates:
      httpEncryption: false
      grpcEncryption: false
      builtInCertManagement:
        enabled: false
----

. Restart the {TempoOperator} pod by running the following command:
+
[source,terminal]
----
$ oc rollout restart deployment.apps/tempo-operator-controller -n openshift-tempo-operator
----


* Missing images for running the {TempoOperator} in restricted environments. The {TempoName} CSV is missing references to the operand images. (link:https://issues.redhat.com/browse/TRACING-3523[TRACING-3523])
+
.Workaround
+
Add the {TempoOperator} related images in the mirroring tool to mirror the images to the registry:
+
[source,yaml]
----
kind: ImageSetConfiguration
apiVersion: mirror.openshift.io/v1alpha2
archiveSize: 20
storageConfig:
  local:
    path: /home/user/images
mirror:
  operators:
  - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.13
    packages:
    - name: tempo-product
      channels:
      - name: stable
  additionalImages:
  - name: registry.redhat.io/rhosdt/tempo-rhel8@sha256:e4295f837066efb05bcc5897f31eb2bdbd81684a8c59d6f9498dd3590c62c12a
  - name: registry.redhat.io/rhosdt/tempo-gateway-rhel8@sha256:b62f5cedfeb5907b638f14ca6aaeea50f41642980a8a6f87b7061e88d90fac23
  - name: registry.redhat.io/rhosdt/tempo-gateway-opa-rhel8@sha256:8cd134deca47d6817b26566e272e6c3f75367653d589f5c90855c59b2fab01e9
  - name: registry.redhat.io/rhosdt/tempo-query-rhel8@sha256:0da43034f440b8258a48a0697ba643b5643d48b615cdb882ac7f4f1f80aad08e
----

[id="otel-release-notes_distributed-tracing-rn-2-9-2"]
== {OTELName}

:FeatureName: The {OTELName}
include::snippets/technology-preview.adoc[leveloffset=+1]

[id="known-issues_otel-release-notes_distributed-tracing-rn-2-9-2"]
=== Known issues

* Currently, you must manually set link:https://operatorframework.io/operator-capabilities/[operator maturity] to Level IV, Deep Insights. (link:https://issues.redhat.com/browse/TRACING-3431[TRACING-3431])

include::modules/support.adoc[leveloffset=+1]

include::modules/making-open-source-more-inclusive.adoc[leveloffset=+1]
