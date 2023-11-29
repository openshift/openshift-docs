// Module included in the following assemblies:
//
// * nodes/nodes/nodes-sno-worker-nodes.adoc

:_mod-docs-content-type: PROCEDURE
[id="ai-authenticating-against-ai-rest-api_{context}"]
= Authenticating against the Assisted Installer REST API

Before you can use the Assisted Installer REST API, you must authenticate against the API using a JSON web token (JWT) that you generate.

.Prerequisites

* Log in to link:https://console.redhat.com/openshift/assisted-installer/clusters[{cluster-manager}] as a user with cluster creation privileges.

* Install `jq`.

.Procedure

. Log in to link:https://console.redhat.com/openshift/token/show[{cluster-manager}] and copy your API token.

. Set the `$OFFLINE_TOKEN` variable using the copied API token by running the following command:
+
[source,terminal]
----
$ export OFFLINE_TOKEN=<copied_api_token>
----

. Set the `$JWT_TOKEN` variable using the previously set `$OFFLINE_TOKEN` variable:
+
[source,terminal]
----
$ export JWT_TOKEN=$(
  curl \
  --silent \
  --header "Accept: application/json" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=refresh_token" \
  --data-urlencode "client_id=cloud-services" \
  --data-urlencode "refresh_token=${OFFLINE_TOKEN}" \
  "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token" \
  | jq --raw-output ".access_token"
)
----
+
[NOTE]
====
The JWT token is valid for 15 minutes only.
====

.Verification

* Optional: Check that you can access the API by running the following command:
+
[source,terminal]
----
$ curl -s https://api.openshift.com/api/assisted-install/v2/component-versions -H "Authorization: Bearer ${JWT_TOKEN}" | jq
----
+
.Example output
[source,yaml]
----
{
    "release_tag": "v2.5.1",
    "versions":
    {
        "assisted-installer": "registry.redhat.io/rhai-tech-preview/assisted-installer-rhel8:v1.0.0-175",
        "assisted-installer-controller": "registry.redhat.io/rhai-tech-preview/assisted-installer-reporter-rhel8:v1.0.0-223",
        "assisted-installer-service": "quay.io/app-sre/assisted-service:ac87f93",
        "discovery-agent": "registry.redhat.io/rhai-tech-preview/assisted-installer-agent-rhel8:v1.0.0-156"
    }
}
----
