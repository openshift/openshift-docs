# Example Dashboards and Alerts

Explore a variety of starting points for monitoring your Kuadrant installation with our [examples](https://github.com/Kuadrant/kuadrant-operator/tree/main/examples) folder. These dashboards and alerts are ready-to-use and easily customizable to fit your environment.

There are some example dashboards uploaded to [Grafana.com](https://grafana.com/grafana/dashboards/) . You can use the ID's listed below to import these dashboards into Grafana:

| Name     | ID |
| ----------- | ----------- |
| [App Developer Dashboard](https://grafana.com/grafana/dashboards/20970)      | `20970`       |
| [Business User Dashboard](https://grafana.com/grafana/dashboards/20981)   | `20981`        |
| [Platform Engineer Dashboard](https://grafana.com/grafana/dashboards/20982) | `20982` |

## Dashboards

### Importing Dashboards into Grafana

For more details on how to import dashboards into Grafana, visit the [import dashboards](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/import-dashboards/) page. 

- **UI Method:**
    - **JSON** -  Use the 'Import' feature in the Grafana UI to upload dashboard JSON files directly.
    - **ID** - Use the 'Import' feature in the Grafana UI to import via [Grafana.com](https://grafana.com/grafana/dashboards/) using a Dashboard ID. 
- **ConfigMap Method:** Automate dashboard provisioning by adding files to a ConfigMap, which should be mounted at `/etc/grafana/provisioning/dashboards`.

Datasources are configured as template variables, automatically integrating with your existing data sources. Metrics for these dashboards are sourced from [Prometheus](https://github.com/prometheus/prometheus). For more details on the metrics used, visit the [metrics](https://docs.kuadrant.io/kuadrant-operator/doc/observability/metrics/) documentation page.

## Alerts

### Setting Up Alerts in Prometheus

You can integrate the [example alerts](https://github.com/Kuadrant/kuadrant-operator/tree/main/examples) into Prometheus as `PrometheusRule` resources. Feel free to adjust alert thresholds to suit your specific operational needs.

Additionally, [Service Level Objective (SLO)](https://sre.google/sre-book/service-level-objectives/) alerts generated with [Sloth](https://sloth.dev/) are included. A benefit of these alerts is the ability to integrate them with this [SLO dashboard](https://grafana.com/grafana/dashboards/14348-slo-detail/), which utilizes generated labels to comprehensively overview your SLOs.

Further information on the metrics used for these alerts can be found on the [metrics](https://docs.kuadrant.io/kuadrant-operator/doc/observability/metrics/) page.
