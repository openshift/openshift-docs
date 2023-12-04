// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-complying-with-psa.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-managing-psa-for-operators-with-escalated-permissions_{context}"]
= Managing pod security admission for Operator workloads that require escalated permissions

If your Operator project requires escalated permissions to run, you must edit your Operator's cluster service version (CSV).

.Procedure

. Set the security context configuration to the required permission level in your Operator's CSV, similar to the following example:
+
.Example `<operator_name>.clusterserviceversion.yaml` file with network administrator privileges
[source,yaml]
----
...
containers:
   - name: my-container
     securityContext:
       allowPrivilegeEscalation: false
       capabilities:
         add:
           - "NET_ADMIN"
...
----

. Set the service account privileges that allow your Operator's workloads to use the required security context constraints (SCC), similar to the following example:
+
.Example `<operator_name>.clusterserviceversion.yaml` file
[source,yaml]
----
...
  install:
    spec:
      clusterPermissions:
      - rules:
        - apiGroups:
          - security.openshift.io
          resourceNames:
          - privileged
          resources:
          - securitycontextconstraints
          verbs:
          - use
        serviceAccountName: default
...
----

. Edit your Operator's CSV description to explain why your Operator project requires escalated permissions similar to the following example:
+
.Example `<operator_name>.clusterserviceversion.yaml` file
[source,yaml]
----
...
spec:
  apiservicedefinitions:{}
  ...
description: The <operator_name> requires a privileged pod security admission label set on the Operator's namespace. The Operator's agents require escalated permissions to restart the node if the node needs remediation.
----
