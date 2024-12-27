:_mod-docs-content-type: PROCEDURE
[id="cluster-logging-collector-log-forward-cloudwatch_{context}"]
= Forwarding logs to Amazon CloudWatch

You can forward logs to Amazon CloudWatch, a monitoring and log storage service hosted by Amazon Web Services (AWS). You can forward logs to CloudWatch in addition to, or instead of, the default log store.

To configure log forwarding to CloudWatch, you must create a `ClusterLogForwarder` custom resource (CR) with an output for CloudWatch, and a pipeline that uses the output.

.Procedure

. Create a `Secret` YAML file that uses the `aws_access_key_id` and `aws_secret_access_key` fields to specify your base64-encoded AWS credentials. For example:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: cw-secret
  namespace: openshift-logging
data:
  aws_access_key_id: QUtJQUlPU0ZPRE5ON0VYQU1QTEUK
  aws_secret_access_key: d0phbHJYVXRuRkVNSS9LN01ERU5HL2JQeFJmaUNZRVhBTVBMRUtFWQo=
----

. Create the secret. For example:
+
[source,terminal]
----
$ oc apply -f cw-secret.yaml
----

. Create or edit a YAML file that defines the `ClusterLogForwarder` CR object. In the file, specify the name of the secret. For example:
+
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: <log_forwarder_name> <1>
  namespace: <log_forwarder_namespace> <2>
spec:
  serviceAccountName: <service_account_name> <3>
  outputs:
   - name: cw <4>
     type: cloudwatch <5>
     cloudwatch:
       groupBy: logType <6>
       groupPrefix: <group prefix> <7>
       region: us-east-2 <8>
     secret:
        name: cw-secret <9>
  pipelines:
    - name: infra-logs <10>
      inputRefs: <11>
        - infrastructure
        - audit
        - application
      outputRefs:
        - cw <12>
----
<1> In legacy implementations, the CR name must be `instance`. In multi log forwarder implementations, you can use any name.
<2> In legacy implementations, the CR namespace must be `openshift-logging`. In multi log forwarder implementations, you can use any namespace.
<3> The name of your service account. The service account is only required in multi log forwarder implementations if the log forwarder is not deployed in the `openshift-logging` namespace.
<4> Specify a name for the output.
<5> Specify the `cloudwatch` type.
<6> Optional: Specify how to group the logs:
+
* `logType` creates log groups for each log type.
* `namespaceName` creates a log group for each application name space. It also creates separate log groups for infrastructure and audit logs.
* `namespaceUUID` creates a new log groups for each application namespace UUID. It also creates separate log groups for infrastructure and audit logs.
<7> Optional: Specify a string to replace the default `infrastructureName` prefix in the names of the log groups.
<8> Specify the AWS region.
<9> Specify the name of the secret that contains your AWS credentials.
<10> Optional: Specify a name for the pipeline.
<11> Specify which log types to forward by using the pipeline: `application,` `infrastructure`, or `audit`.
<12> Specify the name of the output to use when forwarding logs with this pipeline.

. Create the CR object:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

.Example: Using ClusterLogForwarder with Amazon CloudWatch

Here, you see an example `ClusterLogForwarder` custom resource (CR) and the log data that it outputs to Amazon CloudWatch.

Suppose that you are running
ifndef::openshift-rosa[]
an {product-title} cluster
endif::[]
ifdef::openshift-rosa[]
a ROSA cluster
endif::[]
named `mycluster`. The following command returns the cluster's `infrastructureName`, which you will use to compose `aws` commands later on:

[source,terminal]
----
$ oc get Infrastructure/cluster -ojson | jq .status.infrastructureName
"mycluster-7977k"
----

To generate log data for this example, you run a `busybox` pod in a namespace called `app`. The `busybox` pod writes a message to stdout every three seconds:

[source,terminal]
----
$ oc run busybox --image=busybox -- sh -c 'while true; do echo "My life is my message"; sleep 3; done'
$ oc logs -f busybox
My life is my message
My life is my message
My life is my message
...
----

You can look up the UUID of the `app` namespace where the `busybox` pod runs:

[source,terminal]
----
$ oc get ns/app -ojson | jq .metadata.uid
"794e1e1a-b9f5-4958-a190-e76a9b53d7bf"
----

In your `ClusterLogForwarder` custom resource (CR), you configure the `infrastructure`, `audit`, and `application` log types as inputs to the `all-logs` pipeline. You also connect this pipeline to `cw` output, which forwards the logs to a CloudWatch instance in the `us-east-2` region:

