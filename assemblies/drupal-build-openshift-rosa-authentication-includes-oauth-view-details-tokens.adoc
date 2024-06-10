// Module included in the following assemblies:
//
// * authentication/managing-oauth-access-tokens.adoc

:_mod-docs-content-type: PROCEDURE
[id="oauth-view-details-tokens_{context}"]
= Viewing the details of a user-owned OAuth access token

You can view the details of a user-owned OAuth access token.

.Procedure

* Describe the details of a user-owned OAuth access token:
+
[source,terminal]
----
$ oc describe useroauthaccesstokens <token_name>
----
+
.Example output
[source,terminal]
----
Name:                        <token_name> <1>
Namespace:
Labels:                      <none>
Annotations:                 <none>
API Version:                 oauth.openshift.io/v1
Authorize Token:             sha256~Ksckkug-9Fg_RWn_AUysPoIg-_HqmFI9zUL_CgD8wr8
Client Name:                 openshift-browser-client <2>
Expires In:                  86400 <3>
Inactivity Timeout Seconds:  317 <4>
Kind:                        UserOAuthAccessToken
Metadata:
  Creation Timestamp:  2021-01-11T19:27:06Z
  Managed Fields:
    API Version:  oauth.openshift.io/v1
    Fields Type:  FieldsV1
    fieldsV1:
      f:authorizeToken:
      f:clientName:
      f:expiresIn:
      f:redirectURI:
      f:scopes:
      f:userName:
      f:userUID:
    Manager:         oauth-server
    Operation:       Update
    Time:            2021-01-11T19:27:06Z
  Resource Version:  30535
  Self Link:         /apis/oauth.openshift.io/v1/useroauthaccesstokens/<token_name>
  UID:               f9d00b67-ab65-489b-8080-e427fa3c6181
Redirect URI:        https://oauth-openshift.apps.example.com/oauth/token/display
Scopes:
  user:full <5>
User Name:  <user_name> <6>
User UID:   82356ab0-95f9-4fb3-9bc0-10f1d6a6a345
Events:     <none>
----
<1> The token name, which is the sha256 hash of the token. Token names are not sensitive and cannot be used to log in.
<2> The client name, which describes where the token originated from.
<3> The value in seconds from the creation time before this token expires.
<4> If there is a token inactivity timeout set for the OAuth server, this is the value in seconds from the creation time before this token can no longer be used.
<5> The scopes for this token.
<6> The user name associated with this token.
