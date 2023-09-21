// Module included in the following assemblies:
//
// * authentication/tokens-scoping.adoc

:_mod-docs-content-type: CONCEPT
[id="tokens-scoping-about_{context}"]
= About scoping tokens

You can create scoped tokens to delegate some of your permissions to another
user or service account.
For example, a project administrator might want to delegate the
power to create pods.

A scoped token is a token that identifies as a given user but is limited to
certain actions by its scope.
ifndef::openshift-dedicated,openshift-rosa[]
Only a user with the `cluster-admin` role can create scoped tokens.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
Only a user with the `dedicated-admin` role can create scoped tokens.
endif::openshift-dedicated,openshift-rosa[]

Scopes are evaluated by converting the set of scopes for a token into a set of
`PolicyRules`. Then, the request is matched against those rules. The request
attributes must match at least one of the scope rules to be passed to the
"normal" authorizer for further authorization checks.

[id="scoping-tokens-user-scopes_{context}"]
== User scopes

User scopes are focused on getting information about a given user. They are
intent-based, so the rules are automatically created for you:

* `user:full` - Allows full read/write access to the API with all of the user's permissions.
* `user:info` - Allows read-only access to information about the user, such as name and groups.
* `user:check-access` - Allows access to `self-localsubjectaccessreviews` and `self-subjectaccessreviews`.
    These are the variables where you pass an empty user and groups in your request object.
* `user:list-projects` - Allows read-only access to list the projects the user has access to.


[id="scoping-tokens-role-scope_{context}"]
== Role scope
The role scope allows you to have the same level of access as a given role
filtered by namespace.

* `role:<cluster-role name>:<namespace or * for all>` - Limits the scope to the
rules specified by the cluster-role, but only in the specified namespace .
+
[NOTE]
====
Caveat: This prevents escalating access. Even if the role allows access to
resources like secrets, rolebindings, and roles, this scope will deny access
to those resources. This helps prevent unexpected escalations. Many people do
not think of a role like `edit` as being an escalating role, but with access to
a secret it is.
====

* `role:<cluster-role name>:<namespace or * for all>:!` -  This is similar to the
example above, except that including the bang causes this scope to allow
escalating access.
