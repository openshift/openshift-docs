// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-application-secrets-creating-using-sa_{context}"]
= Creating and using secrets

As an administrator, you can create a service account token secret. This allows you to distribute a service account token to applications that must authenticate to the API.

.Procedure

. Create a service account in your namespace by running the following command:
+
[source,terminal]
----
$ oc create sa <service_account_name> -n <your_namespace>
----

. Save the following YAML example to a file named `service-account-token-secret.yaml`. The example includes a `Secret` object configuration that you can use to generate a service account token:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <secret_name> <1>
  annotations:
    kubernetes.io/service-account.name: "sa-name" <2>
type: kubernetes.io/service-account-token <3>
----
<1> Replace `<secret_name>` with the name of your service token secret.
<2> Specifies an existing service account name. If you are creating both the `ServiceAccount` and the `Secret` objects, create the `ServiceAccount` object first.
<3> Specifies a service account token secret type.

. Generate the service account token by applying the file:
+
[source,terminal]
----
$ oc apply -f service-account-token-secret.yaml
----

. Get the service account token from the secret by running the following command:
+
[source,terminal]
-----
$ oc get secret <sa_token_secret> -o jsonpath='{.data.token}' | base64 --decode <1>
-----
+
.Example output
[source,terminal]
----
ayJhbGciOiJSUzI1NiIsImtpZCI6IklOb2dtck1qZ3hCSWpoNnh5YnZhSE9QMkk3YnRZMVZoclFfQTZfRFp1YlUifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImJ1aWxkZXItdG9rZW4tdHZrbnIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiYnVpbGRlciIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjNmZGU2MGZmLTA1NGYtNDkyZi04YzhjLTNlZjE0NDk3MmFmNyIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmJ1aWxkZXIifQ.OmqFTDuMHC_lYvvEUrjr1x453hlEEHYcxS9VKSzmRkP1SiVZWPNPkTWlfNRp6bIUZD3U6aN3N7dMSN0eI5hu36xPgpKTdvuckKLTCnelMx6cxOdAbrcw1mCmOClNscwjS1KO1kzMtYnnq8rXHiMJELsNlhnRyyIXRTtNBsy4t64T3283s3SLsancyx0gy0ujx-Ch3uKAKdZi5iT-I8jnnQ-ds5THDs2h65RJhgglQEmSxpHrLGZFmyHAQI-_SjvmHZPXEc482x3SkaQHNLqpmrpJorNqh1M8ZHKzlujhZgVooMvJmWPXTb2vnvi3DGn2XI-hZxl1yD2yGH1RBpYUHA
----
<1> Replace <sa_token_secret> with the name of your service token secret.

. Use your service account token to authenticate with the API of your cluster:
+
[source,terminal]
----
$ curl -X GET <openshift_cluster_api> --header "Authorization: Bearer <token>" <1> <2>
----
<1> Replace `<openshift_cluster_api>` with the OpenShift cluster API.
<2> Replace `<token>` with the service account token that is output in the preceding command.