[source,yaml]
----
apiVersion: "logging.openshift.io/v1"
kind: ClusterLogForwarder
metadata:
  name: instance
  namespace: openshift-logging
spec:
  outputs:
   - name: cw
     type: cloudwatch
     cloudwatch:
       groupBy: logType
       region: us-east-2
     secret:
        name: cw-secret
  pipelines:
    - name: all-logs
      inputRefs:
        - infrastructure
        - audit
        - application
      outputRefs:
        - cw
----

Each region in CloudWatch contains three levels of objects:

* log group
** log stream
*** log event


With `groupBy: logType` in the `ClusterLogForwarding` CR, the three log types in the `inputRefs` produce three log groups in Amazon Cloudwatch:

[source,terminal]
----
$ aws --output json logs describe-log-groups | jq .logGroups[].logGroupName
"mycluster-7977k.application"
"mycluster-7977k.audit"
"mycluster-7977k.infrastructure"
----

Each of the log groups contains log streams:

[source,terminal]
----
$ aws --output json logs describe-log-streams --log-group-name mycluster-7977k.application | jq .logStreams[].logStreamName
"kubernetes.var.log.containers.busybox_app_busybox-da085893053e20beddd6747acdbaf98e77c37718f85a7f6a4facf09ca195ad76.log"
----

[source,terminal]
----
$ aws --output json logs describe-log-streams --log-group-name mycluster-7977k.audit | jq .logStreams[].logStreamName
"ip-10-0-131-228.us-east-2.compute.internal.k8s-audit.log"
"ip-10-0-131-228.us-east-2.compute.internal.linux-audit.log"
"ip-10-0-131-228.us-east-2.compute.internal.openshift-audit.log"
...
----

[source,terminal]
----
$ aws --output json logs describe-log-streams --log-group-name mycluster-7977k.infrastructure | jq .logStreams[].logStreamName
"ip-10-0-131-228.us-east-2.compute.internal.kubernetes.var.log.containers.apiserver-69f9fd9b58-zqzw5_openshift-oauth-apiserver_oauth-apiserver-453c5c4ee026fe20a6139ba6b1cdd1bed25989c905bf5ac5ca211b7cbb5c3d7b.log"
"ip-10-0-131-228.us-east-2.compute.internal.kubernetes.var.log.containers.apiserver-797774f7c5-lftrx_openshift-apiserver_openshift-apiserver-ce51532df7d4e4d5f21c4f4be05f6575b93196336be0027067fd7d93d70f66a4.log"
"ip-10-0-131-228.us-east-2.compute.internal.kubernetes.var.log.containers.apiserver-797774f7c5-lftrx_openshift-apiserver_openshift-apiserver-check-endpoints-82a9096b5931b5c3b1d6dc4b66113252da4a6472c9fff48623baee761911a9ef.log"
...
----

Each log stream contains log events. To see a log event from the `busybox` Pod, you specify its log stream from the `application` log group:

