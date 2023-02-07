// Module included in the following assemblies:
//
// * monitoring/application-monitoring.adoc

[id="exposing-custom-application-metrics-for-horizontal-pod-autoscaling_{context}"]
= Exposing custom application metrics for horizontal pod autoscaling

You can use the `prometheus-adapter` resource to expose custom application metrics for the horizontal pod autoscaler.

.Prerequisites

* You have a custom Prometheus instance installed. In this example, it is presumed that Prometheus was installed in a user-defined `custom-prometheus` project.
+
[NOTE]
====
Custom Prometheus instances and the Prometheus Operator installed through Operator Lifecycle Manager (OLM) can cause issues with user-defined workload monitoring if it is enabled. Custom Prometheus instances are not supported in {product-title}.
====
+
* You have deployed an application and a service in a user-defined project. In this example, it is presumed that the application and its service monitor were installed in a user-defined `custom-prometheus` project.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a YAML file for your configuration. In this example, the file is called `deploy.yaml`.

. Add configuration details for creating the service account, roles, and role bindings for `prometheus-adapter`:
+
[source,yaml,subs=quotes]
----
kind: ServiceAccount
apiVersion: v1
metadata:
  name: custom-metrics-apiserver
  namespace: custom-prometheus
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: custom-metrics-server-resources
rules:
- apiGroups:
  - custom.metrics.k8s.io
  resources: ["\*"]
  verbs: ["*"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: custom-metrics-resource-reader
rules:
- apiGroups:
  - ""
  resources:
  - namespaces
  - pods
  - services
  verbs:
  - get
  - list
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: custom-metrics:system:auth-delegator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
- kind: ServiceAccount
  name: custom-metrics-apiserver
  namespace: custom-prometheus
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: custom-metrics-auth-reader
  namespace: kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: extension-apiserver-authentication-reader
subjects:
- kind: ServiceAccount
  name: custom-metrics-apiserver
  namespace: custom-prometheus
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: custom-metrics-resource-reader
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: custom-metrics-resource-reader
subjects:
- kind: ServiceAccount
  name: custom-metrics-apiserver
  namespace: custom-prometheus
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: hpa-controller-custom-metrics
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: custom-metrics-server-resources
subjects:
- kind: ServiceAccount
  name: horizontal-pod-autoscaler
  namespace: kube-system
---
----

. Add configuration details for the custom metrics for `prometheus-adapter`:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: adapter-config
  namespace: custom-prometheus
data:
  config.yaml: |
    rules:
    - seriesQuery: 'http_requests_total{namespace!="",pod!=""}' <1>
      resources:
        overrides:
          namespace: {resource: "namespace"}
          pod: {resource: "pod"}
          service: {resource: "service"}
      name:
        matches: "^(.*)_total"
        as: "${1}_per_second" <2>
      metricsQuery: 'sum(rate(<<.Series>>{<<.LabelMatchers>>}[2m])) by (<<.GroupBy>>)'
---
----
<1> Specifies the chosen metric to be the number of HTTP requests.
<2> Specifies the frequency for the metric.

. Add configuration details for registering `prometheus-adapter` as an API service:
+
[source,yaml,subs=quotes]
----
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.beta.openshift.io/serving-cert-secret-name: prometheus-adapter-tls
  labels:
    name: prometheus-adapter
  name: prometheus-adapter
  namespace: custom-prometheus
spec:
  ports:
  - name: https
    port: 443
    targetPort: 6443
  selector:
    app: prometheus-adapter
  type: ClusterIP
---
apiVersion: apiregistration.k8s.io/v1beta1
kind: APIService
metadata:
  name: v1beta1.custom.metrics.k8s.io
spec:
  service:
    name: prometheus-adapter
    namespace: custom-prometheus
  group: custom.metrics.k8s.io
  version: v1beta1
  insecureSkipTLSVerify: true
  groupPriorityMinimum: 100
  versionPriority: 100
---
----

. List the Prometheus Adapter image:
+
[source,terminal]
----
$ oc get -n openshift-monitoring deploy/prometheus-adapter -o jsonpath="{..image}"
----

. Add configuration details for deploying `prometheus-adapter`:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: prometheus-adapter
  name: prometheus-adapter
  namespace: custom-prometheus
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus-adapter
  template:
    metadata:
      labels:
        app: prometheus-adapter
      name: prometheus-adapter
    spec:
      serviceAccountName: custom-metrics-apiserver
      containers:
      - name: prometheus-adapter
        image: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:a46915a206cd7d97f240687c618dd59e8848fcc3a0f51e281f3384153a12c3e0 <1>
        args:
        - --secure-port=6443
        - --tls-cert-file=/var/run/serving-cert/tls.crt
        - --tls-private-key-file=/var/run/serving-cert/tls.key
        - --logtostderr=true
        - --prometheus-url=http://prometheus-operated.default.svc:9090/
        - --metrics-relist-interval=1m
        - --v=4
        - --config=/etc/adapter/config.yaml
        ports:
        - containerPort: 6443
        volumeMounts:
        - mountPath: /var/run/serving-cert
          name: volume-serving-cert
          readOnly: true
        - mountPath: /etc/adapter/
          name: config
          readOnly: true
        - mountPath: /tmp
          name: tmp-vol
      volumes:
      - name: volume-serving-cert
        secret:
          secretName: prometheus-adapter-tls
      - name: config
        configMap:
          name: adapter-config
      - name: tmp-vol
        emptyDir: {}
----
<1> Specifies the Prometheus Adapter image found in the previous step.

. Apply the configuration to the cluster:
+
[source,terminal]
----
$ oc apply -f deploy.yaml
----
+
.Example output
[source,terminal]
----
serviceaccount/custom-metrics-apiserver created
clusterrole.rbac.authorization.k8s.io/custom-metrics-server-resources created
clusterrole.rbac.authorization.k8s.io/custom-metrics-resource-reader created
clusterrolebinding.rbac.authorization.k8s.io/custom-metrics:system:auth-delegator created
rolebinding.rbac.authorization.k8s.io/custom-metrics-auth-reader created
clusterrolebinding.rbac.authorization.k8s.io/custom-metrics-resource-reader created
clusterrolebinding.rbac.authorization.k8s.io/hpa-controller-custom-metrics created
configmap/adapter-config created
service/prometheus-adapter created
apiservice.apiregistration.k8s.io/v1.custom.metrics.k8s.io created
deployment.apps/prometheus-adapter created
----

. Verify that the `prometheus-adapter` pod in your user-defined project is in a `Running` state. In this example the project is `custom-prometheus`:
+
[source,terminal]
----
$ oc -n custom-prometheus get pods prometheus-adapter-<string>
----

. The metrics for the application are now exposed and they can be used to configure horizontal pod autoscaling.
