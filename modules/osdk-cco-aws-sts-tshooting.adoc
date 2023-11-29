// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-token-auth.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-cco-aws-sts-tshooting_{context}"]
= Troubleshooting

[id="osdk-cco-aws-sts-tshooting-auth-fail_{context}"]
== Authentication failure

If authentication was not successful, ensure you can assume the role with web identity by using the token provided to the Operator.

.Procedure

. Extract the token from the pod:
+
[source,terminal]
----
$ oc exec operator-pod -n <namespace_name> \
    -- cat /var/run/secrets/openshift/serviceaccount/token
----

. Extract the role ARN from the pod:
+
[source,terminal]
----
$ oc exec operator-pod -n <namespace_name> \
    -- cat /<path>/<to>/<secret_name> <1>
----
<1> Do not use root for the path.

. Try assuming the role with the web identity token:
+
[source,terminal]
----
$ aws sts assume-role-with-web-identity \
    --role-arn $ROLEARN \
    --role-session-name <session_name> \
    --web-identity-token $TOKEN
----

[id="osdk-cco-aws-sts-tshooting-mounting_{context}"]
== Secret not mounting correctly

Pods that run as non-root users cannot write to the `/root` directory where the AWS shared credentials file is expected to exist by default. If the secret is not mounting correctly to the AWS credentials file path, consider mounting the secret to a different location and enabling the shared credentials file option in the AWS SDK.