[source,terminal]
----
$ aws logs get-log-events --log-group-name mycluster-7977k.application --log-stream-name kubernetes.var.log.containers.busybox_app_busybox-da085893053e20beddd6747acdbaf98e77c37718f85a7f6a4facf09ca195ad76.log
{
    "events": [
        {
            "timestamp": 1629422704178,
            "message": "{\"docker\":{\"container_id\":\"da085893053e20beddd6747acdbaf98e77c37718f85a7f6a4facf09ca195ad76\"},\"kubernetes\":{\"container_name\":\"busybox\",\"namespace_name\":\"app\",\"pod_name\":\"busybox\",\"container_image\":\"docker.io/library/busybox:latest\",\"container_image_id\":\"docker.io/library/busybox@sha256:0f354ec1728d9ff32edcd7d1b8bbdfc798277ad36120dc3dc683be44524c8b60\",\"pod_id\":\"870be234-90a3-4258-b73f-4f4d6e2777c7\",\"host\":\"ip-10-0-216-3.us-east-2.compute.internal\",\"labels\":{\"run\":\"busybox\"},\"master_url\":\"https://kubernetes.default.svc\",\"namespace_id\":\"794e1e1a-b9f5-4958-a190-e76a9b53d7bf\",\"namespace_labels\":{\"kubernetes_io/metadata_name\":\"app\"}},\"message\":\"My life is my message\",\"level\":\"unknown\",\"hostname\":\"ip-10-0-216-3.us-east-2.compute.internal\",\"pipeline_metadata\":{\"collector\":{\"ipaddr4\":\"10.0.216.3\",\"inputname\":\"fluent-plugin-systemd\",\"name\":\"fluentd\",\"received_at\":\"2021-08-20T01:25:08.085760+00:00\",\"version\":\"1.7.4 1.6.0\"}},\"@timestamp\":\"2021-08-20T01:25:04.178986+00:00\",\"viaq_index_name\":\"app-write\",\"viaq_msg_id\":\"NWRjZmUyMWQtZjgzNC00MjI4LTk3MjMtNTk3NmY3ZjU4NDk1\",\"log_type\":\"application\",\"time\":\"2021-08-20T01:25:04+00:00\"}",
            "ingestionTime": 1629422744016
        },
...
----

.Example: Customizing the prefix in log group names

In the log group names, you can replace the default `infrastructureName` prefix, `mycluster-7977k`, with an arbitrary string like `demo-group-prefix`. To make this change, you update the `groupPrefix` field in the `ClusterLogForwarding` CR:

[source,yaml]
----
cloudwatch:
    groupBy: logType
    groupPrefix: demo-group-prefix
    region: us-east-2
----

The value of `groupPrefix` replaces the default `infrastructureName` prefix:

[source,terminal]
----
$ aws --output json logs describe-log-groups | jq .logGroups[].logGroupName
"demo-group-prefix.application"
"demo-group-prefix.audit"
"demo-group-prefix.infrastructure"
----

.Example: Naming log groups after application namespace names

For each application namespace in your cluster, you can create a log group in CloudWatch whose name is based on the name of the application namespace.

If you delete an application namespace object and create a new one that has the same name, CloudWatch continues using the same log group as before.

If you consider successive application namespace objects that have the same name as equivalent to each other, use the approach described in this example. Otherwise, if you need to distinguish the resulting log groups from each other, see the following "Naming log groups for application namespace UUIDs" section instead.

To create application log groups whose names are based on the names of the application namespaces, you set the value of the `groupBy` field to `namespaceName` in the `ClusterLogForwarder` CR:

[source,terminal]
----
cloudwatch:
    groupBy: namespaceName
    region: us-east-2
----

Setting `groupBy` to `namespaceName` affects the application log group only. It does not affect the `audit` and `infrastructure` log groups.

In Amazon Cloudwatch, the namespace name appears at the end of each log group name. Because there is a single application namespace, "app", the following output shows a new `mycluster-7977k.app` log group instead of `mycluster-7977k.application`:

[source,terminal]
----
$ aws --output json logs describe-log-groups | jq .logGroups[].logGroupName
"mycluster-7977k.app"
"mycluster-7977k.audit"
"mycluster-7977k.infrastructure"
----

If the cluster in this example had contained multiple application namespaces, the output would show multiple log groups, one for each namespace.

The `groupBy` field affects the application log group only. It does not affect the `audit` and `infrastructure` log groups.

.Example: Naming log groups after application namespace UUIDs

For each application namespace in your cluster, you can create a log group in CloudWatch whose name is based on the UUID of the application namespace.

If you delete an application namespace object and create a new one, CloudWatch creates a new log group.

If you consider successive application namespace objects with the same name as different from each other, use the approach described in this example. Otherwise, see the preceding "Example: Naming log groups for application namespace names" section instead.

To name log groups after application namespace UUIDs, you set the value of the `groupBy` field to `namespaceUUID` in the `ClusterLogForwarder` CR:

[source,terminal]
----
cloudwatch:
    groupBy: namespaceUUID
    region: us-east-2
----

In Amazon Cloudwatch, the namespace UUID appears at the end of each log group name. Because there is a single application namespace, "app", the following output shows a new `mycluster-7977k.794e1e1a-b9f5-4958-a190-e76a9b53d7bf` log group instead of `mycluster-7977k.application`:

[source,terminal]
----
$ aws --output json logs describe-log-groups | jq .logGroups[].logGroupName
"mycluster-7977k.794e1e1a-b9f5-4958-a190-e76a9b53d7bf" // uid of the "app" namespace
"mycluster-7977k.audit"
"mycluster-7977k.infrastructure"
----

The `groupBy` field affects the application log group only. It does not affect the `audit` and `infrastructure` log groups.
