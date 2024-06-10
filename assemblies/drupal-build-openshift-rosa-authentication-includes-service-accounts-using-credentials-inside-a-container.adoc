// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-using-credentials-inside-a-container_{context}"]
= Using a service account's credentials inside a container

When a pod is created, it specifies a service account (or uses the default
service account), and is allowed to use that service account's API credentials
and referenced secrets.

.Procedure

. View the API token for the pod's service account in the
 *_/var/run/secrets/kubernetes.io/serviceaccount/token_* file.

. Set the token value to the `Token` variable:
+
----
$ TOKEN="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)"
----

. Use the token to make API calls as the pod's service account. For example,
call the `users/~` API to get information about the user identified
by the token:
+
----
$ curl --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt \
    "https://openshift.default.svc.cluster.local/apis/user.openshift.io/v1/users/~" \
    -H "Authorization: Bearer $TOKEN"

kind: "User"
apiVersion: "user.openshift.io/v1"
metadata:
  name: "system:serviceaccount:top-secret:robot"
identities: null
groups:
  - "system:serviceaccounts"
  - "system:serviceaccounts:top-secret"
----
