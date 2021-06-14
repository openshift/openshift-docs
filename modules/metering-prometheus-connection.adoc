// Module included in the following assemblies:
//
// * metering/configuring_metering/metering-configure-reporting-operator.adoc

[id="metering-prometheus-connection_{context}"]
= Securing a Prometheus connection

When you install metering on {product-title}, Prometheus is available at https://prometheus-k8s.openshift-monitoring.svc:9091/.

To secure the connection to Prometheus, the default metering installation uses the {product-title} certificate authority (CA). If your Prometheus instance uses a different CA, you can inject the CA through a config map. You can also configure the Reporting Operator to use a specified bearer token to authenticate with Prometheus.

.Procedure

* Inject the CA that your Prometheus instance uses through a config map. For example:
+
[source,yaml]
----
spec:
  reporting-operator:
    spec:
      config:
        prometheus:
          certificateAuthority:
            useServiceAccountCA: false
            configMap:
              enabled: true
              create: true
              name: reporting-operator-certificate-authority-config
              filename: "internal-ca.crt"
              value: |
                -----BEGIN CERTIFICATE-----
                (snip)
                -----END CERTIFICATE-----
----
+
Alternatively, to use the system certificate authorities for publicly valid certificates, set both `useServiceAccountCA` and `configMap.enabled` to `false`.

* Specify a bearer token to authenticate with Prometheus. For example:

[source,yaml]
----
spec:
  reporting-operator:
    spec:
      config:
        prometheus:
          metricsImporter:
            auth:
              useServiceAccountToken: false
              tokenSecret:
                enabled: true
                create: true
                value: "abc-123"
----
