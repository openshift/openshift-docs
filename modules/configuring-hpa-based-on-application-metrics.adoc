// Module included in the following assemblies:
//
// * machine_management/configuring-hpa-for-an-application.adoc

[id="configuring-hpa-based-on-application-metrics_{context}"]
= Configuring HPA based on application metrics

If you configure an application to export metrics, you can set up Horizontal Pod Autoscaling (HPA) based on these metrics.

.Procedure

. Create a YAML file for your configuration. In this example, it is called `deploy.yaml`.

. Add configuration for deploying the horizontal pod autoscaler for the application. This example configures and deploys HPA based on the application `http_requests_per_second` metric for the sample application configured in the "Application monitoring" section:
+
[source,yaml]
----
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: example-app-scaler
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: example-app <1>
  minReplicas: 3 <2>
  maxReplicas: 10 <3>
  metrics:
  - type: Pods
    pods:
      metricName: http_requests_per_second <4>
      targetAverageValue: 10 <5>
----
<1> `name` specifies the application.
<2> `minReplicas` specifies the minimum number of replicas for the HPA to maintain for the application.
<3> `maxReplicas` specifies the maximum number of replicas for the HPA to maintain for the application.
<4> `metricName` specifies the metric upon which HPA is based. Here, specify the metric you previously exposed for your application.
<5> `targetAverageValue` specifies the value of the metric for the HPA to try to maintain by increasing or decreasing the number of replicas.

. Apply the configuration file to the cluster:
+
[source,terminal]
----
$ oc apply -f deploy.yaml
----
